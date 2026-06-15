"""
gap04_chamber_exclusion.py
==========================
GAP-04 CHAMBER-EXCLUSION / KINEMATIC-FLOOR TEST  (target-blind)

QUESTION
--------
The FRG-4 perturbative potential leans toward a sigma -> -infinity runaway
(V -> -inf as the K6 internal volume SHRINKS). Is that direction even an
ADMISSIBLE deformation in the SELECTED configuration space, or is it
kinematically excluded by a constraint already BANKED for OTHER reasons?

A kinematic floor on -sigma counts ONLY if a PRIOR, independently-banked
theorem forces it, target-blind. This script checks each candidate prior
constraint against the SAME breathing-modulus runaway direction the FRG-4
escape audit already exhibited on disk
(global_escape_audit_unbounded.json: any_runaway_to_negative_modulus_corner
= true, F1_no_runaway_V_to_minus_inf_PASS = false).

HARD GUARD honored: we do NOT delete the runaway because it is bad. We ask,
per banked constraint, whether it ALREADY forbids unbounded shrinking, with
the independent reason it was banked stated. If none does, the honest answer
is NO-KINEMATIC-FLOOR.

GEOMETRY / COORDINATE FACTS (from Fable_GUT_merged.md, frozen registry)
----------------------------------------------------------------------
  * Breathing/shape coordinates of the escape audit:
        sigma = overall log-radius of K6  (walls e^{-4 sigma}, e^{-6 sigma},
                                           e^{-2 sigma}, cross e^{-8 sigma...})
        rho   = log-radius of S^2
        chi   = log-radius of S^1_Y
    -sigma -> -inf  <=>  Vol(K6) -> 0  (internal volume shrinks).

  * Weyl-rigid (W-rig) chamber:  u = (u1,u2,u3) in [1/2, 3/2]^3.
    These u_i are the SHAPE / SQUASHING ratios of the three Cartan 2-planes
    of K6 = SU(3)/T^2 (metric g = u1<,>_m1 + u2<,>_m2 + u3<,>_m3).
    The OVERALL radius is R6 = R0 * u_chamber, R0 = (2 pi M_U)^-1 fixed by the
    threshold-unification target M_U ~ 1e16 GeV (Appendix G), NOT by W-rig.

THE TEST (per candidate prior banked constraint)
------------------------------------------------
  (i)   W-rig projector            -> bounds SHAPE, not overall volume?
  (ii)  flux quantization          -> a quantized 2-form flux through K6/S^2
                                      that cannot be diluted below a quantum?
  (iii) three-family APS index +3  -> does shrinking change/destroy the index
                                      (jump families)?  index is topological?
  (iv)  frozen-anchor preservation -> does sigma -> -inf violate
                                      M_Pl / alpha_i(M_Z) / y_t / |V_us|?
  (v)   selector map               -> does it independently floor -sigma?

Each returns FORCES_FLOOR (bool) + the INDEPENDENT banking reason. A floor is
admissible ONLY if it is PRIOR (banked for an independent reason), not a
constraint reverse-engineered to kill the runaway.
"""
from __future__ import annotations

import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# --- on-disk escape-audit anchor (the runaway we are adjudicating) ----------
ESCAPE_AUDIT = os.path.abspath(os.path.join(
    HERE, os.pardir, os.pardir, os.pardir,
    "Final_physics_articles", "scripts", "gap_04", "outputs",
    "global_escape_audit_unbounded.json",
))


# ---------------------------------------------------------------------------
# Coordinate fact: W-rig bounds SHAPE u_i, the runaway is in overall sigma.
# We make the orthogonality explicit and computable.
# ---------------------------------------------------------------------------
def wrig_bounds_overall_radius() -> dict:
    """
    The W-rig chamber is u in [1/2, 3/2]^3. Show that fixing all SHAPE ratios
    to the chamber center u=(1,1,1) -- i.e. sitting maximally INSIDE the W-rig
    box -- leaves the OVERALL radius (sigma) entirely unconstrained: the
    runaway is a pure rescaling at fixed shape, on which the W-rig box is flat.

    Shape ratios r_ij = u_i/u_j are invariant under an overall rescale
    u_i -> lambda u_i. The escape audit's sigma is exactly that overall
    log-rescale lambda = e^{-sigma-ish}. So the W-rig admissibility predicate
    (a bound on u_i in [1/2,3/2]) does not see sigma at all once we are at the
    symmetric shape u1=u2=u3.
    """
    u_center = (1.0, 1.0, 1.0)
    in_box = all(0.5 <= ui <= 1.5 for ui in u_center)
    # Overall rescale by lambda keeps shape ratios fixed (=1); W-rig predicate
    # tests u_i magnitudes, but the physical overall size lives in R6 = R0*u,
    # and R0 is pinned by M_U (threshold), independent of the W-rig box.
    shape_ratios_at_center = (u_center[0] / u_center[1],
                              u_center[1] / u_center[2])
    return {
        "u_center_in_Wrig_box": in_box,
        "shape_ratios_center": shape_ratios_at_center,
        "Wrig_constrains": "shape/squash ratios u_i (3 Cartan 2-planes)",
        "Wrig_does_NOT_constrain": "overall breathing modulus sigma (Vol(K6))",
        "overall_radius_fixed_by": "threshold target M_U ~ 1e16 GeV (App. G), "
                                   "via R0=(2 pi M_U)^-1 -- NOT by W-rig",
        "runaway_direction_is": "overall rescale (fixed shape) = sigma axis, "
                                "orthogonal to the W-rig shape box",
    }


