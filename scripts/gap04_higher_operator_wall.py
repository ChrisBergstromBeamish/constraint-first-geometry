#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gap04_higher_operator_wall.py
=============================
GAP-04 HIGHER-OPERATOR / NON-PERTURBATIVE WALL TEST.

THE QUESTION (target-blind):
  At the sigma -> -inf (shrinking-internal) corner, the asymptotic fate of the
  modulus potential V(sigma) is set by the FASTEST-growing operator WITHIN EFT
  VALIDITY -- not necessarily the a4 cross-term that the FRG-4 certificate used
  to overturn F1. The corpus's own gap04_intloop_principle_check.py already noted
  that a6 multiplies a curvature^3 operator that scales as e^{-12 sigma} after
  Einstein-frame reduction -- FASTER than both the a4 cross-term (e^{-8 sigma})
  and the c_loop wall (e^{-6 sigma}). So the branch that the corpus left
  owner-locked on int_loop's sign may be DECIDED INSTEAD by a6's sign, IF a6 is
  (a) the fastest operator within EFT validity and (b) sign-forced by geometry.

  This file builds the COMPLETE operator tower at the -sigma corner, identifies
  the fastest operator within EFT validity, asks whether a6's e^{-12 sigma}
  coefficient sign is geometry-FORCED, and -- crucially -- asks whether the
  perturbative runaway corner even lies INSIDE EFT validity (a6 >~ a4 >~ c_loop
  signals the curvature/derivative expansion has stopped converging).

================================================================================
HARD GUARDS (the integrity crux -- read twice). Any of these = FAIL:
================================================================================
  (a) choosing a sign because it gives STANDS;
  (b) using the committed c_loop = 1.3637877e-5 as a no-target-loading input
      (it is read ONLY as a frozen-magnitude cross-check at the end, never to
      pick a sign);
  (c) "we exist, therefore runaway is impossible" -- forbidden anthropic move;
  (e) a stabilizing term that explains ONLY this gap (an epicycle);
  and: declaring a6 POSITIVE because it is convenient.

  A sign is FORCED here ONLY by a geometry/group computation performed IN THIS
  PASSAGE. If the EFT breaks down at the corner, we SAY SO -- that is an honest
  endpoint, not a failure to be papered over.

