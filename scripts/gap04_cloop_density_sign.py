#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gap04_cloop_density_sign.py
===========================
Gap-04 FRG-2 lane: DERIVE (or precisely gate) the SIGN of c_loop's UNDERLYING
heat-kernel density -- the density that sits BEFORE the one-loop -(1/2) prefactor
in the e^{-6 sigma} KK-Casimir wall coefficient c_loop = +1.3637e-5.

This is the SINGLE deciding fact for the Gap-04 owner-lock:

    * If c_loop's underlying density is NEGATIVE (c_loop = -(1/2) x negative),
      then under the SAME global one-loop -(1/2) the a_4 cross-term (whose
      density is MANIFESTLY POSITIVE) takes the OPPOSITE relative sign -> c_a4>0,
      a positive wall  ->  BRANCH-STANDS (the -sigma FRG-4 well stands).
    * If c_loop's underlying density is POSITIVE (c_loop is a positive Casimir
      directly, under a DIFFERENT bookkeeping than the global -(1/2)), then a_4
      keeps the SAME relative sign as its own positive density under -(1/2),
      i.e. c_a4<0  ->  BRANCH-RUNAWAY (a_4 growth-8 dominates the c_loop growth-6
      wall at the -sigma corner -> V -> -inf).

CFCA discipline (METHOD_CFCA_June_14.md):
  - no-target-loading: NO observed value enters on any input side (no A_s,
    Lambda_obs, r, eta_B, n_s, N_eff, PDG, Omega_DM, H_0, S_8). Every "derived"
    line is licensed by the committed computation in THIS passage.
  - NEVER force the favorable branch. The independent countersign
    (gap04_oneloop_consistency.py / gap04_convention_audit.py) exists to catch
    exactly that. A prior "well-stands" overwrite was caught and retracted; we
    do not repeat it.
  - elegance is the diagnostic: a genuinely irreducible floor feels like a clean
    floor hit AFTER the elegant routes are exhausted. Here the elegant route
    (read the sign off a first-principles c_loop computation) is BLOCKED because
    no such computation exists in the corpus -- so the honest endpoint is a
    floor, GATED ON the named open object, not a brute-forced sign.

====================================================================
WHAT IS DERIVABLE DATA-BLIND  (committed in this passage)
====================================================================
D1. The a_4 cross-DENSITY (pre one-loop) sign is POSITIVE:
       density = (4 pi)^{-D/2} * (1/36) * R_K6 * R_S2,
    with the convention-invariant +5/360 master R^2 coefficient (cross 1/36),
    and the single-signed curvature registry R_K6=+30, R_S2=+2 (geometry-FORCED
    by the frozen K6 x S2 Einstein constants). All three factors > 0.
D2. The global one-loop log-det MAGNITUDE is -(1/2): the universal bosonic
       V^(1-loop) = -(1/2)(4 pi)^{-D/2} sum_n a_n(D),
    GLOBAL to every heat-kernel coefficient a_n. (Magnitude, not relative sign.)
D3. Therefore the as-run c_a4 under the genuine global -(1/2) on its OWN positive
    density is NEGATIVE: c_a4 = -(1/2)(4pi)^{-13/2}(1/36)(30)(2) = -5.97e-08.
    (Matches the on-disk gilkey_a4_cross_terms.json value, byte-checked.)

