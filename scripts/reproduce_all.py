#!/usr/bin/env python3
"""reproduce_all.py — top-level reproducibility driver for the staged release.

Runs every Fable verification script in this directory (``scripts/*.py``), in a
fixed sorted order, each in its own subprocess, and prints a PASS / FAIL line per
script plus a final summary. Self-contained: depends only on the 21 staged
scripts beside it — it has NO dependence on any ``/gut/scripts/`` tree.

------------------------------------------------------------------------------
HONEST EXIT-CODE SEMANTICS (read this before trusting a "FAIL")
------------------------------------------------------------------------------
These scripts run under the corpus's CFCA discipline. A script's *process exit
code* encodes a **physics / governance verdict**, not merely "did the code run."
Several scripts are deliberate ``stubs-that-refuse`` or bank an honest negative,
and they signal that with a non-zero exit ON PURPOSE — that refusal IS the
deliverable (``scripts/MANIFEST.md`` documents each). So this driver classifies
three outcomes, and only the third is a real failure:

  * PASS            — the script executed to completion and exited 0.
  * REFUSED/NEGATIVE — the script executed to completion but exited non-zero
                       BY DESIGN (owner-locked refusal, e.g. bg10_four_fix.py
                       exit 2; or a banked honest-negative, e.g.
                       strongcp_realizationB.py exit 1 = route disproved, gate
                       stays OPEN). This is expected and is NOT counted as a
                       failure. It is the corpus "publish the refutation" rule.
  * FAIL            — the harness could not run the script at all, OR the script
                       died with an uncaught Python traceback (a genuine break).

The expected by-design non-zero exits are pinned in EXPECTED_NONZERO below, so a
NEW, unexpected non-zero exit (or any traceback) still surfaces loudly as FAIL.

Process exit of THIS driver:
  * 0  — every script either PASSed or REFUSED/NEGATIVE exactly as expected.
  * 1  — at least one script genuinely FAILED (unexpected exit or traceback).

This driver writes nothing of its own; each child script writes its own
artifacts under ``scripts/outputs/`` (resolved relative to its own ``__file__``).
"""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent

# This driver must never try to run itself.
SELF = Path(__file__).resolve().name

# Per-script timeout (seconds). The heaviest staged script finishes well under
# this; the cap only guards against an environment-level hang.
PER_SCRIPT_TIMEOUT = 600

# By-design non-zero exits (documented in scripts/MANIFEST.md). A script that
# exits with the code listed here is a deliberate refusal / banked-negative and
# is reported as REFUSED/NEGATIVE, not FAIL. Any OTHER non-zero exit is a FAIL.
EXPECTED_NONZERO = {
    "bg10_four_fix.py": 2,          # owner-locked refusal: needs Chris's signed F+ manifest
    "strongcp_realizationB.py": 1,  # banked-negative: Realization-B route disproved, gate stays OPEN
}

# Outcome tags.
PASS = "PASS"
REFUSED = "REFUSED/NEGATIVE (by design)"
FAIL = "FAIL"


def discover_scripts() -> list[Path]:
    """Return the staged verification scripts in deterministic sorted order,
    excluding this driver itself."""
    return sorted(
        p for p in SCRIPTS_DIR.glob("*.py") if p.name != SELF
    )


def run_one(script: Path) -> tuple[str, int, float, str]:
    """Run a single script in a subprocess.

    Returns (outcome_tag, returncode, elapsed_seconds, note).
    """
    start = time.time()
    note = ""
    try:
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(SCRIPTS_DIR),
            capture_output=True,
            text=True,
            timeout=PER_SCRIPT_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start
        return FAIL, -1, elapsed, f"timed out after {PER_SCRIPT_TIMEOUT}s"
    except Exception as exc:  # pragma: no cover - harness-level failure
        elapsed = time.time() - start
        return FAIL, -1, elapsed, f"could not launch: {exc!r}"

    elapsed = time.time() - start
    rc = proc.returncode

    # A genuine break: the child died with an uncaught Python traceback.
    combined_tail = (proc.stderr or "") + (proc.stdout or "")
    has_traceback = "Traceback (most recent call last):" in combined_tail

    if rc == 0 and not has_traceback:
        return PASS, rc, elapsed, ""

    if has_traceback:
        # Surface the last meaningful traceback line for the report.
        last_line = ""
        for line in reversed((proc.stderr or "").strip().splitlines()):
            if line.strip():
                last_line = line.strip()
                break
        return FAIL, rc, elapsed, f"uncaught exception: {last_line}"

    # Non-zero exit, no traceback: is it a documented by-design refusal/negative?
    expected = EXPECTED_NONZERO.get(script.name)
    if expected is not None and rc == expected:
        return REFUSED, rc, elapsed, f"by-design exit {rc} (see MANIFEST.md)"

    # Non-zero exit that we did NOT expect — treat as a real failure.
    return FAIL, rc, elapsed, f"unexpected non-zero exit {rc}"


def main() -> int:
    scripts = discover_scripts()

    print("=" * 72)
    print("reproduce_all.py — Fable staged-release verification driver")
    print(f"scripts dir : {SCRIPTS_DIR}")
    print(f"python      : {sys.version.split()[0]}")
    print(f"discovered  : {len(scripts)} scripts")
    print("=" * 72)
    print()

    results: list[tuple[str, str, int, float, str]] = []
    width = max((len(s.name) for s in scripts), default=20)

    for script in scripts:
        outcome, rc, elapsed, note = run_one(script)
        tag = {PASS: "PASS", REFUSED: "REFUSED", FAIL: "FAIL"}[outcome]
        line = f"[{tag:7}] {script.name:<{width}}  ({elapsed:5.1f}s)"
        if note:
            line += f"  — {note}"
        print(line)
        results.append((outcome, script.name, rc, elapsed, note))

    n_pass = sum(1 for r in results if r[0] == PASS)
    n_refused = sum(1 for r in results if r[0] == REFUSED)
    n_fail = sum(1 for r in results if r[0] == FAIL)
    total_time = sum(r[3] for r in results)

    print()
    print("=" * 72)
    print("SUMMARY")
    print("-" * 72)
    print(f"  scripts run            : {len(results)}")
    print(f"  PASS (exit 0)          : {n_pass}")
    print(f"  REFUSED/NEGATIVE (ok)  : {n_refused}   (by-design non-zero; see MANIFEST.md)")
    print(f"  FAIL                   : {n_fail}")
    print(f"  wall time              : {total_time:5.1f}s")

    if n_refused:
        refused_names = ", ".join(r[1] for r in results if r[0] == REFUSED)
        print(f"  by-design refusals     : {refused_names}")

    if n_fail:
        print("-" * 72)
        print("  FAILURES:")
        for outcome, name, rc, _elapsed, note in results:
            if outcome == FAIL:
                print(f"    - {name}  (rc={rc})  {note}")
        print("=" * 72)
        print("[done] reproduce_all: FAILURES present -> exit 1")
        return 1

    print("=" * 72)
    print("[done] reproduce_all: all scripts ran as intended -> exit 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
