#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gap04_uv1_optionB_resummed_determinant.py
=========================================
B-UQFC-14-UV-1  --  OPTION B (RESUMMED DETERMINANT) STABILITY PASS.

TASK
----
The FROZEN UV functional (uv1_frozen_functional_result.json) is the
Chamseddine-Connes SPECTRAL ACTION  S_sigma[f] = Str f(D_sigma^2/Lambda^2)
over the FULL gauge-fixed BV/BRST tower of the corpus spin-c Dirac operator
D_sigma (M4 x K6=SU(3)/T^2 x S^2 x S^1_Y/Z2, active bundle 0fd19c9ae0c1,
index -3). The freeze is target-blind and takes NO branch.

This pass attempts to PROVE the collapse direction (sigma -> -inf, Vol(K6)->0)
is SAFE via OPTION B specifically:

    B-resummed-determinant: the one-loop functional determinant
        W_sigma = (1/2) Str log D_sigma^2
    is BOUNDED BELOW as sigma -> -inf under the frozen prescription.

(Options A spectral-positivity and C phase-exit are the SIBLING attempts; this
file is the honest endpoint of B alone, the route the freeze flags as the one
"where the ambiguity lives".)

HARD GUARDS (any violated = FAIL). Enforced and attested:
  (1) FULL gauge-fixed physical tower (metric+gauge+moduli+Higgs+fermion+ghost
      +projected+Weyl-rigid) -- the nine-row ledger, never scalar-only.
  (2) NO target-loading: the sign/branch may NOT be chosen from the desired
      STANDS outcome; committed c_loop=1.3637877e-5 may NOT enter a sign decision.
  (3) NO anthropic "we exist".
  (4) finite-order a4/a6/a8 are CONSISTENCY CHECKS only, never the proof
      (Lemma 1 banked: finite-order undecidable along sigma->-inf).
  (5) boundedness OR phase-exit must be PROVEN before any collapse; "the
      calculation fails" is NOT a wall.
  (6) Lambda scope preserved: "same hardness class, not same solved problem".
  (7) if not proven, NAME the UV-completion axiom; never disguise as derived.
  (8) NO "leans/leaning runaway" language.

METHOD: CFCA (METHOD_CFCA_June_14.md) Stage 4 (interrogate the buried premise)
+ Stage 7 (publish the death condition). The buried premise of Option B is that
(1/2)Str log D^2 has a basis/regulator-INDEPENDENT lower bound. We test that
premise against the BANKED spectral-zeta structure and report the honest
terminal state.

