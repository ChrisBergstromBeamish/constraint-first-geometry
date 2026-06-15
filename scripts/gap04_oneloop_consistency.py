#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gap04_oneloop_consistency.py
============================
Gap-04 ONE-LOOP CONSISTENCY FIX -- standalone licensing computation.

Companion to gap04_convention_audit.py and gap04_disjointness.py. It identifies
the corpus's GENUINE single one-loop log-det convention, applies it to the a_4
cross-term from the FROZEN inputs ONLY, and reports the sign c_a4 actually takes
-- WITHOUT forcing the favorable "well-stands" outcome.

NO observed value enters (no A_s, Lambda_obs, r, eta_B, n_s, N_eff, PDG). It does
not flip a gate; it emits a countersign-ready result the owner signs.

====================================================================
THE GENUINE SINGLE CONVENTION -- AND WHAT IT DOES *NOT* FORCE
====================================================================
The bosonic one-loop effective potential in the heat-kernel proper-time
representation is

    V^(1-loop)(x) = -(1/2) (4 pi)^{-D/2} * sum_n a_n(D) * (proper-time moments)

The prefactor  -(1/2)(4 pi)^{-D/2}  is GLOBAL to every heat-kernel coefficient
a_n. This is true and it IS the single convention. BUT a global prefactor common
to all a_n does NOT force two coefficients to the SAME SIGN. The sign of each
term is

    sign(c_n) = sign(global -1/2) x sign(that term's OWN integrand).

For the a_4 cross-term the integrand is (1/36) R_K6 R_S2 with R_K6 = +30,
R_S2 = +2 (single-signed curvature registry; convention-invariant +5/360 master
coefficient). The integrand is MANIFESTLY POSITIVE. Therefore the genuine global
-(1/2) acting on a positive integrand gives

    c_a4 = -(1/2)(4 pi)^{-13/2}(1/36)(30)(2) = -5.97e-08   (NEGATIVE)

-- exactly what the original/as-run gilkey_a4_cross_terms.py computed.

====================================================================
WHY THE RELATIVE-SIGN-VS-c_loop QUESTION IS GENUINELY OWNER-LOCKED
====================================================================
The ONLY way c_a4 comes out POSITIVE is to ASSERT that the stored c_loop
(+1.36e-5) "already absorbed a -(1/2) acting on a NEGATIVE underlying density,"
and then tie c_a4's relative sign to MATCH c_loop. That assertion has NO
derivation behind it:

  * z_renormalized_c_loop.py reads c_loop as a FROZEN inherited number
    (Fable-Latest shell projection) and only multiplies by a Z-factor ~0.99995.
    It derives NO sign from any -(1/2) log-det; the sign of c_loop's underlying
    heat-kernel density is never computed.
  * TOE_FINAL_merged.md records c_loop as OPEN -- "the loop coefficient of V(sigma)
    is not computed from first principles" (Known-weakest-links #13 / the c_loop
    stanza). Its positivity is merely ASSUMED and guarded by falsifier F6.