# ---------------------------------------------------------------------------
# (i) Weyl-rigidity projector
# ---------------------------------------------------------------------------
def check_weyl_rigidity() -> dict:
    geom = wrig_bounds_overall_radius()
    # Banking reason (independent): W-rig was banked to make K6 SHAPE a
    # convention-invariant, non-tuned datum feeding gauge recovery (C) and
    # thresholds (F); it freezes squashing, with center witness (1,1,1).
    # It is an admissibility RULE (oplus-layer), not a dynamical wall, and the
    # manuscript itself (F.9) forbids reading it as global stabilization.
    forces_floor = False  # bounds shape ratios, not overall volume/sigma
    return {
        "candidate": "(i) Weyl-rigidity projector",
        "what_it_freezes": "the 3 Cartan SHAPE moduli u_i of K6 into the box "
                           "[1/2,3/2]^3, center (1,1,1); a SQUASH bound",
        "independent_banking_reason": "make K6 shape a non-tuned, "
                                      "convention-invariant input to gauge "
                                      "recovery (C) and thresholds (F); "
                                      "banked BEFORE the FRG runaway existed",
        "acts_on_overall_volume_sigma": False,
        "forces_lower_bound_on_minus_sigma": forces_floor,
        "note": "F.9 binding distinction: W-rig is ADMISSIBILITY RESTRICTION "
                "(oplus rule), explicitly NOT global stabilization. The "
                "u_i>=1/2 floor is a floor on SHAPE, not on Vol(K6). The "
                "runaway is an overall rescale at fixed shape -> W-rig is flat "
                "along it.",
        "geometry": geom,
    }


# ---------------------------------------------------------------------------
# (ii) flux quantization / wrapped-cycle integers
# ---------------------------------------------------------------------------
def check_flux_quantization() -> dict:
    # Inventory of the theory's ACTUAL quantized/topological data:
    quantized_objects = {
        "Z6_charge_identification": "discrete charge rule (group centers); "
                                    "dimensionless, volume-independent",
        "Wilson_line_winding_n_H": "integer holonomy of K_gauge cycle giving "
                                   "the Higgs; a PHASE/winding, scale-blind",
        "Cartan_torus_tau=omega": "modular fixed point (order-3); a SHAPE/phase "
                                  "datum, not a volume",
        "spinC_family_index": "topological integer (see (iii))",
    }
    # Is there a 2-form gauge FLUX threaded through K6 or S^2 whose magnitude
    # n = (1/2pi) int_{S^2} F is fixed, so that shrinking Vol would force the
    # field strength up and bound the volume from below?  -> NOT in registry.
    flux_through_cycle_with_volume_scaling = False
    forces_floor = False
    return {
        "candidate": "(ii) flux quantization / wrapped-cycle integers",
        "quantized_objects_present": quantized_objects,
        "two_form_flux_through_K6_or_S2_setting_min_volume": (
            flux_through_cycle_with_volume_scaling),
        "independent_banking_reason": "the integers banked (Z6, n_H, tau=omega) "
                                      "were banked for CHARGE quantization, "
                                      "Higgs protection, and CP phase -- all "
                                      "scale-INVARIANT holonomy/phase data",
        "forces_lower_bound_on_minus_sigma": forces_floor,
        "note": "All quantized data here are holonomies / windings / discrete "
                "identifications -- topological phases that do NOT scale with "
                "Vol. There is NO quantized 2-form flux n=(1/2pi)int F whose "
                "fixed quantum forbids dilution below a minimum volume. So flux "
                "quantization sets no floor on -sigma. (Honest: had such a flux "
                "been banked, it WOULD floor volume; it is simply absent here.)",
    }


