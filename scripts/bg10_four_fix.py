#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
bg10_four_fix.py
================
BG-10 / Gap 10 (baryogenesis, TOE §IV) sub-loop orchestrator.

  TERMINAL STATE (current / default / maximal-agent-reachable):
      Precisely-OPEN-with-falsifier  (BLOCKED_BY_NAMED_OBJECT: "Chris does
      the physics").  Four-fix ledger 0/4 at certificate grade.  eta_B = null.

  THIS SCRIPT IS THE STUB-THAT-REFUSES, AND THE STUB IS THE DELIVERABLE.
      It CANNOT run the lane to a claimed eta_B without a Chris-signed
      manifest carrying the 7 F^+ chamber-derived inputs.  Absent that
      signature it REFUSES with exit code 2 on the first failed gate.  It
      NEVER produces an eta_B number.  Producing eta_B REQUIRES Chris's
      signed 7-input F^+ manifest (the owner-locked physics) -- the agent
      ceiling is to assemble the certificate-grade Precisely-OPEN package
      and route the owner-only act to Chris.

WHY A SECOND ORCHESTRATOR.
  The on-disk canonical instrument
      .../Final_physics_articles/scripts/gap_10/four_fix_pipeline_orchestrator.py
  already implements the four halt paths (A/B/C/D -> exit 2) against the
  OPEN-posture manifest .../gap_10/frozen_inputs.yaml.  This rendered
  orchestrator does NOT reimplement that physics-pipeline wiring; it is the
  GAP_CLOSURE_LOOP_DESIGN.md s6.4 deliverable that

    (a) REPRODUCES / ENCODES the fail-closed refusal -- by delegating to the
        canonical on-disk orchestrator when it is reachable, and by carrying
        a SELF-CONTAINED fallback gate set so the refusal holds even when the
        corpus path is absent;
    (b) emits an ALL-NULL, countersign-READY four-fix MANIFEST SKELETON -- the
        4 fix slots + 7 F^+ input leaves, each marked NULL / awaiting-Chris,
        signed:false, signer:null (this is BG10-W2's signing surface);
    (c) FREEZES the pre-registered falsifier window  eta_B in [6.0, 6.2]e-10
        and the SINGLE-COMPARISON protocol (compare ONCE, after freeze, only
        when the signed manifest exists) -- this is BG10-W3's custody.

  It runs today, against today's unsigned manifest, and it MUST exit 2.

==========================================================================
THE FOUR NAMED FIXES  (any BG-10 attempt MUST execute all four; 0/4 now)
==========================================================================
  fix_1  canonical CI            -- the canonical / basis-independent CP
                                    invariant (not a convention-dependent one)
  fix_2  proper Delta L=2        -- the Delta L=2 washout treated explicitly,
                                    NOT folded into kappa (falsifier F6)
  fix_3  N2/N3 damping           -- explicit N_2 and N_3 damping (not N_1-only)
  fix_4  density-matrix flavor   -- density-matrix (off-diagonal-coherent)
                                    flavor evolution, not a diagonal rate eq.

  Each fix is a SLOT here, marked NULL / awaiting-Chris.  No fix is computed.

==========================================================================
THE SEVEN REQUIRED F^+ CHAMBER-DERIVED INPUTS  (all null until Chris stamps)
==========================================================================
  1 Y_nu                 3x3 complex neutrino Yukawa matrix
  2 M_N                  3 real heavy Majorana eigenvalues (GeV)
  3 PMNS_angles          theta_12, theta_13, theta_23 (radians)
  4 Dirac_delta_CP       Dirac CP phase (radians)
  5 Majorana_phases      alpha_21, alpha_31 (radians)
  6 T_RH                 reheating temperature (GeV)
  7 initial_abundances   N_N1, N_N2, N_N3, and the Hermitian 3x3 n_L^{ab}

==========================================================================
SPEC  (written BEFORE any computation -- the EXT-5 freeze)
==========================================================================
INPUTS
  - A signed manifest path (default: the on-disk OPEN-posture
    gap_10/frozen_inputs.yaml).  signed:true + 7 non-null F^+ leaves is the
    ONLY input that unlocks any computation -- and that stamp is Chris's.
OUTPUTS (this run, OPEN posture)
  - refusal record (gate, message, exit code) -> rendered/scripts/outputs/
  - the all-null countersign-READY manifest skeleton (deliverable b)
  - the frozen falsifier window + single-comparison protocol (deliverable c)
  - eta_B : null  (ALWAYS null on this side of Chris's signature)
ACCEPTANCE / EXIT CODES
  2  REFUSE (DEFAULT, EXPECTED): manifest unsigned, or any of the 7 leaves
     null, or any of the 4 fix modules missing, or a target-loading attempt.
     This is the certificate-grade Precisely-OPEN terminal.
  0  reserved for the owner-gated path ONLY: a Chris-signed manifest, all 4
     guards green, all 4 fixes dispatched, all 8 falsifier clauses evaluated,
     and the SINGLE post-freeze comparison performed in the Chris-ruled
     convention.  UNREACHABLE WITHOUT CHRIS.  This script never forces it.
  3  unexpected runtime error.

  NB: a NON-ZERO exit is the SUCCESS condition for the agent ceiling.  An
  exit-0 from agent work alone would be the structural FAIL the 2026-06-04
  same-day withdrawal exists to catch.

==========================================================================
FROZEN PINS  (verbatim, never mutated)
==========================================================================
  status-preservation invariant : "BG-10 = Open / Diagnostic"
  source_hash (TOE_FINAL_REVIEW) : caf7ffc24d46e8b5e586b1cdcaceaa0318533644f880036c15a6bad9627211ec
  withdrawn-result denylist      : R=1.0001, z_1=-0.07-1.35i  (NEVER re-invoked)
  pre-registered falsifier window: eta_B in [6.0, 6.2]e-10 @ 3 sigma  (doc/TOE_FINAL)
  conversion                     : eta_B ~= 7.04 * Y_B
  RECONCILIATION (owner-gated)   : the harness band is the Y_B-style
                                   (8.0 +/- 0.3)e-11 in eta_B units; the doc
                                   window is eta_B in [6.0,6.2]e-10.  WHICH
                                   window is canonical is a CHRIS RULING, not
                                   an agent edit.  This script pins BOTH and
                                   refuses to pick.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from typing import Optional, Tuple


# --------------------------------------------------------------------------
# FROZEN PINS  (verbatim, never mutated)
# --------------------------------------------------------------------------
STATUS_INVARIANT = "BG-10 = Open / Diagnostic"
SOURCE_HASH = (
    "caf7ffc24d46e8b5e586b1cdcaceaa0318533644f880036c15a6bad9627211ec"
)

# The four named fixes, verbatim.  Slots only; nothing computed.
FOUR_NAMED_FIXES = [
    ("fix_1_canonical_CI", "canonical CI",
     "canonical_ci", "compute_cp_invariants"),
    ("fix_2_explicit_deltaL2", "proper Delta L=2",
     "delta_l2_washout", "compute_washout_deltaL2"),
    ("fix_3_N2_N3_damping", "N2/N3 damping",
     "n2_n3_damping", "compute_damping"),
    ("fix_4_density_matrix_flavor", "density-matrix flavor",
     "density_matrix_flavor", "compute_density_matrix_flavor"),
]

# The seven required F^+ chamber-derived inputs, verbatim.  All null.
SEVEN_F_PLUS_INPUTS = [
    "Y_nu",
    "M_N",
    "PMNS_angles",
    "Dirac_delta_CP",
    "Majorana_phases",
    "T_RH",
    "initial_abundances",
]

# Dotted leaves the null-leaf scan must walk (13 leaves spanning the 7 inputs).
SIGNED_LEAVES = [
    "Y_nu",
    "M_N",
    "PMNS_angles.theta_12",
    "PMNS_angles.theta_13",
    "PMNS_angles.theta_23",
    "Dirac_delta_CP",
    "Majorana_phases.alpha_21",
    "Majorana_phases.alpha_31",
    "T_RH",
    "initial_abundances.N_N1",
    "initial_abundances.N_N2",
    "initial_abundances.N_N3",
    "initial_abundances.n_L_ab",
]

# Withdrawn-result denylist.  These tokens must NEVER appear in any output.
WITHDRAWN_RESULT_DENYLIST = [
    "R = 1.0001",
    "R=1.0001",
    "1.0001",
    "-0.07 - 1.35",
    "-0.07-1.35",
    "z_1 = -0.07",
    "z1 = -0.07",
]

# ----- deliverable (c): the FROZEN falsifier window + conversion ----------
# Pre-registered BEFORE any number exists.  Compared to eta_B EXACTLY ONCE,
# after the freeze, only when a Chris-signed manifest exists.
PRE_REGISTERED_WINDOW = {
    "symbol": "eta_B",
    # The TOE_FINAL document window (this task's frozen falsifier window):
    "doc_window": {"low": 6.0e-10, "high": 6.2e-10, "units": "dimensionless",
                   "sigma": 3, "source": "TOE_FINAL_merged.md §IV"},
    # The on-disk harness band (Y_B-style, expressed in eta_B units):
    "harness_band": {"central": 8.0e-11, "half_width": 0.3e-11,
                     "units": "dimensionless",
                     "source": "gap_10/frozen_inputs.yaml "
                               "observed_band_for_post_check_only"},
    "conversion": "eta_B ~= 7.04 * Y_B",
    "RECONCILIATION": (
        "Chris ruling REQUIRED -- NOT resolved here.  The doc window "
        "[6.0,6.2]e-10 and the harness band (8.0 +/- 0.3)e-11 are two "
        "conventions; which is canonical is owner-locked.  This script "
        "pins both and refuses to pick."
    ),
    "pre_registered_in_advance_of_any_future_run": True,
}

SINGLE_COMPARISON_PROTOCOL = (
    "eta_B is compared to the frozen pre-registered window EXACTLY ONCE, at "
    "the final post-prediction gate, AFTER the freeze, and ONLY when a "
    "Chris-signed manifest (signed:true, 7 non-null F^+ inputs) has produced "
    "a non-null eta_B.  No observed value (eta_B_obs, the window, or the "
    "harness band) may enter on the input side of any fix.  One comparison, "
    "one pinned convention (Chris-ruled), no re-centering to fit a result."
)


# --------------------------------------------------------------------------
# deliverable (b): the all-null, countersign-READY four-fix manifest skeleton
# --------------------------------------------------------------------------
def build_manifest_skeleton() -> dict:
    """The empty-but-complete signing surface FOR Chris.  Every F^+ input is
    an explicit null + TODO(physics: Chris, F^+-chamber derivation); every
    fix is a NULL slot.  signed:false, signer:null.  Nothing is computed.

    By design this skeleton FAILS the closure condition (signed:true + all
    leaves non-null): that failure is the point.
    """
    return {
        "manifest_version": 1,
        "gap_id": "10_bg10_baryogenesis_certificate",
        "gate_ids": ["TOE-8"],
        "status_preservation_invariant": STATUS_INVARIANT,
        "status_input": STATUS_INVARIANT,
        "status_output": STATUS_INVARIANT,
        "source_review": "TOE_FINAL_REVIEW.md",
        "source_hash": SOURCE_HASH,
        "promotion_attempted": False,
        "silent_BG10_promotion": False,
        "withdrawn_result_NOT_reinvoked": True,
        "withdrawn_result_descriptor": (
            "2026-06-04 first-pass closure (withdrawn same day after a "
            "ten-parallel-agent audit; forbidden from any new output)"
        ),
        # ----- the four fix SLOTS (0/4 at certificate grade) -----
        "four_fix_ledger": {
            slot: {
                "name_verbatim": name,
                "module": f"{mod}.py",
                "status": "NULL / awaiting-Chris",
                "certificate_grade": False,
            }
            for slot, name, mod, _fn in FOUR_NAMED_FIXES
        },
        "four_fix_ledger_progress": "0/4",
        # ----- signing posture (unsigned) -----
        "signed": False,
        "signer": None,
        "signed_leaves": list(SIGNED_LEAVES),
        # ----- the seven F^+ inputs, all null -----
        "Y_nu": None,            # TODO(physics: Chris, F^+-chamber derivation)
        "M_N": None,             # TODO(physics: Chris, F^+-chamber derivation)
        "PMNS_angles": {"theta_12": None, "theta_13": None, "theta_23": None},
        "Dirac_delta_CP": None,  # TODO(physics: Chris, F^+-chamber derivation)
        "Majorana_phases": {"alpha_21": None, "alpha_31": None},
        "T_RH": None,            # TODO(physics: Chris, F^+ + inflation sector)
        "initial_abundances": {
            "N_N1": None, "N_N2": None, "N_N3": None,
            "n_L_ab": None,      # Hermitian 3x3 -- TODO(physics: Chris)
        },
        # ----- observed band: post-prediction comparison ONLY -----
        "observed_band_for_post_check_only": {
            "symbol": "eta_B",
            "use": "post_prediction_comparison_only",
            "doc_window": PRE_REGISTERED_WINDOW["doc_window"],
            "harness_band": PRE_REGISTERED_WINDOW["harness_band"],
            "RECONCILIATION": PRE_REGISTERED_WINDOW["RECONCILIATION"],
        },
        "target_loading_forbidden": True,
        "withdrawn_result_forbidden_tokens": list(WITHDRAWN_RESULT_DENYLIST),
        # ----- owner handoff -----
        "owner_only_act": (
            "Chris derives the 7 F^+ inputs, stamps signed:true + signer, "
            "rules the window-convention reconciliation, and signs the "
            "§VIII slot after CS2 clears.  No agent may perform any of these."
        ),
    }


# --------------------------------------------------------------------------
# Self-contained fallback gates  (so the refusal holds even with no corpus)
# --------------------------------------------------------------------------
def _walk(d, dotted: str):
    cur = d
    for p in dotted.split("."):
        if not isinstance(cur, dict) or p not in cur:
            return None
        cur = cur[p]
    return cur


def _fallback_gates(manifest: dict) -> Tuple[int, str, str]:
    """Self-contained gate set used when the canonical on-disk orchestrator is
    not reachable.  Returns (exit_code, gate, message).  Mirrors the on-disk
    halt paths A/B; never computes physics; never emits eta_B.
    """
    # Halt path A: signed-manifest gate
    if manifest.get("signed") is not True:
        return 2, "gate_A_signed_manifest", (
            "gate_A: manifest is unsigned (signed != true). Refusing. Chris "
            "must derive + stamp the 7 F^+ chamber inputs and set signed:true."
        )
    # Halt path B: null-leaf scan
    null_paths = [p for p in manifest.get("signed_leaves", [])
                  if _walk(manifest, p) is None]
    if null_paths:
        return 2, "gate_B_null_leaf_scan", (
            "gate_B: null leaves present in signed leaf set: "
            + ", ".join(null_paths)
            + ". F^+ chamber-derived values required for each."
        )
    # If A and B pass here (they cannot, on the OPEN skeleton), the heavy
    # four-fix integration is owner-greenlit ONLY after Chris signs.  This
    # fallback never performs it; it routes to the canonical orchestrator.
    return 2, "gate_owner_required", (
        "gate_owner_required: a signed manifest with non-null leaves was "
        "detected, but the heavy four-fix integration is owner-greenlit only "
        "via the canonical on-disk orchestrator after Chris signs. Refusing "
        "to compute eta_B in the stub. Route to the canonical pipeline."
    )


# --------------------------------------------------------------------------
# Canonical-orchestrator delegation
# --------------------------------------------------------------------------
CANONICAL_ORCHESTRATOR_CANDIDATES = [
    # relative to a corpus root, walked upward from this file
    os.path.join("Final_physics_articles", "scripts", "gap_10",
                 "four_fix_pipeline_orchestrator.py"),
    os.path.join("scripts", "gap_10",
                 "four_fix_pipeline_orchestrator.py"),
]


def _find_canonical_orchestrator() -> Optional[str]:
    """Walk upward from this file looking for the on-disk gap_10 orchestrator."""
    here = os.path.dirname(os.path.abspath(__file__))
    cur = here
    for _ in range(8):
        for rel in CANONICAL_ORCHESTRATOR_CANDIDATES:
            cand = os.path.join(cur, rel)
            if os.path.isfile(cand):
                return cand
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return None


def _delegate_to_canonical(orch_path: str) -> Tuple[int, str]:
    """Run the canonical on-disk orchestrator against its OPEN-posture
    manifest and return (exit_code, tail_of_stderr_or_stdout).  The canonical
    orchestrator owns the real halt paths A/B/C/D and the (owner-gated) live
    pipeline; we mirror its exit code.  We do NOT pass it anything signed.
    """
    proc = subprocess.run(
        [sys.executable, orch_path],
        capture_output=True, text=True,
        cwd=os.path.dirname(orch_path),
    )
    tail = (proc.stderr or proc.stdout or "").strip().splitlines()
    return proc.returncode, ("\n".join(tail[-6:]) if tail else "")


# --------------------------------------------------------------------------
# Denylist guard  (the withdrawn 2026-06-04 result must never reappear)
# --------------------------------------------------------------------------
def _denylist_clean(*blobs: str) -> list:
    hits = []
    for blob in blobs:
        for tok in WITHDRAWN_RESULT_DENYLIST:
            # the bare "1.0001" sub-token would false-positive on benign
            # floats; we only flag the load-bearing withdrawn descriptors.
            if tok in ("1.0001",):
                continue
            if tok and tok in blob:
                hits.append(tok)
    return hits


# --------------------------------------------------------------------------
# Output emission
# --------------------------------------------------------------------------
def _outdir() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "outputs")
    os.makedirs(out, exist_ok=True)
    return out


def _emit_open_package(exit_code: int, gate: str, message: str,
                       canonical_path: Optional[str],
                       canonical_rc: Optional[int]) -> str:
    """Write the certificate-grade Precisely-OPEN package: the refusal record,
    the all-null manifest skeleton, and the frozen falsifier window + protocol.
    Returns the package path.  eta_B is ALWAYS null here.
    """
    out = _outdir()
    manifest = build_manifest_skeleton()

    # The denylist guard runs over everything we are about to emit.
    package = {
        "gap": "BG-10 / Gap 10 (baryogenesis, TOE §IV)",
        "terminal_state": "Precisely-OPEN-with-falsifier",
        "native_status": "BLOCKED_BY_NAMED_OBJECT",
        "blocking_object": "Chris does the physics (signed 7-input F^+ manifest)",
        "status_preservation_invariant": STATUS_INVARIANT,
        "four_fix_ledger_progress": "0/4",
        "eta_B": None,
        "verdict": "OPEN",
        "promotion_attempted": False,
        "silent_BG10_promotion": False,
        # (a) the fail-closed refusal:
        "refusal": {
            "exit_code": exit_code,
            "gate": gate,
            "message": message,
            "canonical_orchestrator": canonical_path,
            "canonical_orchestrator_exit": canonical_rc,
        },
        # (b) the all-null countersign-READY manifest skeleton:
        "manifest_skeleton": manifest,
        # (c) the frozen falsifier window + single-comparison protocol:
        "pre_registered_window": PRE_REGISTERED_WINDOW,
        "single_comparison_protocol": SINGLE_COMPARISON_PROTOCOL,
        # the four required fixes, each NULL / awaiting-Chris:
        "four_named_fixes_status": {
            slot: {"name_verbatim": name, "state": "NULL / awaiting-Chris"}
            for slot, name, _mod, _fn in FOUR_NAMED_FIXES
        },
        "owner_only_acts": [
            "derive the 7 F^+ chamber inputs",
            "stamp signed:true + signer",
            "rule the eta_B window-convention reconciliation",
            "sign the §VIII slot after the physics-closure countersign clears",
        ],
        "anti_overclaim_attestation": (
            "No eta_B produced. No fix computed. No observed value entered any "
            "input. Window pinned before any number exists. Withdrawn result "
            "not re-invoked. The lane refuses correctly; BG-10 = Open / "
            "Diagnostic is preserved."
        ),
    }

    # Denylist guard: scan the payload for the WITHDRAWN result, but EXCLUDE
    # the declared denylist fields themselves (the tokens legitimately appear
    # there AS the denylist, not as a re-invocation -- the "outside declared
    # fields" distinction BG10-CS1 enforces). We strip the declared carriers
    # before scanning.
    scan_payload = json.loads(json.dumps(package, default=str))

    def _strip_declared(node):
        if isinstance(node, dict):
            node.pop("withdrawn_result_forbidden_tokens", None)
            for v in node.values():
                _strip_declared(v)
        elif isinstance(node, list):
            for v in node:
                _strip_declared(v)
    _strip_declared(scan_payload)
    blob = json.dumps(scan_payload, default=str)
    hits = _denylist_clean(blob)
    if hits:
        # If the withdrawn descriptors somehow leaked, refuse to write and
        # escalate -- this would itself be a structural-FAIL candidate.
        package = {
            "verdict": "STRUCTURAL_FAIL_CANDIDATE",
            "reason": "withdrawn-result denylist hit in emission payload",
            "hits": hits,
            "status_preservation_invariant": STATUS_INVARIANT,
        }

    pkg_path = os.path.join(out, "bg10_open_package.json")
    with open(pkg_path, "w", encoding="utf-8") as f:
        json.dump(package, f, indent=2)

    # The manifest skeleton, also written standalone for Chris's signing surface.
    with open(os.path.join(out, "bg10_manifest_skeleton.json"),
              "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    # eta_B prediction row -- ALWAYS blank on this side of the signature.
    with open(os.path.join(out, "bg10_eta_B_prediction.csv"),
              "w", encoding="utf-8") as f:
        f.write("quantity,value,unit,notes\n")
        f.write(f"eta_B,,dimensionless,refused at {gate} "
                "(no signed F^+ manifest)\n")
        f.write("in_window,,bool,not evaluated (refusal upstream)\n")

    return pkg_path


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main() -> int:
    print("=" * 70)
    print("BG-10 / Gap 10 four-fix orchestrator (STUB-THAT-REFUSES)")
    print(f"  invariant: {STATUS_INVARIANT}")
    print("  terminal : Precisely-OPEN-with-falsifier (0/4 fixes)")
    print("=" * 70)

    # (a) reproduce / encode the fail-closed refusal.
    canonical = _find_canonical_orchestrator()
    canonical_rc: Optional[int] = None

    if canonical is not None:
        print(f"[bg10] delegating to canonical orchestrator:\n       {canonical}")
        canonical_rc, tail = _delegate_to_canonical(canonical)
        print(f"[bg10] canonical orchestrator exit = {canonical_rc}")
        if tail:
            for line in tail.splitlines():
                print(f"       | {line}")
        if canonical_rc == 0:
            # The canonical orchestrator should NEVER exit 0 on an unsigned
            # manifest.  If it does, that is a structural-FAIL candidate.
            msg = (
                "STRUCTURAL-FAIL CANDIDATE: canonical orchestrator exited 0 "
                "without a Chris-signed manifest in scope. Refusing to mirror "
                "a closure. BG-10 = Open / Diagnostic preserved."
            )
            print(f"[bg10] {msg}", file=sys.stderr)
            _emit_open_package(2, "structural_fail_guard", msg,
                               canonical, canonical_rc)
            return 2
        exit_code = 2 if canonical_rc == 2 else canonical_rc
        gate = "canonical_orchestrator_refusal"
        message = (
            f"canonical on-disk orchestrator refused (exit {canonical_rc}) on "
            "the OPEN-posture manifest; no Chris-signed F^+ inputs. "
            "BG-10 = Open / Diagnostic preserved."
        )
    else:
        # Self-contained fallback: refuse on the all-null skeleton.
        print("[bg10] canonical orchestrator not found on disk; using "
              "self-contained fallback gates against the all-null skeleton.")
        exit_code, gate, message = _fallback_gates(build_manifest_skeleton())

    print(f"[bg10] gate: {gate}")
    print(f"[bg10] {message}")

    # (b) + (c): emit the all-null countersign-READY package + frozen window.
    pkg = _emit_open_package(exit_code, gate, message, canonical, canonical_rc)
    print(f"[bg10] certificate-grade Precisely-OPEN package -> {pkg}")
    print("[bg10] eta_B = null  (REQUIRES Chris's signed 7-input F^+ manifest)")
    print(f"[bg10] four-fix ledger: 0/4   |   exit {exit_code}")
    print("[bg10] owner-only acts routed to Chris; nothing promoted.")
    return exit_code


if __name__ == "__main__":
    try:
        rc = main()
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001
        print(f"[bg10] UNEXPECTED ERROR: {exc!r}", file=sys.stderr)
        rc = 3
    sys.exit(rc)