So neither branch is forced data-blind:

  BRANCH-RUNAWAY (genuine global -1/2 acts on a positive integrand):
      c_a4 = -5.97e-08 < 0. At the -sigma corner the a_4 operator (growth 8)
      DOMINATES the c_loop wall (growth 6); a negative dominant term => V -> -inf,
      a REAL separate 3-modulus -sigma runaway threatening F1.
  BRANCH-STANDS (owner rules c_loop's underlying density NEGATIVE, so the shared
      one-loop treatment flips a_4's relative sign):
      c_a4 = +5.97e-08 > 0, a positive wall; the -sigma well stands at FRG-4.

The DECIDING FACT -- the sign of c_loop's underlying heat-kernel density -- is
NOT banked anywhere in the corpus (the CONVENTION_FREEZE slot for the a_4 sector
is unfilled). This is exactly an OWNER-MUST-RULE, which gap04_convention_audit.py
ORIGINALLY recorded and gap04_disjointness.py flagged as convention_dependent.

NOTE ON THE FROZEN PREREG: the prereg gilkey_a4_protocol is INTERNALLY
SELF-CONTRADICTORY on this exact point -- einstein_frame_reduction carries the
explicit -(1/2) (=> NEGATIVE c_a4) while honest_sign_assessment drops it and
declares "POSITIVE sign" for the DENSITY, attached to a cross-term scaling
exp(-(14 sigma + 6 rho + 2 chi)) that does NOT match the computed operator
exp(-(8 sigma + 4 rho + chi)). So the prereg's "POSITIVE" is the DENSITY sign,
not a one-loop-consistent c_a4 prediction, and citing it as corroboration of a
POSITIVE c_a4 is selecting the favorable half of a self-contradictory spec. This
script therefore does NOT use the prereg as a tie-breaker.

====================================================================
ENDPOINT CLASSIFICATION (frozen before the run; the script reports which)
  R-STANDS  : the relative one-loop sign is DERIVABLE data-blind and makes c_a4
              SAME sign as c_loop (positive). Requires c_loop's underlying
              density sign to be banked NEGATIVE -- it is not.
  R-RUNAWAY : the relative sign is DERIVABLE data-blind and makes c_a4 OPPOSITE
              to c_loop (negative) -> a real separate -sigma runaway row.
  R-INDET   : the relative one-loop sign is NOT resolvable data-blind (c_loop's
              underlying density sign is unbanked) -> owner rules, BOTH branches
              live. <-- this is the honest outcome.
====================================================================

NON-PROMOTION: no gate flip; countersign-input only. exit 0 on any honest
resolution; exit 2 if frozen inputs unreadable / a forbidden token leaks.
"""

import hashlib
import json
import math
import os
import sys

FA = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
      r"physics_Journal_and_patents/Final_physics_articles/scripts/gap_04")
FROZEN_YAML = os.path.join(FA, "frozen_inputs.yaml")
GILKEY_JSON = os.path.join(FA, "outputs", "gilkey_a4_cross_terms.json")
VEFF_YAML = os.path.join(FA, "outputs", "veff_coefficients_frg4.yaml")
GILKEY_SRC = os.path.join(FA, "src", "gilkey_a4_cross_terms.py")
GILKEY_BAK = os.path.join(FA, "src",
                          "gilkey_a4_cross_terms.py.pre_oneloop_fix_2026-06-14.bak")

FORBIDDEN_TOKENS = [
    "A_s ", "A_s=", "Lambda_obs", "lambda_obs", "eta_B", "n_s_obs",
    "N_eff_obs", "PDG", "Planck_n_s", "BICEP", "LiteBIRD_r", "r_obs",
    "Omega_DM_obs",
]

# ---------------------------------------------------------------------------
# FROZEN inputs (copied by reference from gap_04/frozen_inputs.yaml; these are
# geometry / master-coefficient / normalization constants, NOT observed values).
# ---------------------------------------------------------------------------
R_K6_0 = 30.0          # = n*lambda = 6*5 ; Besse Tab 7.107 (Einstein +5 on F_3)
R_S2_0 = 2.0           # = n*lambda = 2*1 ; round S^2 (Einstein +1)
A4_R2_MASTER_COEFF = 5.0 / 360.0        # convention-INVARIANT master coeff of R^2
A4_CROSS_PREFACTOR = 2.0 * A4_R2_MASTER_COEFF   # = 1/36 (the 2 from R^2 cross)
D_BULK = 13
HK_NORM = 1.0 / (math.pow(4.0 * math.pi, D_BULK / 2.0))   # (4 pi)^{-D/2} > 0

# The GENUINE single one-loop log-det prefactor: the global bosonic -(1/2).
GENUINE_GLOBAL_ONE_LOOP_PREFACTOR = -0.5


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def read_c_loop_from_veff(path):
    val = None
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            s = line.strip()
            if s.startswith("c_loop_Z:"):
                try:
                    val = float(s.split(":", 1)[1].split("#")[0].strip())
                except ValueError:
                    pass
    return val


def c_loop_underlying_density_sign_is_banked(frozen_text, veff_text):
    """
    Is the SIGN of c_loop's underlying heat-kernel density banked anywhere we
    can read? The decisive owner-rule input. We look for an explicit statement
    of the underlying-density sign tied to a -(1/2) log-det -- NOT merely the
    stored positive c_loop value (which is the resolved wall coefficient, whose
    underlying-density sign is exactly the unknown). The corpus does not bank it,
    so this returns False (honest).
    """
    # A banked underlying-density sign would look like an explicit
    # "c_loop_underlying_density_sign: ..." slot. None exists in the frozen
    # inputs or the veff table; c_loop is carried as a frozen positive WALL value
    # only. z_renormalized_c_loop.py applies no -(1/2) and derives no density sign.
    markers = ["c_loop_underlying_density_sign",
               "c_loop_density_sign",
               "c_loop_pre_oneloop_density"]
    for m in markers:
        if m in frozen_text or m in veff_text:
            return True
    return False


def main():
    for p in (FROZEN_YAML, GILKEY_JSON, VEFF_YAML, GILKEY_SRC):
        if not os.path.exists(p):
            sys.stderr.write("REFUSE(exit2): missing input %s\n" % p)
            return 2

    # forbidden-input firewall on the (fixed) derivation source
    with open(GILKEY_SRC, "r", encoding="utf-8") as fh:
        src_text = fh.read()
    leaked = [t for t in FORBIDDEN_TOKENS if t in src_text]
    if leaked:
        sys.stderr.write("REFUSE(exit2): forbidden token(s) in source: %s\n"
                         % leaked)
        return 2

    with open(FROZEN_YAML, "r", encoding="utf-8") as fh:
        frozen_text = fh.read()
    with open(VEFF_YAML, "r", encoding="utf-8") as fh:
        veff_text = fh.read()

    # ---- the a_4 cross-DENSITY (pre one-loop), pinned positive --------------
    density_core = A4_CROSS_PREFACTOR * R_K6_0 * R_S2_0    # (1/36)*30*2 = +5/3
    a4_density_pre_oneloop = HK_NORM * density_core         # strictly > 0
    density_sign = "+" if a4_density_pre_oneloop > 0 else (
        "-" if a4_density_pre_oneloop < 0 else "0")

    # ---- c_a4 under the GENUINE global one-loop prefactor (-1/2) ------------
    # global -1/2 acts on this term's OWN (positive) integrand => NEGATIVE.
    c_a4_genuine = GENUINE_GLOBAL_ONE_LOOP_PREFACTOR * a4_density_pre_oneloop

    # ---- the two LIVE branches ---------------------------------------------
    c_a4_branch_runaway = c_a4_genuine                  # = -5.97e-08
    c_a4_branch_stands = -c_a4_genuine                  # = +5.97e-08 (only if
    #   the owner rules c_loop's underlying density NEGATIVE so the shared
    #   one-loop treatment flips a_4's relative sign)

    # ---- the c_loop wall (frozen positive WALL value, load-bearing F6) ------
    c_loop = read_c_loop_from_veff(VEFF_YAML)
    c_loop_wall_positive = (c_loop is not None and c_loop > 0)

    # ---- IS the deciding fact banked? --------------------------------------
    deciding_fact_banked = c_loop_underlying_density_sign_is_banked(
        frozen_text, veff_text)

    # ---- disjointness dominance at the -sigma corner (mechanical) ----------
    # a_4 operator exp(-(8 sigma + 4 rho + chi)) -> growth at -sigma = +8;
    # c_loop operator exp(-6 sigma) -> growth at -sigma = +6. So a_4 dominates.
    growth_a4_neg_sigma = 8.0
    growth_cloop_neg_sigma = 6.0
    a4_dominates_neg_sigma = growth_a4_neg_sigma > growth_cloop_neg_sigma

    # ---- RESOLUTION (do NOT force stands) ----------------------------------
    if deciding_fact_banked:
        # If (and only if) the corpus had banked c_loop's underlying-density
        # sign, the relative one-loop sign would be derivable; report which way.
        if c_a4_branch_stands > 0 and c_loop_wall_positive:
            resolution = "RESOLVED-well-stands"
        else:
            resolution = "RESOLVED-well-refuted-separate-runaway-row"
        resolution_reason = (
            "c_loop's underlying-density sign IS banked; the relative one-loop "
            "sign is derivable data-blind and selects a single branch.")
    else:
        resolution = "INDETERMINATE-owner-must-rule"
        resolution_reason = (
            "The GENUINE single one-loop convention is the global bosonic "
            "-(1/2)(4pi)^{-D/2}, but a global prefactor does NOT fix the SIGN "
            "of c_a4 relative to c_loop -- each term's sign = (global -1/2) x "
            "(its OWN integrand). Acting on the a_4 cross integrand (MANIFESTLY "
            "POSITIVE: (1/36)*R_K6*R_S2 with R_K6,R_S2 > 0) the genuine -(1/2) "
            "gives c_a4 NEGATIVE (-5.97e-08), the as-run value. To make c_a4 "
            "POSITIVE one must ASSERT c_loop's stored +value already absorbed a "
            "-(1/2) acting on a NEGATIVE underlying density and match a_4 to it; "
            "but c_loop's underlying-density sign is NEVER established in the "
            "corpus (z_renormalized_c_loop.py reads c_loop as a frozen inherited "
            "number and applies no -(1/2); TOE_FINAL records c_loop as OPEN / "
            "not computed from first principles, positivity merely assumed, "
            "guarded by F6). So the relative one-loop sign is NOT resolvable "
            "data-blind: BOTH branches are live (BRANCH-RUNAWAY c_a4<0 -> real "
            "-sigma runaway since a_4 growth 8 dominates c_loop growth 6, "
            "threatening F1; BRANCH-STANDS c_a4>0 only if the owner rules "
            "c_loop's underlying density negative). This is an OWNER-MUST-RULE, "
            "exactly as gap04_convention_audit.py ORIGINALLY recorded and "
            "gap04_disjointness.py flagged (convention_dependent = owner-locked). "
            "We do NOT force 'stands'.")

    result = {
        "schema": "gap04_oneloop_consistency_result_v2",
        "purpose": (
            "Apply the corpus's GENUINE single one-loop log-det convention to "
            "the a_4 cross-term and report the sign c_a4 takes -- without forcing "
            "the favorable well-stands outcome."),
        "resolution": resolution,
        "resolution_reason": resolution_reason,
        "genuine_single_convention": (
            "V^(1-loop) = -(1/2)(4 pi)^{-D/2} sum_n a_n. The -(1/2)(4pi)^{-D/2} "
            "prefactor is GLOBAL to every a_n, but does NOT force same-sign: "
            "sign(c_n) = sign(-1/2) x sign(own integrand). c_a4's integrand "
            "(1/36)*R_K6*R_S2 > 0 => c_a4 NEGATIVE under the genuine convention."),
        "provenance_hashes": {
            "frozen_inputs.yaml": sha256_file(FROZEN_YAML),
            "gilkey_a4_cross_terms.json": sha256_file(GILKEY_JSON),
            "veff_coefficients_frg4.yaml": sha256_file(VEFF_YAML),
            "gilkey_a4_cross_terms.py_FIXED": sha256_file(GILKEY_SRC),
            "gilkey_a4_cross_terms.py.pre_oneloop_fix_2026-06-14.bak":
                sha256_file(GILKEY_BAK) if os.path.exists(GILKEY_BAK) else None,
        },
        "frozen_inputs_used": {
            "R_K6_0": R_K6_0, "R_S2_0": R_S2_0,
            "a4_R2_master_coeff_5_over_360": A4_R2_MASTER_COEFF,
            "a4_cross_prefactor_1_over_36": A4_CROSS_PREFACTOR,
            "D_bulk": D_BULK,
            "factor_4pi_to_minus_D_over_2": HK_NORM,
            "genuine_global_one_loop_prefactor": GENUINE_GLOBAL_ONE_LOOP_PREFACTOR,
        },
        "computation": {
            "a4_cross_density_pre_oneloop": a4_density_pre_oneloop,
            "a4_cross_density_sign": density_sign,
            "c_a4_under_genuine_global_minus_half": c_a4_genuine,
            "c_a4_BRANCH_RUNAWAY_value": c_a4_branch_runaway,
            "c_a4_BRANCH_STANDS_value": c_a4_branch_stands,
            "c_loop_wall_value_frozen": c_loop,
            "c_loop_wall_positive_loadbearing_F6": c_loop_wall_positive,
            "c_loop_underlying_density_sign_banked": deciding_fact_banked,
            "arithmetic_check": (
                "c_a4 = (+/-)0.5*(4pi)^-6.5*(1/36)*30*2 = (+/-)5.97e-08"),
        },
        "disjointness_dominance_at_neg_sigma": {
            "growth_a4_cross": growth_a4_neg_sigma,
            "growth_c_loop_wall": growth_cloop_neg_sigma,
            "a4_dominates_neg_sigma_corner": a4_dominates_neg_sigma,
            "consequence_if_c_a4_negative": (
                "a_4 (growth 8) dominates c_loop (growth 6) at the -sigma corner; "
                "with c_a4 < 0 the dominant term drives V -> -inf, a REAL separate "
                "3-modulus -sigma runaway threatening F1."),
        },
        "branches": {
            "BRANCH_STANDS": {
                "condition": (
                    "owner rules c_loop's UNDERLYING heat-kernel density NEGATIVE, "
                    "so the shared single one-loop treatment flips a_4's relative "
                    "sign to +"),
                "c_a4": c_a4_branch_stands,
                "effect": "c_a4 a POSITIVE wall; -sigma well STANDS at FRG-4.",
                "named_falsifier": (
                    "F1_ext: if the owner banks c_loop underlying density "
                    "negative AND a true interior critical point is found, the "
                    "well stands; refuted if no such point exists."),
            },
            "BRANCH_RUNAWAY": {
                "condition": (
                    "the genuine global -(1/2) acts on both terms' own positive "
                    "densities (c_a4 keeps its as-run NEGATIVE sign)"),
                "c_a4": c_a4_branch_runaway,
                "effect": (
                    "c_a4 < 0 and DOMINATES the -sigma corner (growth 8 > 6); "
                    "V -> -inf: a REAL separate 3-modulus -sigma runaway row."),
                "named_falsifier": (
                    "F1: any unbounded direction with V_eff -> -inf. Under this "
                    "branch the -sigma FRG-4 corner FAILS F1 at decision grade "
                    "unless a non-perturbative wall (B-UQFC-14-NP-1) supplies a "
                    "barrier."),
            },
        },
        "deciding_fact_for_owner": (
            "The SIGN of c_loop's underlying heat-kernel density (equivalently: "
            "is c_loop a -(1/2) log-det of a NEGATIVE-density object, or a "
            "positive Casimir wall under a DIFFERENT bookkeeping?). It is NOT "
            "banked anywhere (the CONVENTION_FREEZE a_4-sector slot is unfilled). "
            "Banking it resolves the relative one-loop sign and selects one "
            "branch."),
        "prereg_is_self_contradictory_not_a_tiebreaker": (
            "frozen_inputs.yaml gilkey_a4_protocol carries the explicit -(1/2) in "
            "einstein_frame_reduction (=> c_a4 NEGATIVE) AND 'POSITIVE sign' in "
            "honest_sign_assessment (dropping the -(1/2); referring to the DENSITY "
            "sign, attached to exp(-(14 sigma+6 rho+2 chi)) which does NOT match "
            "the computed operator exp(-(8 sigma+4 rho+chi))). The prereg's "
            "'POSITIVE' is the density sign, not a one-loop-consistent c_a4 "
            "prediction; citing it as corroboration of a positive c_a4 selects "
            "the favorable half of a self-contradictory spec. NOT used as a "
            "tie-breaker here."),
        "implication_for_well": (
            "The -sigma FRG-4 well's survival is CONDITIONAL on the owner-locked "
            "relative one-loop sign. It is NOT forced to stand (the genuine "
            "convention gives c_a4 NEGATIVE on its own positive integrand), and "
            "it is NOT forced to fail (the relative sign vs c_loop is unbanked). "
            "Owner must rule; both branches carry named falsifiers."),
        "implication_for_v10": (
            "INDEPENDENT of this ruling: v10's Section-II 'well UNCONDITIONAL in "
            "c_loop' is TRUE AS STATED and needs NO erratum. It quantifies over "
            "the SINGLE-sigma potential V(sigma)=c_KK e^-4s + c_bdry e^-2s + "
            "c_Wilson cos(theta_W) e^-4s + c_loop e^-6s, whose well-robustness "
            "rides on c_bdry < 0 (no value of c_loop in the declared lane "
            "threatens the well). The a_4 cross-term exp(-(8s+4r+chi)) is a "
            "SEPARATE 3-modulus FRG-4 object NOT present in the §II potential, so "
            "v10's claim does not quantify over it. The v10 'no erratum' "
            "reconciliation is correct; it does NOT, however, imply the FRG-4 "
            "3-modulus well stands -- that is the owner-locked item above."),
        "no_target_loading": True,
        "non_promotion": (
            "no gate flipped; source edit is backed up and reversible (the as-run "
            "-1/2 is restored, module is self-consistent); this artifact is a "
            "countersign-READY both-branches packet the owner signs."),
    }

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gap04_oneloop_consistency_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    print("=" * 72)
    print("Gap-04 ONE-LOOP CONSISTENCY -- genuine convention, both branches")
    print("=" * 72)
    print("genuine single convention: -(1/2)(4pi)^{-D/2} GLOBAL to all a_n")
    print("  but sign(c_n) = sign(-1/2) x sign(own integrand) -- NOT same-sign")
    print("-" * 72)
    print("a_4 cross-density (pre one-loop, MANIFESTLY +): %g  [sign %s]"
          % (a4_density_pre_oneloop, density_sign))
    print("c_a4 under GENUINE global -1/2 (own + integrand): %g  [NEGATIVE]"
          % c_a4_genuine)
    print("  BRANCH-RUNAWAY  c_a4 = %g  (as-run; a_4 growth 8 > c_loop 6)"
          % c_a4_branch_runaway)
    print("  BRANCH-STANDS   c_a4 = %g  (only if c_loop underlying density -)"
          % c_a4_branch_stands)
    print("c_loop wall (frozen + WALL value, F6 load-bearing): %g  [%s]"
          % (c_loop, "POSITIVE" if c_loop_wall_positive else "?"))
    print("c_loop UNDERLYING-density sign banked anywhere: %s  <-- the gap"
          % deciding_fact_banked)
    print("-" * 72)
    print("RESOLUTION:", resolution)
    print("  (we do NOT force 'stands'; the relative one-loop sign is owner-locked)")
    print("artifact:", out_path)
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
