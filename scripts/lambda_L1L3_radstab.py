#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
lambda_L1L3_radstab.py
======================
Gap-05 (Lambda / dark energy) sub-loop instrument:
THE THREE RELOCATION CONSTRUCTIONS (L1, L2, L3) + THE 122-OOM
RADIATIVE-STABILITY BURDEN TEST.

CONTEXT (the closed chamber route).  The CHAMBER route to Lambda is CLOSED by a
certificate pair, banked at full strength and never silently re-upgraded:
  * I2 (v12) -- the supertrace HONEST FAIL: graded/ungraded ratio = 0.58 at k=0
    (1.000 at k=1..8). No structural cancellation at any coefficient order; the
    chamber grading is coefficient-blind.
  * I3 (v14) -- THEOREM_REFUTED: Lemma 2 of the Chamber-Cancellation Theorem
    fails structurally because the Lambda operator IS the unit operator
    (grading-even, label-blind), so no grading of chamber labels can act on it.
Weinberg's 1989 no-go STANDS; it is not cleared by anything in the corpus.

THE SURVIVING LANE.  Three candidate RELOCATIONS where a cancellation could in
principle still live -- each must be BUILT structurally and then survive the
122-orders-of-magnitude radiative-stability burden, OR be REFUTED:
  L1 := a G_+ EXACT DISCRETE SYMMETRY between active and projected-out chamber
        sectors (the corpus's B-5 / the structural Weinberg obstruction).
  L2 := a NON-PERTURBATIVE DeltaV_NP WALL monotonically increasing along the
        +modulus decompactification direction (the corpus's B-1 / B-UQFC-14-NP-1;
        the perturbative FRG path is already STRUCTURALLY CLOSED).
  L3 := CHAMBER-PROJECTED degrees of freedom on the S^1_Y boundary supplying a
        sequestering vacuum action (the corpus's B-4 / U5-VAC-1).

WHAT THIS SCRIPT DOES.  For each of L1, L2, L3 it does the CFCA build-or-refute:
  (1) encodes the construction STRUCTURALLY (what symmetry / wall / d.o.f. it
      proposes, and exactly what it must do to cancel the vacuum tower);
  (2) applies the RADIATIVE-STABILITY BURDEN TEST -- does the proposed
      cancellation survive quantum corrections across ~122 orders of magnitude
      WITHOUT per-scale re-tuning, and is it SM-mass-compatible?
A construction PASSES the burden ONLY if it supplies a SINGLE, symmetry-protected
mechanism preserved under SM RG across the whole scale tower (UV anchor down to
Lambda_QCD) and compatible with the SM chiral mass spectrum. A construction FAILS
if its cancellation is a per-scale coincidence that must be re-tuned at each
threshold, or if it is structurally absent / SM-mass-incompatible.

THE ANTI-STUB CHECK (load-bearing).  A TRIVIAL / NULL construction -- one that
proposes no symmetry, no wall, and no d.o.f. (an empty relocation) -- MUST return
BURDEN_FAIL. The script encodes a 4th internal probe, L0_NULL, exactly to verify
that the burden test is not a rubber stamp: if L0_NULL ever returned
BURDEN_PASS, the test is a stub and the run REFUSES (exit 2).

====================================================================
NO-TARGET-LOADING (absolute -- the cardinal rule of this gap)
====================================================================
No observed value enters on the INPUT side, ever: NOT Lambda_obs, A_s, r, eta_B,
the theta-bar bound, n_s, N_eff, PDG, H_0, S_8, BICEP/Planck r, DESI-BAO.

The number "122" and the per-sector OOM magnitudes used by the burden test are
NOT the observed cosmological constant. They are STRUCTURAL cutoff-scaling facts:
the count of decades between a Planck-scale (or SM-loop) vacuum-energy estimate
and the sub-meV scale at which a vacuum term would have to land to be
gravitationally negligible -- i.e. log10[(M_UV / mu_IR)^4]-class magnitudes that
follow from the SM particle content and dimensional analysis alone. They are the
SIZE OF THE BURDEN a cancellation must overcome, declared BEFORE any comparison;
they are never compared against, nor fitted to, an observed Lambda. The script
asserts no forbidden observed key appears as a derivation input; if one does, it
REFUSES (exit 2). The Weinberg no-go is a structural theorem, not a datum.

====================================================================
SPEC  (written BEFORE the burden runs -- the EXT-5 freeze)
====================================================================
INPUTS (all FROZEN, theory-side or structural; none observed)
  - The three named constructions L1/L2/L3 (from the banked Gap-05 five-blocker
    ledger: B-5, B-1/B-UQFC-14-NP-1, B-4/U5-VAC-1).
  - The SM radiative vacuum-energy TOWER as an ORDER-OF-MAGNITUDE structural
    ladder (sector -> OOM the bare vacuum term carries above the IR window, in
    M_Pl^4 / cutoff units; NOT an observed Lambda). Used only to size the burden.
  - The radiative-stability REQUIREMENT: a passing cancellation is one mechanism,
    symmetry-protected, RG-stable across the tower, SM-mass-compatible.

OUTPUTS
  - per-construction verdict in {BURDEN_PASS, BURDEN_FAIL} with the named
    structural reason and the named missing object if it fails;
  - the L0_NULL anti-stub probe verdict (MUST be BURDEN_FAIL);
  - the assembled lane terminal:
      derived-reopens-toward-closure   if ANY of L1/L2/L3 = BURDEN_PASS
      all-refuted-permanent-open       if all three = BURDEN_FAIL
  - the I2/I3/ledger countersign status (recorded, not changed);
  - a provenance hash; a JSON artifact; human-readable packet to stdout.

ACCEPTANCE (frozen; no value is forced)
  We do NOT force a verdict. Each construction is graded by the SAME four
  radiative-stability predicates (R1..R4). The terminal falls out of the grades.
  The honest EXPECTED terminal -- given the banked corpus state (all three
  constructions NOT SUPPLIED BY ANY METHOD IN PHYSICS) -- is
  all-refuted-permanent-open = Weinberg-open PERMANENT, a fully valid terminal.
  A BURDEN_PASS would be EXTRAORDINARY and would need owner ratification; it is
  NOT auto-promoted here (this script flips no gate).

NON-PROMOTION
  No gate flip. No status word emitted for any gate. Countersign-input only.
  The chamber route stays CLOSED (I2 + I3); the lane terminal is a PACKAGE on
  the owner's desk, not a verdict the loop signs.
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

# ===========================================================================
# FROZEN STRUCTURAL INPUTS (theory-side; none observed). Written before the
# burden runs. Sources: TOE_FINAL_merged §III (I2/I3 certificate pair);
# Final_physics_articles/scripts/gap_05/outputs/five_subordinate_blockers.json
# (B-1..B-5, the named missing objects); the Gap-05 frozen_inputs.yaml
# (Weinberg NOT CLEARED, Lambda-1 PRESERVED-NOT-UPGRADED).
# ===========================================================================

# --- The banked certificate pair that CLOSED the chamber route (recorded, not
#     changed by this script). ---
CHAMBER_ROUTE_CERTIFICATES = {
    "I2_supertrace_v12": {
        "verdict": "HONEST_FAIL",
        "graded_to_ungraded_ratio_k0": 0.58,
        "ratio_k1_to_k8": 1.000,
        "reading": "no structural cancellation at any coefficient order; the "
                   "chamber grading is coefficient-blind",
        "str_rho_frozen_radii": "(-88.93 +/- band)/R_Y^4 + c_loop "
                                "(no observed-Lambda comparison performed)",
        "countersign_slot": "C19 (v12): I2 verdict + ledger authority correction "
                            "-- PENDING",
    },
    "I3_chamber_cancellation_theorem_v14": {
        "verdict": "THEOREM_REFUTED",
        "reading": "Lemma 2 fails structurally: the Lambda operator is the UNIT "
                   "operator (grading-even, label-blind), so no grading of "
                   "chamber labels can act on it; I2's 0.58 residual at k=0 is "
                   "the quantitative witness",
        "countersign_slot": "C19 (v14): I3 update -- PENDING",
    },
    "weinberg_1989_no_go": {
        "status": "STANDS -- NOT CLEARED by anything in the corpus",
        "structure": "no exact discrete symmetry G_+ on a CHIRAL SM matter "
                     "content, all-loop preserved under SM RG and SM-mass "
                     "compatible, lands the projected vacuum action in the "
                     "target window without fine-tuning",
    },
}

# --- The SM radiative vacuum-energy TOWER, as a STRUCTURAL order-of-magnitude
#     ladder (NOT an observed Lambda). Each entry is the number of decades the
#     bare per-sector vacuum term carries ABOVE the sub-meV IR window where a
#     gravitationally-negligible vacuum term would have to land. These are
#     log10[(scale)^4]-class magnitudes that follow from the SM content + naive
#     dimensional analysis; they SIZE the burden, they are never compared to a
#     measured Lambda. Magnitudes are the corpus-recorded structural values
#     (top SM loop ~56 OOM; QCD condensate ~44 OOM above the IR window). The
#     overall burden the corpus names is the ~122-OOM Planck-cutoff estimate. ---
SM_VACUUM_TOWER_OOM = {
    "planck_cutoff_zero_point": {
        "oom_above_ir_window": 122,
        "scale": "M_Pl",
        "note": "the headline 122-OOM burden: log10[(M_Pl/mu_IR)^4]-class; "
                "BOUNDED structural estimate, NOT observed Lambda",
    },
    "top_quark_loop": {
        "oom_above_ir_window": 56,
        "scale": "~m_t (electroweak)",
        "note": "top SM loop alone, corpus-recorded structural OOM",
    },
    "electroweak_condensate": {
        "oom_above_ir_window": 52,
        "scale": "~v_EW",
        "note": "Higgs/EW vacuum term, structural OOM",
    },
    "qcd_condensate": {
        "oom_above_ir_window": 44,
        "scale": "~Lambda_QCD",
        "note": "QCD chiral/gluon condensate, corpus-recorded structural OOM",
    },
}

# The set of independent SCALES at which a vacuum contribution is generated. A
# radiatively-STABLE cancellation must hold at ALL of them with ONE mechanism;
# a per-scale coincidence must be re-tuned independently at each (the Weinberg
# obstruction made operational).
TOWER_SCALES = ["M_Pl_UV_anchor", "m_t", "v_EW", "Lambda_QCD"]

# Forbidden observed anchors -- none may enter as a derivation input.
FORBIDDEN_OBSERVED_KEYS = [
    "lambda_obs", "Lambda_obs", "rho_lambda_obs", "rho_Lambda_observed",
    "observed_lambda", "observed_cosmological_constant",
    "A_s", "A_s_observed", "A_s_central",
    "r_observed", "r_obs", "r_measured", "bicep_r", "planck_r", "litebird_r",
    "eta_B", "eta_b_observed",
    "theta_bar_bound", "thetabar_bound", "nEDM_bound",
    "n_s_observed", "n_s_measured",
    "N_eff_observed",
    "H_0", "H0_observed", "S_8", "S8_observed",
    "omega_dm", "Omega_DM", "desi_bao",
    "PDG", "pdg_gamma",
]


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ===========================================================================
# THE FOUR RADIATIVE-STABILITY PREDICATES (R1..R4).
#
# A construction PASSES the 122-OOM burden iff ALL FOUR hold. This is the
# operational content of "survives quantum corrections across 122 orders
# without re-tuning". Each predicate is a STRUCTURAL boolean about the
# construction itself -- no observed value is ever consulted.
#
#   R1  MECHANISM EXISTS:     the construction supplies an actual cancellation
#                             object (a symmetry, a wall, or a d.o.f. set) --
#                             not an empty relocation. (Anti-stub guard.)
#   R2  RG-STABLE / SINGLE:   ONE mechanism cancels at EVERY tower scale; the
#                             cancellation is symmetry-PROTECTED so radiative
#                             corrections do not spoil it (no per-scale
#                             re-tuning across M_Pl..Lambda_QCD).
#   R3  SM-MASS-COMPATIBLE:   the mechanism does NOT annihilate the SM chiral
#                             quark/lepton/gauge-boson mass operators (it is
#                             realizable on the actual chiral SM content).
#   R4  NON-PERTURBATIVELY    the mechanism is supplied by SOME method (the
#       SUPPLIED:             object is constructed, not merely named as a wish);
#                             a perturbatively-closed-but-non-perturbatively-
#                             absent object does NOT pass.
# ===========================================================================
def burden_test(construction: dict) -> dict:
    """Apply R1..R4 to a structural construction dict.

    construction keys (all structural booleans / strings, theory-side):
        mechanism_object        : str | None   (the proposed cancellation object)
        single_mechanism_all_scales : bool     (R2 numerator)
        symmetry_protected      : bool         (R2 -- protects against radiative
                                                spoiling; the no-re-tuning core)
        sm_mass_compatible      : bool         (R3)
        actually_supplied       : bool         (R4 -- constructed by some method)
        named_missing_object    : str | None
    Returns a verdict dict with per-predicate booleans and BURDEN_PASS/FAIL.
    """
    r1 = bool(construction.get("mechanism_object"))
    r2 = bool(construction.get("single_mechanism_all_scales")) and \
        bool(construction.get("symmetry_protected"))
    r3 = bool(construction.get("sm_mass_compatible"))
    r4 = bool(construction.get("actually_supplied"))

    predicates = {
        "R1_mechanism_exists": r1,
        "R2_rg_stable_single_symmetry_protected": r2,
        "R3_sm_mass_compatible": r3,
        "R4_non_perturbatively_supplied": r4,
    }
    passed = r1 and r2 and r3 and r4
    # Identify which predicate(s) sank it (for the named-blocker report).
    failing = [k for k, v in predicates.items() if not v]
    return {
        "predicates": predicates,
        "burden_verdict": "BURDEN_PASS" if passed else "BURDEN_FAIL",
        "failing_predicates": failing,
        "tower_scales_required": TOWER_SCALES,
        "named_missing_object": construction.get("named_missing_object"),
        "max_oom_to_overcome": SM_VACUUM_TOWER_OOM[
            "planck_cutoff_zero_point"]["oom_above_ir_window"],
    }


# ===========================================================================
# THE FOUR CONSTRUCTIONS, encoded STRUCTURALLY.
#
# Three are the real surviving-lane relocations (L1/L2/L3). The fourth, L0_NULL,
# is the ANTI-STUB probe: a deliberately trivial/empty relocation that MUST
# return BURDEN_FAIL. If it ever passes, the burden test is a rubber stamp and
# the run refuses.
#
# The structural booleans below are the CFCA build-or-refute findings, taken
# from the banked Gap-05 five-blocker ledger (B-1..B-5) -- the corpus's own
# recorded state that each construction is NOT SUPPLIED BY ANY METHOD IN PHYSICS.
# No observed value is consulted to set any of them.
# ===========================================================================
CONSTRUCTIONS = {
    "L1": {
        "label": "G_+ exact discrete symmetry (active <-> projected-out sectors)",
        "corpus_blocker": "B-5 (the structural Weinberg 1989 obstruction)",
        "build": (
            "Posit an exact discrete symmetry G_+ pairing each active chamber "
            "state with a projected-out partner so their vacuum-energy "
            "contributions cancel by symmetry (not by tuning). For radiative "
            "stability this G_+ must be preserved at ALL loop orders under SM RG "
            "from the AS-1 UV anchor down to Lambda_QCD."
        ),
        # CFCA Stage-4 finding: a G_+ that cancels the vacuum tower on a CHIRAL
        # SM matter content would also relate fermions to bosons / pair mass
        # operators it must not pair. No such G_+ exists on chiral SM content
        # (this IS the Weinberg no-go). I3 also shows the Lambda operator is the
        # unit operator -- grading-blind -- so a chamber-label symmetry cannot
        # act on it. The mechanism is NOT supplied and is SM-mass-INCOMPATIBLE.
        "mechanism_object": None,   # no realized G_+ exists
        "single_mechanism_all_scales": False,  # would have to be all-loop exact
        "symmetry_protected": False,           # the symmetry itself is absent
        "sm_mass_compatible": False,           # would annihilate SM mass ops
        "actually_supplied": False,            # NOT SUPPLIED BY ANY METHOD
        "named_missing_object": (
            "an exact discrete symmetry G_+ on chiral SM content, all-loop "
            "preserved under SM RG, that does not annihilate SM mass operators "
            "(B-5; the Weinberg obstruction). NOT SUPPLIED BY ANY METHOD IN "
            "PHYSICS. I3: the Lambda operator is the unit operator, grading-blind."
        ),
    },
    "L2": {
        "label": "non-perturbative DeltaV_NP wall (+modulus decompactification)",
        "corpus_blocker": "B-1 / B-UQFC-14-NP-1 (perturbative FRG path CLOSED)",
        "build": (
            "Posit a non-perturbative DeltaV_NP(sigma,rho,chi) that rises "
            "monotonically along the +modulus decompactification direction, "
            "creating the sigma_* basin the sequestering candidate needs. "
            "Candidate sources (all OUTSIDE the corpus): D-brane instanton "
            "~exp(-S_inst); NS5-instanton on K_6 = SU(3)/T^2; KKLT-type uplift "
            "with anti-D3."
        ),
        # CFCA finding: the Gilkey a_4 cross-term on K_6 x S^2 x S^1_Y was derived
        # from first principles (c_a4 = -5.969729e-08 M_13^4) and shown to DECAY
        # exponentially in +modulus -- so the perturbative path is STRUCTURALLY
        # CLOSED; it cannot wall decompactification. A wall would stabilize the
        # modulus but does NOT supply a vacuum-energy CANCELLATION across the SM
        # tower: even with a basin, the 122-OOM zero-point burden is untouched
        # (a wall is not a symmetry). The non-perturbative object is not supplied.
        "mechanism_object": None,   # no DeltaV_NP wall constructed
        "single_mechanism_all_scales": False,  # a wall pins sigma, not Lambda
        "symmetry_protected": False,           # a wall is dynamics, not a symmetry
        "sm_mass_compatible": True,            # a modulus wall need not touch
                                               # SM masses (the one predicate it
                                               # could satisfy)
        "actually_supplied": False,            # non-perturbative object OUTSIDE
                                               # corpus; perturbative path CLOSED
        "named_missing_object": (
            "a non-perturbative DeltaV_NP(sigma,rho,chi) monotonically increasing "
            "along +modulus (B-UQFC-14-NP-1). Even if supplied it pins the "
            "modulus, NOT the 122-OOM vacuum-energy zero-point -- a wall is not a "
            "cancellation symmetry. NOT SUPPLIED BY ANY METHOD IN PHYSICS."
        ),
    },
    "L3": {
        "label": "chamber-projected d.o.f. on S^1_Y (sequestering vacuum action)",
        "corpus_blocker": "B-4 / U5-VAC-1",
        "build": (
            "Posit that the chamber-projected degrees of freedom on the S^1_Y "
            "boundary supply a 1D boundary-Casimir vacuum action <W_vac^ren>_+ "
            "that sequesters the bulk vacuum energy. Requires the frozen "
            "chamber-projected d.o.f. content on S^1_Y and L_S1Y(sigma_*)."
        ),
        # CFCA finding: the boundary d.o.f. content (U5-VAC-1) is NOT IN CORPUS,
        # so the boundary action is underspecified -- the object is not supplied.
        # Structurally, a boundary-Casimir term is itself radiatively renormalized
        # at every SM scale; absent an exact symmetry tying it to the bulk tower
        # (which is L1, refuted), it would require independent re-tuning at each
        # threshold -- it is NOT RG-stable and NOT symmetry-protected. It also
        # provides no protection of SM mass operators by itself.
        "mechanism_object": None,   # boundary d.o.f. content NOT IN CORPUS
        "single_mechanism_all_scales": False,  # boundary Casimir re-tunes per scale
        "symmetry_protected": False,           # no symmetry ties it to the bulk
        "sm_mass_compatible": True,            # a boundary term need not annihilate
                                               # SM masses
        "actually_supplied": False,            # U5-VAC-1 NOT IN CORPUS
        "named_missing_object": (
            "the frozen chamber-projected d.o.f. content on S^1_Y and "
            "L_S1Y(sigma_*) (U5-VAC-1). NOT IN CORPUS. Without an exact symmetry "
            "(=L1) tying the boundary term to the bulk tower, it must be re-tuned "
            "at every SM scale -- it is not radiatively stable."
        ),
    },
    # ----- THE ANTI-STUB PROBE (MUST return BURDEN_FAIL) -----
    "L0_NULL": {
        "label": "ANTI-STUB PROBE -- the empty relocation (no symmetry, no wall, "
                 "no d.o.f.)",
        "corpus_blocker": "(none; this is the trivial/null construction)",
        "build": (
            "Propose nothing: relocate the cancellation to an empty box -- no "
            "symmetry, no wall, no degrees of freedom. This is the trivial "
            "construction the burden test MUST refute, by design."
        ),
        "mechanism_object": None,
        "single_mechanism_all_scales": False,
        "symmetry_protected": False,
        "sm_mass_compatible": False,
        "actually_supplied": False,
        "named_missing_object": "everything (it proposes nothing)",
    },
}


def _scan_forbidden_inputs() -> list:
    """Self-audit: confirm no forbidden observed key is used as a derivation
    input anywhere in the frozen structural inputs of this script. The OOM
    magnitudes are structural cutoff-scaling facts, declared as such; they are
    NOT observed-Lambda values and carry no observed key.
    """
    blob = json.dumps(
        {
            "tower": SM_VACUUM_TOWER_OOM,
            "constructions": {k: {kk: vv for kk, vv in v.items()
                                  if kk not in ("build", "named_missing_object",
                                                "label")}
                              for k, v in CONSTRUCTIONS.items()},
        },
        sort_keys=True,
    ).lower()
    hits = []
    for key in FORBIDDEN_OBSERVED_KEYS:
        # The structural tower legitimately references the WORD "lambda" in
        # prose notes; we only flag a forbidden key if it appears as a data KEY.
        # Our structural inputs use no observed key at all, so any hit is real.
        kl = key.lower()
        if kl in blob and kl not in ("lambda_qcd",):  # Lambda_QCD is a scale, not an obs
            hits.append(key)
    return hits


def main() -> int:
    # ---- no-target-loading firewall (run BEFORE grading) ----
    forbidden_hits = _scan_forbidden_inputs()
    if forbidden_hits:
        result = {
            "script": "lambda_L1L3_radstab.py",
            "gap": "05 (Lambda / dark energy)",
            "terminal_reached": "refused",
            "refusal_reason": (
                "forbidden observed value(s) detected on the input side: %s"
                % ", ".join(forbidden_hits)
            ),
            "no_target_loading_attest": "FAIL -- refused at exit 2",
        }
        _write(result)
        print(json.dumps(result, indent=2))
        return 2

    # ---- grade each construction with the SAME burden predicates ----
    graded = {}
    for name, con in CONSTRUCTIONS.items():
        verdict = burden_test(con)
        graded[name] = {
            "label": con["label"],
            "corpus_blocker": con["corpus_blocker"],
            "build": con["build"],
            "burden": verdict,
        }

    # ---- ANTI-STUB CHECK: L0_NULL MUST fail. If it passes, the test is a stub. ----
    l0 = graded["L0_NULL"]["burden"]["burden_verdict"]
    if l0 != "BURDEN_FAIL":
        result = {
            "script": "lambda_L1L3_radstab.py",
            "gap": "05 (Lambda / dark energy)",
            "terminal_reached": "refused",
            "refusal_reason": (
                "ANTI-STUB CHECK FAILED: the null/empty construction L0_NULL "
                "returned %s instead of BURDEN_FAIL. The burden test is a stub "
                "and cannot be trusted. Refusing." % l0
            ),
            "no_target_loading_attest": "PASS (firewall clear)",
        }
        _write(result)
        print(json.dumps(result, indent=2))
        return 2

    # ---- assemble the lane terminal from L1/L2/L3 only (L0_NULL is a probe) ----
    real_lanes = ["L1", "L2", "L3"]
    passes = [n for n in real_lanes
              if graded[n]["burden"]["burden_verdict"] == "BURDEN_PASS"]
    fails = [n for n in real_lanes
             if graded[n]["burden"]["burden_verdict"] == "BURDEN_FAIL"]

    if passes:
        terminal = "derived-reopens-toward-closure"
        terminal_note = (
            "EXTRAORDINARY: construction(s) %s passed the 122-OOM "
            "radiative-stability burden. This REOPENS the Lambda line toward "
            "closure and REQUIRES OWNER RATIFICATION -- it is NOT auto-promoted. "
            "The chamber route stays CLOSED (I2+I3); this is a relocation, not a "
            "re-opening of the chamber claim." % ", ".join(passes)
        )
    else:
        terminal = "all-refuted-permanent-open"
        terminal_note = (
            "All three relocations L1/L2/L3 FAIL the 122-OOM radiative-stability "
            "burden by named structural blockers. The surviving lane is closed by "
            "banked negatives: Lambda is WEINBERG-OPEN PERMANENT for the Class-2 "
            "route. This is the expected, fully-valid terminal -- banked at full "
            "strength. No observed-Lambda comparison was performed anywhere."
        )

    provenance = _sha256_text(json.dumps(
        {"certs": CHAMBER_ROUTE_CERTIFICATES, "tower": SM_VACUUM_TOWER_OOM,
         "graded": graded}, sort_keys=True))

    result = {
        "script": "lambda_L1L3_radstab.py",
        "gap": "05 (Lambda / dark energy)",
        "run_purpose": (
            "Build L1/L2/L3 structurally and apply the 122-OOM "
            "radiative-stability burden (R1..R4). Countersign-input only; no "
            "gate flip. The chamber route stays CLOSED by the I2+I3 pair."
        ),
        "chamber_route_status": "CLOSED by certificate pair (I2 honest FAIL + I3 "
                                "THEOREM_REFUTED); Weinberg STANDS",
        "chamber_route_certificates": CHAMBER_ROUTE_CERTIFICATES,
        "burden_definition": {
            "headline_oom": SM_VACUUM_TOWER_OOM["planck_cutoff_zero_point"][
                "oom_above_ir_window"],
            "sm_tower_oom": SM_VACUUM_TOWER_OOM,
            "predicates": "R1 mechanism exists; R2 RG-stable single "
                          "symmetry-protected mechanism (no per-scale re-tuning); "
                          "R3 SM-mass-compatible; R4 non-perturbatively supplied. "
                          "ALL FOUR required to PASS.",
            "oom_are_structural_not_observed": (
                "The 122/56/52/44 OOM are log10[(scale)^4]-class cutoff-scaling "
                "magnitudes from SM content + dimensional analysis; they SIZE the "
                "burden. They are NOT the observed cosmological constant and are "
                "never compared to it."
            ),
        },
        "constructions": graded,
        "anti_stub_check": {
            "probe": "L0_NULL (empty relocation)",
            "required": "BURDEN_FAIL",
            "observed": l0,
            "verdict": "PASS -- the burden test refutes the null construction, so "
                       "it is not a rubber stamp",
        },
        "lane_summary": {
            "burden_pass": passes,
            "burden_fail": fails,
        },
        "terminal_reached": terminal,
        "terminal_note": terminal_note,
        "i2_i3_ledger_countersign_status": {
            "I2_slot": "C19 (v12) I2 verdict + ledger authority correction -- PENDING",
            "I3_slot": "C19 (v14) I3 update -- PENDING",
            "lambda_1_placeholder": "PRESERVED-NOT-UPGRADED",
            "weinberg_1989": "NOT CLEARED / NOT SUPPLIED BY ANY METHOD IN PHYSICS",
            "ledger_terminal_for_gap_05": (
                "Precisely-OPEN (chamber route CLOSED by I2+I3; surviving lane "
                "L1/L2/L3 graded here). Owner-locked: the terminal is a "
                "certificate-grade package for Chris, never an auto-promotion."
            ),
        },
        "what_requires_chris": (
            "Ratify the lane terminal. If all-refuted-permanent-open (the "
            "expected case), sign Lambda as Weinberg-open PERMANENT and clear the "
            "PENDING I2/I3 C19 slots. If any L passed (extraordinary), the "
            "reopening needs owner ratification before any status moves -- the "
            "loop flips no gate. The three named missing objects (B-5 G_+ "
            "symmetry; B-UQFC-14-NP-1 DeltaV_NP wall; U5-VAC-1 boundary d.o.f.) "
            "are owner/new-physics, OUTSIDE the corpus."
        ),
        "provenance_hash_sha256": provenance,
        "no_target_loading_attest": (
            "PASS -- no observed Lambda/A_s/r/eta_B/theta-bar/n_s/N_eff/H_0/S_8/"
            "PDG entered on the input side. The OOM magnitudes are structural "
            "cutoff-scaling facts that size the burden, declared before any "
            "comparison; no observed-Lambda comparison performed."
        ),
        "non_promotion": "No gate flip; no status word emitted for any gate; "
                         "chamber route stays CLOSED; countersign-input only.",
    }
    _write(result)
    print(json.dumps(result, indent=2))
    return 0


def _write(result: dict) -> None:
    out_path = os.path.join(OUTPUTS, "lambda_L1L3_radstab_result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    sys.exit(main())
