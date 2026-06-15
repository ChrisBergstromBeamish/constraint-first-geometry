#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
inflation_sigma_map_read.py
===========================
Gap-08 / K13-2 sub-loop instrument: THE FROZEN SIGMA-MAP READ.

Gap 08 is Conditional-with-named-gate. The one named gate that separates the
operative branch (T6) from the textbook-ruling branch (T_u) is a SINGLE READ of
the frozen sigma-map yaml: the kinetic-normalization declaration that decides
which of the two binary conventions the geometry actually uses.

This script:
  (1) Searches the corpus for the frozen sigma-map yaml at its canonical paths.
  (2) If the yaml EXISTS, reads its declaration and SELECTS the operative branch
      by the textbook ruling, emitting that branch's r-band at decision grade.
  (3) If the yaml is ABSENT (the named gate is PENDING / EXTERNAL, never
      committed), it reports the gate is unread, recovers the four r-bands and
      the union falsifier from the FROZEN manuscript-banked values, and carries
      slip-vs-intent to its honest terminal (precisely-OPEN, Chris rules intent).

It NEVER resolves slip-vs-intent by fiat if the yaml does not. It NEVER lets an
observed r or n_s enter on the input side (the four r-bands are the theory's own
PROJECTED outputs; observed comparators are forbidden here -- they belong on the
far side of the freeze, in the LiteBIRD falsifier, not in this read).

====================================================================
SPEC  (written BEFORE the read -- the EXT-5 freeze)
====================================================================
PURPOSE
  Read the frozen sigma-map yaml and emit:
    - the operative branch in {T6, T_u, D6, D_u} (or "unread" if the gate is
      absent),
    - the four r-bands (T6 / T_u / D6 / D_u),
    - the n_s window (Planck-centered, near-universal across branches),
    - the convention-independent union falsifier,
    - a provenance hash of the inputs the read consumed.

THE FOUR-BRANCH TABLE (banked v11/v15; FROZEN; PROJECTED outputs, NOT inputs)
  Branches are labelled by two binary conventions:
    T = textbook / standard-reduction normalization   ((D4-2) = 2 denominator)
    D = the D.1 normalization                          ((D-2) = 11 denominator;
                                                         exceeds standard by 81/22)
    subscript 6 = K6-only breathing
    subscript u = uniform breathing across n = (6, 2, 1)

    branch   r-band (x 1e-3, PROJECTED)   n_s
    ------   -------------------------    --------------------------------
    T6       [3.5, 10]                    [0.9643, 0.9679]  (Planck dead-center)
    T_u      [6.1, 17]                    Planck-centered
    D6       [8, 24]                      robust across branches
    D_u      [10, 36]                     robust across branches

  Union falsifier (BOUNDED, convention-INDEPENDENT): if LiteBIRD/CMB-S4 measures
    r OUTSIDE [3.5, 36] x 1e-3, the sigma-inflaton is falsified regardless of
    which normalization convention the geometry uses.

THE READ (what the yaml decides)
  The geometry's *operative* frozen branch is T6 (v10/v11): the band the corpus
  carries forward as the working point. The *source* fact recovered at v15 is
  that D.1.0 (the kinetic-normalization sub-section of Appendix D) DECLARES
  uniform breathing -- and a TEXTBOOK ruling on that declaration lands on T_u
  (r in [6.1, 17] x 1e-3). The two are not the same branch.

  The single remaining inference -- SLIP vs INTENT -- is exactly:
      Was the D.1 denominator ((D-2) = 11, the 81/22 excess) a derivational
      SLIP (a normalization that should have reduced like the textbook (D4-2)=2,
      in which case the operative T6 stands) or the author's INTENT (a genuine
      uniform-breathing normalization, in which case the textbook ruling on
      D.1.0 makes T_u operative)?

  This is left OPEN by rule. The yaml read is what would resolve it: if the
  frozen sigma-map yaml carries an OPERATIVE 'uniform_breathing: true' /
  'kinetic_denominator: D_minus_2_eq_11' as the *declared intent*, the textbook
  ruling lands T_u; if it carries 'K6_only' / standard reduction as operative,
  T6 stands.