# ---------------------------------------------------------------------------
# (iii) three-family APS / spin-C index (+3 on K6)
# ---------------------------------------------------------------------------
def check_three_family_index() -> dict:
    # The index is ind(D) = int_M Ahat(M) ch(E) (+ APS eta on the fold).
    # This is a TOPOLOGICAL invariant: independent of the Riemannian metric
    # SCALE. Shrinking K6 (sigma -> -inf) is a smooth metric deformation that
    # leaves Ahat ch(E) (a characteristic-class integral) unchanged, and the
    # eta-invariant's parity contribution is a discrete fold datum, also not
    # changed by an overall rescale. So +3 PERSISTS under shrinking.
    index_is_topological_scale_invariant = True
    # KEY TARGET-BLIND CONSEQUENCE:
    #   Because the index does NOT jump as Vol -> 0, the shrinking corner does
    #   NOT destroy the 3 families. The corner therefore remains INDEX-ADMISSIBLE
    #   -- the index gives NO reason to exclude it. (A floor would require the
    #   index to CHANGE below some volume; it does not.)
    shrinking_changes_index = (not index_is_topological_scale_invariant)
    forces_floor = False
    # Manuscript corroboration (target-blind): "the index is robust against
    # continuous deformation ... within the declared search category"
    return {
        "candidate": "(iii) three-family APS/spin-C index (+3 on K6)",
        "index_value": -3,
        "abs_family_count": 3,
        "index_is_topological_scale_invariant": index_is_topological_scale_invariant,
        "shrinking_below_some_volume_changes_index": shrinking_changes_index,
        "independent_banking_reason": "banked to COUNT 3 families as a "
                                      "metric-independent topological integer "
                                      "(Borel-Weil-Bott / APS) -- its whole "
                                      "virtue is scale-invariance (no dial)",
        "forces_lower_bound_on_minus_sigma": forces_floor,
        "note": "The index's defining property -- topological invariance -- is "
                "exactly what makes it USELESS as a volume floor: it does NOT "
                "jump as Vol(K6) -> 0, so it never renders the shrinking corner "
                "index-inadmissible while preserving 3 families. The +3 is "
                "preserved ALL ALONG the runaway. No floor.",
    }


# ---------------------------------------------------------------------------
# (iv) frozen-anchor preservation (M_Pl, alpha_i(M_Z), y_t, |V_us|)
# ---------------------------------------------------------------------------
def check_anchor_preservation() -> dict:
    # The four anchors are the ONLY declared free inputs. Are any of them a
    # FUNCTION of sigma that breaks as sigma -> -inf?  From the GAP-04
    # irreducibles closure (Q2 positive exhibit): every acting structure on the
    # anchors is unit-blind / scale-invariant:
    #   M_Pl       : overall dimensionful units; 4D Planck mass is an INPUT
    #                (declared "ordinary", not emergent). M_Pl^2 ~ Vol(X) M_*^{11}
    #                relation, IF imposed, would tie M_Pl to volume -- but here
    #                M_Pl is a DECLARED ANCHOR, frozen-before-comparison, NOT
    #                solved from the running volume. So it does not, by itself,
    #                impose a kinematic floor target-blind (it would be
    #                target-loading to demand "Vol must give the observed M_Pl").
    #   alpha_i(MZ): IR boundary values of RG trajectories; group/threshold data.
    #   y_t, |V_us|: Yukawa NORMALIZATION + first-row magnitude; the geometry
    #                forces only PHASES/textures (holonomy, kappa-ladder),
    #                invariant under the overall volume.
    # None of the four is structurally a monotone function of sigma whose
    # definedness fails at sigma -> -inf. They are inputs, frozen, scale-blind.
    anchor_breaks_at_minus_inf = {
        "M_Pl":        False,   # declared input; tying Vol->M_Pl would be target-loading
        "alpha_i(M_Z)":False,   # IR boundary value; scale-invariant group data
        "y_t":         False,   # Yukawa normalization; geometry fixes phase only
        "|V_us|":      False,   # first-row magnitude; geometry fixes texture/phase
    }
    forces_floor = any(anchor_breaks_at_minus_inf.values())
    return {
        "candidate": "(iv) frozen-anchor preservation",
        "anchor_violated_by_sigma_to_minus_inf": anchor_breaks_at_minus_inf,
        "independent_banking_reason": "the 4 anchors are the declared "
                                      "frozen-before-comparison inputs; each "
                                      "acting structure on them is unit-blind / "
                                      "scale-invariant (Q2 positive exhibit)",
        "forces_lower_bound_on_minus_sigma": forces_floor,
        "note": "No anchor is a definedness-breaking function of sigma. M_Pl is "
                "a DECLARED input (not solved from Vol); demanding 'Vol must "
                "reproduce observed M_Pl' would be TARGET-LOADING (forbidden "
                "guard b), and even then would pin a value, not forbid the "
                "-inf corner kinematically. So anchor preservation does NOT "
                "force a target-blind kinematic floor.",
    }


