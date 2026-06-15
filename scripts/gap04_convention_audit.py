#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gap04_convention_audit.py
=========================
Gap-04 sub-loop instrument: HEAT-KERNEL SIGN-CONVENTION AUDIT.

Companion to gap04_disjointness.py. That script established the -sigma well is
governed at FRG-4 by the a_4 cross-term (growth 8 > 6) with NEGATIVE coefficient,
and flagged the sign as "convention_dependent = owner-locked, not resolved here."

THIS script goes one step further (CFCA: treat the convention as a Duhem-Quine
auxiliary and try to ELIMINATE the inconsistent option). It asks the sharper
question the prior run deferred:

    Is the sign of c_a4_K6_S2 a GENUINELY FREE heat-kernel convention choice, or
    is it PINNED by the corpus's OWN frozen conventions (the curvature-sign
    registry + the one-loop log-det prefactor used elsewhere in the same V_eff)?

It does NOT promote any gate. It emits a result artifact
{convention_pins_sign, c_a4_sign_under_corpus_convention, implication, ...}
that a diff/countersign may cite. It loads the REAL frozen FRG-4 coefficients +
the real gilkey_a4 derivation off disk (no observed value may enter).

====================================================================
SPEC  (written BEFORE the audit -- the EXT-5 freeze)
====================================================================
PURPOSE
  Decompose the sign of c_a4_K6_S2 into its two independent factors and decide,
  for EACH factor, whether the corpus pins it:

    c_a4_K6_S2  =  [ONE_LOOP_SIGN]  x  [HEAT_KERNEL_a4_CROSS_DENSITY]
                 =  [   -1/2     ]  x  [ (1/(4pi)^{D/2}) * (1/36) * R_K6 * R_S2 ]

  FACTOR 1 -- the heat-kernel a_4 cross-DENSITY.
    Master formula (Gilkey 1995 Eq. 4.1.7, the corpus's declared authority):
        a_4 = (1/360) tr[ +5 R^2 - 2 |Ric|^2 + 2 |Riem|^2 - 60 RE + 180 E^2
                          + 60 lap E + 12 lap R ] I + (1/12) tr[Omega^2]
    On a product manifold R = R_1 + R_2 + R_3 is ADDITIVE, so the ONLY cross
    term is in +5 R^2: (5/360)*2*R_i*R_j = (1/36) R_i R_j. |Ric|^2 and |Riem|^2
    are block-additive (no cross). So the cross-density sign is the sign of
        (+1/36) * R_K6 * R_S2.
    Under the corpus's FROZEN curvature-sign registry (R=+n*lambda > 0 on every
    factor: K6 Ric=+5g R=+30; S2 Ric=+g R=+2; verbatim in gap_04/frozen_inputs
    and in TOE_FINAL §II "R = 30, Ric = 5g"), R_K6 and R_S2 are BOTH POSITIVE,
    so the cross-density is PINNED POSITIVE. (This is checked numerically below
    from the on-disk registry; it does NOT depend on a Laplacian-sign choice:
    the a_4 master coefficient of R^2 is +5/360 in BOTH the D=-(nabla^2+E) and
    the D=-(nabla^2)-E Gilkey/Vassilevich conventions, because R^2 is even in
    the curvature and the +5/360 coefficient is convention-invariant.)

  FACTOR 2 -- the one-loop log-det prefactor ONE_LOOP_SIGN.
    gilkey_a4_cross_terms.py multiplies by ONE_LOOP_SIGN = -1/2 (the standard
    -(1/2) ln det from a bosonic one-loop determinant). THIS factor is what makes
    c_a4 negative -- NOT the curvature convention.

  THE PIN TEST (the Duhem-Quine elimination):
    The SAME V_eff already contains c_loop (the e^{-6 sigma} wall) whose sign is
    FROZEN POSITIVE and load-bearing (F6: "c_loop sign positive PRESERVES the
    small-sigma wall"). c_loop is ALSO a one-loop object (a loop term; the
    corpus calls it "one from loops"). For the V_eff to be CONSISTENT, the one
    one-loop sign convention must be applied to BOTH c_loop and c_a4.

      - If the corpus applies -(1/2) log-det to c_a4 (negative) but takes c_loop
        as a +positive wall WITHOUT the same -(1/2), the two terms are under
        DIFFERENT one-loop conventions -> the FRG-4 V_eff is internally
        INCONSISTENT, and the inconsistency is in the SIGN BOOKKEEPING, not in
        the geometry. The honest fix is to put BOTH under one convention.
      - Whichever single convention makes c_loop a +positive wall (F6, frozen,
        load-bearing) is the corpus convention; applied to the POSITIVE a_4
        cross-density it yields the SAME sign as c_loop on its own density.

    So the audit's job is to report: (a) the curvature convention is single and
    pins the a_4 DENSITY positive; (b) the sign of c_a4 then rides entirely on
    the one-loop prefactor, which the corpus ALSO applies (with a fixed sign) to
    c_loop; (c) therefore the sign of c_a4 is NOT a free physical convention --
    it is PINNED to be the SAME relative sign treatment as c_loop. The remaining
    question (does that pinned treatment make c_a4 of the SAME sign as c_loop's
    density, i.e. a +wall, or the opposite) is the single owner-rule item.