ACCEPTANCE  (frozen before the run -- no value is forced)
  We do NOT force a branch. We report machine facts and let the verdict fall out:
    FACT 1: does a frozen sigma-map yaml exist on disk?            -> bool
    FACT 2: if so, what does it declare for breathing-mode?        -> enum / None
    FACT 3: if so, what does it declare for kinetic-denominator?   -> enum / None
    FACT 4: is the declaration OPERATIVE (intent) or merely        -> enum / None
            DESCRIPTIVE (a recorded slip)?
  Then:
    operative_branch :=
       if no yaml                       -> "unread"  (gate PENDING)
       elif yaml operative == uniform   -> "T_u" (textbook ruling on D.1.0)
       elif yaml operative == K6_only   -> "T6"  (frozen operative stands)
       else                             -> "ambiguous" (yaml present but silent
                                                         on slip-vs-intent)

  TERMINAL (one of three; the script computes which):
    resolved-branch-decision-grade :
        the yaml UNAMBIGUOUSLY selects a branch -> deliver that branch's r-band
        at decision grade, with the two PENDING countersigns named.
    precisely-open-slip-vs-intent :
        the yaml is absent OR present-but-silent on slip-vs-intent -> stays
        precisely-OPEN; Chris rules intent; the convention-independent union
        falsifier travels with it.
    refuted :
        an observed r/n_s was detected on the input side (forbidden) -> refuse.

NO-TARGET-LOADING
  No observed A_s, Lambda_obs, r, eta_B, n_s, N_eff, PDG, LiteBIRD/Planck r may
  enter on the input side. The four r-bands and the n_s window are the theory's
  own FROZEN PROJECTED outputs (banked v11/v15), declared before any comparison.
  The script asserts none of the forbidden observational anchors appear in any
  yaml it reads as a derivation input; if one does, it REFUSES (exit 2).

OUTPUTS
  - JSON artifact -> outputs/inflation_sigma_map_read_result.json
  - human-readable decision packet to stdout
  - exit 0 if artifact produced (any honest terminal is a valid outcome)
  - exit 2 if a forbidden observed value is detected on the input side (refuse)

NON-PROMOTION
  No gate flip. No status word emitted for any gate. Countersign-input only.
====================================================================
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUTS = os.path.join(HERE, "outputs")
os.makedirs(OUTPUTS, exist_ok=True)

# ---------------------------------------------------------------------------
# FROZEN, banked PROJECTED outputs (v11/v15). These are the theory's own
# outputs, declared here BEFORE any comparison. They are NOT observed values.
# Source: TOE_FINAL_merged.md / TOE_FINAL (2).md, capsule v11/v15, §IV
# "The four-branch table and the LiteBIRD falsifier (K13-2)".
# ---------------------------------------------------------------------------
FOUR_BRANCH_TABLE = {
    "T6": {
        "convention": "textbook/standard-reduction normalization; K6-only breathing",
        "r_band_x1e3": [3.5, 10.0],
        "n_s": "[0.9643, 0.9679] (Planck dead-center)",
        "standing": "FROZEN operative branch (v10/v11); countersign slot PENDING",
    },
    "T_u": {
        "convention": "textbook normalization; uniform breathing across n=(6,2,1)",
        "r_band_x1e3": [6.1, 17.0],  # v15 source-check sharpening of [6,17]
        "n_s": "Planck-centered",
        "standing": "the branch a TEXTBOOK ruling lands on if D.1.0's "
                    "uniform-breathing declaration is the operative intent (v15)",
    },
    "D6": {
        "convention": "D.1 normalization ((D-2)=11 denominator); K6-only breathing",
        "r_band_x1e3": [8.0, 24.0],
        "n_s": "robust across branches (v11)",
        "standing": "survives current bound r < 0.036 (MEASURED comparator)",
    },
    "D_u": {
        "convention": "D.1 normalization; uniform breathing",
        "r_band_x1e3": [10.0, 36.0],
        "n_s": "robust across branches (v11)",
        "standing": "survives r < 0.036 (MEASURED comparator)",
    },
}

# Convention-independent union falsifier (BOUNDED): r outside this band kills
# the sigma-inflaton regardless of normalization convention.
UNION_FALSIFIER_x1e3 = [3.5, 36.0]

# n_s window, near-universal across branches (Planck dead-center). PROJECTED
# output; the comparator (Planck) is MEASURED and lives only on the far side
# of the freeze -- never an input here.
N_S_WINDOW = [0.9643, 0.9679]

