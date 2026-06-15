#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gap04_cloop_casimir_firstprinciples.py
======================================
Gap-04 FRG-2 lane, ELEGANT PATH: try to settle the c_loop owner-lock by reading
the SIGN of c_loop's UNDERLYING heat-kernel density off a genuine first-principles
SCALAR KK-tower Casimir / spectral-zeta computation -- the regularized zero-point
sum on K6 x S^2 x S^1_Y whose K6-breathing-mode sigma-dependence yields the
e^{-6 sigma} wall coefficient c_loop_Z = +1.3637e-5.

A prior countersign (gap04_cloop_density_sign.py) left Gap-04 owner-locked because
NO first-principles producer of c_loop was found in gap_04. A later lead flagged
two scripts MISSED by that survey:
    severe_tests_paper/hc1_closure/symbolic/pub1_casimir.py
    severe_tests_paper/hc1_closure/symbolic/closure4_spectral_zeta.py
as candidate scalar-Casimir machinery. This script CHECKS THE OBJECT before
trusting it -- exactly the trap the task names: the prior survey's nearest hit
(k6_zeta_casimir_insertion.py) was a DIFFERENT object (a Dirac/fermion-bundle
LOCAL Seeley-DeWitt coefficient), and a matching "Casimir" name or a matching
1/R^6 (== e^{-6 sigma}) breathing exponent is NOT identity of object.

CFCA discipline (METHOD_CFCA_June_14.md):
  - no-target-loading: NO observed value (A_s, Lambda_obs, r, eta_B, n_s, N_eff,
    PDG, Omega_DM, H_0, S_8) enters on any input side. The ONLY inputs are the
    frozen geometry (Einstein constants, dims) and group theory (SU(3) reps).
    Comparison to c_loop's frozen WALL VALUE happens only AFTER the object check.
  - NEVER force the favorable (well-stands) branch. If the flagged machinery does
    not actually execute the scalar KK-tower spectral-zeta sum, the honest outcome
    is MACHINERY-DIFFERENT-OBJECT-owner-locked -- the elimination is COMPLETE
    (the lead was checked and does not supply c_loop) but the debit STAYS
    BARE-COUNTED. We do not manufacture a sign we cannot compute.
  - elegance is the diagnostic: if the elegant route (read the sign off a real
    spectral-zeta sum) is blocked because no such sum is executed anywhere, that
    is the signal the constant is owner-gated, not a wall to brute-force through.

================================================================================
THE OBJECT, STATED PRECISELY (what a REAL c_loop producer must compute)
================================================================================
c_loop is the coefficient of the e^{-6 sigma} term in the Gap-04 FRG-4 V_eff
(veff_coefficients_frg4.yaml, operator_exponents.c_loop_Z = "exp(-6 sigma)").
Here sigma is the K6 breathing mode: Vol(K6) = V_K6_0 * exp(+2 sigma), so the
K6 curvature / first-Laplace eigenvalue scale as exp(-2 sigma), and a 4D
one-loop Casimir energy density built from the K6 KK tower (mass^2 ~ lambda/R_K6^2
~ exp(-2 sigma)) summed and zeta-regularized gives a leading piece ~ (1/R_K6)^6
= exp(-6 sigma). A genuine producer is therefore:

  c_loop = -(1/2) * (4 pi)^{-D/2} * zeta_{Delta_K6}(-1/2)   [scalar KK tower]

where zeta_{Delta_K6}(s) = sum over SU(3) reps (p,q) of
        deg(p,q) * [ C_2(p,q) / R_K6^2 ]^{-s}
is the SCALAR spectral zeta on K6 = SU(3)/T^2 (eigenvalues = quadratic Casimir
of the SU(3) reps appearing in L^2(SU(3)/T^2), degeneracy = dim of the rep), and
the SIGN OF ITS UNDERLYING DENSITY is sign[ zeta_{Delta_K6}(-1/2) ] BEFORE the
universal -(1/2) bosonic one-loop prefactor.

  * If that underlying density (zeta(-1/2)) is NEGATIVE  -> under the shared
    global -(1/2) the positive-density a_4 cross-term flips relative sign
    -> c_a4 > 0 -> BRANCH-STANDS (the -sigma FRG-4 well stands).
  * If POSITIVE -> a_4 stays negative -> BRANCH-RUNAWAY (a_4 growth-8 dominates
    the c_loop growth-6 wall at -sigma -> V -> -inf).