ACCEPTANCE  (frozen before the run)
  We do NOT force the well to stand. We report three machine facts and let the
  classification fall out:
    FACT A: curvature registry is single-signed (all R_i > 0)            -> bool
    FACT B: a_4 master R^2 coefficient is +5/360 (convention-invariant)  -> bool
    FACT C: the a_4 cross-DENSITY sign (pre one-loop) is POSITIVE        -> sign
    FACT D: c_loop frozen sign is POSITIVE and load-bearing (F6)          -> sign
    FACT E: c_a4 negativity comes SOLELY from ONE_LOOP_SIGN = -1/2        -> bool
  Then:
    convention_pins_curvature_sign := FACT A and FACT B and (FACT C == '+')
    c_a4_density_sign := FACT C
    sign_is_free_physical_convention := NOT (the one-loop prefactor is shared
        with c_loop)  -> i.e. if c_loop and c_a4 must share one one-loop
        convention, the RELATIVE sign is pinned, not free.

  RESOLUTION (one of three; the script computes which):
    R1 RESOLVED-well-refuted-v10-erratum : corpus convention pins c_a4 NEGATIVE
       in the SAME V_eff where c_loop is positive (i.e. the two one-loop signs
       are genuinely opposite by the corpus's own log-det rule) -> the -sigma
       well genuinely fails at FRG-4 -> v10 "unconditional-in-c_loop" withdrawn.
    R2 RESOLVED-well-stands : the corpus's single one-loop convention, applied
       consistently, makes c_a4 the SAME sign as c_loop's wall (positive) ->
       the FRG-4 run used an inconsistent sign for ONE of the two terms; fixing
       it makes the well stand.
    R3 IRREDUCIBLE-owner-must-rule : the curvature convention is pinned (so the
       DENSITY is positive, not free) BUT whether the one-loop log-det enters
       c_a4 with the same sign as the c_loop wall is a genuine physical
       bookkeeping choice the corpus has not frozen in one place -> owner rules,
       with the decision-grade packet this script prints.

OUTPUTS
  - JSON artifact -> outputs/gap04_convention_audit_result.json
  - human-readable decision-grade packet to stdout
  - exit 0 if artifact produced (any resolution is a valid honest outcome)
  - exit 2 if inputs unreadable / forbidden input detected (refuse)

NON-PROMOTION
  No gate flip. No status word emitted for any gate. Countersign-input only.
====================================================================
"""

import hashlib
import json
import math
import os
import sys

# ---------------------------------------------------------------------------
# On-disk real artifacts (no observed value may enter).
# ---------------------------------------------------------------------------
FA = r"C:/Users/cberg/Desktop/VS Code Projects Random/physics_Journal_and_patents/Final_physics_articles/scripts/gap_04"
GILKEY_JSON = os.path.join(FA, "outputs", "gilkey_a4_cross_terms.json")
VEFF_YAML = os.path.join(FA, "outputs", "veff_coefficients_frg4.yaml")
FROZEN_YAML = os.path.join(FA, "frozen_inputs.yaml")
GILKEY_SRC = os.path.join(FA, "src", "gilkey_a4_cross_terms.py")

FORBIDDEN_TOKENS = [
    "A_s", "Lambda_obs", "lambda_obs", "eta_B", "n_s_obs", "N_eff_obs",
    "PDG", "Planck_n_s", "BICEP", "LiteBIRD_r", "r_obs", "Omega_DM_obs",
]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def grep_value(path, key):
    """Tiny line scanner for 'key: value' (yaml) or '"key": value' (json-ish)."""
    out = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            if key in line:
                out.append(line.strip())
    return out


def main():
    # ---- locate inputs (refuse if missing) --------------------------------
    for p in (GILKEY_JSON, VEFF_YAML, FROZEN_YAML, GILKEY_SRC):
        if not os.path.exists(p):
            sys.stderr.write("REFUSE(exit2): missing input %s\n" % p)
            return 2

    with open(GILKEY_JSON, "r", encoding="utf-8") as fh:
        gilkey = json.load(fh)

    # forbidden-input firewall on the derivation source itself
    with open(GILKEY_SRC, "r", encoding="utf-8") as fh:
        src_text = fh.read()
    leaked = [t for t in FORBIDDEN_TOKENS if t in src_text]
    # The token "A_s" etc must not appear as an INPUT in the derivation. The
    # gilkey source legitimately has none; assert clean.
    if leaked:
        sys.stderr.write("REFUSE(exit2): forbidden token(s) in derivation: %s\n"
                         % leaked)
        return 2
    if gilkey.get("forbidden_inputs_used", True) is not False:
        sys.stderr.write("REFUSE(exit2): gilkey forbidden_inputs_used not False\n")
        return 2

    # ---- FACT A: single-signed curvature registry -------------------------
    reg = gilkey["geometric_constants_inherited"]
    R_K6 = float(reg["R_K6_0"])
    R_S2 = float(reg["R_S2_0"])
    # all nonzero scalar curvatures positive?
    nonzero = [v for v in (R_K6, R_S2) if v != 0.0]
    fact_A_single_signed = all(v > 0 for v in nonzero) and len(nonzero) > 0

    # ---- FACT B: a_4 master coefficient of R^2 is +5/360 ------------------
    # convention-invariant: R^2 is quadratic in curvature; the +5/360 lead is
    # the same in the D=-(nabla^2+E) (Gilkey) and D=-(nabla^2)-E (Vassilevich)
    # conventions. Read it from the recorded master formula string + the
    # explicit cross prefactor 1/36 = 2*5/360.
    cross_prefactor = float(
        gilkey["product_manifold_decomposition_summary"][
            "R_squared_cross_term_coefficient_in_a4"])
    fact_B_master_R2_positive = abs(cross_prefactor - (1.0 / 36.0)) < 1e-12
    # cross density (pre one-loop, pre 4pi norm) sign:
    density_core = cross_prefactor * R_K6 * R_S2   # = (1/36)*30*2 = +5/3

    # ---- FACT C: a_4 cross-DENSITY sign (pre one-loop prefactor) ----------
    hk_norm = float(gilkey["heat_kernel_normalization"][
        "factor_4pi_to_minus_D_over_2"])  # +7.16e-08 > 0
    a4_density_pre_oneloop = hk_norm * density_core  # strictly positive
    fact_C_density_sign = "+" if a4_density_pre_oneloop > 0 else (
        "-" if a4_density_pre_oneloop < 0 else "0")

    # ---- FACT E: c_a4 negativity comes solely from ONE_LOOP_SIGN ----------
    one_loop_sign = float(gilkey["heat_kernel_normalization"][
        "one_loop_log_det_sign"])  # -0.5
    c_a4 = float(gilkey["a4_cross_terms"]["K6_x_S2"][
        "coefficient_value_M13_4_units"])  # -5.97e-08
    # reconstruct: c_a4 == one_loop_sign * a4_density_pre_oneloop ?
    reconstructed = one_loop_sign * a4_density_pre_oneloop
    fact_E_sign_from_oneloop = (
        math.copysign(1.0, c_a4) == math.copysign(1.0, one_loop_sign)
        and abs(reconstructed - c_a4) < 1e-12 * max(1.0, abs(c_a4))
        and a4_density_pre_oneloop > 0
    )

    # ---- FACT D: c_loop frozen sign positive + load-bearing (F6) ----------
    # Read c_loop_Z from the veff yaml (positive); it is the e^{-6 sigma} wall.
    c_loop_lines = grep_value(VEFF_YAML, "c_loop_Z")
    c_loop_val = None
    for ln in c_loop_lines:
        if ln.startswith("c_loop_Z:"):
            try:
                c_loop_val = float(ln.split(":", 1)[1].split("#")[0].strip())
            except ValueError:
                pass
    fact_D_cloop_positive = (c_loop_val is not None and c_loop_val > 0)

    # ---- THE PIN TEST -----------------------------------------------------
    # Curvature convention pins the DENSITY sign (positive). The remaining sign
    # of c_a4 rides ENTIRELY on the one-loop prefactor. The same V_eff makes
    # c_loop a POSITIVE wall. The decisive owner-rule item is whether the
    # corpus's single one-loop log-det treatment puts c_a4 at the SAME sign as
    # the c_loop wall (its own density times the SAME prefactor) or the opposite.
    #
    # What the script can settle data-blind:
    #   - the curvature convention is SINGLE and PINS the density positive (so
    #     the sign is NOT free at the geometry level);
    #   - the negativity is a one-loop-prefactor choice, not a curvature choice;
    #   - c_loop and c_a4 are BOTH one-loop objects in ONE V_eff, so they must
    #     share ONE one-loop sign convention to be consistent.
    convention_pins_curvature_sign = bool(
        fact_A_single_signed and fact_B_master_R2_positive
        and fact_C_density_sign == "+")

    sign_rides_on_oneloop_only = bool(fact_E_sign_from_oneloop)

    # Is the one-loop sign treatment SHARED between c_loop and c_a4 in the
    # on-disk run? In the on-disk run c_loop is taken as a frozen +positive
    # input (no explicit -(1/2) applied in z_renormalized_c_loop.py), while
    # c_a4 has an explicit -(1/2). So as-run they are under DIFFERENT one-loop
    # sign treatments -> internally inconsistent bookkeeping.
    as_run_shares_one_loop_convention = False  # documented mismatch (see SPEC)

    # ---- RESOLUTION -------------------------------------------------------
    # We CANNOT, data-blind, derive whether the physically-correct single
    # convention makes c_a4 a +wall or a -runaway relative to c_loop: that is
    # the genuine sign of a one-loop log-det on a curvature-squared operator vs
    # a KK Casimir loop, which the corpus has NOT frozen in a single
    # source-of-truth doc (the CONVENTION_FREEZE handoff lists "heat-subtraction
    # scheme" and "Nomizu curvature convention" as REQUIRED-to-freeze slots but
    # does not bank the one-loop log-det sign for the a_4 sector). Therefore the
    # honest, non-target-loaded resolution is R3: the CURVATURE sign is pinned
    # (density positive, NOT free), but the one-loop relative sign is a genuine
    # owner-rule item -- with the decisive simplification that it reduces to a
    # SINGLE yes/no the owner can answer (does the a_4 sector carry the same
    # one-loop log-det sign as the c_loop wall?), NOT an open landscape.
    if not convention_pins_curvature_sign:
        resolution = "IRREDUCIBLE-owner-must-rule"
        resolution_reason = (
            "Curvature registry is NOT single-signed as read; cannot pin the "
            "a_4 density sign. Owner must rule on the curvature convention.")
    else:
        # RECONCILED 2026-06-14 (gap04_oneloop_consistency.py v2; restoring the
        # ORIGINAL honest verdict after a manufactured 'well-stands' overwrite was
        # caught by the countersign). The CURVATURE convention is single and pins
        # the a_4 cross-DENSITY positive -- but that does NOT settle the RELATIVE
        # one-loop sign of c_a4 versus the c_loop wall. The single one-loop
        # convention is the GLOBAL bosonic -(1/2)(4pi)^{-D/2}; a global prefactor
        # does NOT force two coefficients to the same SIGN -- sign(c_n) =
        # sign(-1/2) x sign(own integrand). c_a4's integrand (1/36)*R_K6*R_S2 is
        # POSITIVE, so the genuine -(1/2) gives c_a4 NEGATIVE (the as-run value).
        # Making c_a4 positive REQUIRES asserting c_loop's stored +value already
        # absorbed a -(1/2) acting on a NEGATIVE underlying density -- a sign that
        # is NEVER established in the corpus (z_renormalized_c_loop.py reads c_loop
        # as a frozen inherited number; TOE_FINAL records c_loop OPEN, positivity
        # merely assumed, F6-guarded). So the relative one-loop sign is genuinely
        # OWNER-LOCKED with BOTH branches live. We do NOT force 'stands'.
        resolution = "IRREDUCIBLE-owner-must-rule"
        resolution_reason = (
            "The corpus curvature-sign convention is SINGLE and pins the a_4 "
            "cross-DENSITY POSITIVE (FACT A,B,C). The negativity of as-run c_a4 "
            "is the genuine global one-loop prefactor -(1/2) acting on that "
            "POSITIVE density (FACT E) -- NOT an inconsistent extra minus. The "
            "single one-loop convention V^(1-loop) = -(1/2)(4pi)^{-D/2} sum_n a_n "
            "has a GLOBAL prefactor, but a global prefactor does NOT force c_a4 "
            "and c_loop to the same SIGN: each term's sign = (global -1/2) x "
            "(its OWN integrand). To make c_a4 POSITIVE one must assert that the "
            "stored c_loop (FACT D, frozen + WALL value, F6-guarded) already "
            "absorbed a -(1/2) acting on a NEGATIVE underlying density, then "
            "MATCH a_4's relative sign to c_loop. But c_loop's underlying-density "
            "sign is NEVER established (z_renormalized_c_loop.py reads c_loop as "
            "a frozen inherited number and applies no -(1/2); TOE_FINAL records "
            "c_loop as OPEN / not computed from first principles, positivity "
            "merely assumed and guarded by F6). So the RELATIVE one-loop sign is "
            "NOT resolvable data-blind: BOTH branches are live -- BRANCH-RUNAWAY "
            "(genuine -1/2 on a positive density: c_a4 < 0, dominates the -sigma "
            "corner at growth 8 > 6, V -> -inf, a real separate runaway "
            "threatening F1) and BRANCH-STANDS (only if the owner rules c_loop's "
            "underlying density negative: c_a4 > 0, a positive wall, well stands). "
            "This is exactly the OWNER-MUST-RULE this audit ORIGINALLY recorded "
            "and gap04_disjointness.py flagged (convention_dependent). NOT "
            "target-loaded; NOT forced to 'stands'.")

    result = {
        "schema": "gap04_convention_audit_result_v1",
        "purpose": (
            "Decide whether the sign of c_a4_K6_S2 is a FREE heat-kernel "
            "convention or PINNED by the corpus's own conventions."),
        "resolution": resolution,
        "resolution_reason": resolution_reason,
        "provenance_hashes": {
            "gilkey_a4_cross_terms.json": sha256_file(GILKEY_JSON),
            "veff_coefficients_frg4.yaml": sha256_file(VEFF_YAML),
            "gilkey_a4_cross_terms.py": sha256_file(GILKEY_SRC),
        },
        "facts": {
            "FACT_A_curvature_registry_single_signed": fact_A_single_signed,
            "FACT_A_values": {"R_K6_0": R_K6, "R_S2_0": R_S2},
            "FACT_B_a4_master_R2_coeff_is_5_over_360": fact_B_master_R2_positive,
            "FACT_B_cross_prefactor_1_over_36": cross_prefactor,
            "FACT_C_a4_cross_density_sign_pre_oneloop": fact_C_density_sign,
            "FACT_C_density_value_pre_oneloop": a4_density_pre_oneloop,
            "FACT_D_c_loop_frozen_sign_positive_loadbearing_F6":
                fact_D_cloop_positive,
            "FACT_D_c_loop_value": c_loop_val,
            "FACT_E_c_a4_negativity_solely_from_one_loop_prefactor":
                fact_E_sign_from_oneloop,
            "ONE_LOOP_SIGN": one_loop_sign,
            "c_a4_K6_S2_value": c_a4,
        },
        "derived": {
            "convention_pins_curvature_sign": convention_pins_curvature_sign,
            "c_a4_density_sign_under_corpus_convention": fact_C_density_sign,
            "c_a4_sign_rides_on_one_loop_prefactor_only":
                sign_rides_on_oneloop_only,
            "as_run_c_loop_and_c_a4_share_one_loop_convention":
                as_run_shares_one_loop_convention,
            "the_single_owner_rule_item": (
                "Does the a_4 (curvature^2) one-loop log-det enter V_eff with "
                "the SAME sign as the c_loop KK-Casimir wall? Equivalently: is "
                "c_loop's UNDERLYING heat-kernel density NEGATIVE (so the shared "
                "global -(1/2) flips a_4's relative sign to + -> well STANDS), or "
                "is c_loop a positive Casimir wall under a different bookkeeping "
                "(so the genuine global -(1/2) on a_4's own POSITIVE integrand "
                "keeps c_a4 NEGATIVE -> a SEPARATE 3-modulus -sigma runaway row)? "
                "This is one yes/no, owner-locked; NOT a free landscape. The "
                "deciding fact -- the sign of c_loop's underlying density -- is "
                "NOT banked in the corpus, so the script CANNOT resolve it "
                "data-blind. RECONCILED FINDING (gap04_oneloop_consistency.py v2, "
                "2026-06-14): the genuine single one-loop prefactor -(1/2)(4pi)^"
                "{-D/2} is GLOBAL to every a_n, but a global prefactor does NOT "
                "force same-SIGN -- sign(c_n)=sign(-1/2)*sign(own integrand). "
                "c_a4's integrand is POSITIVE, so the genuine -(1/2) gives c_a4 "
                "NEGATIVE (BRANCH-RUNAWAY, the as-run value). c_a4 is POSITIVE "
                "only if the owner banks c_loop's underlying density negative "
                "(BRANCH-STANDS). Both branches are LIVE; the prior "
                "'well-stands' was a manufactured selection of the favorable "
                "branch and is RETRACTED. This stays IRREDUCIBLE-owner-must-rule."),
        },
        "implication_for_v10": (
            "v10 'well UNCONDITIONAL in c_loop' lives in the SINGLE-sigma §II "
            "potential V(sigma)=c_KK e^-4s + c_bdry e^-2s + c_Wilson e^-4s + "
            "c_loop e^-6s, where the well's robustness comes from c_bdry<0 and "
            "the claim is about the c_loop RESIDUE not threatening the well. "
            "The a_4 cross-term e^-(8s+4r+chi) is a THREE-modulus FRG-4 object "
            "NOT present in the §II potential. So v10's 'unconditional in "
            "c_loop' is literally true AS STATED (it quantifies over c_loop), "
            "but it does NOT cover the a_4 cross-term. The FRG-4 result does "
            "not refute v10's c_loop claim; it raises a SEPARATE FRG-4 object "
            "whose sign is the owner-rule item above. RECONCILED: v10's "
            "Section-II unconditional-in-c_loop claim is TRUE AS STATED and "
            "requires NO erratum -- it quantifies over the single-sigma c_loop "
            "residue, not the 3-modulus a_4 cross-term. NOTE (countersign "
            "correction): the v10 'no erratum' finding is correct on its own "
            "terms, but it does NOT imply the FRG-4 3-modulus well stands -- the "
            "a_4 cross-term's relative one-loop sign is owner-locked with both "
            "branches live (it is NOT established to be a positive wall). "
            "'No erratum for v10' and 'the FRG-4 well stands' are SEPARATE "
            "claims; only the former is settled here."),
        "implication_for_well": (
            "The -sigma well's survival at FRG-4 depends on the SINGLE owner "
            "yes/no. The curvature convention does NOT by itself sink the well "
            "(it pins the DENSITY positive); only the one-loop relative sign "
            "does. The well is NOT refuted by the corpus curvature convention; "
            "it is CONDITIONAL on the one-loop log-det relative sign, which is "
            "owner-locked."),
        "no_target_loading": True,
        "non_promotion": "no gate flipped; artifact is countersign-input only",
    }

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gap04_convention_audit_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- decision-grade packet to stdout ----------------------------------
    print("=" * 72)
    print("Gap-04 HEAT-KERNEL SIGN-CONVENTION AUDIT")
    print("=" * 72)
    print("c_a4_K6_S2 = ONE_LOOP_SIGN x heat-kernel a_4 cross-density")
    print("           = (%g) x [ (4pi)^-D/2 * (1/36) * R_K6 * R_S2 ]"
          % one_loop_sign)
    print("           = (%g) x (%g)  =  %g" %
          (one_loop_sign, a4_density_pre_oneloop, c_a4))
    print("-" * 72)
    print("FACT A  curvature registry single-signed (R_K6=%g, R_S2=%g > 0): %s"
          % (R_K6, R_S2, fact_A_single_signed))
    print("FACT B  a_4 master R^2 coeff = +5/360 -> cross 1/36 (conv-invar): %s"
          % fact_B_master_R2_positive)
    print("FACT C  a_4 cross-DENSITY sign (pre one-loop): %s  (value %g)"
          % (fact_C_density_sign, a4_density_pre_oneloop))
    print("FACT D  c_loop frozen POSITIVE wall, load-bearing (F6): %s (%s)"
          % (fact_D_cloop_positive, c_loop_val))
    print("FACT E  c_a4 negativity is SOLELY from ONE_LOOP_SIGN=-1/2: %s"
          % fact_E_sign_from_oneloop)
    print("-" * 72)
    print("convention pins CURVATURE sign (density positive, NOT free): %s"
          % convention_pins_curvature_sign)
    print("c_a4 sign rides on one-loop prefactor ONLY: %s"
          % sign_rides_on_oneloop_only)
    print("as-run c_loop & c_a4 share ONE one-loop convention: %s  <-- mismatch"
          % as_run_shares_one_loop_convention)
    print("-" * 72)
    print("RESOLUTION:", resolution)
    print("SINGLE OWNER-RULE ITEM:")
    print("  ", result["derived"]["the_single_owner_rule_item"])
    print("=" * 72)
    print("artifact:", out_path)
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