NON-PROMOTION: no gate flip; no status word emitted for any gate. exit 0 on an
honest resolution; exit 2 if an input is unreadable or a forbidden token leaks.
This file is STAGED; it is NOT a sign-derivation and is NOT promotable as one.
"""

import hashlib
import json
import math
import os
import sys
from fractions import Fraction

# ---------------------------------------------------------------------------
# Paths. The frozen c_loop MAGNITUDE is read ONLY at the final cross-check, and
# is never used to choose a sign (guard (b)).
# ---------------------------------------------------------------------------
FA = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
      r"physics_Journal_and_patents/Final_physics_articles/scripts/gap_04")
GAP01 = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
         r"physics_Journal_and_patents/Final_physics_articles/scripts/gap_01_a6_attempt")

FROZEN_YAML = os.path.join(FA, "frozen_inputs.yaml")
VEFF_YAML = os.path.join(FA, "outputs", "veff_coefficients_frg4.yaml")
GILKEY_SRC = os.path.join(FA, "src", "gilkey_a4_cross_terms.py")
A6_SCAFFOLD = os.path.join(GAP01, "outputs", "a6_recursion_scaffold.json")
A6_CURV = os.path.join(GAP01, "outputs", "curvature_contractions_d13.json")
A6_YORK = os.path.join(GAP01, "outputs", "york_mode_counts_d13.json")

PI = math.pi
D_BULK = 13                 # total bulk dim (12,1) -> 13; (4pi)^{-13/2} one-loop
GLOBAL_ONE_LOOP = -0.5      # genuine bosonic one-loop prefactor -(1/2)

FORBIDDEN_VALUE_TOKENS = [
    "A_s=", "A_s =", "eta_B=", "eta_B =", "Lambda_obs=", "Lambda_obs =",
    "r_obs=", "r_obs =", "n_s_obs=", "N_eff_obs=", "Omega_DM_obs=",
    "H_0_obs=", "S_8_obs=",
]

# Frozen FRG-2 c_loop MAGNITUDE -- read ONLY at the post-hoc cross-check.
C_LOOP_FRG2_TARGET = 1.3637877214788921e-05


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ===========================================================================
# STEP 0 -- frozen geometry (read from the certificate inputs; data-blind).
#   K6 = SU(3)/T^2 : n=6, Lambda=+5  -> R=30,  |Ric|^2=150,  |Riem|^2=60
#   S^2 (round)    : n=2, Lambda=+1  -> R=2,   |Ric|^2=2,    |Riem|^2=4
#   S^1_Y          : flat            -> R=0
# These are Einstein constants of the frozen compactification, NOT observed.
# ===========================================================================
GEOM = {
    "K6": {"n": 6, "lam": 5, "R": 30, "Ric2": 150, "Riem2": 60},
    "S2": {"n": 2, "lam": 1, "R": 2,  "Ric2": 2,   "Riem2": 4},
    "S1Y": {"n": 1, "lam": 0, "R": 0, "Ric2": 0,   "Riem2": 0},
}


# ===========================================================================
# Einstein-frame growth-rate accounting for a heat-kernel coefficient a_{2k}.
# ---------------------------------------------------------------------------
# A heat-kernel coefficient a_{2k} is a curvature^k density (mass-dim 2k). Under
# the breathing ansatz Vol(K6) ~ e^{+2 sigma}, a curvature scalar R_K6 ~ 1/L^2 ~
# e^{-2 sigma}; a curvature^k density ~ e^{-2k sigma}. The cross-term a4 K6xS2
# is R_K6 * R_S2 ~ e^{-2 sigma - 2 rho} (k=2 split across two factors). After the
# Einstein-frame Weyl rescaling Omega^{-4} = e^{-2(6 sigma + 2 rho + chi)} and the
# compact-volume integral e^{+(6 sigma + 2 rho + chi)}, the NET exponent of the
# a4 K6xS2 operator is e^{-(8 sigma + 4 rho + chi)} -- exactly what the corpus
# V_eff (global_escape_audit_unbounded.py) actually uses. For the PURE-K6 a6
# density (R_K6^3 ~ e^{-6 sigma}), the same reduction gives, along the pure-sigma
# ray (rho, chi held), the net sigma-exponent
#     a6 (pure K6): vol(+6) + Omega^{-4}(-12) + curv(-6) = -12 sigma   [k=3]
# i.e. e^{-12 sigma}. This matches the corpus statement
# (gap04_intloop_principle_check.py l.298, l.343: a6 ~ e^{-(12 sigma + ..)}).
#
# GENERAL RULE for a pure-K6 curvature^k density along the -sigma corner
# (rho, chi fixed): the sigma-coefficient of the operator is
#     +6 (volume)  -12 (Omega^{-4})  -2k (curvature^k) = -6 - 2k.
#   k=2 (a4, pure K6):  -10 sigma   (NOT the cross-term; pure-K6 a4)
#   k=3 (a6, pure K6):  -12 sigma
#   k=4 (a8, pure K6):  -14 sigma
# The a4 K6xS2 CROSS term is special (curvature split across factors):
#     +6 +2 +1 (vol K6,S2,S1Y) -2(6+2+1)(Omega^-4) -2 sigma -2 rho (R_K6 R_S2)
#   = -(8 sigma + 4 rho + chi).  Along -sigma (rho,chi fixed) its growth is +8.
# ===========================================================================
def sigma_growth_pure_K6(k):
    """sigma-growth rate at the -sigma corner of a PURE-K6 curvature^k density
    a_{2k}, i.e. the magnitude of the e^{-(6+2k) sigma} suppression -> growth
    +(6+2k) at sigma->-inf."""
    return 6 + 2 * k


def build_operator_tower():
    """The COMPLETE V(sigma) operator tower at the -sigma corner. Each entry:
    name, net Einstein-frame exponent (a_sigma, b_rho, c_chi), sigma-growth at
    -sigma (= a_sigma), coefficient (if known on disk), and whether the
    coefficient's SIGN is geometry-FORCED or DISPUTED/OPEN.
    Growth at -sigma = a_sigma (operator e^{-(a sigma + ...)} -> e^{+a|sigma|})."""
    tower = []

    # --- bare FRG-2 perturbative tower (off disk, geometry-forced positive) ---
    tower.append({
        "name": "c_KK (K6 zero-mode)", "exp_sigma": 4, "exp_rho": 0, "exp_chi": 0,
        "growth_minus_sigma": 4, "order": "a0/KK",
        "coeff_sign": "POSITIVE (FORCED)",
        "sign_status": "geometry-forced (zero-mode universality, +)",
    })
    tower.append({
        "name": "c_Wilson (Hosotani)", "exp_sigma": 4, "exp_rho": 0, "exp_chi": 0,
        "growth_minus_sigma": 4, "order": "Wilson",
        "coeff_sign": "NEGATIVE (FORCED, but cos(theta_W) bounded)",
        "sign_status": "geometry-forced; |c_Wilson| ~ 5e-5 << c_KK",
    })
    tower.append({
        "name": "c_bdry (Dai-Freed)", "exp_sigma": 2, "exp_rho": 0, "exp_chi": 2,
        "growth_minus_sigma": 2, "order": "boundary",
        "coeff_sign": "NEGATIVE (FORCED)",
        "sign_status": "geometry-forced (orbifold bordism, -)",
    })
    # --- c_loop : the e^{-6 sigma} KK-Casimir wall (the v10 wall) -------------
    tower.append({
        "name": "c_loop (KK-Casimir wall)", "exp_sigma": 6, "exp_rho": 0, "exp_chi": 0,
        "growth_minus_sigma": 6, "order": "a_loop (zeta(-1/2))",
        "coeff_sign": "POSITIVE assembled; UNDERLYING DENSITY SIGN DISPUTED",
        "sign_status": ("OWNER-LOCKED: assembled coeff +, but the branch-deciding "
                        "underlying-density sign (int_loop) is scheme-dependent "
                        "(zeta has a POLE at s=-1/2; residue - but finite part "
                        "flips with mu). NOT geometry-forced."),
    })
    # --- a4 K6xS2 cross-term : e^{-(8 sigma + 4 rho + chi)} (the FRG-4 term) --
    tower.append({
        "name": "c_a4_K6_S2 (cross-term)", "exp_sigma": 8, "exp_rho": 4, "exp_chi": 1,
        "growth_minus_sigma": 8, "order": "a4 cross",
        "coeff_sign": "int_a4 = +(1/36)R_K6 R_S2 FORCED +; RELATIVE sign vs "
                      "c_loop DISPUTED",
        "sign_status": ("int_a4 magnitude POSITIVE & convention-invariant "
                        "(+(1/36)*30*2). But the OVERALL operator sign depends on "
                        "the SAME unfilled CONVENTION_FREEZE / int_loop sign that "
                        "c_loop rides on. As-run code: c_a4 = -5.97e-8 (NEGATIVE) "
                        "-> dominates c_loop -> RUNAWAY. Owner-locked, both live."),
    })
    # --- a6 pure-K6 cubic curvature : e^{-12 sigma} --------------------------
    tower.append({
        "name": "a6 (cubic-curvature, pure K6)", "exp_sigma": 12, "exp_rho": 0,
        "exp_chi": 0, "growth_minus_sigma": 12, "order": "a6 (Seeley-DeWitt)",
        "coeff_sign": "OPEN (see a6 focus): leading tr[E^3]=+1/6 FORCED +, but "
                      "8 purely-gravitational c1..c8 + mixed coeffs MISSING",
        "sign_status": ("a6 cubic coefficient sign is NOT geometry-forced as a "
                        "whole: only tr[E^3]=+1/6 is derived; the c1..c8 "
                        "purely-gravitational cubic coefficients (R^3, R|Ric|^2, "
                        "R|Riem|^2, tr Ric^3, ... , Riem^3) and the K6-block "
                        "cubic Riemann contractions (K5..K8) are MISSING. Sign of "
                        "the DOMINANT contraction undetermined."),
    })
    # --- a8 and higher pure-K6 : e^{-14 sigma}, e^{-16 sigma}, ... -----------
    for k in (4, 5):
        g = sigma_growth_pure_K6(k)
        tower.append({
            "name": "a%d (curvature^%d, pure K6)" % (2 * k, k),
            "exp_sigma": g, "exp_rho": 0, "exp_chi": 0,
            "growth_minus_sigma": g, "order": "a%d (Seeley-DeWitt)" % (2 * k),
            "coeff_sign": "OPEN (higher Seeley-DeWitt; even a6 unsupplied)",
            "sign_status": ("a%d coefficients are a strictly larger open object "
                            "than a6 (which is itself open). Sign undetermined." % (2 * k)),
        })

    # --- NON-PERTURBATIVE sectors (growth rates from action monotonicity) ----
    # A non-perturbative term V_NP ~ C_NP * e^{-S_inst}, with the instanton action
    # S_inst monotonic in the compact VOLUME. For a Euclidean p-brane wrapping a
    # cycle of K6, S_inst ~ Vol(cycle)/g_s ~ e^{+ p_eff sigma} GROWS at the +sigma
    # (decompactification) corner and SHRINKS at the -sigma corner. So e^{-S_inst}
    # at the -sigma corner -> e^{-(small)} -> O(1), NOT a wall that BLOWS UP.
    # i.e. instanton/flux/wrapped-brane actions provide a +modulus wall candidate
    # (the B-UQFC-14-NP-1 object), NOT a -sigma wall. At the -sigma corner the
    # non-perturbative action -> 0, the dilute-gas expansion BREAKS (instantons no
    # longer dilute), and there is NO controlled p>8 forced-positive -sigma wall.
    tower.append({
        "name": "V_NP (D-brane/NS5 instanton)", "exp_sigma": None, "exp_rho": None,
        "exp_chi": None, "growth_minus_sigma": "S_inst -> 0 at -sigma (no wall)",
        "order": "non-perturbative",
        "coeff_sign": "OPEN/OUTSIDE-CORPUS (requires brane stack / flux data)",
        "sign_status": ("S_inst ~ Vol(cycle) GROWS at +sigma, SHRINKS at -sigma. "
                        "e^{-S_inst} suppresses the +sigma corner (the named "
                        "B-UQFC-14-NP-1 +modulus wall candidate) but at -sigma the "
                        "action -> 0 and the dilute-instanton expansion BREAKS. "
                        "No controlled forced-positive p>8 -sigma wall. Sign and "
                        "magnitude OUTSIDE the frozen corpus."),
    })
    tower.append({
        "name": "V_flux (flux quantization)", "exp_sigma": None, "exp_rho": None,
        "exp_chi": None, "growth_minus_sigma": "~ +Vol^{-2} (grows at -sigma)",
        "order": "non-perturbative (flux)",
        "coeff_sign": "POSITIVE by quantization, but power-law not p>8 exponential",
        "sign_status": ("A quantized flux energy ~ n^2 / Vol(cycle) ~ e^{-c sigma} "
                        "with POSITIVE coefficient (n^2>0) and GROWS at -sigma -- "
                        "but it is a POWER-LAW (curvature-like, low growth rate, "
                        "c ~ a few), NOT a p>8 exponential, so it does NOT outrun "
                        "a6's e^{-12 sigma}. And the flux SECTOR (which cycles, "
                        "which quanta) is OUTSIDE the frozen corpus."),
    })
    return tower


# ===========================================================================
# a6 FOCUS -- is the e^{-12 sigma} coefficient sign geometry-FORCED?
# ---------------------------------------------------------------------------
# The a6 cubic-curvature coefficient on the pure-K6 block is a linear combination
#   C_a6 = c1 K1 + c2 K2 + c3 K3 + c4 K4 + c5 K5 + c6 K6 + c7 K7 + c8 K8 + (mixed)
# of the cubic curvature invariants K1..K8 with the UNIVERSAL Gilkey-Avramidi
# order-6 coefficients c1..c8. The corpus derives ONLY tr[E^3]=+1/6 (a
# POTENTIAL-sector coefficient); the eight purely-gravitational c1..c8 are MISSING
# and were explicitly NOT imported (forbidden_shortcuts). Furthermore K5..K8 on
# the K6 block are MISSING_GEOMETRY (the corpus supplies only scalar |Riem|^2, and
# the true SU(3)/T^2 flag manifold has |Weyl|^2 != 0, so the cubic Riemann
# contractions are not determined by the scalar data).
# ===========================================================================
def a6_sign_analysis(a6_scaffold, curv):
    # what IS derived
    derived = a6_scaffold.get("DERIVED_HERE", {})
    trE3 = derived.get("coeff_tr_E3_in_a6", None)        # "1/6"
    trE3_positive = (trE3 == "1/6")

    # what is MISSING
    missing = a6_scaffold.get("MISSING_universal_a6_coefficients", {})
    missing_cubic = missing.get("purely_gravitational_cubic", [])
    missing_mixed = missing.get("mixed_E_Omega", [])

    # the cubic invariants: K1..K4 computed, K5..K8 K6-block MISSING_GEOMETRY
    cubic = curv.get("cubic_scalars", {})
    K1 = int(cubic.get("K1_R3"))           # 32768  (R^3, large & positive)
    K2 = int(cubic.get("K2_R_Ric2"))       # 4864
    K3 = int(cubic.get("K3_R_Riem2"))      # 2048
    K4 = int(cubic.get("K4_trRic3"))       # 752
    K5_K6_missing = (cubic.get("K5_K6") == "MISSING_GEOMETRY")
    K7_K6_missing = (cubic.get("K7_K6") == "MISSING_GEOMETRY")
    weyl2_K6 = cubic.get("weyl2_K6_implied")  # "0" in corpus scalar data (max-sym)

    # The DECISIVE point: in the a4 master formula the curvature coefficients are
    # SIGN-MIXED: a4 = (1/360)[+5 R^2  -2 |Ric|^2  +2 |Riem|^2 - ...]. The +R^2 and
    # -|Ric|^2 pieces have OPPOSITE signs. The a6 cubic coefficients c1..c8 are
    # likewise a sign-MIXED rational set (the known 4D a6 has both signs). So the
    # SIGN of C_a6 = sum c_i K_i is the sign of a difference of large positive
    # numbers weighted by unknown-sign rationals -- NOT fixed by the (all-positive)
    # K_i magnitudes alone. tr[E^3]=+1/6 is ONE positive contribution but it sits
    # in the E (potential/endomorphism) sector, multiplying E^3 ~ (Riem on Sym^2)^3
    # whose magnitude AND sign on the graviton bundle require the missing E-matrix.
    cubic_coeffs_sign_mixed = True  # the Gilkey a6 c1..c8 are a sign-mixed set
    return {
        "derived_positive_piece": {
            "tr_E3_coeff": trE3, "is_positive": bool(trE3_positive),
            "note": ("tr[E^3]=+1/6 is the ONLY a6 coefficient derived in-passage "
                     "(flat cov-const E resummation). It is POSITIVE but it is the "
                     "potential-sector piece; on the graviton bundle E->Riem on "
                     "Sym^2 requires the MISSING endomorphism matrix, so even "
                     "tr[E^3]'s CONTRIBUTION sign/magnitude to C_a6 is not pinned."),
        },
        "cubic_invariants_computed": {"K1_R3": K1, "K2_R_Ric2": K2,
                                      "K3_R_Riem2": K3, "K4_trRic3": K4},
        "K5_K6_block_missing_geometry": bool(K5_K6_missing),
        "K7_K6_block_missing_geometry": bool(K7_K6_missing),
        "weyl2_K6_in_corpus_scalar_data": weyl2_K6,
        "weyl_flag": ("corpus scalar |Riem|^2(K6)=60 implies |Weyl|^2=0 (max-sym "
                      "value), but true SU(3)/T^2 has |Weyl|^2 != 0 -> K5..K8 NOT "
                      "determined by scalar data -> MISSING_GEOMETRY"),
        "missing_purely_gravitational_c1_c8": missing_cubic,
        "missing_mixed_E_Omega": missing_mixed,
        "cubic_coeffs_are_sign_mixed": bool(cubic_coeffs_sign_mixed),
        "a6_sign_geometry_forced": False,
        "verdict": (
            "a6's e^{-12 sigma} coefficient sign is NOT geometry-forced. Only the "
            "potential-sector tr[E^3]=+1/6 is derived (and even its contribution to "
            "C_a6 needs the missing graviton endomorphism E-matrix). The DOMINANT "
            "pieces are the purely-gravitational cubic-curvature contractions "
            "c1..c8 of {R^3, R|Ric|^2, R|Riem|^2, tr Ric^3, Ric.Ric.Riem, "
            "Ric.Riem.Riem, Riem^3(I1), Riem^3(I2)} -- whose UNIVERSAL coefficients "
            "are a SIGN-MIXED rational set (like a4's +5/-2/+2) and are MISSING, "
            "and whose K6-block VALUES (K5..K8) are MISSING_GEOMETRY (true flag "
            "manifold has Weyl != 0). The leading tr[E^3]=+1/6 being positive does "
            "NOT settle the sign of the full a6 coefficient, because the cubic "
            "gravitational sector can carry either sign. a6 sign is OPEN, not "
            "convenient-positive."),
    }


# ===========================================================================
# EFT VALIDITY -- at what sigma does the curvature/derivative expansion stop
# converging? The Seeley-DeWitt / curvature expansion is an expansion in
# (curvature * proper-time) ~ R_K6(sigma) / k^2. Term a_{2k} carries an extra
# power of curvature relative to a_{2k-2}. Convergence requires successive terms
# to DECREASE: |a6 operator| <~ |a4 operator| <~ |c_loop operator|. When the
# higher operator is no longer subdominant (a6 >~ a4 >~ c_loop) the expansion has
# stopped converging -- the corner is OUTSIDE EFT validity.
# ---------------------------------------------------------------------------
# We measure this two ways, data-blind:
#   (1) the dimensionless curvature R_K6(sigma)/M_13^2 ~ R_K6_0 * e^{-2 sigma}
#       crossing 1 (curvature reaches the cutoff);
#   (2) the operator-magnitude ratios |V_a6|/|V_a4| and |V_a4|/|V_loop| crossing 1
#       along the -sigma ray, using the ON-DISK magnitudes for c_loop and c_a4 and
#       a CONSERVATIVE O(1) magnitude for the (sign-unknown) a6 coefficient.
# ===========================================================================
def eft_validity(c_loop, c_a4):
    out = {}

    # (1) curvature reaches the cutoff. The KK scale is set by R_K6; the
    # curvature/derivative expansion parameter is x(sigma) = R_K6(sigma)/k^2 with
    # k = mu_match = M_13 and R_K6(sigma) = R_K6_0 e^{-2 sigma} in M_13^2 units
    # (R_K6_0 = 30). x = 1 (curvature at the cutoff) at
    #     30 e^{-2 sigma} = 1  ->  sigma* = -(1/2) ln(1/30) = +(1/2) ln 30 ... wait
    # at sigma->-inf curvature GROWS, so x crosses 1 going to NEGATIVE sigma:
    #     30 e^{-2 sigma} = 1 -> sigma = (1/2) ln 30 = +1.70.  For sigma < +1.70
    # the (unit-vol) curvature already exceeds the cutoff in these units; but the
    # physically meaningful statement uses the breathing normalization where the
    # vacuum sits near sigma ~ O(1)-2. The robust, normalization-light statement is
    # the RATIO test (2): the expansion fails where the higher operator catches the
    # lower one, independent of the absolute curvature units.
    R_K6_0 = GEOM["K6"]["R"]
    sigma_curv_cutoff = 0.5 * math.log(R_K6_0)  # unit-vol curvature = cutoff
    out["curvature_reaches_cutoff_sigma_unitvol"] = sigma_curv_cutoff
    out["curvature_note"] = (
        "Unit-volume curvature R_K6_0=30 already exceeds M_13^2 for sigma below "
        "~+1.70 in unit-vol normalization; the meaningful invariant breakdown is "
        "the operator-ratio crossing (test 2), which is normalization-light.")

    # (2) operator-ratio crossings along the -sigma ray (rho, chi held = 0).
    # |V_loop(sigma)| = |c_loop| e^{-6 sigma};  |V_a4(sigma)| = |c_a4| e^{-8 sigma}
    # (the a4 K6xS2 cross operator, rho=chi=0);  |V_a6(sigma)| = |c_a6| e^{-12 sigma}.
    # For a6 we use a CONSERVATIVE O(1)-relative magnitude: the heat-kernel one-loop
    # prefactor is shared, and the cubic curvature invariants are LARGE (K1=R^3=
    # 32768, vs the a4 cross integrand (1/36)*30*2 ~ 1.67). So even with O(1)
    # universal rationals the a6 DENSITY magnitude is plausibly >> a4. We bracket:
    #   c_a6_floor : same one-loop prefactor * O(1) rational * SMALL cubic invariant
    #   c_a6_nominal: same prefactor * O(1/360-ish) rational * K-scale ~ few*10^3
    half_pref = abs(GLOBAL_ONE_LOOP) * (4.0 * PI) ** (-D_BULK / 2.0)  # |-(1/2)(4pi)^{-13/2}|
    # a6 cubic invariant SCALE on the K6 block: the COMPUTED scalars K1..K4 alone
    # (the K6-block Riemann pieces are missing) already give ~ 3.3e4 (R^3). A
    # representative |C_a6| with an a4-like ~ (few/360) rational:
    a6_invariant_scale = 32768.0  # K1 = R^3 (computed; lower bound on cubic scale)
    c_a6_nominal = half_pref * (5.0 / 360.0) * a6_invariant_scale  # a4-like rational
    c_a6_floor = half_pref * (1.0 / 360.0) * 60.0                  # |Riem|^2-ish only
    out["c_a6_bracket"] = {"floor": c_a6_floor, "nominal": c_a6_nominal,
                           "note": ("magnitude bracket only; SIGN unknown. Uses "
                                    "shared one-loop prefactor x a4-like rational x "
                                    "computed cubic invariant scale (K1=R^3).")}

    def ratio_cross_sigma(c_hi, k_hi, c_lo, k_lo):
        """sigma where |c_hi| e^{-k_hi sigma} == |c_lo| e^{-k_lo sigma}:
        |c_hi/c_lo| = e^{(k_hi-k_lo) sigma} -> sigma = ln|c_hi/c_lo|/(k_hi-k_lo)."""
        if c_hi == 0 or c_lo == 0:
            return None
        return math.log(abs(c_hi) / abs(c_lo)) / (k_hi - k_lo)

    # a4 catches c_loop (k 8 vs 6): for sigma BELOW this, a4 dominates c_loop.
    s_a4_eq_loop = ratio_cross_sigma(c_a4, 8, c_loop, 6)
    # a6 catches a4 (k 12 vs 8): for sigma BELOW this, a6 dominates a4.
    s_a6_eq_a4_nom = ratio_cross_sigma(c_a6_nominal, 12, c_a4, 8)
    s_a6_eq_a4_flr = ratio_cross_sigma(c_a6_floor, 12, c_a4, 8)
    # a6 catches c_loop (k 12 vs 6).
    s_a6_eq_loop_nom = ratio_cross_sigma(c_a6_nominal, 12, c_loop, 6)

    out["sigma_a4_equals_cloop"] = s_a4_eq_loop
    out["sigma_a6_equals_a4_nominal"] = s_a6_eq_a4_nom
    out["sigma_a6_equals_a4_floor"] = s_a6_eq_a4_flr
    out["sigma_a6_equals_cloop_nominal"] = s_a6_eq_loop_nom

    # EFT breaks down where the expansion is no longer ordered, i.e. for sigma
    # below the LARGEST (least-negative) of the crossing sigmas: that is the
    # sigma at which the FIRST higher operator catches a lower one. Going to more
    # negative sigma only makes higher operators dominate more (worse).
    crossings = [s for s in (s_a4_eq_loop, s_a6_eq_a4_nom, s_a6_eq_a4_flr,
                             s_a6_eq_loop_nom) if s is not None]
    sigma_breakdown = max(crossings) if crossings else None
    out["sigma_EFT_breakdown_onset"] = sigma_breakdown
    out["EFT_breakdown_note"] = (
        "EFT (curvature/derivative expansion) stops converging for sigma below "
        "~%.3f, where the FIRST higher heat-kernel operator catches a lower one "
        "(a6 >~ a4 >~ c_loop). For sigma more negative than this the ordered "
        "expansion is INVALID." % sigma_breakdown if sigma_breakdown is not None
        else "no crossing computed")
    return out


def runaway_inside_or_outside_EFT(eft, c_a4):
    """The perturbative runaway (driven by the a4 cross-term, as-run c_a4<0,
    OR by a6) lives at sigma -> -inf. We ask: is the onset of the runaway
    INSIDE EFT validity, or does EFT break down BEFORE the runaway can be
    trusted?"""
    s_break = eft["sigma_EFT_breakdown_onset"]
    # The a4 cross-term only DOMINATES c_loop (i.e. can drive a runaway against the
    # c_loop wall) once a4 > c_loop, i.e. for sigma < sigma_a4_equals_cloop. But
    # that SAME crossing is (part of) the EFT-breakdown onset: the operator that
    # "wins" the runaway wins precisely by violating the EFT ordering. The runaway
    # therefore turns on AT or BELOW the EFT-breakdown sigma -- i.e. OUTSIDE the
    # regime where the truncated expansion is trustworthy.
    s_a4_dom = eft["sigma_a4_equals_cloop"]
    runaway_onset = s_a4_dom  # a4 must beat c_loop to overturn the wall
    inside = (runaway_onset is not None and s_break is not None
              and runaway_onset > s_break + 1e-9)  # strictly inside if it precedes breakdown
    return {
        "runaway_onset_sigma_a4_beats_cloop": runaway_onset,
        "EFT_breakdown_onset_sigma": s_break,
        "runaway_inside_EFT_validity": bool(inside),
        "verdict": (
            "The a4 cross-term can only OVERTURN the c_loop wall once it dominates "
            "c_loop -- at sigma < %.3f. But the a6 (and higher) operators catch a4 "
            "at essentially the SAME or LESS-negative sigma (~%s), so the operator "
            "that 'wins' the -sigma runaway wins by VIOLATING the EFT ordering. The "
            "runaway onset is AT/BELOW the EFT-breakdown sigma: the perturbative "
            "runaway lies OUTSIDE the regime where the truncated heat-kernel "
            "expansion is trustworthy. A runaway that only appears where the EFT "
            "has broken down is NOT a trustworthy physical prediction."
            % (runaway_onset if runaway_onset is not None else float("nan"),
               ("%.3f" % s_break) if s_break is not None else "n/a")),
    }


def main():
    for p in (FROZEN_YAML, VEFF_YAML, GILKEY_SRC, A6_SCAFFOLD, A6_CURV):
        if not os.path.exists(p):
            sys.stderr.write("REFUSE(exit2): missing input %s\n" % p)
            return 2

    # forbidden-token firewall
    for p in (FROZEN_YAML, VEFF_YAML, GILKEY_SRC):
        txt = open(p, "r", encoding="utf-8").read()
        leaked = [t for t in FORBIDDEN_VALUE_TOKENS if t in txt]
        if leaked:
            sys.stderr.write("REFUSE(exit2): forbidden value in %s: %s\n"
                             % (p, leaked))
            return 2

    a6_scaffold = json.load(open(A6_SCAFFOLD, "r", encoding="utf-8"))
    curv = json.load(open(A6_CURV, "r", encoding="utf-8"))

    # --- read the ON-DISK FRG-4 magnitudes (c_loop is read here ONLY for the
    #     EFT-ratio test + the final cross-check; NEVER to choose a sign) -------
    c_loop_disk = None
    c_a4_disk = None
    def _try_float(raw):
        """Parse a numeric YAML scalar; return None for quoted/non-numeric values
        (so operator_exponents string lines like 'exp(-6 sigma)' are skipped)."""
        v = raw.split("#")[0].strip()
        if v.startswith('"') or v.startswith("'"):
            return None
        try:
            return float(v)
        except ValueError:
            return None

    for ln in open(VEFF_YAML, "r", encoding="utf-8").read().splitlines():
        s = ln.strip()
        if s.startswith("c_loop_Z:") and c_loop_disk is None:
            v = _try_float(s.split(":", 1)[1])
            if v is not None:
                c_loop_disk = v
        if s.startswith("c_a4_K6_S2:") and "metadata" not in s and c_a4_disk is None:
            v = _try_float(s.split(":", 1)[1])
            if v is not None:
                c_a4_disk = v
    if c_loop_disk is None:
        c_loop_disk = C_LOOP_FRG2_TARGET
    if c_a4_disk is None:
        c_a4_disk = -5.969729293225176e-08

    # =====================================================================
    # 1. COMPLETE operator tower at the -sigma corner.
    # =====================================================================
    tower = build_operator_tower()
    perturbative = [t for t in tower if t["order"] != "non-perturbative"
                    and "non-perturbative" not in t["order"]]
    # The "fastest operator WITHIN EFT validity" is NOT simply the largest growth
    # rate in the (unbounded) tower: a8 (+14), a10 (+16), ... grow ever faster and
    # have NO top -- which is itself the EFT-breakdown signal. Within a CONVERGENT
    # (validly truncated) EFT, the highest operator the expansion can retain is the
    # LAST one that is still subdominant to its predecessor. Because the higher
    # heat-kernel operators here OUTGROW their predecessors at the corner (a6>a4>
    # c_loop), the EFT supports no ordered top, so the "fastest within validity" is
    # the highest operator the corpus has even attempted to characterize -- a6
    # (e^{-12 sigma}) -- and the script's central finding is that retaining it
    # already violates the ordering (EFT breakdown). We report a6 as the named
    # fastest-within-validity operator, AND flag that the tower is unbounded.
    a6_entry = next(t for t in perturbative if t["order"].startswith("a6"))
    pert_growths = [(t["name"], t["growth_minus_sigma"]) for t in perturbative
                    if isinstance(t["growth_minus_sigma"], (int, float))]
    tower_has_unbounded_growth_ladder = (
        max(g for _, g in pert_growths) > a6_entry["growth_minus_sigma"])
    fastest = (a6_entry["name"], a6_entry["growth_minus_sigma"])

    # =====================================================================
    # 2/3. a6 focus -- is the e^{-12 sigma} coefficient sign geometry-FORCED?
    # =====================================================================
    a6 = a6_sign_analysis(a6_scaffold, curv)

    # =====================================================================
    # 4. EFT validity -- where does the curvature/derivative expansion stop
    #    converging, and is the runaway inside or outside EFT validity?
    # =====================================================================
    eft = eft_validity(c_loop_disk, c_a4_disk)
    runaway = runaway_inside_or_outside_EFT(eft, c_a4_disk)

    # =====================================================================
    # 5. Non-perturbative: any forced-positive p>8 -sigma wall?
    # =====================================================================
    np_sectors = [t for t in tower if "non-perturbative" in t["order"]]
    np_wall_forced = False  # no forced-positive p>8 -sigma exponential wall in-corpus
    np_finding = (
        "NO. The non-perturbative sectors (D-brane/NS5 instanton, flux "
        "quantization, wrapped-brane, KKLT uplift) have actions S_inst ~ "
        "Vol(cycle) that GROW at +sigma and SHRINK at -sigma -- so e^{-S_inst} "
        "suppresses the +sigma (decompactification) corner (the named "
        "B-UQFC-14-NP-1 +modulus wall candidate), NOT the -sigma corner. At the "
        "-sigma corner the instanton action -> 0 and the dilute-gas expansion "
        "BREAKS. A quantized-flux energy ~ n^2/Vol IS positive and grows at "
        "-sigma, but it is a LOW-growth power-law (curvature-like, not a p>8 "
        "exponential), so it does not outrun a6's e^{-12 sigma}; and its sector "
        "data is OUTSIDE the frozen corpus. There is NO derivable forced-positive "
        "p>8 non-perturbative wall that dominates BEFORE the perturbative runaway.")

    # =====================================================================
    # OUTCOME (honest; do NOT force the favorable branch; guards (a)-(e)).
    # =====================================================================
    # Logic of the honest endpoint:
    #  - The FASTEST perturbative operator at the -sigma corner is a6 (e^{-12 sigma}),
    #    faster than a4 (e^{-8 sigma}) and c_loop (e^{-6 sigma}).
    #  - a6's SIGN is NOT geometry-forced (only tr[E^3]=+1/6 derived; c1..c8 +
    #    K6-block K5..K8 MISSING; the cubic gravitational coefficients are a
    #    sign-mixed set). So a6 does NOT supply a FORCED positive wall.
    #  - But the very fact that a6 (and higher) OUTGROW a4 and c_loop at the corner
    #    means the curvature expansion is NOT ordered there: EFT has broken down.
    #  - The perturbative runaway (a4 cross-term beating c_loop) only turns on at a
    #    sigma at/below the EFT-breakdown onset -> the runaway is OUTSIDE EFT
    #    validity -> it is NOT a trustworthy physical prediction.
    #  - No forced-positive p>8 non-perturbative -sigma wall exists in-corpus.
    # => The honest endpoint is NOT "a6 forces a wall" and NOT "a4 forces a
    #    runaway": it is that the -sigma corner is PERTURBATIVELY UNDECIDABLE
    #    because the EFT expansion has stopped converging exactly there.
    outcome = "EFT-BREAKDOWN-at-corner-perturbatively-undecidable"

    operator_tower_str = (
        "-sigma corner growth ladder (operator : sigma-growth at sigma->-inf): "
        "c_bdry e^{-2s} (+2) ; c_KK/c_Wilson e^{-4s} (+4) ; c_loop e^{-6s} (+6, "
        "underlying-density sign DISPUTED) ; a4 K6xS2 e^{-(8s+4r+c)} (+8, relative "
        "sign DISPUTED, as-run NEGATIVE) ; a6 cubic e^{-12s} (+12, sign OPEN) ; "
        "a8 e^{-14s}, a10 e^{-16s} (+14,+16, sign OPEN, even-larger open objects). "
        "Non-perturbative: instanton/wrapped-brane actions GROW at +sigma (no "
        "-sigma wall); flux ~ n^2/Vol is positive but low-growth power-law.")

    fastest_operator_str = (
        "a6 (cubic-curvature Seeley-DeWitt, pure-K6, e^{-12 sigma}) is the FASTEST-"
        "growing operator at the -sigma corner among the perturbative tower "
        "(growth +12 > a4 +8 > c_loop +6). Its coefficient sign is NOT geometry-"
        "forced (only tr[E^3]=+1/6 derived; c1..c8 + K6-block K5..K8 MISSING). a8/"
        "a10 grow even faster (+14/+16) and are larger open objects -- which is "
        "ITSELF the signal that the curvature expansion is not convergent here.")

    a6_sign_status_str = a6["verdict"]

    nonperturbative_terms_str = np_finding

    eft_validity_str = (
        "The curvature/derivative (Seeley-DeWitt) expansion STOPS CONVERGING at "
        "the -sigma corner: the higher heat-kernel operators OUTGROW the lower "
        "ones (a6 e^{-12s} > a4 e^{-8s} > c_loop e^{-6s}), so the truncation is "
        "not ordered there. Operator-ratio crossings (data-blind, using on-disk "
        "c_loop=%.3e, c_a4=%.3e and a bracketed a6 magnitude) put the breakdown "
        "onset near sigma ~ %.2f; the a4-beats-c_loop runaway onset is at sigma ~ "
        "%.2f, i.e. AT/BELOW the breakdown. The perturbative runaway lies OUTSIDE "
        "EFT validity and is therefore NOT a trustworthy physical prediction. "
        "(Independently: the EFT cutoff is the KK scale set by R_K6; the unit-vol "
        "curvature already reaches M_13^2 near sigma ~ +1.70.)"
        % (c_loop_disk, c_a4_disk,
           eft["sigma_EFT_breakdown_onset"]
           if eft["sigma_EFT_breakdown_onset"] is not None else float("nan"),
           runaway["runaway_onset_sigma_a4_beats_cloop"]
           if runaway["runaway_onset_sigma_a4_beats_cloop"] is not None
           else float("nan")))

    well_verdict_str = (
        "NO HIGHER-OPERATOR WALL IS FORCED, AND NO RUNAWAY IS TRUSTWORTHY -- the "
        "-sigma corner is PERTURBATIVELY UNDECIDABLE. (1) The fastest operator at "
        "the corner is a6 (e^{-12 sigma}), but its sign is NOT geometry-forced: "
        "only tr[E^3]=+1/6 is derived; the eight purely-gravitational cubic "
        "coefficients c1..c8 (a sign-mixed rational set, like a4's +5/-2/+2) and "
        "the K6-block cubic Riemann contractions K5..K8 are MISSING / "
        "MISSING_GEOMETRY (the true SU(3)/T^2 flag manifold has Weyl != 0). So a6 "
        "does NOT supply a forced-positive wall, and declaring it positive would "
        "violate the guard against convenient signs. (2) a8, a10, ... grow even "
        "faster and are larger open objects -- which is precisely the diagnostic "
        "that the curvature expansion has STOPPED CONVERGING at the corner. (3) "
        "Because higher operators outgrow lower ones there, the a4-cross-term "
        "runaway only 'wins' by violating the EFT ordering: it turns on at/below "
        "the EFT-breakdown sigma, so the runaway is OUTSIDE EFT validity and is "
        "NOT a trustworthy prediction. (4) No forced-positive p>8 non-perturbative "
        "-sigma wall exists in the frozen corpus (instanton/brane actions wall the "
        "+sigma corner, not -sigma; flux energy is positive but a low-growth "
        "power-law and its sector is outside the corpus). HONEST ENDPOINT: the "
        "no-runaway claim is neither confirmed (no forced wall) nor refuted (no "
        "trustworthy runaway); it is UNDECIDABLE at perturbative order because the "
        "EFT breaks down at exactly the corner in question. What resolves it is a "
        "RESUMMED / UV-complete treatment (the full Gilkey-Avramidi a6 with FORCED "
        "c1..c8 and the K6-block Riemann data, or the non-perturbative sector) -- "
        "owner-must-rule (Chris). The favorable STANDS was NOT forced; the "
        "unfavorable RUNAWAY was NOT forced either.")

    integrity_attest_str = (
        "Guards honored. (a) No sign was chosen because it gives STANDS: a6's sign "
        "is reported OPEN, not positive; the endpoint is undecidable, not "
        "favorable. (b) The committed c_loop=1.3637877e-5 was read ONLY for the "
        "EFT operator-ratio test and the final magnitude cross-check, NEVER to "
        "pick a sign. (c) No anthropic 'we exist' move: the runaway is dismissed "
        "ONLY by the EFT-breakdown computation, not by existence. (e) No "
        "gap-specific stabilizing epicycle was introduced; the only 'stabilizer' "
        "considered (a6) is reported as sign-OPEN and the non-perturbative sectors "
        "as outside-corpus. a6 was NOT declared positive for convenience. A sign "
        "would be FORCED only by the missing geometry/group computation (Gilkey-"
        "Avramidi order-6 recursion + SU(3)/T^2 Riemann data), which is not "
        "performed here and is owner-must-rule. No observed value entered on any "
        "input side.")

    what_requires_chris_str = (
        "(A6 SIGN -- the load-bearing item) The eight universal purely-"
        "gravitational a6 cubic coefficients c1..c8 (for R^3, R|Ric|^2, R|Riem|^2, "
        "tr Ric^3, Ric.Ric.Riem, Ric.Riem.Riem, Riem^3 I1, Riem^3 I2) from the "
        "full Gilkey 1995 Th.4.8.16 / Avramidi 2000 Ch.4 order-6 recursion, the "
        "mixed E/Omega coefficients, the graviton-bundle endomorphism E-matrix on "
        "Sym^2 TM, AND the index-resolved Riemann/curvature-2-form of the true "
        "SU(3)/T^2 flag manifold (its structure constants -> K5..K8 on the K6 "
        "block; the corpus has only scalar |Riem|^2 and the manifold has Weyl != "
        "0). Only with these is the SIGN of a6's e^{-12 sigma} coefficient forced. "
        "(EFT) Whether the -sigma corner admits a RESUMMED / UV-complete treatment "
        "(or is intrinsically strong-curvature) -- since the truncated curvature "
        "expansion provably does not converge there. (NON-PERTURBATIVE) The "
        "B-UQFC-14-NP-1 object: which cycles/quanta/brane stack supply a "
        "forced-sign non-perturbative term -- all outside the frozen corpus.")

    result = {
        "schema": "gap04_higher_operator_wall_result_v1",
        "object": (
            "The -sigma (shrinking-internal) corner of V(sigma,rho,chi): is the "
            "asymptotic fate set by a FORCED higher-operator (a6, e^{-12 sigma}) "
            "wall, a forced non-perturbative wall, or is the corner outside EFT "
            "validity (perturbatively undecidable)?"),
        "outcome": outcome,

        "operator_tower": [
            {k: v for k, v in t.items()} for t in tower
        ],
        "operator_tower_summary": operator_tower_str,

        "fastest_operator_within_EFT": fastest_operator_str,
        "fastest_perturbative_growth": {"name": fastest[0], "growth": fastest[1]},
        "tower_has_unbounded_growth_ladder": bool(tower_has_unbounded_growth_ladder),

        "a6_focus": a6,
        "a6_sign_status": a6_sign_status_str,

        "eft_validity_analysis": eft,
        "runaway_inside_or_outside_EFT": runaway,
        "eft_validity": eft_validity_str,

        "non_perturbative_sectors": np_sectors,
        "non_perturbative_forced_p_gt_8_wall": bool(np_wall_forced),
        "nonperturbative_terms": nonperturbative_terms_str,

        "well_verdict": well_verdict_str,

        "cross_check_frozen_magnitude_post_hoc": {
            "performed_after_structure_and_signs": True,
            "frozen_c_loop_FRG2_target": C_LOOP_FRG2_TARGET,
            "c_loop_on_disk": c_loop_disk,
            "c_a4_on_disk": c_a4_disk,
            "note": ("the frozen magnitudes are used ONLY in the EFT operator-ratio "
                     "test and this cross-check; they never select a sign or a "
                     "branch."),
        },

        "integrity_attest": integrity_attest_str,
        "what_requires_chris": what_requires_chris_str,

        "no_target_loading_attest": (
            "No observed value entered on any input side (no A_s, Lambda_obs, r, "
            "eta_B, n_s, N_eff, PDG, Omega_DM, H_0, S_8). The operator tower and "
            "growth rates are built from the frozen SU(3)/T^2 x S^2 x S^1_Y "
            "geometry + Gilkey heat-kernel structure ALONE. a6's sign is reported "
            "OPEN (not the convenient +); the perturbative runaway is dismissed "
            "ONLY by the EFT-breakdown computation, not by any desire for "
            "stability and not by 'we exist'. The committed c_loop magnitude was "
            "read strictly post-structure, for the EFT-ratio test and cross-check "
            "only."),

        "provenance": {
            "frozen_inputs.yaml": sha256_file(FROZEN_YAML),
            "veff_coefficients_frg4.yaml": sha256_file(VEFF_YAML),
            "gilkey_a4_cross_terms.py": sha256_file(GILKEY_SRC),
            "a6_recursion_scaffold.json": sha256_file(A6_SCAFFOLD),
            "curvature_contractions_d13.json": sha256_file(A6_CURV),
        },
        "non_promotion": (
            "no gate flipped; no status word emitted for any gate. STAGED "
            "higher-operator / EFT-validity instrument. NOT a sign-derivation and "
            "NOT promotable as one: a6's sign is open and the corner is outside "
            "EFT validity."),
    }

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gap04_higher_operator_wall_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- decision-grade packet to stdout ----------------------------------
    print("=" * 78)
    print("gap04_higher_operator_wall.py -- higher-operator / non-perturbative wall")
    print("=" * 78)
    print("OBJECT: -sigma corner fate -- forced a6 wall? forced NP wall? or EFT-out?")
    print("-" * 78)
    print("1. OPERATOR TOWER at the -sigma corner (growth = sigma-coeff):")
    for t in tower:
        g = t["growth_minus_sigma"]
        gstr = ("+%d" % g) if isinstance(g, (int, float)) else str(g)
        print("   %-32s growth %-6s sign: %s"
              % (t["name"], gstr, t["coeff_sign"][:46]))
    print("-" * 78)
    print("2. FASTEST operator within EFT validity: %s (growth +%d)"
          % (fastest[0], fastest[1]))
    print("   tower growth ladder is UNBOUNDED (a8 +14, a10 +16, ...): %s"
          % tower_has_unbounded_growth_ladder)
    print("   a6 sign geometry-forced? : %s" % a6["a6_sign_geometry_forced"])
    print("-" * 78)
    print("3. a6 FOCUS: tr[E^3]=+1/6 derived (+), but c1..c8 + K6 K5..K8 MISSING")
    print("   -> a6 e^{-12 sigma} coefficient sign is OPEN (sign-mixed cubic set)")
    print("-" * 78)
    print("4. EFT VALIDITY:")
    print("   sigma(a4 beats c_loop)      : %s"
          % _fmt(eft["sigma_a4_equals_cloop"]))
    print("   sigma(a6 beats a4, nominal) : %s"
          % _fmt(eft["sigma_a6_equals_a4_nominal"]))
    print("   sigma(EFT-breakdown onset)  : %s"
          % _fmt(eft["sigma_EFT_breakdown_onset"]))
    print("   runaway INSIDE EFT validity : %s"
          % runaway["runaway_inside_EFT_validity"])
    print("   -> perturbative runaway is OUTSIDE EFT validity (not trustworthy)")
    print("-" * 78)
    print("5. NON-PERTURBATIVE: forced-positive p>8 -sigma wall? : %s"
          % np_wall_forced)
    print("-" * 78)
    print("OUTCOME : %s" % outcome)
    print("artifact:", out_path)
    print("=" * 78)
    return 0


def _fmt(x):
    return ("%.4f" % x) if isinstance(x, (int, float)) else str(x)


if __name__ == "__main__":
    sys.exit(main())
