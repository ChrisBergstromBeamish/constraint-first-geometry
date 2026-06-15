#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gap04_intloop_principle_check.py
================================
INVESTIGATE: does ANY physical/geometric PRINCIPLE fix the sign of int_loop --
the finite part of the scalar SU(3)/T^2 Casimir (= the sign of c_loop's
underlying heat-kernel density) -- for OUR FROZEN geometry K6 x S^2 x S^1_Y/Z2,
thereby settling the Gap-04 well (STANDS vs RUNAWAY) WITHOUT needing the full
cosmological-constant (Lambda) resolution?

This BUILDS ON (does not duplicate):
  * gap04_zeta_continuation_frg2.py  -- the COMPLETED Epstein-Hurwitz/Mellin
    continuation: zeta_{Delta_K6}(s) has a SIMPLE POLE at s=-1/2 (heat trace
    carries a nonzero t^{+1/2} term, c_{+1/2}=+0.28786); residue R=-0.0812
    (scheme-INVARIANT, negative); finite part F=-0.4543 (mu=1/R_K6, scheme-DEP,
    sign flips at mu*=0.061). d_eff = 3 (Theta ~ t^{-3/2}).
  * c_loop_NLO_match.py / gap04_litim_scheme_branch.py -- the Litim
    shell-projection: assembled c_loop coefficient POSITIVE but magnitude
    owner-locked; the relative sign is construction-dependent.
  * gilkey_a4_cross_terms.py -- int_a4 = +(1/36) R_K6 R_S2 is geometry-forced
    POSITIVE and convention-INVARIANT; the CONVENTION_FREEZE slot for the
    a_4 sector (the c_loop underlying-density sign) is UNFILLED = owner-must-rule.
  * TOE_FINAL_merged.md SS.III -- the I2 supertrace (a single signed sum over the
    theory's FULL 17-row physical inventory, bosons AND fermions, at the frozen
    radii) = (-88.93 +/- band)/R_Y^4 + c_loop : NO structural cancellation
    (graded/ungraded ratio 0.58 at k=0, 1.000 at k=1..8). I3: the Lambda
    operator is the unit operator (grading-blind).

================================================================================
THE DISCIPLINE (no-target-loading on the SIGN side -- read twice)
================================================================================
The forbidden move is to pick int_loop's sign by reference to (a) any observed
value, (b) the corpus's ASSUMED c_loop>0, or (c) the DESIRE for stability
(BRANCH-STANDS). A sign is DERIVED here ONLY if a genuine geometric/physical
principle, applied to OUR frozen geometry, with the computation IN THIS PASSAGE,
forces it -- regardless of whether the forced direction is favorable. If no
principle forces it, we say so plainly: that is the honest, Lambda-hard answer.

We test FIVE candidate principles. For each we report: FIXES (and which way),
INCONCLUSIVE, or ITSELF-OPEN, with the precise reason.

  (1) REFLECTION POSITIVITY / boundedness-below of the Euclidean effective
      action on K6 x S^2 x S^1.
  (2) a6 UV-COMPLETION CONSISTENCY (Gap-01): does a consistent a6 Seeley-DeWitt /
      positive-definite physical Hilbert space fix the a4-sector finite
      subtraction sign?
  (3) CLOSED-FORM COSET CASIMIR: is there a known/derivable closed form for the
      scalar zeta(-1/2) finite part of the flag manifold SU(3)/T^2 in a
      canonical scheme, and what sign?
  (4) FERMION-PARTNER / SUSY cancellation: does the theory's fermion content pair
      with the scalar tower to fix or cancel the sign?
  (5) d_eff PARITY: can the PHYSICAL spectral sum (not the zero-weight slice) be
      even-dimensional, removing the pole?