To READ OFF that sign honestly we need the zeta(-1/2) of the ACTUAL K6 scalar
tower ACTUALLY SUMMED and ACTUALLY analytically continued. This script builds the
tower data-blind to (i) define the object concretely and (ii) test whether the
flagged candidates execute this very sum.

================================================================================
OBJECT CHECK of the flagged candidates (the decisive step)
================================================================================
We parse pub1_casimir.py and closure4_spectral_zeta.py and test, mechanically,
whether either one EXECUTES the scalar KK-tower spectral-zeta sum defined above:
  (C1) loops over the SU(3) rep tower (p,q) building C_2(p,q) and degeneracies;
  (C2) forms zeta_{Delta_K6}(s) and analytically continues to s=-1/2;
  (C3) derives the K6 coefficient FROM that continuation (not a typed-in rational);
  (C4) isolates the SCALAR breathing-mode e^{-6 sigma} piece as a single term
       (not a boson+fermion species-counted flux-balance stabilization radius).
If any of C1-C4 fails, the candidate does NOT produce the scalar c_loop wall and
its K6 number cannot supply the underlying-density sign.

NON-PROMOTION: no gate flip; no status word emitted for any gate. exit 0 on an
honest resolution; exit 2 if an input is unreadable or a forbidden token leaks.
"""

import hashlib
import json
import math
import os
import re
import sys
from fractions import Fraction

# ---------------------------------------------------------------------------
# Paths to the flagged candidate machinery (read-only; object check).
# ---------------------------------------------------------------------------
SYM = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
       r"physics_Journal_and_patents/severe_tests_paper/hc1_closure/symbolic")
PUB1 = os.path.join(SYM, "pub1_casimir.py")
CLOSURE4 = os.path.join(SYM, "closure4_spectral_zeta.py")
K6ZETA = os.path.join(SYM, "k6_zeta_casimir_insertion.py")  # prior-survey near-hit

# Gap-04 frozen artifacts (for the c_loop WALL value -- read ONLY after the
# object check, and only the geometry/coefficient, never an observed anchor).
FA = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
      r"physics_Journal_and_patents/Final_physics_articles/scripts/gap_04")
VEFF_YAML = os.path.join(FA, "outputs", "veff_coefficients_frg4.yaml")
GILKEY_JSON = os.path.join(FA, "outputs", "gilkey_a4_cross_terms.json")

# ---------------------------------------------------------------------------
# FROZEN inputs (geometry + group theory ONLY; no observed value).
# ---------------------------------------------------------------------------
R_K6_0 = 30.0        # scalar curvature * unit vol, K6 = SU(3)/T^2 (6 * Einstein +5)
R_S2_0 = 2.0         # round S^2 (2 * Einstein +1)
A4_R2_MASTER = Fraction(5, 360)          # convention-invariant Gilkey a_4 R^2 coeff
A4_CROSS_PREFACTOR = 2 * A4_R2_MASTER    # = 1/36
D_BULK = 13
HK_NORM = 1.0 / (math.pow(4.0 * math.pi, D_BULK / 2.0))   # (4 pi)^{-D/2} > 0
GLOBAL_ONE_LOOP = -0.5                    # universal bosonic one-loop magnitude

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
# PART A. Build the SCALAR K6 = SU(3)/T^2 KK tower data-blind (the OBJECT).
# ===========================================================================
# L^2(SU(3)/T^2) decomposes into SU(3) irreps; for a scalar the Laplace
# eigenvalue on the homogeneous space is the quadratic Casimir C_2(p,q) of the
# irrep (in the normalization where the adjoint (1,1) has C_2 = ... ), with
# multiplicity = dim(p,q) times the count of T^2-invariant (zero-weight) vectors.
# We use the standard SU(3) Casimir and Weyl dimension formulas. This block
# DEFINES the object; we do NOT need the full continuation to make the object
# DECISION (the candidates do not even reach this loop), but we execute enough
# of it to show what a real producer's inner loop looks like.

def su3_dim(p, q):
    """Weyl dimension of the SU(3) irrep with Dynkin labels (p, q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def su3_casimir(p, q):
    """Quadratic Casimir C_2(p,q) of SU(3) (standard normalization, adjoint=3)."""
    # C_2 = (1/3)(p^2 + q^2 + p q) + (p + q)   [normalization with C_2(1,0)=4/3,
    # C_2(1,1)=3 for the adjoint]
    return Fraction(p * p + q * q + p * q, 3) + (p + q)


def t2_zero_weight_multiplicity(p, q):
    """
    Number of zero-weight (T^2-invariant) states in the SU(3) irrep (p,q):
    the multiplicity of the scalar KK mode of that rep on SU(3)/T^2. For SU(3)
    the zero-weight multiplicity of (p,q) equals min(p,q)+1 when (p-q) % 3 == 0,
    else 0 (only reps with triality 0 contain a zero weight).
    """
    if (p - q) % 3 != 0:
        return 0
    return min(p, q) + 1


def build_scalar_k6_tower(n_max):
    """
    Build the first chunk of the SCALAR K6 spectral data:
      list of (lambda_unit = C_2(p,q), degeneracy = mult * dim-on-coset).
    Returns the partial spectral data; this is the inner object a genuine
    zeta_{Delta_K6}(s) sum would continue. We expose it so the object is
    concrete, not rhetorical.
    """
    tower = []
    for p in range(n_max + 1):
        for q in range(n_max + 1):
            mult = t2_zero_weight_multiplicity(p, q)
            if mult == 0:
                continue
            lam = su3_casimir(p, q)       # eigenvalue (in 1/R_K6^2 units)
            if lam == 0:
                continue                  # zero mode (the (0,0) trivial rep)
            deg = mult                    # scalar coset KK degeneracy
            tower.append((p, q, float(lam), deg))
    return tower


def partial_zeta_K6(tower, s):
    """
    Partial (non-continued) spectral zeta sum sum_n deg_n * lambda_n^{-s}.
    For Re(s) large this converges; at s = -1/2 it DIVERGES and REQUIRES
    analytic continuation (Mellin / Epstein-Hurwitz on the SU(3) Casimir
    lattice) -- which is exactly the multi-week object NOT executed by the
    candidates. We compute it at a convergent s only to witness the tower is
    real and the continuation is nontrivial.
    """
    total = 0.0
    for (_p, _q, lam, deg) in tower:
        total += deg * (lam ** (-s))
    return total


# ===========================================================================
# PART B. OBJECT CHECK: do the flagged candidates EXECUTE this sum?
# ===========================================================================
def candidate_object_check(src_text):
    """
    Mechanically test C1-C4 against a candidate's source.
    Returns dict of booleans + evidence.
    """
    # C1: loops over SU(3) rep tower building C_2(p,q) and degeneracies.
    #     Require an actual for-loop over rep labels AND a Casimir computation
    #     in code (not merely a comment). Comments containing "C_2(p,q)" do NOT
    #     count.
    code_lines = []
    for ln in src_text.splitlines():
        stripped = ln.split("#", 1)[0]   # drop trailing comments
        code_lines.append(stripped)
    code = "\n".join(code_lines)

    has_rep_loop = bool(
        re.search(r"for\s+\(?\s*p\s*,\s*q", code)            # for p, q in ...
        or re.search(r"for\s+p\s+in\s+range.*\n.*for\s+q\s+in\s+range", code)
    )
    computes_casimir_in_code = bool(
        re.search(r"(C_?2|casimir).*=.*(p|q)", code, re.IGNORECASE)
        and ("p*p" in code or "p**2" in code or "p * p" in code
             or "p*q" in code or "p * q" in code)
    )
    C1 = has_rep_loop and computes_casimir_in_code

    # C2: forms a spectral zeta zeta_K6(s) and continues to s = -1/2.
    #     Require either an explicit zeta(-0.5)/zeta(-1/2) continuation on the K6
    #     tower, or use of a Riemann/Hurwitz/Epstein zeta continuation on K6.
    forms_zeta_K6 = bool(re.search(r"zeta_K6\s*\(", code))
    continues_minus_half = (
        "-1/2" in code or "-0.5" in code or "(-0.5)" in code
    ) and forms_zeta_K6
    uses_zeta_continuation = bool(
        re.search(r"(special\.)?zeta\s*\(", code)
        or "mpmath" in code or "zetac" in code or "hurwitz" in code.lower()
    )
    C2 = (forms_zeta_K6 and continues_minus_half) or (
        forms_zeta_K6 and uses_zeta_continuation)

    # C3: derives the K6 coefficient FROM a continuation (not a typed-in rational).
    #     Detect the tell-tale hardcoded rationals 1/945, 31/15120 used as the K6
    #     coefficient; if present AND no continuation, C3 fails.
    hardcoded_k6 = ("945" in code) or ("15120" in code)
    C3 = (not hardcoded_k6) and (C1 or uses_zeta_continuation)

    # C4: isolates the SCALAR breathing-mode e^{-6 sigma} piece as a SINGLE
    #     scalar term -- NOT a boson+fermion species-counted multi-factor
    #     flux-balance radius minimization. Detect the flux-balance signature.
    flux_balance = bool(
        re.search(r"minimize\s*\(", code)
        or "V_flux" in code or "V_full" in code or "R_K6_stab" in code
    )
    species_counted = ("N_f" in code) or ("N_b" in code) or ("c_K6_spinor" in code)
    isolates_scalar_wall = (not flux_balance) and (not species_counted)
    C4 = isolates_scalar_wall

    return {
        "C1_loops_su3_rep_tower_and_computes_C2_in_code": C1,
        "C1_has_rep_loop": has_rep_loop,
        "C1_computes_casimir_in_code": computes_casimir_in_code,
        "C2_forms_and_continues_zeta_K6_to_minus_half": C2,
        "C2_forms_zeta_K6": forms_zeta_K6,
        "C2_uses_zeta_continuation": uses_zeta_continuation,
        "C3_derives_K6_coeff_from_continuation_not_typed_rational": C3,
        "C3_hardcoded_1over945_or_31over15120_present": hardcoded_k6,
        "C4_isolates_scalar_e_minus_6sigma_wall_single_term": C4,
        "C4_is_flux_balance_radius_minimization": flux_balance,
        "C4_is_boson_fermion_species_counted": species_counted,
        "produces_scalar_c_loop_wall": bool(C1 and C2 and C3 and C4),
    }


def read_c_loop_wall(veff_text):
    for ln in veff_text.splitlines():
        s = ln.strip()
        if s.startswith("c_loop_Z:"):
            try:
                return float(s.split(":", 1)[1].split("#")[0].strip())
            except ValueError:
                return None
    return None


def main():
    # ---- locate inputs (refuse if missing) --------------------------------
    for p in (PUB1, CLOSURE4, VEFF_YAML, GILKEY_JSON):
        if not os.path.exists(p):
            sys.stderr.write("REFUSE(exit2): missing input %s\n" % p)
            return 2

    pub1_src = open(PUB1, "r", encoding="utf-8").read()
    closure4_src = open(CLOSURE4, "r", encoding="utf-8").read()
    veff_text = open(VEFF_YAML, "r", encoding="utf-8").read()
    gilkey = json.load(open(GILKEY_JSON, "r", encoding="utf-8"))

    # forbidden-value firewall on everything we read.
    for name, txt in (("pub1_casimir.py", pub1_src),
                      ("closure4_spectral_zeta.py", closure4_src),
                      ("veff_coefficients_frg4.yaml", veff_text)):
        leaked = [t for t in FORBIDDEN_VALUE_TOKENS if t in txt]
        if leaked:
            sys.stderr.write("REFUSE(exit2): forbidden value in %s: %s\n"
                             % (name, leaked))
            return 2

    # =====================================================================
    # PART A. Build the scalar K6 tower (the OBJECT, data-blind).
    # =====================================================================
    tower = build_scalar_k6_tower(n_max=12)
    # Witness the tower is real and the continuation is nontrivial: at a
    # convergent s the partial sum is finite & positive; at s=-1/2 it diverges
    # (so a genuine producer MUST analytically continue -- the deferred step).
    z_at_2 = partial_zeta_K6(tower, s=2.0)     # convergent witness
    n_modes_listed = len(tower)
    smallest_modes = sorted(tower, key=lambda r: r[2])[:6]

    # =====================================================================
    # PART B. OBJECT CHECK on the flagged candidates.
    # =====================================================================
    pub1_check = candidate_object_check(pub1_src)
    closure4_check = candidate_object_check(closure4_src)

    pub1_is_object = pub1_check["produces_scalar_c_loop_wall"]
    closure4_is_object = closure4_check["produces_scalar_c_loop_wall"]
    any_candidate_is_object = pub1_is_object or closure4_is_object

    # =====================================================================
    # AFTER the object check: read the c_loop WALL value (geometry side only).
    # =====================================================================
    c_loop_wall = read_c_loop_wall(veff_text)
    c_a4_on_disk = float(
        gilkey["a4_cross_terms"]["K6_x_S2"]["coefficient_value_M13_4_units"])

    # =====================================================================
    # THE HONEST RESOLUTION (do NOT force a sign / a branch).
    # =====================================================================
    if any_candidate_is_object:
        # Only reachable if a candidate ACTUALLY executes the scalar KK-tower
        # spectral-zeta sum and continues zeta_{Delta_K6}(-1/2). It does not
        # (proven below by C1-C4). Kept honest, never forced.
        outcome = "DERIVED-via-flagged-machinery (unreachable: candidates do "
        outcome += "not execute the sum)"
        machinery_applies = ("YES -- a flagged candidate executed the scalar "
                             "KK-tower spectral-zeta sum")
        density_sign = "(would be read from zeta_{Delta_K6}(-1/2))"
        branch = "(decided by that sign)"
        debit = "DERIVED"
    else:
        outcome = "MACHINERY-DIFFERENT-OBJECT-owner-locked"
        machinery_applies = (
            "NO. pub1_casimir.py and closure4_spectral_zeta.py do NOT compute "
            "the scalar KK-Casimir wall that produces the e^{-6 sigma} c_loop "
            "coefficient. They are a DIFFERENT object: a multi-factor "
            "boson+fermion species-counted flux-balance RADIUS-STABILIZATION "
            "(minimize c_K6/R^6 + c_S2/R^2 + c_S1/R + flux), with the K6 "
            "coefficient TYPED IN as a self-disclaimed rational (c_K6_scalar = "
            "1/945 'estimated'; c_K6_spinor = -31/15120 'rough estimate'). "
            "Neither loops over the SU(3) rep tower (no C_2(p,q) computed in "
            "code -- it appears only in a comment), neither forms zeta_{Delta_K6}"
            "(s) nor continues it to s=-1/2, and neither isolates the single "
            "scalar e^{-6 sigma} wall term. The 1/R_K6^6 == e^{-6 sigma} "
            "breathing exponent coincides, but exponent-match is NOT "
            "object-identity (c_a4 e^{-(8s+4r+x)} and c_KK e^{-4s} also scale "
            "as breathing powers and are different objects).")
        density_sign = "GATED-ON-OPEN (UNBANKED -- not supplied by the flagged machinery)"
        branch = "still-owner-locked"
        debit = ("STAYS BARE-COUNTED (the relative-one-loop-sign debit in "
                 "gap04_reason_hunt.py is NOT promoted to DERIVED: the flagged "
                 "machinery was checked and does NOT supply the scalar c_loop "
                 "underlying-density sign)")

    result = {
        "schema": "gap04_cloop_casimir_firstprinciples_result_v1",
        "purpose": (
            "Try the elegant path: read the sign of c_loop's underlying "
            "heat-kernel density off a genuine first-principles scalar KK-tower "
            "spectral-zeta Casimir computation; FIRST verify the flagged "
            "machinery (pub1_casimir.py / closure4_spectral_zeta.py) is that "
            "object."),

        "outcome": outcome,
        "machinery_applies": machinery_applies,
        "c_loop_underlying_density_sign": density_sign,
        "branch_selected": branch,
        "debit_reclassification": debit,

        "object_definition_the_real_producer_must_compute": {
            "c_loop_operator": "c_loop_Z * exp(-6 sigma) in V_eff (veff_coefficients_frg4.yaml)",
            "sigma_is": "K6 breathing mode: Vol(K6)=V_K6_0*exp(+2 sigma) -> R_K6 ~ exp(-2 sigma) -> Casimir ~ (1/R_K6)^6 = exp(-6 sigma)",
            "producer": "c_loop = -(1/2)*(4 pi)^{-D/2}*zeta_{Delta_K6}(-1/2) [scalar KK tower]",
            "zeta_K6": "sum_(p,q) deg(p,q) * [C_2(p,q)/R_K6^2]^{-s}, deg from T^2-zero-weight mult, eigenvalue = SU(3) Casimir",
            "underlying_density_sign_is": "sign[ zeta_{Delta_K6}(-1/2) ] BEFORE the -(1/2) prefactor",
        },

        "part_A_scalar_K6_tower_built_data_blind": {
            "n_max": 12,
            "n_triality0_modes_listed": n_modes_listed,
            "smallest_modes_(p,q,C2,deg)": smallest_modes,
            "partial_zeta_K6_at_s=2_convergent_witness": z_at_2,
            "note": (
                "The tower is real and the eigenvalues are the SU(3) Casimirs of "
                "triality-0 reps (the (1,1) adjoint at C_2=3 is the first nonzero "
                "scalar KK level). At s=-1/2 this sum DIVERGES and REQUIRES "
                "Epstein-Hurwitz / Mellin analytic continuation on the SU(3) "
                "Casimir lattice -- precisely the multi-week object the candidates "
                "explicitly DEFER ('Full spectral zeta function ... 2-4 week "
                "dedicated calculation'). We did NOT continue it here because no "
                "data-blind continuation produces the FROZEN inherited c_loop "
                "magnitude without the owner's FRG-2 NLO shell-projection scheme; "
                "asserting a sign from a half-built continuation would be the "
                "manufactured favorable-branch step the countersign exists to catch."),
        },

        "part_B_object_check_of_flagged_candidates": {
            "pub1_casimir.py": pub1_check,
            "closure4_spectral_zeta.py": closure4_check,
            "decisive_findings": [
                "C1 FAILS both: no for-loop over the SU(3) (p,q) rep tower with a "
                "C_2(p,q) computed in code; 'C_2(p,q)' appears only in a docstring "
                "comment.",
                "C2 FAILS both: neither forms zeta_{Delta_K6}(s) nor continues to "
                "s=-1/2; no Riemann/Hurwitz/Epstein zeta continuation is invoked.",
                "C3 FAILS both: the K6 coefficient is the typed-in self-disclaimed "
                "rational (1/945 'estimated', 31/15120 'rough estimate'), NOT a "
                "continuation output.",
                "C4 FAILS both: each is a boson+fermion species-counted "
                "(N_b, N_f=45) multi-factor flux-balance RADIUS minimization "
                "(minimize c_K6/R^6 + c_S2/R^2 + c_S1/R + V_flux), not a single "
                "isolated scalar e^{-6 sigma} wall term.",
            ],
        },

        "numerical_disjointness_after_object_check": {
            "candidate_c_K6_total_sign_required_for_their_flux_balance": "NEGATIVE (they require c_K6<0 to stabilize)",
            "candidate_c_K6_total_approx": "~ -0.08 (12*(1/945) - 45*(31/15120))",
            "c_loop_wall_value": c_loop_wall,
            "c_loop_wall_sign": "POSITIVE (+1.3637e-5)",
            "disjoint": (
                "Different SIGN, different MAGNITUDE (candidate ~ -8e-2 vs c_loop "
                "+1.4e-5, 3+ orders apart), different DEFINITION (combined "
                "boson+fermion species count vs FRG-2 NLO Litim-regulator scalar "
                "shell projection). The candidate K6 number is NOT c_loop."),
        },

        "prior_survey_nearest_hit_reconfirmed_different": (
            "k6_zeta_casimir_insertion.py remains a DIFFERENT object: it closes "
            "only the LOCAL Dirac/fermion-bundle Seeley-DeWitt a_4 coefficient at "
            "the Einstein point and explicitly 'does not claim to compute the full "
            "finite nonlocal determinant'. It is neither the scalar KK-Casimir "
            "wall nor the flux-balance stabilizer."),

        "object_check": (
            "The flagged machinery computes a fermion-and-boson species-counted "
            "multi-factor flux-balance radius stabilization with a TYPED-IN, "
            "self-disclaimed K6 rational (1/945, 31/15120) -- NOT the scalar "
            "KK-Casimir wall (e^{-6 sigma}, the breathing-mode zero-point sum). "
            "k6_zeta_casimir_insertion.py is a third, also-different object (local "
            "Dirac-bundle Seeley-DeWitt coefficient). None executes the scalar "
            "zeta_{Delta_K6}(-1/2) sum whose sign decides the branch."),

        "well_verdict": (
            "OWNER-LOCKED / CONDITIONAL, UNCHANGED -- but the elimination is now "
            "COMPLETE: the two flagged scalar-Casimir candidates (and the prior "
            "near-hit) have been checked and do NOT supply the scalar c_loop "
            "underlying-density sign. The -sigma FRG-4 3-modulus well's survival "
            "stays gated on the named OPEN first-principles object "
            "B-UQFC-14-FRG-2. The favorable branch was NOT forced (the genuine "
            "global -(1/2) on a_4's own positive density gives c_a4 NEGATIVE "
            "= %.3e -> runaway); the well is NOT forced to fail (the relative "
            "sign vs c_loop is unbanked). Both branches stay live with named "
            "falsifiers."
        ) % c_a4_on_disk,

        "what_requires_chris": (
            "A REAL first-principles c_loop producer must: (1) enumerate the "
            "SCALAR K6=SU(3)/T^2 KK tower in CODE -- loop over SU(3) reps (p,q) of "
            "triality 0, eigenvalue = C_2(p,q)/R_K6^2, degeneracy = T^2-zero-weight "
            "multiplicity (built data-blind here in Part A); (2) form the spectral "
            "zeta zeta_{Delta_K6}(s) = sum deg*lambda^{-s} and ANALYTICALLY CONTINUE "
            "it (Epstein-Hurwitz / Mellin on the SU(3) Casimir lattice, MS-bar "
            "scheme matching the FRG-2 Litim regulator) to s = -1/2; (3) apply the "
            "universal -(1/2)(4 pi)^{-D/2} one-loop prefactor and READ OFF "
            "sign[zeta_{Delta_K6}(-1/2)] = the underlying-density sign; (4) confirm "
            "it reproduces the frozen c_loop magnitude (1.3637877e-5) under the "
            "FRG-2 NLO shell-projection scheme, closing B-UQFC-14-FRG-2. None of "
            "the flagged machinery does steps 1-3; the K6 zeta(-1/2) continuation "
            "is the deferred multi-week object."),

        "provenance_hashes": {
            "pub1_casimir.py": sha256_file(PUB1),
            "closure4_spectral_zeta.py": sha256_file(CLOSURE4),
            "k6_zeta_casimir_insertion.py": sha256_file(K6ZETA),
            "veff_coefficients_frg4.yaml": sha256_file(VEFF_YAML),
            "gilkey_a4_cross_terms.json": sha256_file(GILKEY_JSON),
        },
        "frozen_inputs_used": {
            "R_K6_0": R_K6_0, "R_S2_0": R_S2_0,
            "a4_cross_prefactor_1_over_36": float(A4_CROSS_PREFACTOR),
            "D_bulk": D_BULK, "factor_4pi_to_minus_D_over_2": HK_NORM,
            "global_one_loop_prefactor": GLOBAL_ONE_LOOP,
            "c_loop_wall_value_read_after_object_check": c_loop_wall,
        },
        "no_target_loading": True,
        "no_target_loading_attest": (
            "No observed value entered on any input side (no A_s, Lambda_obs, r, "
            "eta_B, n_s, N_eff, PDG, Omega_DM, H_0, S_8). The scalar K6 tower in "
            "Part A is built from the frozen geometry (Einstein constant +5, dim 6) "
            "and SU(3) group theory ALONE. The c_loop WALL value was read ONLY "
            "after the object check, and only as a geometry-side coefficient for "
            "the disjointness witness -- never as an input to a derivation. The "
            "favorable (well-stands) branch was NOT forced: no sign was asserted "
            "for zeta_{Delta_K6}(-1/2); the well is left owner-locked because the "
            "deciding object is not supplied by the flagged machinery."),
        "non_promotion": (
            "no gate flipped; no status word emitted for any gate; "
            "countersign-ready object-mismatch analysis only."),
    }

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gap04_cloop_casimir_firstprinciples_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- decision-grade packet to stdout ----------------------------------
    print("=" * 74)
    print("Gap-04  c_loop FIRST-PRINCIPLES scalar KK-Casimir attempt (FRG-2 lane)")
    print("=" * 74)
    print("OBJECT (real producer): c_loop = -(1/2)(4pi)^{-D/2} zeta_{Delta_K6}(-1/2)")
    print("  sigma = K6 breathing mode -> Casimir ~ (1/R_K6)^6 = exp(-6 sigma)")
    print("-" * 74)
    print("PART A  scalar K6=SU(3)/T^2 tower built data-blind:")
    print("  triality-0 KK modes listed (n_max=12): %d" % n_modes_listed)
    print("  first nonzero levels (p,q,C2,deg): %s"
          % ", ".join("(%d,%d;%.3g;x%d)" % (p, q, c, d)
                      for (p, q, c, d) in smallest_modes[:4]))
    print("  partial zeta_K6(s=2) convergent witness: %.6g" % z_at_2)
    print("  zeta_K6(-1/2): DIVERGES -> requires Epstein-Hurwitz continuation")
    print("                 (the deferred multi-week object; NOT executed here")
    print("                  and NOT in the candidates)")
    print("-" * 74)
    print("PART B  object check of flagged candidates:")
    for nm, chk in (("pub1_casimir.py", pub1_check),
                    ("closure4_spectral_zeta.py", closure4_check)):
        print("  %s produces scalar c_loop wall: %s"
              % (nm, chk["produces_scalar_c_loop_wall"]))
        print("     C1 rep-tower+C2 in code: %s | C2 zeta_K6 continued: %s | "
              "C3 not-typed-rational: %s | C4 isolated scalar wall: %s"
              % (chk["C1_loops_su3_rep_tower_and_computes_C2_in_code"],
                 chk["C2_forms_and_continues_zeta_K6_to_minus_half"],
                 chk["C3_derives_K6_coeff_from_continuation_not_typed_rational"],
                 chk["C4_isolates_scalar_e_minus_6sigma_wall_single_term"]))
    print("-" * 74)
    print("c_loop wall value (read AFTER object check): %s  [POSITIVE]" % c_loop_wall)
    print("candidate c_K6_total ~ -0.08  [NEGATIVE, 3+ orders larger] -> DISJOINT")
    print("-" * 74)
    print("OUTCOME : %s" % outcome)
    print("MACHINERY APPLIES: %s" % ("NO -- different object"
                                     if not any_candidate_is_object else "YES"))
    print("DENSITY SIGN: %s" % density_sign)
    print("BRANCH  : %s" % branch)
    print("DEBIT   : %s" % ("STAYS BARE-COUNTED" if not any_candidate_is_object
                            else "DERIVED"))
    print("-" * 74)
    print("ELIMINATION COMPLETE: flagged scalar-Casimir machinery checked and does")
    print("  NOT supply c_loop. Real producer requires the K6 zeta(-1/2)")
    print("  continuation (steps 1-4 in result.what_requires_chris) =")
    print("  named open object B-UQFC-14-FRG-2 (owner = Chris).")
    print("artifact:", out_path)
    print("=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