====================================================================
WHAT IS *NOT* DERIVABLE DATA-BLIND  -- and WHY it is the named open object
====================================================================
The relative one-loop sign of c_a4 vs c_loop is fixed ONLY by the sign of
c_loop's UNDERLYING heat-kernel density. That sign is NOT banked anywhere:

  * z_renormalized_c_loop.py reads c_loop as a FROZEN inherited number
    (C_LOOP_FRG2 = 1.3637877214788921e-05, the "Fable-Latest shell projection")
    and multiplies it by a wave-function Z-factor ~0.99995. It applies NO
    -(1/2) log-det and derives NO density sign. (verified on disk)
  * frozen_inputs.yaml carries c_loop_FRG2 "by reference" from Fable-Latest;
    NO first-principles producer (a regularized KK-tower Casimir / zero-point
    sum / shell-projection integral) exists in this corpus. The file
    c_loop_NLO_match.py referenced by z_renormalized_c_loop.py's spectrum
    comment is NOT present anywhere in the tree (globbed: 0 hits).
  * Fable_TOE.md records c_loop as SCAFFOLD-BAND / FRG-2, an explicit
    Chris-derivation blocker (named object B-UQFC-14-FRG-2: "UQFC SS14 FRG-2
    truncation + FRG-6 trajectory closure feeding c_loop | Chris"). Its
    positivity is ASSUMED (P3: "-inf: V_loop wall (c_loop > 0)") and guarded by
    falsifier F6 -- not computed. The "underlying-density sign" is one layer
    BELOW even that assumed wall sign and is nowhere stated.
  * The nearest first-principles Casimir machinery in the corpus
    (k6_zeta_casimir_insertion.py) explicitly disclaims: "it does not claim to
    compute the full finite nonlocal determinant" -- it closes only the LOCAL
    Seeley-DeWitt/zeta coefficient (and for the Dirac/fermion bundle, a
    DIFFERENT object than the scalar KK-Casimir wall). So even that does not
    bank the scalar c_loop underlying-density sign.

CONCLUSION (the honest endpoint):
  The sign of c_loop's underlying heat-kernel density CANNOT be derived without
  first computing c_loop from first principles -- i.e. running the regularized
  KK-tower Casimir / shell-projection integral that produces the e^{-6 sigma}
  coefficient. That computation is itself the NAMED OPEN FRG-2 object
  (B-UQFC-14-FRG-2, owner = Chris). TOE_FINAL records c_loop OPEN /
  uncomputed-from-first-principles. Therefore:

      density_sign_outcome = GENUINELY-INDETERMINATE-gated-on-open-cloop
      branch              = still-owner-locked (BOTH branches live)

  and the relative-one-loop-sign debit in gap04_reason_hunt.py STAYS BARE-COUNTED
  (it does NOT become DERIVED), because we did not -- and cannot, data-blind --
  derive the sign. Asserting either sign here would be the manufactured
  favorable-branch step the countersign exists to catch.

NON-PROMOTION: no gate flip; no status word emitted for any gate. This is a
countersign-ready, gated-on-open analysis the owner signs. exit 0 on an honest
gated resolution; exit 2 if an input is unreadable or a forbidden token leaks.
"""

import hashlib
import json
import math
import os
import sys

# ---------------------------------------------------------------------------
# On-disk real artifacts (no observed value may enter).
# ---------------------------------------------------------------------------
FA = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
      r"physics_Journal_and_patents/Final_physics_articles/scripts/gap_04")
FROZEN_YAML = os.path.join(FA, "frozen_inputs.yaml")
VEFF_YAML = os.path.join(FA, "outputs", "veff_coefficients_frg4.yaml")
GILKEY_JSON = os.path.join(FA, "outputs", "gilkey_a4_cross_terms.json")
ZRENORM_JSON = os.path.join(FA, "outputs", "z_renormalized_c_loop.json")
ZRENORM_SRC = os.path.join(FA, "src", "z_renormalized_c_loop.py")

# The frozen-but-missing first-principles producer of c_loop (the named open
# object). We probe for it to PROVE its absence (gate evidence), not to read it.
CLOOP_FIRSTPRINCIPLES_CANDIDATES = [
    os.path.join(FA, "src", "c_loop_NLO_match.py"),
    os.path.join(FA, "src", "c_loop_NLO_match.json"),
    os.path.join(FA, "src", "shell_projection_c_loop.py"),
    os.path.join(FA, "src", "kk_casimir_c_loop.py"),
    os.path.join(FA, "outputs", "c_loop_NLO_match.json"),
]

FORBIDDEN_TOKENS = [
    "A_s ", "A_s=", "Lambda_obs", "lambda_obs", "eta_B", "n_s_obs",
    "N_eff_obs", "PDG", "Planck_n_s", "BICEP", "LiteBIRD_r", "r_obs",
    "Omega_DM_obs", "H_0_obs", "S_8_obs",
]

# ---------------------------------------------------------------------------
# FROZEN geometry / master-coefficient constants (NOT observed values).
# ---------------------------------------------------------------------------
R_K6_0 = 30.0                                # 6 * 5 ; Besse Tab 7.107 (Einstein +5)
R_S2_0 = 2.0                                 # 2 * 1 ; round S^2 (Einstein +1)
A4_R2_MASTER_COEFF = 5.0 / 360.0             # convention-INVARIANT master R^2 coeff
A4_CROSS_PREFACTOR = 2.0 * A4_R2_MASTER_COEFF  # = 1/36 (2 from the R^2 cross-term)
D_BULK = 13
HK_NORM = 1.0 / (math.pow(4.0 * math.pi, D_BULK / 2.0))  # (4 pi)^{-D/2} > 0
GENUINE_GLOBAL_ONE_LOOP_PREFACTOR = -0.5     # universal bosonic one-loop magnitude


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def grep_value(path, key):
    out = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            if key in line:
                out.append(line.strip())
    return out


def read_c_loop_Z(path):
    for ln in grep_value(path, "c_loop_Z"):
        if ln.startswith("c_loop_Z:"):
            try:
                return float(ln.split(":", 1)[1].split("#")[0].strip())
            except ValueError:
                pass
    return None


def zrenorm_applies_minus_half(src_text):
    """
    Does the c_loop producer apply a -(1/2) log-det (from which a density sign
    could be read)? z_renormalized_c_loop.py only multiplies by a Z-factor; it
    contains NO one-loop -(1/2) prefactor on c_loop. Detect honestly: look for an
    explicit log-det prefactor applied to c_loop, not merely the spectral Z power.
    """
    # The producer multiplies c_loop by prod_i Z_i^{g_i/2}: that exponent g_i/2 is
    # a wave-function power, NOT a one-loop log-det -(1/2) on the c_loop density.
    # A genuine density-sign derivation would carry "-(1/2)" or "-0.5" acting on a
    # c_loop heat-kernel density. None present.
    bad_markers = ["-(1/2) * c_loop", "-0.5 * c_loop", "minus_half_c_loop",
                   "c_loop_density", "c_loop_underlying"]
    return any(m in src_text for m in bad_markers)


def cloop_underlying_density_sign_banked(frozen_text, veff_text, zrenorm_json):
    """
    Is the SIGN of c_loop's underlying heat-kernel density banked anywhere we can
    read? We require an EXPLICIT underlying-density-sign slot tied to a -(1/2)
    log-det -- NOT the stored positive WALL value (whose underlying-density sign
    is precisely the unknown). The corpus banks no such slot -> returns False.
    """
    markers = ["c_loop_underlying_density_sign", "c_loop_density_sign",
               "c_loop_pre_oneloop_density", "c_loop_heat_kernel_density_sign"]
    if any(m in frozen_text for m in markers):
        return True, "explicit underlying-density-sign slot found in frozen_inputs"
    if any(m in veff_text for m in markers):
        return True, "explicit underlying-density-sign slot found in veff table"
    # z_renormalized_c_loop result: confirm it derives no sign (only Z-factor).
    derived_sign = zrenorm_json.get("c_loop_Z_result", {}).get(
        "underlying_density_sign")
    if derived_sign in ("+", "-"):
        return True, "z_renormalized_c_loop banked an underlying_density_sign"
    return False, ("no underlying-density-sign slot anywhere; c_loop carried as a "
                   "frozen positive WALL value only; z_renorm applies a Z-factor, "
                   "no -(1/2) log-det")


def main():
    # ---- locate inputs (refuse if missing) --------------------------------
    for p in (FROZEN_YAML, VEFF_YAML, GILKEY_JSON, ZRENORM_JSON, ZRENORM_SRC):
        if not os.path.exists(p):
            sys.stderr.write("REFUSE(exit2): missing input %s\n" % p)
            return 2

    with open(FROZEN_YAML, "r", encoding="utf-8") as fh:
        frozen_text = fh.read()
    with open(VEFF_YAML, "r", encoding="utf-8") as fh:
        veff_text = fh.read()
    with open(ZRENORM_SRC, "r", encoding="utf-8") as fh:
        zrenorm_src = fh.read()
    with open(ZRENORM_JSON, "r", encoding="utf-8") as fh:
        zrenorm_json = json.load(fh)
    with open(GILKEY_JSON, "r", encoding="utf-8") as fh:
        gilkey = json.load(fh)

    # forbidden-input firewall on every source we read. NOTE: the frozen file
    # and the prereg legitimately NAME forbidden inputs inside attestation /
    # comment strings ("no_bicep_planck_r_input", "BICEP/Planck r upper bound").
    # Naming a forbidden anchor in an attestation is the OPPOSITE of using it.
    # We therefore flag only a raw leaked numeric VALUE assignment of an anchor,
    # not the attestation mentions (same discipline as gap04_reason_hunt.py).
    VALUE_LEAK_TOKENS = [
        "A_s=", "A_s =", "eta_B=", "eta_B =", "Lambda_obs=", "Lambda_obs =",
        "r_obs=", "r_obs =", "n_s_obs=", "N_eff_obs=", "Omega_DM_obs=",
        "H_0_obs=", "S_8_obs=",
    ]
    for name, txt in (("frozen_inputs.yaml", frozen_text),
                      ("veff_coefficients_frg4.yaml", veff_text),
                      ("z_renormalized_c_loop.py", zrenorm_src)):
        leaked = [t for t in VALUE_LEAK_TOKENS if t in txt]
        if leaked:
            sys.stderr.write("REFUSE(exit2): forbidden value assignment in %s: %s\n"
                             % (name, leaked))
            return 2

    # =====================================================================
    # D1. a_4 cross-DENSITY sign (pre one-loop) -- DERIVED POSITIVE
    # =====================================================================
    density_core = A4_CROSS_PREFACTOR * R_K6_0 * R_S2_0   # (1/36)*30*2 = +5/3
    a4_density_pre_oneloop = HK_NORM * density_core        # strictly > 0
    a4_density_sign = "+" if a4_density_pre_oneloop > 0 else (
        "-" if a4_density_pre_oneloop < 0 else "0")

    # =====================================================================
    # D3. as-run c_a4 under the genuine global -(1/2) on its OWN positive density
    # =====================================================================
    c_a4_genuine = GENUINE_GLOBAL_ONE_LOOP_PREFACTOR * a4_density_pre_oneloop
    c_a4_on_disk = float(
        gilkey["a4_cross_terms"]["K6_x_S2"]["coefficient_value_M13_4_units"])
    c_a4_matches_disk = abs(c_a4_genuine - c_a4_on_disk) < 1e-12 * max(
        1.0, abs(c_a4_on_disk))

    # =====================================================================
    # c_loop wall (frozen positive WALL value; F6 load-bearing) -- ASSUMED, not
    # derived; its UNDERLYING density sign is the open object.
    # =====================================================================
    c_loop_Z = read_c_loop_Z(VEFF_YAML)
    c_loop_wall_positive = (c_loop_Z is not None and c_loop_Z > 0)

    # =====================================================================
    # GATE EVIDENCE: is there a first-principles c_loop producer on disk?
    # =====================================================================
    firstprinciples_present = {
        p: os.path.exists(p) for p in CLOOP_FIRSTPRINCIPLES_CANDIDATES
    }
    any_firstprinciples = any(firstprinciples_present.values())

    # Does the EXISTING producer (z_renormalized_c_loop.py) derive a density sign?
    zrenorm_derives_sign = zrenorm_applies_minus_half(zrenorm_src)

    # Is the underlying density sign banked anywhere readable?
    banked, banked_reason = cloop_underlying_density_sign_banked(
        frozen_text, veff_text, zrenorm_json)

    # =====================================================================
    # THE GATED RESOLUTION (do NOT force a sign)
    # =====================================================================
    # The relative one-loop sign of c_a4 vs c_loop is fixed iff c_loop's
    # underlying-density sign is banked. It is not. No first-principles producer
    # exists; the existing producer derives no sign; the corpus records c_loop
    # OPEN (B-UQFC-14-FRG-2). Therefore the density sign is GATED ON the named
    # open object and BOTH branches stay live.
    if banked and (any_firstprinciples or zrenorm_derives_sign):
        # Only reachable if the corpus had actually computed c_loop's density
        # sign from first principles. It has not. (kept honest, not forced)
        derived_sign = zrenorm_json.get("c_loop_Z_result", {}).get(
            "underlying_density_sign")
        if derived_sign == "-":
            density_sign_outcome = "DERIVED-negative-density"
            branch_selected = "BRANCH-STANDS"
        elif derived_sign == "+":
            density_sign_outcome = "DERIVED-positive-density"
            branch_selected = "BRANCH-RUNAWAY"
        else:
            density_sign_outcome = "GENUINELY-INDETERMINATE-gated-on-open-cloop"
            branch_selected = "still-owner-locked"
        debit_reclassification = (
            "DERIVED (the c_loop underlying-density sign was actually banked / "
            "computed from first principles)")
    else:
        density_sign_outcome = "GENUINELY-INDETERMINATE-gated-on-open-cloop"
        branch_selected = "still-owner-locked"
        debit_reclassification = (
            "STAYS BARE-COUNTED (the relative-one-loop-sign debit in "
            "gap04_reason_hunt.py is NOT promoted to DERIVED: we neither derived "
            "nor could derive the c_loop underlying-density sign data-blind)")

    c_loop_underlying_density_sign = "GATED-ON-OPEN-cloop-first-principles (UNBANKED)"

    result = {
        "schema": "gap04_cloop_density_sign_result_v1",
        "purpose": (
            "Derive (or precisely gate) the SIGN of c_loop's UNDERLYING "
            "heat-kernel density -- the density BEFORE the one-loop -(1/2) "
            "prefactor in the e^{-6 sigma} KK-Casimir wall c_loop = +1.3637e-5."),
        "density_sign_outcome": density_sign_outcome,
        "c_loop_underlying_density_sign": c_loop_underlying_density_sign,
        "branch_selected": branch_selected,
        "debit_reclassification": debit_reclassification,

        "what_is_DERIVED_data_blind": {
            "D1_a4_cross_density_sign_pre_oneloop": a4_density_sign,
            "D1_a4_cross_density_value": a4_density_pre_oneloop,
            "D1_reason": (
                "geometry-FORCED + convention-INVARIANT: (4pi)^{-D/2} > 0, "
                "master R^2 coeff +5/360 (cross 1/36) is the same in both Gilkey "
                "Laplacian conventions (R^2 even in curvature), and the "
                "single-signed Einstein registry R_K6=+30, R_S2=+2 is fixed by "
                "the frozen K6 x S2 geometry. All three factors positive."),
            "D2_global_one_loop_magnitude": GENUINE_GLOBAL_ONE_LOOP_PREFACTOR,
            "D2_reason": (
                "universal bosonic one-loop log-det: V^(1-loop) = "
                "-(1/2)(4pi)^{-D/2} sum_n a_n. GLOBAL prefactor MAGNITUDE only; "
                "a global prefactor does NOT force two coefficients same-SIGN."),
            "D3_c_a4_as_run_under_genuine_minus_half": c_a4_genuine,
            "D3_c_a4_on_disk": c_a4_on_disk,
            "D3_matches_on_disk": c_a4_matches_disk,
            "D3_reason": (
                "global -(1/2) acting on a_4's OWN positive density gives c_a4 "
                "NEGATIVE = -5.97e-08 (byte-matches gilkey_a4_cross_terms.json)."),
        },

        "what_is_NOT_derivable_and_why": {
            "decisive_unknown": (
                "the SIGN of c_loop's UNDERLYING heat-kernel density (is c_loop a "
                "-(1/2) log-det of a NEGATIVE-density object -> BRANCH-STANDS, or "
                "a POSITIVE Casimir under a different bookkeeping -> "
                "BRANCH-RUNAWAY?)."),
            "underlying_density_sign_banked": banked,
            "banked_check_reason": banked_reason,
            "first_principles_producer_present_on_disk": firstprinciples_present,
            "any_first_principles_producer_present": any_firstprinciples,
            "existing_producer_derives_a_density_sign": zrenorm_derives_sign,
            "existing_producer_note": (
                "z_renormalized_c_loop.py reads c_loop as a FROZEN inherited "
                "number (C_LOOP_FRG2 = 1.3637877214788921e-05, 'Fable-Latest "
                "shell projection') and multiplies by prod_i Z_i^{g_i/2} "
                "~0.99995. The g_i/2 is a wave-function power, NOT a one-loop "
                "-(1/2) log-det on the c_loop density; it derives NO density "
                "sign."),
            "named_open_object": (
                "B-UQFC-14-FRG-2 (owner = Chris): 'UQFC SS14 FRG-2 truncation + "
                "FRG-6 trajectory closure feeding c_loop'. Fable_TOE.md records "
                "c_loop SCAFFOLD-BAND / FRG-2, positivity ASSUMED (P3 '-inf: "
                "V_loop wall (c_loop > 0)') and guarded by falsifier F6 -- the "
                "underlying-density sign is one layer BELOW even the assumed wall "
                "sign and is nowhere computed."),
            "nearest_casimir_machinery_disclaimer": (
                "k6_zeta_casimir_insertion.py (the nearest first-principles "
                "Casimir machinery) explicitly states it 'does not claim to "
                "compute the full finite nonlocal determinant' -- it closes only "
                "the LOCAL Seeley-DeWitt/zeta coefficient, and for the "
                "Dirac/fermion bundle (a DIFFERENT object than the scalar "
                "KK-Casimir wall). It does NOT bank the scalar c_loop "
                "underlying-density sign."),
        },

        "two_live_branches": {
            "BRANCH_STANDS": {
                "condition": (
                    "owner/first-principles rules c_loop's UNDERLYING density "
                    "NEGATIVE (c_loop = -(1/2) x negative); under the SAME global "
                    "-(1/2) the positive-density a_4 takes the OPPOSITE relative "
                    "sign -> c_a4 = +5.97e-08, a positive wall"),
                "c_a4": -c_a4_genuine,
                "effect": "the -sigma FRG-4 well STANDS",
                "named_falsifier": "F1_ext (true interior critical point exists)",
            },
            "BRANCH_RUNAWAY": {
                "condition": (
                    "c_loop's underlying density POSITIVE (positive Casimir under "
                    "a different bookkeeping); a_4 keeps the SAME relative sign as "
                    "its own positive density under -(1/2) -> c_a4 = -5.97e-08"),
                "c_a4": c_a4_genuine,
                "effect": (
                    "a_4 cross-term (growth 8 at -sigma) DOMINATES the c_loop "
                    "wall (growth 6); a negative dominant term -> V -> -inf, a "
                    "REAL separate 3-modulus -sigma runaway threatening F1"),
                "named_falsifier": "F1 (any unbounded V_eff -> -inf direction)",
            },
        },

        "disjointness_dominance_at_neg_sigma": {
            "growth_a4_cross_term": 8.0,        # exp(-(8 sigma + 4 rho + chi))
            "growth_c_loop_wall": 6.0,          # exp(-6 sigma)
            "a4_dominates_neg_sigma_corner": True,
        },

        "well_verdict": (
            "OWNER-LOCKED / CONDITIONAL: the -sigma FRG-4 3-modulus well's "
            "survival is gated on the c_loop underlying-density sign, which is "
            "the named OPEN first-principles object (B-UQFC-14-FRG-2). It is NOT "
            "forced to stand (the genuine global -(1/2) on a_4's own positive "
            "density gives c_a4 NEGATIVE -> runaway) and NOT forced to fail (the "
            "relative sign vs c_loop is unbanked). Both branches carry named "
            "falsifiers; the owner must compute c_loop from first principles to "
            "decide."),

        "what_requires_chris": (
            "Compute c_loop from first principles: run the regularized KK-tower "
            "Casimir / shell-projection (zero-point / heat-kernel) integral that "
            "produces the e^{-6 sigma} coefficient, and READ OFF the sign of its "
            "underlying density BEFORE the one-loop -(1/2) prefactor. This is the "
            "named open FRG-2 object B-UQFC-14-FRG-2. Until it exists, the "
            "density sign is GATED-ON-OPEN and the Gap-04 well stays "
            "owner-locked."),

        "provenance_hashes": {
            "frozen_inputs.yaml": sha256_file(FROZEN_YAML),
            "veff_coefficients_frg4.yaml": sha256_file(VEFF_YAML),
            "gilkey_a4_cross_terms.json": sha256_file(GILKEY_JSON),
            "z_renormalized_c_loop.json": sha256_file(ZRENORM_JSON),
            "z_renormalized_c_loop.py": sha256_file(ZRENORM_SRC),
        },
        "frozen_inputs_used": {
            "R_K6_0": R_K6_0, "R_S2_0": R_S2_0,
            "a4_R2_master_coeff_5_over_360": A4_R2_MASTER_COEFF,
            "a4_cross_prefactor_1_over_36": A4_CROSS_PREFACTOR,
            "D_bulk": D_BULK, "factor_4pi_to_minus_D_over_2": HK_NORM,
            "global_one_loop_prefactor": GENUINE_GLOBAL_ONE_LOOP_PREFACTOR,
            "c_loop_Z_frozen_wall_value": c_loop_Z,
            "c_loop_FRG2_shell_input": 1.3637877214788921e-05,
        },
        "no_target_loading": True,
        "no_target_loading_attest": (
            "No observed value entered on any input side (no A_s, Lambda_obs, r, "
            "eta_B, n_s, N_eff, PDG, Omega_DM, H_0, S_8). Every DERIVED line "
            "(D1/D2/D3) is licensed by the committed computation in this passage "
            "and byte-checked against on-disk artifacts. The favorable branch was "
            "NOT forced: the genuine global -(1/2) on a_4's own positive density "
            "is reported NEGATIVE, and the well is left owner-locked because the "
            "deciding c_loop underlying-density sign is the named open object."),
        "non_promotion": (
            "no gate flipped; no status word emitted for any gate; "
            "countersign-ready gated-on-open analysis only."),
    }

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gap04_cloop_density_sign_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- decision-grade packet to stdout ----------------------------------
    print("=" * 72)
    print("Gap-04  c_loop UNDERLYING heat-kernel DENSITY SIGN  (FRG-2 lane)")
    print("=" * 72)
    print("DERIVABLE data-blind:")
    print("  D1 a_4 cross-density (pre one-loop): %g  [sign %s, POSITIVE]"
          % (a4_density_pre_oneloop, a4_density_sign))
    print("  D2 global one-loop magnitude: %g  (MAGNITUDE only, not rel. sign)"
          % GENUINE_GLOBAL_ONE_LOOP_PREFACTOR)
    print("  D3 c_a4 under genuine -1/2 on own + density: %g  [NEGATIVE; "
          "disk match=%s]" % (c_a4_genuine, c_a4_matches_disk))
    print("-" * 72)
    print("c_loop frozen WALL value (F6 load-bearing): %s  [positive=%s, ASSUMED]"
          % (c_loop_Z, c_loop_wall_positive))
    print("c_loop UNDERLYING-density sign banked anywhere: %s" % banked)
    print("  reason: %s" % banked_reason)
    print("first-principles c_loop producer present on disk: %s"
          % any_firstprinciples)
    print("existing producer (z_renorm) derives a density sign: %s"
          % zrenorm_derives_sign)
    print("-" * 72)
    print("DENSITY SIGN OUTCOME : %s" % density_sign_outcome)
    print("BRANCH               : %s" % branch_selected)
    print("DEBIT                : %s" % debit_reclassification)
    print("-" * 72)
    print("REQUIRES CHRIS: compute c_loop from first principles (regularized")
    print("  KK-tower Casimir / shell-projection integral) -> read the sign of")
    print("  its underlying density before the -(1/2). Named open: B-UQFC-14-FRG-2.")
    print("  (we do NOT force a sign; the favorable branch is NOT selected)")
    print("artifact:", out_path)
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