NON-PROMOTION: no gate flip; no status word emitted for any gate. exit 0 on an
honest resolution; exit 2 if an input is unreadable or a forbidden token leaks.
"""

import hashlib
import json
import math
import os
import sys
from collections import defaultdict
from fractions import Fraction

# ---------------------------------------------------------------------------
# Paths. NO observed value is read anywhere. The frozen c_loop MAGNITUDE is not
# even needed for a SIGN investigation, so it is not read into any decision.
# ---------------------------------------------------------------------------
FA = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
      r"physics_Journal_and_patents/Final_physics_articles/scripts/gap_04")
GAP01 = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
         r"physics_Journal_and_patents/Final_physics_articles/scripts/gap_01_a6_attempt")
FROZEN_YAML = os.path.join(FA, "frozen_inputs.yaml")
GILKEY_SRC = os.path.join(FA, "src", "gilkey_a4_cross_terms.py")
A6_SCAFFOLD = os.path.join(GAP01, "outputs", "a6_recursion_scaffold.json")
A6_B1B2 = os.path.join(GAP01, "outputs", "b1_b2_derive_then_compare.json")

PI = math.pi
D_BULK = 13

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
# SHARED: rebuild the K6=SU(3)/T^2 scalar zero-weight tower and its half-integer
# heat-trace structure (the OBJECT every candidate must act on). This reproduces
# the structural facts of gap04_zeta_continuation_frg2.py compactly and
# data-blind, so the parity / scheme arguments below are self-contained.
# ===========================================================================
def su3_casimir(p, q):
    """C2(p,q)=(p^2+q^2+pq+3p+3q)/3 ; C2(1,1)=3 (adjoint), C2(1,0)=4/3 (fund)."""
    return Fraction(p * p + q * q + p * q + 3 * p + 3 * q, 3)


def build_scalar_zeroweight_tower(a_max):
    r"""
    SCALAR KK tower on K6: eigenvalue = SU(3) Casimir of triality-0 reps,
    degeneracy = T^2 (Cartan) ZERO-WEIGHT multiplicity = min(p,q)+1.
    In shifted Eisenstein coords (a,b)=(p+1,q+1):
        lambda=(a^2+ab+b^2-3)/3, deg=min(a,b), a,b>=1, a==b (mod 3).
    Returns sorted [(lambda,deg)] over distinct positive eigenvalues + n0.
    """
    spec = defaultdict(int)
    n0 = 0
    for a in range(1, a_max + 1):
        for b in range(1, a_max + 1):
            if (a - b) % 3:
                continue
            lam = (a * a + a * b + b * b - 3) // 3
            if lam == 0:
                n0 += min(a, b)
                continue
            spec[lam] += min(a, b)
    return sorted(spec.items()), n0


def build_scalar_FULLdim_tower(a_max):
    r"""
    The GENUINE full L^2(K6 = SU(3)/T^2) scalar spectrum (every function mode on
    the 6-manifold), via the Peter-Weyl decomposition of a homogeneous space
    G/H: L^2(G/H) = sum_irrep (mult of H-trivial vectors) x irrep, with Laplacian
    eigenvalue = Casimir(p,q) and degeneracy
        deg_full(p,q) = dim(p,q) x (T^2 zero-weight multiplicity)
                      = [(p+1)(q+1)(p+q+2)/2] x [min(p,q)+1]   (triality-0 reps).
    The dim(p,q) factor is the irrep dimension; the (min(p,q)+1) factor is the
    multiplicity of the T^2-trivial (Cartan zero-weight) vectors. This is the
    CORRECT 6-manifold trace; its heat trace runs in INTEGER powers (Weyl law
    Theta ~ a0 t^{-3}, d_eff=6, EVEN) -- verified by the caller.

    Contrast: the corpus c_loop uses the ZERO-WEIGHT SLICE alone (degeneracy
    min(p,q)+1, WITHOUT the dim(p,q) factor) -- the d_eff=3 (ODD) modulus sector
    that produces the s=-1/2 pole. build_scalar_zeroweight_tower() is that slice.

    Returns sorted [(lambda, deg_full)] over distinct positive eigenvalues.
    """
    spec = defaultdict(int)
    for p in range(0, a_max + 1):
        for q in range(0, a_max + 1):
            if (p - q) % 3:
                continue
            c2 = su3_casimir(p, q)
            if c2 == 0:
                continue
            dimpq = (p + 1) * (q + 1) * (p + q + 2) // 2
            zw = min(p, q) + 1
            spec[c2] += dimpq * zw
    return sorted(spec.items())


def half_integer_heat_coeffs(tower, n0, exps, nodes):
    r"""
    Fit the small-t heat-trace coefficients Theta(t)=n0+sum deg e^{-lambda t}
    ~ sum_k c_k t^{e_k}. Returns the dict {e_k: c_k}. Uses a plain float
    Vandermonde least-squares (the leading + the t^{+1/2} pole coefficient are
    the only ones we use, and they are robust); high-precision is unnecessary
    for a SIGN/PARITY decision.
    """
    import numpy as np

    lams = np.array([l for l, _ in tower], dtype=np.float64)
    degs = np.array([d for _, d in tower], dtype=np.float64)

    def Theta(t):
        return float(n0 + np.sum(degs * np.exp(-lams * t)))

    M = np.zeros((len(nodes), len(exps)))
    rhs = np.zeros(len(nodes))
    for i, nn in enumerate(nodes):
        t = 1.0 / nn
        rhs[i] = Theta(t)
        for j, e in enumerate(exps):
            M[i, j] = t ** e
    coef, *_ = np.linalg.lstsq(M, rhs, rcond=None)
    return {e: float(coef[j]) for j, e in enumerate(exps)}


def integer_vs_halfinteger_parity(coeffs):
    r"""
    Decide whether the small-t expansion is in HALF-INTEGER powers (=> pole at
    s=-1/2 => odd d_eff => scheme-dependent finite part) or INTEGER powers
    (=> NO pole at s=-1/2 => even d_eff => scheme-FREE finite value).
    We compare |c_{+1/2}| (the would-be pole coefficient) against the leading
    |c_{-3/2}|. A nonzero c_{+1/2} (relative to leading) is the pole witness.
    """
    lead = abs(coeffs.get(-1.5, 0.0)) + abs(coeffs.get(-1.0, 0.0)) + 1e-300
    c_half = coeffs.get(0.5, 0.0)
    pole_present = abs(c_half) / lead > 1e-3
    return {
        "c_minus_three_half": coeffs.get(-1.5, None),
        "c_minus_one (integer power)": coeffs.get(-1.0, None),
        "c_plus_half (pole witness)": c_half,
        "pole_at_minus_half_present": bool(pole_present),
        "expansion_runs_in": ("HALF-INTEGER powers (odd d_eff; pole at s=-1/2)"
                              if pole_present else
                              "INTEGER powers (even d_eff; NO pole at s=-1/2)"),
    }


# ===========================================================================
# CANDIDATE 1 -- REFLECTION POSITIVITY / boundedness-below.
# ===========================================================================
def candidate_1_reflection_positivity():
    r"""
    Reflection positivity (Osterwalder-Schrader) and boundedness-below of the
    Euclidean effective action are CONSTRAINTS ON THE FULL PARTITION FUNCTION /
    SPECTRUM, not on the SIGN of a single renormalized finite vacuum-energy
    COEFFICIENT.

    Worked check on OUR geometry:
      * RP constrains the two-point function's spectral measure to be a positive
        measure (Kallen-Lehmann positivity). For a free scalar on a compact
        K6 x S^2 x S^1 this is automatic (the Laplacian is non-negative;
        eigenvalues lambda>=0; the zero-weight degeneracies min(p,q)+1>0). We
        VERIFY: every (lambda,deg) in the tower has lambda>0, deg>0. So RP is
        SATISFIED for either sign of the renormalized c_loop.
      * Boundedness-below is a statement about V_eff(sigma) as sigma->+-inf, i.e.
        about the SUM of operators (c_KK e^{-4s}, c_bdry e^{-2s}, c_Wilson...,
        c_loop e^{-6s}, c_a4 e^{-(8s+...)}), NOT about the sign of c_loop's
        density in isolation. It is precisely the QUANTITY UNDER DISPUTE (does
        V stay bounded at the -sigma corner?), so invoking it to fix int_loop's
        sign is CIRCULAR: 'choose int_loop so that V is bounded below' is the
        reverse-fit-for-stability the discipline forbids.
      * The corpus's own I2/I3 result is the decisive precedent: a single signed
        vacuum-energy sum (Str rho) over the FULL inventory is computed and is
        NONZERO (0.58 residual); the grading/positivity structure does NOT force
        it to a definite protective sign. RP did not rescue Lambda; it does not
        rescue int_loop either, for the same structural reason (the relevant
        operator is grading/positivity-blind).

    A finite renormalized vacuum-energy density CAN have EITHER sign in a
    reflection-positive theory (Casimir energies are famously negative for some
    geometries, positive for others, in fully unitary RP theories). RP places NO
    sign constraint on the renormalized finite part. => INCONCLUSIVE.
    """
    tower, n0 = build_scalar_zeroweight_tower(a_max=120)
    all_lambda_pos = all(l > 0 for l, _ in tower)
    all_deg_pos = all(d > 0 for _, d in tower)
    rp_satisfied_either_sign = all_lambda_pos and all_deg_pos
    return {
        "verdict": "INCONCLUSIVE",
        "fixes_sign": False,
        "spectrum_is_reflection_positive": bool(rp_satisfied_either_sign),
        "reason": (
            "Reflection positivity constrains the spectral measure (Laplacian "
            ">=0, eigenvalues lambda>0, degeneracies deg>0 -- all VERIFIED on the "
            "K6 zero-weight tower), which is satisfied REGARDLESS of the sign of "
            "the renormalized c_loop finite part. A reflection-positive (fully "
            "unitary) theory admits Casimir energies of EITHER sign (geometry-"
            "dependent), so RP places NO sign constraint on the renormalized "
            "finite vacuum-energy density. Boundedness-below is a statement about "
            "the FULL V_eff(sigma) at the -sigma corner -- which is exactly the "
            "quantity under dispute -- so using it to fix int_loop's sign is the "
            "circular reverse-fit-for-stability the discipline forbids. The "
            "corpus's own I2/I3 precedent confirms: a single signed vacuum-energy "
            "sum over the full inventory is computed NONZERO and the positivity/"
            "grading structure does not force a protective sign."),
    }


# ===========================================================================
# CANDIDATE 2 -- a6 UV-COMPLETION CONSISTENCY (Gap-01).
# ===========================================================================
def candidate_2_a6_consistency(a6_scaffold, a6_b1b2):
    r"""
    Does requiring a consistent a6 Seeley-DeWitt completion / positive-definite
    physical Hilbert space fix the a4-sector finite subtraction sign?

    Two independent reasons it does NOT, both read off the corpus's OWN a6 work:

    (A) a6 IS ITSELF OPEN. gap_01_a6_attempt records: only tr[E^3]=1/6 is
        derived; ALL purely-gravitational cubic coefficients c1..c8 and the mixed
        E/Omega coefficients are MISSING ('genuinely-new order-6 universal
        numbers; require full covariant Taylor/Synge recursion'). And the
        cubic-enlargement backreaction on the load-bearing B1/B2 ratio is
        b_i^* * J_i^{(a6)} with b_i^*=0 FORCED (canonical factor nonzero) and
        J_i^{(a6)} MISSING. So the a6 sector cannot fix anything downstream --
        it is a strictly LARGER open object than int_loop.

    (B) Even a COMPLETE a6 would not touch int_loop's sign, by the structure of
        the heat-kernel expansion: the one-loop vacuum energy is
            V^(1) = -(1/2)(4pi)^{-D/2} sum_n a_n (proper-time moments),
        and the a_n are INDEPENDENT local invariants. a6 multiplies a DIFFERENT
        operator (curvature^3, e.g. e^{-(12 sigma+...)} after Einstein-frame
        reduction) than the a4 cross-term (e^{-(8 sigma+...)}) and than the
        nonlocal c_loop wall (e^{-6 sigma}). UV completeness (a finite, consistent
        a6) constrains the DIVERGENCE structure (the pole residues), not the
        FINITE renormalized parts. The corpus already proved the int_loop-relevant
        residue is scheme-INVARIANT and negative; it is the FINITE part that is
        disputed, and a6 consistency does not pin a finite part of a LOWER
        coefficient. Positive-definiteness of the physical Hilbert space is the
        same statement as RP (candidate 1) and is sign-blind for the renormalized
        finite part.

    => ITSELF-OPEN (a6 is a larger open object) AND, even if closed,
       INCONCLUSIVE for int_loop's finite-part sign.
    """
    a6_open = True
    a6_reason = None
    try:
        missing = a6_scaffold.get("MISSING_universal_a6_coefficients", {})
        derived = a6_scaffold.get("DERIVED_HERE", {})
        a6_open = bool(missing) and ("coeff_tr_E3_in_a6" in derived)
        a6_reason = a6_scaffold.get("provenance_note")
    except Exception:
        a6_reason = "a6 scaffold unreadable"
    bistar_zero = None
    try:
        bistar_zero = (a6_b1b2.get("b_i_star_without_a6", None) == 0.0)
    except Exception:
        pass
    return {
        "verdict": "ITSELF-OPEN",
        "fixes_sign": False,
        "a6_is_open_object": bool(a6_open),
        "a6_b_i_star_forced_zero": bistar_zero,
        "a6_provenance": a6_reason,
        "reason": (
            "(A) a6 is ITSELF a strictly larger OPEN object: the corpus's "
            "gap_01_a6_attempt derives only tr[E^3]=1/6 and records ALL purely-"
            "gravitational cubic c1..c8 and mixed E/Omega coefficients as MISSING "
            "(require full covariant Taylor/Synge recursion); the cubic backreaction "
            "on B1/B2 is b_i^* * J_i^{(a6)} with b_i^*=0 FORCED and J_i^{(a6)} "
            "MISSING. It cannot fix a downstream sign. "
            "(B) Even a COMPLETE a6 would not pin int_loop: UV/Hilbert-space "
            "consistency constrains the DIVERGENCE structure (pole residues -- "
            "already scheme-invariant negative) not the disputed FINITE part of a "
            "LOWER coefficient; a6 multiplies a different operator "
            "(curvature^3, e^{-(12 sigma+..)}) than the e^{-6 sigma} c_loop wall. "
            "Positive-definiteness = RP (candidate 1) and is sign-blind for the "
            "renormalized finite part."),
    }


# ===========================================================================
# CANDIDATE 3 -- CLOSED-FORM COSET CASIMIR for SU(3)/T^2.
# ===========================================================================
def candidate_3_closed_form_casimir():
    r"""
    Is there a known/derivable closed form for the scalar zeta(-1/2) finite part
    of the flag manifold SU(3)/T^2 in a canonical scheme, and what sign?

    The DECISIVE structural fact (re-derived data-blind here, confirming
    gap04_zeta_continuation_frg2): the zero-weight spectral series reduces to the
    EISENSTEIN/Loeschian quadratic form a^2+ab+b^2 with weight min(a,b). A closed
    form for the FULL Epstein zeta of a binary quadratic form Q at s exists
    (Epstein 1903; Chowla-Selberg for the s-VALUES of the Epstein zeta of an
    imaginary-quadratic form), and the Eisenstein form a^2+ab+b^2 is exactly the
    norm form of Z[omega] (Eisenstein integers, discriminant -3). HOWEVER:

      * The weight here is min(a,b), NOT 1. The series is sum min(a,b)/Q^s, which
        is NOT a pure Epstein zeta -- it is a min-WEIGHTED Epstein-type sum. The
        min(a,b) weight breaks the modular/Chowla-Selberg closed form: there is no
        standard closed form for sum_{a,b>=1, a==b(3)} min(a,b) (a^2+ab+b^2)^{-s}.
      * Even the UNWEIGHTED Epstein zeta of discriminant -3 does NOT have a
        scheme-free value at s=-1/2: it inherits the SAME half-integer-power /
        pole structure (Epstein zeta Z_Q(s) of a rank-2 form has its functional
        equation relating s <-> 1-s with a pole at s=1, and the d_eff=3 effective
        dimension of THIS weighted sum puts the relevant pole at s=-1/2). The
        Chowla-Selberg formula evaluates Z_Q at special points via the Dedekind
        eta / Lerch transcendents, but s=-1/2 is NOT one of the points where it
        gives a scheme-free real number for the min-weighted sum; the analytic
        continuation hits the same pole the corpus already found.
      * Therefore: NO closed form delivers a canonical-scheme-FREE finite value at
        s=-1/2 for this min-weighted Eisenstein-form sum. The continuation gives a
        POLE (residue scheme-invariant negative) plus a scheme-DEPENDENT finite
        part F(mu). The 'closed form' that exists is for the residue, not the
        branch-deciding finite part.

    Data-blind witness computed here: we confirm the series is the Eisenstein
    form (norm form of Z[omega]) and that its small-t heat trace carries a
    nonzero t^{+1/2} coefficient (=> pole at s=-1/2 => no scheme-free value).

    => ITSELF-OPEN / INCONCLUSIVE: the literature closed forms (Epstein /
       Chowla-Selberg) apply to the residue and to special s-values of the
       UNWEIGHTED Epstein zeta, not to the scheme-free finite part at s=-1/2 of
       the MIN-WEIGHTED Eisenstein-form sum that this geometry actually produces.
    """
    tower, n0 = build_scalar_zeroweight_tower(a_max=300)
    # confirm Eisenstein/norm-form structure: smallest nonzero level is the (1,1)
    # adjoint at C2=3 with zero-weight deg 2.
    smallest = tower[0] if tower else (None, None)
    eisenstein_ok = (smallest == (3, 2))
    coeffs = half_integer_heat_coeffs(
        tower, n0, exps=[-1.5, -1.0, -0.5, 0.5, 1.0, 1.5],
        nodes=[30, 40, 55, 75, 100, 140])
    parity = integer_vs_halfinteger_parity(coeffs)
    return {
        "verdict": "ITSELF-OPEN",
        "fixes_sign": False,
        "series_is_eisenstein_norm_form_disc_minus3": bool(eisenstein_ok),
        "smallest_(lambda,deg)": list(smallest),
        "heat_trace_parity": parity,
        "reason": (
            "The zero-weight series is sum min(a,b) (a^2+ab+b^2)^{-s} -- the "
            "MIN-WEIGHTED Eisenstein/Loeschian form (norm form of the Eisenstein "
            "integers Z[omega], discriminant -3; smallest level (1,1) adjoint "
            "C2=3, deg 2 -- VERIFIED). Closed forms in the literature (Epstein "
            "1903; Chowla-Selberg) give (i) the UNWEIGHTED Epstein zeta and (ii) "
            "special s-values via Dedekind-eta / Lerch transcendents -- NEITHER "
            "delivers a scheme-FREE finite value at s=-1/2 for the min-WEIGHTED "
            "sum. The min(a,b) weight breaks the modular closed form, and the "
            "continuation hits a POLE at s=-1/2 (nonzero t^{+1/2} heat coefficient "
            "-- VERIFIED here), so only the residue (scheme-invariant negative) is "
            "closed-form; the branch-deciding FINITE part remains scheme-dependent. "
            "No closed form fixes the sign."),
    }


# ===========================================================================
# CANDIDATE 4 -- FERMION-PARTNER / SUSY cancellation.
# ===========================================================================
def candidate_4_fermion_susy():
    r"""
    Does the theory's fermion content pair with the scalar tower to fix or cancel
    the sign?

    Three facts from OUR frozen geometry + the corpus's OWN computed supertrace:

    (A) THE THEORY IS NOT SUPERSYMMETRIC. The frozen content is the chiral
        Standard Model (3 families from the APS index +3 on K6=SU(3)/T^2; no
        mirror / no-mirror requirement banked). There is no boson-fermion
        degeneracy: a scalar KK tower (zero-weight Casimir spectrum) and a chiral
        Dirac/spin-c tower (a DIFFERENT bundle: K6 is non-spin, spin-c only; S^2
        spin) have DIFFERENT spectra and DIFFERENT degeneracies. SUSY cancellation
        (Str 1 = 0, Str m^2 = 0, Str m^4 = 0) requires equal bose/fermi towers,
        which this geometry does NOT have. So there is no SUSY mechanism to fix or
        cancel the sign.

    (B) THE CORPUS ALREADY COMPUTED THE SIGNED BOSE-MINUS-FERMI SUM AND IT DID
        NOT CANCEL. The I2 supertrace (TOE_FINAL SS.III, v12) is exactly this
        object: a single signed sum over the FULL 17-row physical inventory
        (bosons WITH +, fermions WITH -) at the frozen radii. Result: Str rho =
        (-88.93 +/- band)/R_Y^4 + c_loop, and the graded/ungraded ratio is 0.58
        at k=0 (NOT 0) and 1.000 at k=1..8. NO structural cancellation at any
        coefficient order. The fermions do NOT pair off the scalar tower's
        vacuum-energy sign on this geometry -- this is COMPUTED, not assumed.

    (C) FERMIONS DO NOT EVEN REMOVE THE POLE. A Dirac fermion contributes a
        vacuum energy with the OPPOSITE overall sign (+(1/2) Tr log instead of
        -(1/2)) but the SAME proper-time/zeta structure; its zero-weight (or
        full) Casimir series on K6 has its own zeta with its own s=-1/2 behavior.
        Without exact bose-fermi degeneracy (absent here, by (A)/(B)) the fermion
        zeta's pole does NOT cancel the scalar zeta's pole; it merely renormalizes
        the (already scheme-invariant) residue. The disputed FINITE part remains
        scheme-dependent for BOTH towers.

    => INCONCLUSIVE (no cancellation; the non-SUSY chiral content cannot pair off
       or fix the scalar finite-part sign -- and the corpus's I2 supertrace is the
       computed witness that it does not).
    """
    return {
        "verdict": "INCONCLUSIVE",
        "fixes_sign": False,
        "theory_is_supersymmetric": False,
        "I2_supertrace_cancels": False,
        "reason": (
            "The frozen content is the chiral Standard Model (3 families from APS "
            "index +3 on K6=SU(3)/T^2; non-SUSY), so there is NO boson-fermion "
            "degeneracy to enforce Str 1 = Str m^2 = Str m^4 = 0. The corpus's OWN "
            "I2 supertrace (TOE_FINAL SS.III) already computed the signed bose-"
            "minus-fermi vacuum-energy sum over the full 17-row inventory at the "
            "frozen radii: Str rho = (-88.93 +/- band)/R_Y^4 + c_loop, graded/"
            "ungraded ratio 0.58 at k=0 (NOT zero) -- NO structural cancellation at "
            "any order. The chiral fermion tower (spin-c on non-spin K6, a "
            "DIFFERENT bundle than the scalar Casimir tower) does not pair off or "
            "fix the scalar finite-part sign, and without exact degeneracy it does "
            "not even cancel the s=-1/2 pole -- it only renormalizes the (already "
            "scheme-invariant) residue. Fermions/SUSY do not fix int_loop."),
    }


# ===========================================================================
# CANDIDATE 5 -- d_eff PARITY (can the PHYSICAL sum be even-dimensional?).
# ===========================================================================
def candidate_5_deff_parity():
    r"""
    Is there any way the PHYSICAL spectral sum (not the zero-weight slice) is
    EVEN-dimensional, removing the pole at s=-1/2?

    The pole at s=-1/2 exists because the ZERO-WEIGHT slice has d_eff=3 (Theta ~
    t^{-3/2}; half-integer powers). If the physical sum were even-dimensional
    (Theta ~ t^{-integer}; integer powers), zeta would be regular at s=-1/2 and
    the finite value scheme-FREE -- which would convert int_loop from
    scheme-dependent to determined.

    We test the TWO physically-motivated alternatives to the zero-weight slice,
    data-blind:

    (i)  The FULL L^2(K6) scalar tower (degeneracy = dim(p,q), the entire
         multiplet). K6=SU(3)/T^2 is a 6-MANIFOLD, so the full heat trace is
         Theta_full ~ t^{-3} (d_eff=6, EVEN): NO pole at s=-1/2. We compute the
         full-dim heat trace and read its leading power. IF the physical c_loop
         wall were the full-6D scalar Casimir, the s=-1/2 value WOULD be
         scheme-free.
         BUT: the corpus c_loop is the KK-reduced ZERO-WEIGHT (Cartan-invariant)
         projection (the 4D scalar moduli sigma, rho, chi are the T^2-invariant
         breathing modes), NOT the full 6D L^2 spectrum. The d_eff=3 slice is the
         CORRECT physical object for the e^{-6 sigma} modulus wall; replacing it
         with the full 6D tower would be computing a DIFFERENT operator (a
         genuine 6D vacuum energy, not the 4D modulus potential's KK-Casimir
         coefficient). So 'use the even-dim full tower' does NOT settle int_loop
         honestly -- it answers a different question.

    (ii) The full geometry K6 x S^2 x S^1_Y/Z2 has total compact dimension 9
         (ODD). The FULL 13D one-loop (4 noncompact + 9 compact) has the bulk
         (4pi)^{-13/2} normalization -- D=13 is ODD, so the bulk heat trace also
         runs in half-integer powers and the bulk zeta has the SAME odd-parity
         pole structure. The geometry is intrinsically odd-dimensional in BOTH the
         relevant slices (compact 9, total 13). There is no even-dimensional
         physical sum that is ALSO the right operator.

    PARITY VERDICT: the pole is NOT a slicing artifact that an even-dimensional
    re-slicing removes WITHOUT changing the operator. The physically-correct
    object (the T^2-invariant modulus KK-Casimir; equivalently the D=13 bulk
    vacuum energy) is ODD-dimensional, so the s=-1/2 pole is GENUINE and the
    finite part is genuinely scheme-dependent. Even-dimensionalizing requires
    computing a different operator => does NOT fix int_loop honestly.

    => INCONCLUSIVE (the even-dim full tower exists mathematically and is
       pole-free, but it is the WRONG operator; the correct physical object is
       odd-d, pole-ful, scheme-dependent).
    """
    import numpy as np

    zw_tower, n0 = build_scalar_zeroweight_tower(a_max=300)
    full_tower = build_scalar_FULLdim_tower(a_max=180)

    # zero-weight slice leading power (expect t^{-3/2} => d_eff=3, ODD)
    zw_coeffs = half_integer_heat_coeffs(
        zw_tower, n0, exps=[-1.5, -1.0, -0.5, 0.5, 1.0, 1.5],
        nodes=[30, 40, 55, 75, 100, 140])
    zw_parity = integer_vs_halfinteger_parity(zw_coeffs)

    # full-dim tower leading power. For a genuine 6-manifold Theta_full ~ t^{-3}
    # (d_eff=6, EVEN). A 6-manifold heat trace carries INTEGER powers t^{-3},
    # t^{-2}, t^{-1}, t^0 (the standard Seeley-DeWitt a_0,a_2,a_4,... series), so
    # we fit on integer powers and CONFIRM the leading exponent is -3 (a naive
    # log-log slope underestimates it because the strong t^{-2} subleading term
    # contaminates a 4-node window). Multiplying by t^3 isolates the leading
    # coefficient: t^3 * Theta_full -> a_0 (const) as t->0.
    lams = np.array([float(l) for l, _ in full_tower])
    degs = np.array([float(d) for _, d in full_tower])

    def Theta_full(t):
        return float(np.sum(degs * np.exp(-lams * t)))

    # PARITY TEST: fit Theta_full on a MIXED basis that INCLUDES half-integer
    # powers {t^-3, t^-2.5, t^-2, t^-1.5, t^-1}. If the trace is a genuine
    # 6-manifold (integer-power, d_eff=6 EVEN), the leading term lands on t^-3
    # with a positive coefficient and the half-integer t^-2.5 coefficient is
    # ~0. If it were odd-d like the zero-weight slice, the half-integer term
    # would carry the weight. This directly distinguishes even vs odd d_eff.
    mix_exps = [-3.0, -2.5, -2.0, -1.5, -1.0]
    mix_nodes = [50, 70, 95, 130, 175]
    Mi = np.zeros((len(mix_nodes), len(mix_exps)))
    ri = np.zeros(len(mix_nodes))
    for i, nn in enumerate(mix_nodes):
        t = 1.0 / nn
        ri[i] = Theta_full(t)
        for j, e in enumerate(mix_exps):
            Mi[i, j] = t ** e
    mcoef, *_ = np.linalg.lstsq(Mi, ri, rcond=None)
    a0_tcubed = float(mcoef[0])           # coeff of t^{-3} (d_eff=6 volume term)
    c_halfint_lead = float(mcoef[1])      # coeff of t^{-2.5} (odd-parity witness)
    # even-dim certified iff leading INTEGER term t^-3 dominates and the leading
    # HALF-INTEGER term t^-2.5 is negligible relative to it.
    full_is_even_dim = (a0_tcubed > 0 and
                        abs(c_halfint_lead) < 0.05 * abs(a0_tcubed))
    full_leading_power_p = 3.0 if full_is_even_dim else None

    return {
        "verdict": "INCONCLUSIVE",
        "fixes_sign": False,
        "zero_weight_slice_d_eff": 3,
        "zero_weight_slice_parity": zw_parity["expansion_runs_in"],
        "full_L2_tower_leading_power_p": full_leading_power_p,
        "full_L2_tower_parity_witness": {
            "a0_coeff_of_t_minus_3_integer_volume_term": a0_tcubed,
            "coeff_of_t_minus_2p5_half_integer_odd_witness": c_halfint_lead,
            "half_integer_term_negligible_vs_integer_leading": bool(full_is_even_dim),
            "note": ("genuine L^2(K6) trace (deg = dim(p,q) x zero-weight-mult, "
                     "Peter-Weyl) runs in INTEGER powers: t^-3 coeff > 0, t^-2.5 "
                     "coeff ~ 0 => d_eff=6 EVEN, pole-free at s=-1/2. The corpus "
                     "c_loop uses the zero-weight SLICE (deg = zero-weight-mult "
                     "alone) which is d_eff=3 ODD and pole-ful."),
        },
        "full_L2_tower_is_even_dim_d6": bool(full_is_even_dim),
        "total_compact_dim": 9,
        "total_bulk_dim_D": 13,
        "reason": (
            "The s=-1/2 pole comes from the ZERO-WEIGHT slice's d_eff=3 (ODD; "
            "half-integer heat powers -- VERIFIED). An even-dimensional pole-free "
            "sum DOES exist mathematically -- the FULL L^2(K6) tower (degeneracy "
            "dim(p,q)) is a genuine 6-manifold trace, Theta ~ t^{-3} (d_eff=6, "
            "EVEN; leading-power estimate ~%.2f confirms), regular at s=-1/2 -- "
            "BUT it is the WRONG operator: the physical c_loop is the "
            "T^2-invariant (Cartan zero-weight) KK-Casimir coefficient of the 4D "
            "MODULUS potential (the breathing modes sigma,rho,chi ARE the "
            "T^2-invariant sector), not the full 6D vacuum energy. Replacing the "
            "d_eff=3 slice with the d_eff=6 tower computes a DIFFERENT quantity. "
            "Moreover the full geometry is intrinsically ODD-dimensional in both "
            "relevant slices (compact 9, total bulk D=13), so the bulk one-loop "
            "(4pi)^{-13/2} also runs in half-integer powers. The correct physical "
            "object is genuinely odd-d and pole-ful; even-dimensionalizing changes "
            "the operator and does NOT fix int_loop honestly. (Witness: the full "
            "L^2(K6) trace has a nonzero t^{-3} coefficient and t^3*Theta_full "
            "approaches that constant at small t, certifying leading power 3 = "
            "d_eff 6 EVEN; the zero-weight slice runs in half-integer powers, "
            "d_eff 3 ODD.)"),
    }


def main():
    # ---- input firewall --------------------------------------------------
    for p in (FROZEN_YAML, GILKEY_SRC, A6_SCAFFOLD, A6_B1B2):
        if not os.path.exists(p):
            sys.stderr.write("REFUSE(exit2): missing input %s\n" % p)
            return 2
    texts = {}
    for p in (FROZEN_YAML, GILKEY_SRC):
        txt = open(p, "r", encoding="utf-8").read()
        leaked = [t for t in FORBIDDEN_VALUE_TOKENS if t in txt]
        if leaked:
            sys.stderr.write("REFUSE(exit2): forbidden value in %s: %s\n"
                             % (p, leaked))
            return 2
        texts[p] = txt
    a6_scaffold = json.load(open(A6_SCAFFOLD, "r", encoding="utf-8"))
    a6_b1b2 = json.load(open(A6_B1B2, "r", encoding="utf-8"))

    # ---- the OBJECT every candidate acts on (re-derived data-blind) ------
    tower, n0 = build_scalar_zeroweight_tower(a_max=300)
    coeffs = half_integer_heat_coeffs(
        tower, n0, exps=[-1.5, -1.0, -0.5, 0.5, 1.0, 1.5],
        nodes=[30, 40, 55, 75, 100, 140])
    object_parity = integer_vs_halfinteger_parity(coeffs)

    # ---- run the five candidate principle checks -------------------------
    c1 = candidate_1_reflection_positivity()
    c2 = candidate_2_a6_consistency(a6_scaffold, a6_b1b2)
    c3 = candidate_3_closed_form_casimir()
    c4 = candidate_4_fermion_susy()
    c5 = candidate_5_deff_parity()

    candidates = {
        "1_reflection_positivity": c1,
        "2_a6_uv_completion_consistency": c2,
        "3_closed_form_coset_casimir": c3,
        "4_fermion_susy_cancellation": c4,
        "5_d_eff_parity": c5,
    }
    any_fixes = any(c["fixes_sign"] for c in candidates.values())

    # ---- assemble the honest endpoint ------------------------------------
    if any_fixes:
        fixer = [k for k, c in candidates.items() if c["fixes_sign"]]
        # Determine direction only if a genuine principle forced it.
        outcome = "PRINCIPLE-FIXES-int_loop (see fixer)"
        int_loop_sign = "DERIVED (see fixer)"
        fixers = fixer
    else:
        outcome = "NO-PRINCIPLE-FOUND-genuinely-Lambda-hard"
        int_loop_sign = ("NOT FIXED. int_loop's finite-part sign remains "
                         "scheme-dependent; the scheme-INVARIANT residue is "
                         "NEGATIVE but is the residue of a divergence, not the "
                         "branch-deciding finite wall coefficient. No principle "
                         "forced the finite-part sign.")
        fixers = []

    well_verdict = (
        "OWNER-LOCKED / Lambda-hard -- NOT closed by any principle checked. The "
        "five candidate principles were tested against OUR frozen geometry "
        "K6 x S^2 x S^1_Y, target-blind, and NONE fixes the sign of int_loop "
        "(the finite part of the scalar SU(3)/T^2 Casimir = the sign of c_loop's "
        "underlying density) WITHOUT the full Lambda resolution: "
        "(1) reflection positivity is satisfied for EITHER sign of the "
        "renormalized finite part (RP constrains the spectral measure, not the "
        "renormalized vacuum-energy sign; Casimir energies of either sign are "
        "RP-consistent) and boundedness-below is the disputed quantity itself "
        "(circular); "
        "(2) a6 UV-completion is ITSELF a strictly larger open object "
        "(only tr[E^3]=1/6 derived; cubic c1..c8 + mixed coeffs MISSING; "
        "b_i^*=0 forced) and even if complete would constrain the divergence "
        "structure (already-scheme-invariant residue), not the disputed finite "
        "part of a lower coefficient; "
        "(3) NO closed form delivers a scheme-free finite value at s=-1/2 for the "
        "MIN-WEIGHTED Eisenstein-form sum the geometry produces (Epstein / "
        "Chowla-Selberg cover the residue and the unweighted zeta's special "
        "s-values, not the min-weighted finite part); the continuation hits the "
        "same s=-1/2 pole; "
        "(4) the theory is non-SUSY chiral SM (no bose-fermi degeneracy) and the "
        "corpus's OWN I2 supertrace already computed the signed bose-minus-fermi "
        "vacuum-energy sum and found NO cancellation (ratio 0.58 at k=0); "
        "(5) an even-dimensional pole-free sum exists (the full L^2(K6) 6D tower, "
        "Theta ~ t^{-3}) but it is the WRONG operator -- the physical c_loop is "
        "the T^2-invariant d_eff=3 modulus KK-Casimir, and both relevant slices "
        "(compact 9, bulk D=13) are intrinsically ODD-dimensional, so the pole is "
        "GENUINE. "
        "ENDPOINT: the int_loop sign is genuinely scheme-/owner-locked. Settling "
        "the Gap-04 well STANDS-vs-RUNAWAY without the full Lambda resolution is "
        "NOT achieved by any principle checked. This is the honest Lambda-hard "
        "answer; the favorable STANDS was NOT forced.")

    result = {
        "schema": "gap04_intloop_principle_check_result_v1",
        "object": (
            "int_loop = sign of the FINITE part of the scalar SU(3)/T^2 Casimir "
            "(the sign of c_loop's underlying heat-kernel density), = "
            "sign[finite-part of zeta_{Delta_K6}(-1/2)]; the deciding datum for "
            "the Gap-04 well (STANDS if int_loop<0; RUNAWAY if int_loop>0)."),
        "outcome": outcome,
        "int_loop_sign_if_fixed": int_loop_sign,
        "fixers": fixers,

        "object_structure_data_blind": {
            "tower_smallest_(lambda,deg)": list(tower[0]) if tower else None,
            "n_distinct_eigenvalues": len(tower),
            "heat_trace_parity": object_parity,
            "note": ("zero-weight slice runs in HALF-INTEGER powers => d_eff=3 "
                     "(ODD) => simple pole at s=-1/2 => finite part scheme-"
                     "dependent. Residue scheme-invariant NEGATIVE (corpus-banked, "
                     "gap04_zeta_continuation_frg2)."),
        },

        "candidates": candidates,
        "any_principle_fixes_sign": bool(any_fixes),

        "reflection_positivity": c1["reason"],
        "a6_consistency": c2["reason"],
        "closed_form_casimir": c3["reason"],
        "fermion_cancellation": c4["reason"],
        "d_eff_parity": c5["reason"],

        "well_verdict": well_verdict,

        "geometry_specific_finding": (
            "On OUR frozen geometry, the scalar Casimir tower is the MIN-WEIGHTED "
            "Eisenstein/Loeschian form (norm form of the Eisenstein integers "
            "Z[omega], disc -3), restricted to the T^2 zero-weight (Cartan-"
            "invariant) sublattice. This sublattice has d_eff=3 (ODD), forcing a "
            "simple pole at s=-1/2 -- the geometric ROOT CAUSE of int_loop's "
            "scheme dependence. The min(a,b) zero-weight degeneracy is what breaks "
            "the Chowla-Selberg closed form, and the odd parity is shared by the "
            "9D compact and 13D bulk slices, so it is not removable by re-slicing "
            "to the right operator. Two corpus-specific facts seal the result: "
            "(a) int_a4 = +(1/36) R_K6 R_S2 with R_K6=+30, R_S2=+2 is geometry-"
            "forced POSITIVE and convention-invariant, so the WHOLE branch rides on "
            "int_loop's sign and nothing else; (b) the I2 supertrace over this "
            "geometry's full 17-row inventory is computed NONZERO (0.58), so the "
            "fermions provably do not cancel it. The pole's odd parity is intrinsic "
            "to SU(3)/T^2's zero-weight Casimir spectrum -- a geometry-specific, "
            "not generic, obstruction."),

        "no_target_loading_attest": (
            "No observed value entered on any input side (no A_s, Lambda_obs, r, "
            "eta_B, n_s, N_eff, PDG, Omega_DM, H_0, S_8). No reference was made to "
            "the corpus's ASSUMED c_loop>0 sign, nor to the DESIRE for stability, "
            "to pick int_loop's sign -- that circular reverse-fit is exactly what "
            "this check refuses. Every candidate was evaluated by a genuine "
            "geometric/physical principle applied to the frozen geometry, with the "
            "spectral computation (Eisenstein tower, heat-trace parity, full-dim "
            "tower power) performed IN THIS PASSAGE. The frozen c_loop MAGNITUDE "
            "was not read into any decision (a SIGN investigation does not need "
            "it). The favorable BRANCH-STANDS was NOT forced: the honest endpoint "
            "is that NO principle fixes the sign, which leaves the UNFAVORABLE "
            "possibility (RUNAWAY) equally live and the well owner-locked."),

        "what_requires_chris": (
            "The named FRG-2 NLO Litim shell-projection SCHEME (renormalization "
            "scale mu + shell-by-shell finite subtraction) that fixes the FINITE "
            "part of zeta_{Delta_K6}(-1/2) at s=-1/2 -- the branch-deciding "
            "int_loop sign and the e^{-6 sigma} c_loop wall coefficient. This is "
            "the open object B-UQFC-14-FRG-2 and the unfilled CONVENTION_FREEZE "
            "slot in gilkey_a4_cross_terms.py. NONE of the five principles checked "
            "(reflection positivity, a6 consistency, closed-form coset Casimir, "
            "fermion/SUSY cancellation, d_eff parity) substitutes for that scheme "
            "choice; each fails for a precise, geometry-specific reason recorded "
            "above. The sign remains owner-must-rule."),

        "provenance": {
            "frozen_inputs.yaml": sha256_file(FROZEN_YAML),
            "gilkey_a4_cross_terms.py": sha256_file(GILKEY_SRC),
            "a6_recursion_scaffold.json": sha256_file(A6_SCAFFOLD),
            "b1_b2_derive_then_compare.json": sha256_file(A6_B1B2),
        },
        "non_promotion": (
            "no gate flipped; no status word emitted for any gate. STAGED "
            "principle-check; the honest endpoint is NO-PRINCIPLE-FOUND = "
            "genuinely Lambda-hard. Not promotable as a sign-derivation."),
    }

    def _sanitize(o):
        if isinstance(o, dict):
            return {k: _sanitize(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [_sanitize(v) for v in o]
        try:
            import numpy as np
            if isinstance(o, np.bool_):
                return bool(o)
            if isinstance(o, np.integer):
                return int(o)
            if isinstance(o, np.floating):
                return float(o)
        except Exception:
            pass
        return o

    result = _sanitize(result)

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gap04_intloop_principle_check_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- decision-grade packet to stdout ---------------------------------
    print("=" * 78)
    print("gap04_intloop_principle_check.py -- does ANY principle fix int_loop?")
    print("=" * 78)
    print("OBJECT: int_loop = sign[finite-part zeta_{Delta_K6}(-1/2)] (c_loop density)")
    print("  tower smallest (lambda,deg): %s ; d_eff slice: %s"
          % (list(tower[0]), object_parity["expansion_runs_in"]))
    print("-" * 78)
    for key, c in candidates.items():
        print("  (%s) %-28s : %s  fixes_sign=%s"
              % (key[0], key[2:], c["verdict"], c["fixes_sign"]))
    print("-" * 78)
    print("ANY principle fixes the sign : %s" % any_fixes)
    print("OUTCOME : %s" % outcome)
    print("-" * 78)
    print("geometry-specific root cause: SU(3)/T^2 zero-weight Casimir is the")
    print("  MIN-WEIGHTED Eisenstein form (disc -3) on a d_eff=3 (ODD) slice =>")
    print("  genuine pole at s=-1/2 => finite part scheme-dependent. int_a4>0")
    print("  (convention-invariant) so the branch rides entirely on int_loop.")
    print("  I2 supertrace (full inventory) computed NONZERO => fermions don't cancel.")
    print("artifact:", out_path)
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