# The two PENDING countersigns the decision-grade terminal must name.
PENDING_COUNTERSIGNS = [
    "C19 slot: kappa_13 closed-form + the four-branch table (v11; PENDING)",
    "C19 slot: sigma-advancement / plateau outputs / E2 second upgrade (v10; PENDING)",
]

# The kinetic-normalization datum, FROZEN, source-confirmed at v15.
K13_2_DATUM = {
    "D_minus_2": 11,            # the D.1 kinetic denominator (verbatim, L10268)
    "D4_minus_2": 2,            # the standard / textbook reduction denominator
    "excess_ratio": "81/22",   # D.1 exceeds standard reduction by exactly this
    "source_line": "L10268 of the corpus reduction appendix (Appendix D, EXTERNAL)",
    "D_1_0_declares": "uniform breathing across n = (6, 2, 1)",
    "lambda_sq": "1/6 = 4/K_sigmasigma, set by the 13D split n=(6,2,1)",
}

# Forbidden observational anchors -- none may enter on the input side.
FORBIDDEN_OBSERVED_KEYS = [
    "A_s", "A_s_central", "A_s_observed",
    "lambda_obs", "Lambda_obs",
    "r_observed", "r_obs", "r_measured", "r_upper", "r_upper_95",
    "eta_B", "eta_b_observed",
    "n_s_observed", "n_s_central", "n_s_measured",
    "N_eff_observed",
    "litebird_r_measured", "planck_r", "bicep_r", "keck_r",
    "PDG", "pdg_gamma",
]

# Canonical search locations for the frozen sigma-map yaml.
CANDIDATE_YAML_PATHS = [
    os.path.join(HERE, "sigma_map.yaml"),
    os.path.join(HERE, "frozen_sigma_map.yaml"),
    os.path.join(HERE, "inputs", "sigma_map.yaml"),
    os.path.normpath(os.path.join(
        HERE, "..", "..", "..", "Final_physics_articles", "scripts",
        "gap_08", "sigma_map.yaml")),
    os.path.normpath(os.path.join(
        HERE, "..", "..", "..", "Final_physics_articles", "scripts",
        "gap_08", "frozen_sigma_map.yaml")),
    os.path.normpath(os.path.join(
        HERE, "..", "..", "..", "Final_physics_articles", "scripts",
        "gap_08", "k13_2_sigma_map.yaml")),
]


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _load_yaml_text(path: str):
    """Return (raw_text, parsed_or_None). Avoids a hard PyYAML dependency."""
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    parsed = None
    try:
        import yaml  # type: ignore
        parsed = yaml.safe_load(raw)
    except Exception:
        parsed = None  # raw text still inspectable for forbidden keys
    return raw, parsed


def _detect_forbidden(raw: str, parsed) -> list:
    """Detect any forbidden observed value used as a DERIVATION INPUT.

    Comparison-surface declarations are allowed only if explicitly flagged
    'comparison_surface: true' / 'observation_windows:'; bare observed keys in
    a derivation block are a refusal.
    """
    hits = []
    lowered = raw.lower()
    # If the yaml explicitly fences observed values as a comparison surface,
    # those occurrences are permitted. We only flag observed keys that appear
    # OUTSIDE such a fence -- conservatively, if no fence marker is present at
    # all but observed keys are, we flag.
    fenced = ("comparison_surface" in lowered) or ("observation_windows" in lowered)
    for key in FORBIDDEN_OBSERVED_KEYS:
        if key.lower() in lowered and not fenced:
            hits.append(key)
    return hits