# ---------------------------------------------------------------------------
# (v) selector map
# ---------------------------------------------------------------------------
def check_selector_map() -> dict:
    # The selector (App. B1) ELIMINATES off-chamber branches by INVOKING the
    # stabilization gate (Gate 6) and the W-rig admissibility rule. It is
    # DOWNSTREAM of (i)/(vi); it carries no INDEPENDENT volume floor of its own.
    # It cannot manufacture a kinematic floor the underlying constraints lack.
    forces_floor = False
    return {
        "candidate": "(v) selector map",
        "independent_banking_reason": "Occam selector banked to pick the unique "
                                      "gate-closing branch; it INHERITS its "
                                      "exclusions from Gate 6 / W-rig, adds no "
                                      "new volume constraint",
        "forces_lower_bound_on_minus_sigma": forces_floor,
        "note": "The selector eliminates off-W-rig-chamber branches by citing "
                "the stabilization gate -- it is parasitic on (i). It floors "
                "-sigma only if (i) does, and (i) does not. No independent floor.",
    }


def main() -> int:
    audit = None
    if os.path.exists(ESCAPE_AUDIT):
        with open(ESCAPE_AUDIT, "r", encoding="utf-8") as fp:
            a = json.load(fp)
        audit = {
            "any_runaway_to_negative_modulus_corner":
                a.get("any_runaway_to_negative_modulus_corner"),
            "F1_no_runaway_V_to_minus_inf_PASS":
                a.get("F1_no_runaway_V_to_minus_inf_PASS"),
            "any_runaway_to_decompactification_corner":
                a.get("any_runaway_to_decompactification_corner"),
            "V_at_(-3,-3,-3)_M13_4":
                a.get("V_at_diagonal_seeds", {}).get("V_at_(-3,-3,-3)_M13_4"),
        }

    checks = [
        check_weyl_rigidity(),
        check_flux_quantization(),
        check_three_family_index(),
        check_anchor_preservation(),
        check_selector_map(),
    ]
    any_prior_floor = any(c["forces_lower_bound_on_minus_sigma"] for c in checks)

    verdict = (
        "BANKED-THEOREM-EXCLUDES" if any_prior_floor
        else "NO-KINEMATIC-FLOOR-runaway-admissible"
    )

    result = {
        "schema_version": "0.1.0-gap04-chamber-exclusion",
        "question": "Is the sigma -> -inf (shrink-K6) runaway kinematically "
                    "excluded by a PRIOR banked constraint, target-blind?",
        "runaway_on_disk": audit,
        "candidate_constraints": checks,
        "any_prior_banked_constraint_forces_floor_on_minus_sigma": any_prior_floor,
        "verdict": verdict,
        "why": (
            "The runaway is the OVERALL breathing modulus sigma (Vol(K6)->0). "
            "Every prior banked constraint is either (a) a SHAPE/squash bound "
            "(W-rig u_i in [1/2,3/2]^3) flat along the overall rescale, (b) a "
            "SCALE-INVARIANT topological datum (Z6, Wilson winding, tau=omega, "
            "the +3 index -- whose very virtue is metric-independence, so it "
            "never jumps as Vol->0), or (c) a DECLARED frozen anchor that is "
            "not a definedness-breaking function of sigma. NONE floors -sigma. "
            "The genuine wall against V->-inf is the relative one-loop sign "
            "sign[zeta_{Delta_K6}(-1/2)] (open object B-UQFC-14-FRG-2), a "
            "DYNAMICAL/spectral fact -- NOT a kinematic exclusion. Excluding "
            "the runaway by fiat would be the forbidden 'delete the bad "
            "direction' move (guard f)."
        ),
        "what_requires_owner": (
            "The sign that makes the well STAND vs RUN -- "
            "sign[zeta_{Delta_K6}(-1/2)], B-UQFC-14-FRG-2 -- is owner-locked "
            "(Chris). It is a deferred spectral-zeta computation, not a banked "
            "kinematic theorem."
        ),
    }

    out = os.path.join(HERE, "outputs")
    os.makedirs(out, exist_ok=True)
    out_path = os.path.join(out, "gap04_chamber_exclusion_result.json")
    with open(out_path, "w", encoding="utf-8") as fp:
        json.dump(result, fp, indent=2, sort_keys=True)

    print(f"WROTE {out_path}")
    print(f"VERDICT: {verdict}")
    print(f"any prior banked floor on -sigma: {any_prior_floor}")
    for c in checks:
        print(f"  - {c['candidate']}: "
              f"forces_floor={c['forces_lower_bound_on_minus_sigma']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