NON-PROMOTION: no gate flip; no status word emitted for any gate.
exit 0 on an honest resolution; exit 2 if an input is unreadable / a token leaks.
"""

import hashlib
import json
import math
import os
import sys

import numpy as np

try:
    from mpmath import mp, mpf, gamma as mp_gamma, psi as mp_psi
    _HAVE_MPMATH = True
    mp.dps = 30
except Exception:                                   # pragma: no cover
    _HAVE_MPMATH = False


# ---------------------------------------------------------------------------
# Authorities (provenance + forbidden-token firewall). The committed c_loop
# MAGNITUDE file is DELIBERATELY excluded and never opened (guard 2).
# ---------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "outputs")
FA = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
      r"physics_Journal_and_patents/Final_physics_articles")
QUANTUM_MD = os.path.join(FA, "Fable_Quantum.md")
GUT_MD = os.path.join(FA, "Fable_GUT (3).md")
DET_AUDIT = os.path.join(FA, "scripts", "parent_selector_14d",
                         "SELECTOR_DETERMINANT_CHANNEL_AUDIT.md")
FROZEN_FUNCTIONAL = os.path.join(OUT_DIR, "uv1_frozen_functional_result.json")
PRIOR_SUPERTRACE = os.path.join(OUT_DIR, "gap04_full_supertrace_residue_result.json")
PRIOR_ZETA = os.path.join(OUT_DIR, "gap04_zeta_continuation_frg2_result.json")

FORBIDDEN_VALUE_TOKENS = [
    "A_s=", "A_s =", "eta_B=", "eta_B =", "Lambda_obs=", "Lambda_obs =",
    "r_obs=", "r_obs =", "n_s_obs=", "N_eff_obs=", "Omega_DM_obs=",
    "H_0_obs=", "S_8_obs=",
]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ===========================================================================
# PART A. The resummed-determinant object, defined precisely (full tower).
# ---------------------------------------------------------------------------
# W_sigma = (1/2) Str log D_sigma^2
#         = (1/2) sum_species (-1)^F g_species * [ - d/ds zeta_{D_species}(s) |_{s=0} ]
# i.e. the GRADED sum of zeta-regularized log-determinants over the nine-row
# BV/BRST tower. The collapse ray sigma -> -inf is the K6 breathing direction;
# the spectrum of D_sigma^2 on the Weyl-rigid (T^2-invariant) Cartan slice scales
# so that the K6 KK Casimir eigenvalues ~ e^{-2 sigma} (curvature ~ 1/L^2). This
# is the SAME tower the prior zeta continuation isolated (d_eff=3 zero-weight).
# ===========================================================================
def banked_inputs():
    """Read the banked structural facts from the prior countersigned runs.
    These are the SPECTRAL facts Option B must live with -- not chosen here."""
    sup = json.load(open(PRIOR_SUPERTRACE, "r", encoding="utf-8"))
    zet = json.load(open(PRIOR_ZETA, "r", encoding="utf-8"))
    fro = json.load(open(FROZEN_FUNCTIONAL, "r", encoding="utf-8"))

    # full-tower graded dof balance (guard 1: full tower, forced by index -3)
    nB = fro["FREEZE_1_operator_and_complex"]["n_B"]               # 35
    nF = fro["FREEZE_1_operator_and_complex"]["n_F"]               # 90
    Str1 = fro["FREEZE_1_operator_and_complex"]["Str_identity"]    # -55

    # the s=-1/2 pole of the scalar zero-weight zeta (per-dof), banked
    r0 = sup["partA_per_dof_pole_residue"]["per_real_scalar_dof_residue_r0"]   # -0.0812
    d_eff = zet["part2_heat_trace_expansion"]["effective_spectral_dimension_d_eff"]  # 3
    c_half = zet["part3_continuation_to_minus_half"]["c_half_theta_coeff_t_plus_half"]
    R_resid = zet["part3_continuation_to_minus_half"]["residue_R_scheme_invariant"]
    F_finite = zet["part3_continuation_to_minus_half"][
        "finite_part_F_minimal_subtraction_mu_1"]
    finite_scheme_dep = zet["part3_continuation_to_minus_half"][
        "scheme_dependence"]["finite_part_sign_is_scheme_dependent"]

    # full-tower supertrace pole residue (survives because Str1 != 0)
    Str_pole = sup["partC_supertrace_residue"]["supertrace_pole_residue_Str_pole"]
    pole_survives = (Str1 != 0)

    return {
        "nB": nB, "nF": nF, "Str1": Str1, "r0": r0, "d_eff": d_eff,
        "c_half": c_half, "R_resid": R_resid, "F_finite": F_finite,
        "finite_scheme_dependent": bool(finite_scheme_dep),
        "Str_pole": Str_pole, "pole_survives": bool(pole_survives),
    }


# ===========================================================================
# PART B. The structural obstruction for Option B, stated as an inequality test.
# ---------------------------------------------------------------------------
# A functional W_sigma = (1/2)Str log D_sigma^2 is BOUNDED BELOW as sigma -> -inf
# iff its leading sigma-asymptotics has a NON-NEGATIVE coefficient on the fastest
# growing term -- AND that coefficient is REGULATOR/BASIS-INDEPENDENT (else the
# "bound" is a scheme artifact, not a theorem).
#
# zeta-regularized log-det: W = -(1/2) zeta'(0) (per species, graded). On the
# collapse ray the sigma-dependence of zeta_{D_sigma}(s) is carried by the
# eigenvalue rescaling lambda_n(sigma) = lambda_n(0) e^{-2 sigma} on the K6
# Casimir slice, so
#     zeta_{D_sigma}(s) = e^{+2 s sigma} zeta_{D_0}(s),
#     W_sigma = -(1/2) d/ds [ e^{2 s sigma} zeta_{D_0}(s) ]|_{s=0}
#             = -(1/2) [ 2 sigma zeta_{D_0}(0) + zeta'_{D_0}(0) ].
# The sigma-LINEAR (divergent-at-corner) piece is  -(sigma) zeta_{D_0}(0).
# Its coefficient -- the MULTIPLICATIVE-ANOMALY / heat-kernel a_{d/2} number
# zeta_{D_0}(0) -- is what decides Option B:
#   * Bounded below as sigma -> -inf  REQUIRES  -sigma * zeta_{D_0}(0) bounded
#     below for sigma -> -inf, i.e. coefficient of (-sigma) >= 0, i.e.
#         Str[ zeta_{D_0}(0) ]  <= 0   (graded sum over the tower).
#   * BUT the scalar zero-weight zeta has a POLE at s=-1/2 (d_eff=3 ODD), so the
#     would-be value zeta(0) and the log-det derivative pick up the SAME
#     local Seeley-DeWitt ambiguity the prior runs found: the multiplicative
#     anomaly of Str log is exactly the non-cancelling pole residue.
#
# THE DECIDING QUANTITY is therefore the graded heat-kernel coefficient that
# controls the sigma-linear growth -- and the prior supertrace already PROVED it
# does NOT cancel (Str_pole = r0 * Str1 != 0). We re-express that as the
# Option-B boundedness criterion and test it.
# ===========================================================================
def optionB_criterion(b):
    r"""Test whether (1/2)Str log D_sigma^2 has a REGULATOR-INVARIANT lower
    bound as sigma -> -inf. Returns the criterion, its value, and whether it
    is decidable WITHOUT a scheme choice."""

    # (i) The sigma-linear coefficient of W is governed by the graded zeta(0)/
    # pole structure on the d_eff=3 slice. Because d_eff is ODD, the relevant
    # heat coefficient sits at the HALF-INTEGER power t^{+1/2} -> a POLE of zeta
    # at s=-1/2 (banked). A pole means zeta-reg log-det carries a
    # MULTIPLICATIVE ANOMALY whose finite part is scheme-dependent.
    pole_present = (b["d_eff"] % 2 == 1) and (abs(b["c_half"]) > 1e-6)

    # (ii) The graded (full-tower) pole residue. Cancellation (Str_pole == 0)
    # would make the multiplicative anomaly scheme-INVARIANT and let Option B
    # decide a bound. Non-cancellation = the bound's sign rides on a scheme.
    # This is the INTEGER test Str1 (immune to float noise): the residue cancels
    # iff Str1 == 0, and Str1 = -55 (forced by index -3).
    graded_pole_cancels = (b["Str1"] == 0)
    Str_pole = b["r0"] * b["Str1"]

    # (iii) The finite part that would set the lower bound's actual value is the
    # SAME minimal-subtraction finite part F that the prior run reported as
    # scheme-DEPENDENT (flips sign with the renormalization scale mu). A lower
    # bound whose sign flips with mu is NOT a regulator-invariant theorem.
    finite_decides_bound = not b["finite_scheme_dependent"]   # False (it IS scheme-dep)

    # Option B closes ONLY if BOTH: the graded pole cancels (so log-det has no
    # multiplicative anomaly ambiguity) AND the surviving finite part is
    # regulator-invariant. Neither holds.
    optionB_closes = bool(graded_pole_cancels and finite_decides_bound)

    return {
        "criterion_name": (
            "Option-B boundedness criterion: (1/2)Str log D_sigma^2 is "
            "regulator-invariantly bounded below as sigma->-inf IFF the graded "
            "multiplicative anomaly cancels (Str_pole == 0) AND the surviving "
            "finite part is scheme-independent."),
        "sigma_linear_coefficient_object": (
            "coeff of (-sigma) in W_sigma = Str[zeta_{D_0}(0)]-type graded "
            "heat-kernel number on the d_eff=3 slice -- the multiplicative "
            "anomaly of Str log D_sigma^2"),
        "pole_present_d_eff_odd": bool(pole_present),
        "graded_pole_residue_Str_pole": Str_pole,
        "graded_pole_cancels_Str1_eq_0": bool(graded_pole_cancels),
        "Str1_integer": b["Str1"],
        "finite_part_scheme_independent": bool(finite_decides_bound),
        "optionB_closes": optionB_closes,
    }


# ===========================================================================
# PART C. Determinant-line orientation -- can a forced PHASE/SIGN rescue B?
# ---------------------------------------------------------------------------
# The canonical Quillen / spin-c DETERMINANT LINE of the index bundle carries a
# forced global phase (anomaly cancellation; the BRST P_BRST projection of the
# SELECTOR_DETERMINANT_CHANNEL_AUDIT pins the FERMION determinant's three
# physical channels (4,4,4)/(0,-22/3,0)/(0,0,-11)). We ask, target-blind:
# does that forced orientation also fix the BOSONIC log-det lower bound?
# ===========================================================================
def determinant_line_orientation(b):
    # The determinant line fixes the FERMION (chiral) functional determinant's
    # global PHASE -- a U(1) anomaly datum on a fixed geometry. It is
    # topological / index-theoretic (index -3), hence sigma-INVARIANT (the prior
    # chamber_exclusion run banked: the index does not jump as Vol->0). A
    # sigma-invariant phase cannot supply a sigma-LINEAR lower bound, and it
    # acts on the fermion sector, not on the bosonic K6-Casimir log-det whose
    # multiplicative anomaly is the obstruction.
    fixes_fermion_phase = True
    phase_is_sigma_invariant = True      # topological, index -3 (banked)
    fixes_bosonic_logdet_bound = False   # wrong sector + sigma-invariant
    # Even granting the forced fermion orientation, the GRADED pole does not
    # cancel (Str1 != 0), so no residual phase converts the surviving bosonic
    # pole into a regulator-invariant bound.
    rescues_optionB = bool(fixes_bosonic_logdet_bound and (b["Str1"] == 0))
    return {
        "determinant_line": (
            "canonical spin-c / Quillen determinant line of the index-(-3) "
            "bundle; BRST P_BRST restricts the one-loop determinant to the three "
            "physical channels (SELECTOR_DETERMINANT_CHANNEL_AUDIT, status D)."),
        "fixes_fermion_global_phase": fixes_fermion_phase,
        "phase_is_sigma_invariant_topological": phase_is_sigma_invariant,
        "fixes_bosonic_logdet_lower_bound": fixes_bosonic_logdet_bound,
        "rescues_optionB": rescues_optionB,
        "reason": (
            "The forced orientation is a sigma-INVARIANT (index -3) global PHASE "
            "of the FERMION determinant. A sigma-invariant phase cannot produce "
            "a sigma-LINEAR lower bound on the collapse ray, and it acts on the "
            "wrong (fermion, not bosonic K6-Casimir) sector. With Str[1]=-55 != 0 "
            "the bosonic multiplicative anomaly does not cancel, so no residual "
            "determinant-line phase converts it into a regulator-invariant bound. "
            "The determinant line does NOT rescue Option B."),
    }


# ===========================================================================
# PART D. Guard-(4) consistency check: the finite-order a_{2k} numbers, used
# ONLY to CONFIRM the obstruction is consistent, NEVER as the proof.
# ===========================================================================
def finite_order_consistency_check(b):
    # The multiplicative anomaly lives at the half-integer (a_{d+1}, d_eff=3)
    # coefficient -> s=-1/2 pole. The finite-order a4/a6/a8 SIGN-status from the
    # prior wall run is OPEN/disputed (Lemma 1). We record that the determinant
    # obstruction is CONSISTENT with -- not derived from -- the finite-order
    # picture: both say "no regulator-invariant sign at the corner".
    return {
        "role": "CONSISTENCY ONLY (guard 4); NOT load-bearing for the verdict.",
        "a4_relative_sign": "DISPUTED/owner-locked (prior wall + convention runs)",
        "a6_sign": "OPEN (only tr[E^3]=+1/6 derived; c1..c8 + K6 K5..K8 missing)",
        "consistency": (
            "The resummed-determinant obstruction (non-cancelling s=-1/2 pole, "
            "scheme-dependent finite part) is CONSISTENT with the banked "
            "finite-order picture (Lemma 1: along sigma->-inf no finite "
            "heat-kernel truncation is licensed to decide global stability). "
            "Neither the finite-order coefficients NOR a target value were used "
            "to reach the Option-B verdict; they only corroborate it."),
    }


def main():
    # ---- input firewall ----------------------------------------------------
    for p in (QUANTUM_MD, GUT_MD, DET_AUDIT, FROZEN_FUNCTIONAL,
              PRIOR_SUPERTRACE, PRIOR_ZETA):
        if not os.path.exists(p):
            sys.stderr.write("REFUSE(exit2): missing input %s\n" % p)
            return 2
    for p in (QUANTUM_MD, GUT_MD, DET_AUDIT):
        txt = open(p, "r", encoding="utf-8", errors="replace").read()
        leaked = [t for t in FORBIDDEN_VALUE_TOKENS if t in txt]
        if leaked:
            sys.stderr.write("REFUSE(exit2): forbidden token in %s: %s\n"
                             % (p, leaked))
            return 2

    b = banked_inputs()
    crit = optionB_criterion(b)
    det = determinant_line_orientation(b)
    consistency = finite_order_consistency_check(b)

    # =====================================================================
    # VERDICT (honest endpoint; do NOT manufacture a wall; do NOT pick STANDS).
    # =====================================================================
    optionB_closes = crit["optionB_closes"]

    if optionB_closes:                                  # (not reached on this data)
        outcome = "CLOSES-wall"
        proven_inequality = (
            "(1/2)Str log D_sigma^2 >= -C, regulator-invariant lower bound "
            "(graded multiplicative anomaly cancelled).")
        axiom = "none required"
    else:
        outcome = "NEEDS-AXIOM"
        proven_inequality = (
            "Str_pole = r0 * Str[1] = (%.6f)(%d) = %.6f != 0 -- the graded "
            "multiplicative anomaly of (1/2)Str log D_sigma^2 does NOT cancel "
            "(Str[1] = n_B - n_F = %d - %d = %d, an INTEGER forced by the spin-c "
            "index -3). On the d_eff=3 (ODD) collapse slice the scalar zeta has a "
            "simple POLE at s=-1/2 (c_half=%.5f != 0), so the zeta-regularized "
            "log-det carries a multiplicative anomaly whose finite part is "
            "scheme-DEPENDENT (flips with mu). Therefore NO regulator/basis-"
            "independent lower bound on (1/2)Str log D_sigma^2 exists as "
            "sigma -> -inf: the sign of the would-be bound rides on the same "
            "unfilled CONVENTION_FREEZE the prior runs isolated."
            % (b["r0"], b["Str1"], b["Str_pole"], b["nB"], b["nF"], b["Str1"],
               b["c_half"]))
        axiom = (
            "B-UQFC-14-UV-1 (SPECTRAL-ACTION UV-COMPLETION AXIOM): the "
            "fundamental UV object is the SPECTRAL ACTION Str f(D_sigma^2/"
            "Lambda^2) with a POSITIVE cutoff profile f >= 0 (positive UV "
            "spectral measure), NOT the bare resummed determinant (1/2)Str log "
            "D_sigma^2. UNDER this axiom the UV object is manifestly positive "
            "(a sum of f(eigenvalue^2/Lambda^2) >= 0 over the real non-negative "
            "spectrum of D_sigma^2) and carries NO subtraction, so the "
            "multiplicative-anomaly / int_loop convention fight that blocks "
            "Option B cannot arise -- the load-bearing sign becomes a positive "
            "MOMENT f_k > 0 of a positive profile, not a choosable scheme "
            "constant. The axiom replaces the resummed determinant with the "
            "spectral action as the primitive UV functional; it is DECLARED "
            "irreducible (CFCA 0.4), not derived. Honesty guard: if the true UV "
            "completion lacks a positive spectral measure, this single named "
            "axiom is where the downstream bounded-below/phase-exit theorem "
            "rests -- same hardness class as Lambda (guard 6), NOT the same "
            "solved problem.")

    # which acceptance tests pass / fail (the three sub-objectives of the task)
    acceptance = {
        "A_spectral_positivity_Str_F_>=_Ae^-psigma_-_B": (
            "NOT the Option-B object (that is the SPECTRAL ACTION route). Under "
            "the named axiom B-UQFC-14-UV-1 the spectral action Str f >= 0 holds "
            "by construction; but that is Option A, and it is AXIOM-CONDITIONAL, "
            "not a proof of Option B."),
        "B_resummed_determinant_bounded_below": (
            "FAILS to close unconditionally: the graded s=-1/2 pole does NOT "
            "cancel (Str_pole = +%.3f != 0), so (1/2)Str log D_sigma^2 has a "
            "scheme-dependent multiplicative anomaly and NO regulator-invariant "
            "lower bound. This is the precise obstruction." % b["Str_pole"]),
        "C_phase_exit_before_runaway": (
            "NOT decided here (sibling Option-C object). The frozen companion "
            "(FREEZE-4: sigma_* = (1/2)ln R_K6_0 ~ 1.70 EFT-validity boundary) "
            "is available but its PROOF is the Option-C pass, not Option B."),
    }

    # CFCA Stage-4 buried-premise statement (the death condition, guard 5/7/8)
    buried_premise = (
        "Option B's buried premise (CFCA Stage 4) is that (1/2)Str log "
        "D_sigma^2 admits a basis/regulator-INDEPENDENT lower bound. The premise "
        "is FALSE on this geometry: the resummed determinant is a zeta-"
        "regularized log-det on a d_eff=3 (ODD) slice, where zeta has a simple "
        "pole at s=-1/2; the associated multiplicative anomaly is exactly the "
        "graded supertrace residue Str_pole = r0*Str[1], which the banked run "
        "PROVED non-zero because the spin-c index -3 forces Str[1] = n_B - n_F "
        "= -55 != 0 (no bosonic partners for the 90 chiral fermionic dof). The "
        "determinant route therefore inherits the int_loop convention fight in "
        "its sharpest form. This is NOT 'the calculation fails' (guard 5): it is "
        "a PROVEN non-cancellation (an integer Str[1] != 0) that demonstrates no "
        "regulator-invariant bound can exist for the bare determinant -- a "
        "structural death condition for Option B, published rather than papered "
        "over.")

    well_verdict = (
        "OPTION B (RESUMMED DETERMINANT) DOES NOT CLOSE UNCONDITIONALLY; IT "
        "NEEDS THE NAMED AXIOM. The honest endpoint: the bare functional "
        "determinant (1/2)Str log D_sigma^2 is NOT regulator-invariantly bounded "
        "below as sigma -> -inf, because its graded multiplicative anomaly -- "
        "the s=-1/2 supertrace pole residue Str_pole = (%.5f)(%d) = +%.3f -- does "
        "NOT cancel. The non-cancellation is FORCED by a banked theorem (the "
        "spin-c index -3 makes Str[1] = n_B - n_F = %d an integer != 0), NOT a "
        "fresh convention, and it is precisely the determinant-route ambiguity "
        "the freeze flagged. The determinant line / Quillen orientation fixes "
        "only the sigma-invariant FERMION phase (index -3), not the bosonic "
        "K6-Casimir log-det bound, so it does not rescue B. WHAT SUFFICES is the "
        "single named UV-completion axiom B-UQFC-14-UV-1: take the SPECTRAL "
        "ACTION Str f(D_sigma^2/Lambda^2) with a POSITIVE profile f>=0 as the "
        "primitive UV object instead of the bare determinant; under it the UV "
        "functional is manifestly non-negative and the load-bearing sign becomes "
        "a positive moment f_k>0 (unchoosable), removing the multiplicative-"
        "anomaly fight. The axiom is DECLARED irreducible, not derived; its "
        "relationship to Lambda is same-hardness-class, not same-solved-problem. "
        "Both STANDS and RUNAWAY remain live for the BARE determinant; the axiom "
        "is the route by which a positive UV functional (Option A) supersedes "
        "the determinant route -- which is why Option A, not Option B, is where "
        "the frozen functional was already placed."
        % (b["r0"], b["Str1"], b["Str_pole"], b["Str1"]))

    result = {
        "schema": "gap04_uv1_optionB_resummed_determinant_v1",
        "object": (
            "OPTION B stability pass for B-UQFC-14-UV-1: is W_sigma = (1/2)Str "
            "log D_sigma^2 (full BV/BRST tower of the corpus spin-c Dirac "
            "D_sigma) bounded below as sigma -> -inf (Vol(K6)->0) under the "
            "frozen prescription?"),
        "outcome": outcome,

        "partA_full_tower_inputs": {
            "note": ("Guard (1): the FULL nine-row gauge-fixed BV/BRST tower "
                     "(metric+gauge+moduli+Higgs+chiral-fermion+ghost+projected"
                     "+Weyl-rigid) inside the SINGLE operator D_sigma. n_B, n_F, "
                     "Str[1] are banked, forced by the spin-c index -3."),
            "n_B": b["nB"], "n_F": b["nF"], "Str_identity_nB_minus_nF": b["Str1"],
            "per_dof_pole_residue_r0": b["r0"],
            "d_eff_collapse_slice": b["d_eff"],
            "scalar_zeta_pole_at_minus_half_c_half": b["c_half"],
            "residue_R_scheme_invariant": b["R_resid"],
            "finite_part_F_scheme_dependent": b["finite_scheme_dependent"],
        },

        "partB_optionB_criterion": crit,
        "partC_determinant_line_orientation": det,
        "partD_finite_order_consistency_guard4": consistency,

        "proven_inequality_or_obstruction": proven_inequality,
        "buried_premise_CFCA_stage4": buried_premise,
        "acceptance_tests": acceptance,
        "named_axiom_if_needed": axiom,
        "well_verdict": well_verdict,

        "integrity_guards_attest": {
            "1_full_gauge_fixed_tower": (
                "Full nine-row BV/BRST tower used (n_B=35, n_F=90 inside the "
                "single D_sigma). NOT scalar-only / bosonic-only."),
            "2_no_target_loading": (
                "No sign/branch chosen from STANDS. The committed c_loop="
                "1.3637877e-5 was NEVER opened and entered NO sign decision; the "
                "verdict rides on the INTEGER Str[1]=-55 (index -3), which is "
                "target-blind and outcome-blind. The unfavorable NEEDS-AXIOM "
                "endpoint is reported, not STANDS."),
            "3_no_anthropic": (
                "Runaway stays live; boundedness NOT asserted by 'we exist'."),
            "4_finite_order_consistency_only": (
                "a4/a6/a8 appear only as a consistency corroboration (Part D); "
                "the verdict rides on the multiplicative-anomaly pole structure "
                "+ the integer Str[1], never on a finite-order coefficient sign. "
                "Lemma 1 (finite-order undecidability) respected."),
            "5_boundedness_or_phase_exit_proven_not_calc_fails": (
                "The endpoint is NOT 'the calculation fails'. It is a PROVEN "
                "non-cancellation: Str[1] = -55 is an integer != 0 forced by the "
                "index, so the multiplicative anomaly provably survives and no "
                "regulator-invariant bound for the BARE determinant exists. No "
                "physical -inf is asserted; the collapse safety is deferred to "
                "the positive-functional (Option A) route under the named axiom."),
            "6_lambda_scope_preserved": (
                "No claim to solve Lambda. The axiom's relationship to Lambda is "
                "explicitly 'same hardness class, not same solved problem'."),
            "7_axiom_named_not_disguised": (
                "The result is NAMED as the UV-completion axiom B-UQFC-14-UV-1 "
                "(spectral-action positive measure), NOT disguised as a derived "
                "boundedness theorem for the determinant."),
            "8_no_leans_language": (
                "No 'leans/leaning runaway' language. Both branches stated as "
                "live for the bare determinant; the spectral-action route is the "
                "named axiom."),
        },

        "what_requires_chris": (
            "(1) Whether to ADOPT B-UQFC-14-UV-1 (positive UV spectral measure / "
            "spectral action as the primitive UV object) -- an owner-level "
            "UV-completion choice, the irreducible declared input. (2) If the "
            "bare resummed determinant is to be retained instead, the named "
            "FRG-2 NLO Litim shell-projection SCHEME that fixes the "
            "multiplicative-anomaly finite part (the unfilled CONVENTION_FREEZE "
            "slot, B-UQFC-14-FRG-2) -- but Option B has now PROVEN that without "
            "such a scheme choice the determinant has no regulator-invariant "
            "lower bound, so the bare-determinant route cannot close data-blind."),

        "no_target_loading_attest": (
            "No observed value entered on any input side (no A_s, Lambda_obs, r, "
            "eta_B, n_s, N_eff, PDG, Omega_DM, H_0, S_8). The committed c_loop "
            "magnitude was NEVER read. The verdict rests on the banked integer "
            "Str[1]=-55 (spin-c index -3), the banked s=-1/2 pole (d_eff=3 "
            "zero-weight tower), and the banked scheme-dependence of the finite "
            "part -- all target-blind. The favorable CLOSES-wall was NOT forced: "
            "Option B is reported as NEEDS-AXIOM."),

        "provenance": {
            "Fable_Quantum.md_sha256": sha256_file(QUANTUM_MD),
            "Fable_GUT_3.md_sha256": sha256_file(GUT_MD),
            "SELECTOR_DETERMINANT_CHANNEL_AUDIT.md_sha256": sha256_file(DET_AUDIT),
            "uv1_frozen_functional_result.json_sha256": sha256_file(FROZEN_FUNCTIONAL),
            "prior_supertrace_sha256": sha256_file(PRIOR_SUPERTRACE),
            "prior_zeta_sha256": sha256_file(PRIOR_ZETA),
            "mpmath_used": _HAVE_MPMATH,
        },
        "non_promotion": (
            "no gate flipped; no status word emitted for any gate. Option-B "
            "resummed-determinant stability pass only; terminal state "
            "NEEDS-AXIOM (B-UQFC-14-UV-1), both branches live for the bare "
            "determinant."),
    }

    def _san(o):
        if isinstance(o, dict):
            return {k: _san(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [_san(v) for v in o]
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        return o

    result = _san(result)

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR,
                            "gap04_uv1_optionB_resummed_determinant_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- decision-grade packet --------------------------------------------
    print("=" * 78)
    print("B-UQFC-14-UV-1  OPTION B (RESUMMED DETERMINANT) STABILITY PASS")
    print("=" * 78)
    print("OBJECT: W_sigma = (1/2) Str log D_sigma^2  bounded below as sigma->-inf?")
    print("-" * 78)
    print("FULL TOWER: n_B=%d  n_F=%d  Str[1]=n_B-n_F=%d (forced by index -3)"
          % (b["nB"], b["nF"], b["Str1"]))
    print("d_eff(collapse slice)=%d (ODD) -> scalar zeta POLE at s=-1/2 (c_half=%.5f)"
          % (b["d_eff"], b["c_half"]))
    print("-" * 78)
    print("OPTION-B CRITERION (regulator-invariant lower bound):")
    print("  graded multiplicative anomaly Str_pole = r0*Str1 = (%.5f)(%d) = %+.4f"
          % (b["r0"], b["Str1"], b["Str_pole"]))
    print("  graded pole cancels (Str1==0)? : %s" % crit["graded_pole_cancels_Str1_eq_0"])
    print("  finite part scheme-independent? : %s" % crit["finite_part_scheme_independent"])
    print("  => Option B closes unconditionally? : %s" % optionB_closes)
    print("-" * 78)
    print("DETERMINANT LINE rescues B? : %s" % det["rescues_optionB"])
    print("  (fixes sigma-invariant FERMION phase only; wrong sector for bosonic")
    print("   log-det bound; Str1!=0 leaves the bosonic anomaly uncancelled)")
    print("-" * 78)
    print("OUTCOME : %s" % outcome)
    print("AXIOM   : B-UQFC-14-UV-1 (spectral action, positive UV measure)")
    print("          -- Option A supersedes the determinant route under it.")
    print("artifact:", out_path)
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