def _classify_yaml(parsed):
    """From a parsed sigma-map yaml, decide the operative branch.

    Returns (operative_branch, declaration_dict). operative_branch is one of
    {"T6","T_u","D6","D_u","ambiguous"}.
    """
    decl = {
        "breathing_mode": None,    # "uniform" | "K6_only"
        "kinetic_denominator": None,  # "D_minus_2_eq_11" | "standard_D4_minus_2"
        "operative_or_descriptive": None,  # "operative"/"intent" | "descriptive"/"slip"
        "normalization_family": None,  # "T" (textbook) | "D" (D.1)
    }
    if not isinstance(parsed, dict):
        return "ambiguous", decl

    # Be liberal about key spellings the frozen yaml might use.
    def _get(*keys):
        for k in keys:
            if k in parsed:
                return parsed[k]
        return None

    bm = _get("breathing_mode", "breathing", "sigma_breathing")
    if isinstance(bm, str):
        low = bm.lower()
        if "uniform" in low:
            decl["breathing_mode"] = "uniform"
        elif "k6" in low or "k_6" in low or "k6_only" in low:
            decl["breathing_mode"] = "K6_only"

    kd = _get("kinetic_denominator", "kinetic_normalization", "denominator")
    if kd is not None:
        s = str(kd).lower()
        if "11" in s or "d_minus_2" in s or "d-2" in s:
            decl["kinetic_denominator"] = "D_minus_2_eq_11"
        elif "2" in s or "d4" in s or "standard" in s or "textbook" in s:
            decl["kinetic_denominator"] = "standard_D4_minus_2"

    op = _get("declaration_status", "operative", "intent_or_slip",
              "slip_vs_intent")
    if op is not None:
        s = str(op).lower()
        if "operativ" in s or "intent" in s:
            decl["operative_or_descriptive"] = "operative"
        elif "descriptiv" in s or "slip" in s:
            decl["operative_or_descriptive"] = "descriptive"

    nf = _get("normalization", "normalization_family", "reduction")
    if nf is not None:
        s = str(nf).lower()
        if s.startswith("d") or "d.1" in s or "81/22" in s:
            decl["normalization_family"] = "D"
        elif s.startswith("t") or "textbook" in s or "standard" in s:
            decl["normalization_family"] = "T"

    # ---- Branch selection from the declaration. ----
    # A genuine, OPERATIVE uniform-breathing declaration => textbook ruling lands
    # T_u. A K6_only operative declaration => the frozen T6 stands. Anything that
    # leaves the operative-vs-descriptive (slip-vs-intent) axis unstated is
    # ambiguous -- we do NOT resolve it by fiat.
    fam = decl["normalization_family"] or "T"  # textbook ruling is the default
    if decl["operative_or_descriptive"] != "operative":
        return "ambiguous", decl  # yaml present but silent on slip-vs-intent
    if decl["breathing_mode"] == "uniform":
        return ("T_u" if fam == "T" else "D_u"), decl
    if decl["breathing_mode"] == "K6_only":
        return ("T6" if fam == "T" else "D6"), decl
    return "ambiguous", decl


def main() -> int:
    # --- locate the frozen sigma-map yaml ---
    found_path = None
    for p in CANDIDATE_YAML_PATHS:
        if os.path.isfile(p):
            found_path = p
            break

    provenance_parts = []
    # Provenance always includes the frozen banked table + datum (the inputs
    # this read consumes regardless of yaml presence).
    provenance_parts.append(json.dumps(FOUR_BRANCH_TABLE, sort_keys=True))
    provenance_parts.append(json.dumps(K13_2_DATUM, sort_keys=True))
    provenance_parts.append(json.dumps(UNION_FALSIFIER_x1e3))

    yaml_block = {
        "frozen_sigma_map_yaml_found": bool(found_path),
        "searched_paths": CANDIDATE_YAML_PATHS,
        "found_path": found_path,
        "declaration": None,
        "yaml_sha256": None,
        "forbidden_observed_on_input_side": [],
    }

    operative_branch = "unread"
    terminal = "precisely-open-slip-vs-intent"
    slip_vs_intent = (
        "OPEN by rule. The single remaining inference: was the D.1 kinetic "
        "denominator ((D-2)=11, the 81/22 excess) a derivational SLIP (operative "
        "branch stays T6) or the author's uniform-breathing INTENT (textbook "
        "ruling on D.1.0 makes T_u operative)? Not resolved here; Chris rules "
        "intent. The convention-independent union falsifier travels with it."
    )

    if found_path:
        raw, parsed = _load_yaml_text(found_path)
        provenance_parts.append(raw)
        yaml_block["yaml_sha256"] = _sha256_text(raw)

        forbidden = _detect_forbidden(raw, parsed)
        yaml_block["forbidden_observed_on_input_side"] = forbidden
        if forbidden:
            # REFUSE: an observed value entered on the input side.
            result = {
                "script": "inflation_sigma_map_read.py",
                "gap": "08 / K13-2 (sigma-kinetic normalization)",
                "terminal_reached": "refuted",
                "branch_verdict": "ambiguous",
                "refusal_reason": (
                    "forbidden observed value(s) detected on the input side of "
                    "the sigma-map yaml: %s" % ", ".join(forbidden)
                ),
                "no_target_loading_attest": "FAIL -- refused at exit 2",
            }
            _write(result)
            print(json.dumps(result, indent=2))
            return 2

        operative_branch, decl = _classify_yaml(parsed)
        yaml_block["declaration"] = decl
        if operative_branch in ("T6", "T_u", "D6", "D_u"):
            terminal = "resolved-branch-decision-grade"
            slip_vs_intent = (
                "RESOLVED by the frozen sigma-map yaml: it carries an OPERATIVE "
                "declaration (%s breathing; %s normalization), so the textbook "
                "ruling lands branch %s. Decision grade -- two countersigns "
                "still PENDING." % (
                    decl.get("breathing_mode"),
                    decl.get("normalization_family") or "T",
                    operative_branch,
                )
            )
        else:
            # yaml present but silent on slip-vs-intent -> stays precisely-OPEN
            operative_branch = "unread"
            terminal = "precisely-open-slip-vs-intent"

    provenance_hash = _sha256_text("\n".join(provenance_parts))

    selected_band = None
    if operative_branch in FOUR_BRANCH_TABLE:
        selected_band = {
            "branch": operative_branch,
            "r_band_x1e3": FOUR_BRANCH_TABLE[operative_branch]["r_band_x1e3"],
            "n_s": FOUR_BRANCH_TABLE[operative_branch]["n_s"],
        }

    result = {
        "script": "inflation_sigma_map_read.py",
        "gap": "08 / K13-2 (sigma-kinetic normalization)",
        "run_purpose": (
            "Read the frozen sigma-map yaml; select the operative branch; emit "
            "the four r-bands + n_s window + convention-independent union "
            "falsifier + provenance hash. Countersign-input only; no gate flip."
        ),
        "terminal_reached": terminal,
        "operative_branch": operative_branch,
        "branch_verdict": operative_branch if operative_branch != "unread" else "T_u_textbook_vs_T6_operative_UNRESOLVED",
        "selected_branch_band": selected_band,
        "four_branch_table": FOUR_BRANCH_TABLE,
        "n_s_window": N_S_WINDOW,
        "n_s_note": "Planck-centered, near-universal across branches (PROJECTED "
                    "output; comparator is MEASURED and lives only past the freeze)",
        "union_falsifier": {
            "r_band_x1e3": UNION_FALSIFIER_x1e3,
            "statement": "If LiteBIRD/CMB-S4 measures r outside [3.5, 36]x1e-3, "
                         "the sigma-inflaton is falsified regardless of "
                         "normalization convention (BOUNDED, convention-INDEPENDENT).",
        },
        "k13_2_datum": K13_2_DATUM,
        "frozen_textbook_ruling": (
            "D.1.0 declares uniform breathing => a TEXTBOOK ruling lands on T_u "
            "(r in [6.1, 17]x1e-3, n_s Planck-centered). The FROZEN operative "
            "branch carried by the corpus is T6 (r in [3.5, 10]x1e-3). The gap "
            "between 'frozen operative = T6' and 'textbook ruling = T_u' IS the "
            "slip-vs-intent question."
        ),
        "slip_vs_intent": slip_vs_intent,
        "pending_countersigns": PENDING_COUNTERSIGNS,
        "what_requires_chris": (
            "Chris rules slip-vs-intent: whether the D.1 denominator ((D-2)=11) "
            "is a slip (T6 operative) or intent (T_u operative). The loop may "
            "NOT resolve this by fiat. Plus the two PENDING countersigns above."
        ),
        "yaml": yaml_block,
        "provenance_hash_sha256": provenance_hash,
        "no_target_loading_attest": (
            "PASS -- no observed A_s/Lambda_obs/r/eta_B/n_s/N_eff/PDG/LiteBIRD/"
            "Planck r entered on the input side. The four r-bands and the n_s "
            "window are the theory's own FROZEN PROJECTED outputs (banked "
            "v11/v15), declared before any comparison."
        ),
        "non_promotion": "No gate flip; no status word emitted; countersign-input only.",
    }
    _write(result)
    print(json.dumps(result, indent=2))
    return 0


def _write(result: dict) -> None:
    out_path = os.path.join(OUTPUTS, "inflation_sigma_map_read_result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    sys.exit(main())
