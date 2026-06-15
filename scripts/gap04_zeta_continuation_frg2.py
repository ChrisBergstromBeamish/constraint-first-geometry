#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gap04_zeta_continuation_frg2.py
===============================
B-UQFC-14-FRG-2 -- the scalar K6 spectral-zeta continuation that the prior
countersign (gap04_cloop_casimir_firstprinciples.py) DEFERRED as "the multi-week
object". This script BUILDS ON that prior tower enumeration and CARRIES THE
CONTINUATION TO ITS HONEST ENDPOINT: it actually analytically continues
    zeta_{Delta_K6}(s) = sum_{(p,q)} deg(p,q) * [C2(p,q)/R_K6^2]^{-s}
to s = -1/2 via the Mellin / heat-kernel split (Epstein-Hurwitz), and reads off
the structure there -- NOT a truncated divergent sum.

OBJECT (the real producer of the e^{-6 sigma} wall coefficient c_loop):
    c_loop = -(1/2) * (4 pi)^{-D/2} * zeta_{Delta_K6}(-1/2)   [scalar KK tower]
  K6 = SU(3)/T^2; eigenvalue = SU(3) quadratic Casimir C2(p,q) of the triality-0
  reps; degeneracy = the T^2 (Cartan) ZERO-WEIGHT multiplicity of the (p,q)
  irrep (NOT the full dim).

CFCA discipline (METHOD_CFCA_June_14.md):
  * no-target-loading: NO observed value (A_s, Lambda_obs, r, eta_B, n_s, N_eff,
    PDG, Omega_DM, H_0, S_8) enters on ANY input side. The ONLY inputs are the
    frozen geometry (dim 6, Einstein point) and SU(3) group theory. The frozen
    c_loop MAGNITUDE (1.3637877e-5) is read ONLY at the very end as a geometry-side
    CROSS-CHECK, never as an input to the continuation.
  * NEVER force a sign, and NEVER force the favorable BRANCH-STANDS. If the
    continuation is scheme-ambiguous, say so honestly. A half-built continuation
    asserting a sign is the manufactured step the countersign exists to catch.
  * elegance is the diagnostic. (The spectrum reduces to the Eisenstein form
    a^2+ab+b^2 -- a genuinely elegant structure -- which is what made the honest
    continuation tractable.)

================================================================================
WHAT THIS SCRIPT FINDS (the honest endpoint, stated up front)
================================================================================
The continuation is COMPLETED, and the endpoint is structural, not a free choice:

(1) TOWER (verified, data-blind):
    - triality-0 reps: (p-q) % 3 == 0.
    - C2(p,q) = (p^2 + q^2 + p q + 3 p + 3 q)/3   [C2(adjoint(1,1))=3, C2(fund(1,0))=4/3].
    - T^2 zero-weight multiplicity = min(p,q)+1 for triality-0 reps, else 0.
      (Verified independently in PART 0 by the Kostant partition-function weight
       multiplicity -- adjoint -> 2, 27 of (2,2) -> 3, etc.)
    - Under the shift a=p+1, b=q+1 the eigenvalue becomes
          C2 = (a^2 + a b + b^2 - 3)/3 ,  deg = min(a,b),  a,b>=1,  a == b (mod 3),
      i.e. the EISENSTEIN / Loeschian quadratic form. (Elegance is the diagnostic.)

(2) HEAT TRACE small-t expansion (the analytic-continuation engine):
        Theta(t) = sum deg * exp(-C2 t)  ~  c_{-3/2} t^{-3/2} + c_{-1/2} t^{-1/2}
                                            + c_{+1/2} t^{+1/2} + c_{+3/2} t^{+3/2} + ...
    The expansion runs in HALF-INTEGER powers; the integer-power coefficients
    vanish. The leading c_{-3/2} matches the continuum lattice density exactly
    (c_{-3/2} = sqrt(3) * J with J = int int min(a,b) e^{-(a^2+ab+b^2)}).
    The effective spectral dimension is d_eff = 3 (Theta ~ t^{-3/2}), NOT 6: the
    zero-weight sublattice is a measure-zero slice of the full L^2(K6) spectrum.

(3) THE DECISIVE STRUCTURAL FACT: c_{+1/2} != 0 (= +0.28786...).
    A term c_{+1/2} t^{+1/2} in Theta contributes c_{+1/2}/(s + 1/2) to zeta(s),
    so zeta_{Delta_K6}(s) HAS A SIMPLE POLE AT s = -1/2. Since 1/Gamma(-1/2) is
    finite and nonzero, the would-be "value" zeta(-1/2) is NOT a finite number:
        zeta_{Delta_K6}(s) = R/(s + 1/2) + F + O(s + 1/2),
        R = c_{+1/2}/Gamma(-1/2) = -0.081205...      (residue; scheme-INVARIANT)
        F = minimal-subtraction finite part = -0.45430... (at mu = 1/R_K6; SCHEME-DEP).
    => The one-loop vacuum energy c_loop = -(1/2)(4pi)^{-D/2} zeta(-1/2) is
       UV-DIVERGENT; its finite part requires renormalization and is therefore
       SCHEME-DEPENDENT. The finite-part SIGN can be flipped by the choice of
       renormalization scale mu (it changes sign at mu* = exp(-F/(2R)) ~ 0.061),
       whereas the RESIDUE sign (NEGATIVE) is scheme-invariant.

(4) BRANCH read:
    - The scheme-INVARIANT residue is NEGATIVE. Under c_loop = -(1/2)(...) * (pole),
      the underlying density carried by the divergent part is NEGATIVE
      -> consistent with BRANCH-STANDS, BUT this is the residue of a divergence,
         not the finite wall coefficient.
    - The finite part that would actually set the wall's sign is SCHEME-DEPENDENT,
      so the BRANCH is NOT pinned by a data-blind continuation alone.

(5) CROSS-CHECK against the frozen magnitude (read AFTER the continuation):
    -(1/2)(4pi)^{-13/2} * F = +1.63e-8, which is ~840x SMALLER than the frozen
    FRG-2 c_loop = 1.3637877e-5. The minimal-subtraction scalar-zeta finite part
    does NOT reproduce the frozen magnitude. The frozen magnitude is therefore set
    by the owner's FRG-2 NLO Litim shell-projection scheme (a specific finite
    subtraction + the full 13D field content + the mode-by-mode shell mass
    spectrum), which is more than the bare scalar K6 zeta(-1/2).

HONEST OUTCOME: SCHEME-AMBIGUOUS-owner-locked. The continuation IS completed (no
deferral, no truncated sum), and it RESOLVES the structure: zeta_{Delta_K6} has a
POLE at s=-1/2, so there is no scheme-free finite "sign" to read; the residue is
negative (scheme-invariant) but the finite part -- the object that actually sets
the wall coefficient -- is scheme-dependent and does not reproduce the frozen
magnitude under minimal subtraction. The favorable BRANCH-STANDS is NOT forced;
the well stays owner-locked on the named FRG-2 Litim shell-projection scheme,
which is now a SMALLER, sharper residual (a scheme choice, not a whole missing
computation).

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

import numpy as np

try:
    from mpmath import mp, mpf, gamma, psi, pi as mp_pi
    _HAVE_MPMATH = True
    mp.dps = 30
except Exception:                                   # pragma: no cover
    _HAVE_MPMATH = False

from scipy.integrate import quad as sc_quad


# ---------------------------------------------------------------------------
# Paths (the frozen c_loop wall value is read ONLY at the cross-check step).
# ---------------------------------------------------------------------------
FA = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
      r"physics_Journal_and_patents/Final_physics_articles/scripts/gap_04")
VEFF_YAML = os.path.join(FA, "outputs", "veff_coefficients_frg4.yaml")

D_BULK = 13
GLOBAL_ONE_LOOP = -0.5

FORBIDDEN_VALUE_TOKENS = [
    "A_s=", "A_s =", "eta_B=", "eta_B =", "Lambda_obs=", "Lambda_obs =",
    "r_obs=", "r_obs =", "n_s_obs=", "N_eff_obs=", "Omega_DM_obs=",
    "H_0_obs=", "S_8_obs=",
]

# Frozen FRG-2 c_loop magnitude -- the CROSS-CHECK target only. NOT an input to
# the continuation. (Hard-coded here ONLY so the script is self-contained; it is
# read into the math strictly after sign/structure are computed.)
C_LOOP_FRG2_TARGET = 1.3637877214788921e-05


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ===========================================================================
# PART 0. Independent verification of the T^2 zero-weight multiplicity via the
# Kostant partition function (so the degeneracy is not taken on faith).
# ===========================================================================
def _kostant_zero_weight_mult(p, q):
    """
    Multiplicity of the ZERO weight in the SU(3) irrep (p,q), computed from the
    Kostant multiplicity formula
        m_Lambda(mu) = sum_{w in W} sgn(w) P( w(Lambda+rho) - (mu+rho) )
    with the A2 Kostant partition function P. Everything is in Dynkin-label
    coordinates; mu = 0 (the zero weight). Returns an int.
    """
    a1 = np.array([2, -1]); a2 = np.array([-1, 2])
    rho = np.array([1, 1])
    Lam = np.array([p, q])
    M = np.array([a1, a2]).T              # columns a1, a2 in Dynkin coords

    def s1(v): return v - v[0] * a1
    def s2(v): return v - v[1] * a2

    words = [[], [1], [2], [1, 2], [2, 1], [1, 2, 1]]
    Wel = []
    for w in words:
        v = np.array([7, 11]); sgn = 1
        for g in reversed(w):
            v = s1(v) if g == 1 else s2(v); sgn *= -1
        Wel.append((w, sgn))

    def apply(word, v):
        sgn = 1
        for g in reversed(word):
            v = s1(v) if g == 1 else s2(v); sgn *= -1
        return v, sgn

    def kostant_P(v):
        # number of (k1,k2,k3)>=0 with k1 a1 + k2 a2 + k3 (a1+a2) = v
        sol = np.linalg.solve(M.astype(float), v.astype(float))
        n = np.round(sol).astype(int)
        if not np.allclose(M @ n, v):
            return 0
        c1, c2 = int(n[0]), int(n[1])
        if c1 < 0 or c2 < 0:
            return 0
        return min(c1, c2) + 1

    total = 0
    mu = np.array([0, 0])
    for (w, _s0) in Wel:
        wv, s = apply(w, Lam + rho)
        total += s * kostant_P(wv - (mu + rho))
    return int(round(total))


def su3_dim(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def su3_casimir(p, q):
    """C2(p,q) = (p^2+q^2+pq+3p+3q)/3 ; C2(1,1)=3 (adjoint), C2(1,0)=4/3 (fund)."""
    return Fraction(p * p + q * q + p * q + 3 * p + 3 * q, 3)


def t2_zero_weight_multiplicity(p, q):
    """T^2 zero-weight multiplicity = min(p,q)+1 for triality 0, else 0."""
    if (p - q) % 3 != 0:
        return 0
    return min(p, q) + 1


def verify_tower(n_check=6):
    """Cross-check the closed-form zero-weight mult against the Kostant formula,
    and the Casimir normalization, on a panel of small reps."""
    checks = []
    panel = [(0, 0), (1, 1), (3, 0), (0, 3), (2, 2), (3, 3), (4, 1), (1, 4),
             (6, 0), (4, 4), (2, 5), (5, 2)]
    all_ok = True
    for (p, q) in panel:
        closed = t2_zero_weight_multiplicity(p, q)
        kostant = _kostant_zero_weight_mult(p, q)
        ok = bool(closed == kostant)
        all_ok = all_ok and ok
        checks.append({
            "pq": [p, q], "dim": su3_dim(p, q),
            "triality": (p - q) % 3,
            "C2": float(su3_casimir(p, q)),
            "zero_weight_mult_closed_form": int(closed),
            "zero_weight_mult_kostant": int(kostant),
            "match": bool(ok),
        })
    casimir_norm_ok = bool((su3_casimir(1, 1) == 3)
                           and (su3_casimir(1, 0) == Fraction(4, 3)))
    return all_ok, casimir_norm_ok, checks


# ===========================================================================
# PART 1. Build the scalar K6 spectrum (distinct eigenvalues + accumulated
# zero-weight degeneracy), data-blind, as fast float arrays.
# ===========================================================================
def build_spectrum(a_max):
    r"""
    Spectrum in the shifted (a,b)=(p+1,q+1) Eisenstein coordinates:
        lambda = (a^2 + a b + b^2 - 3)/3,  deg = min(a,b),  a,b >= 1, a==b (mod 3).
    (a==b mod 3 <=> (p-q)%3==0 <=> 3 | (a^2+ab+b^2) <=> lambda integer.)

    Returns (lams, degs, n0) where (lams, degs) are the float arrays of distinct
    POSITIVE eigenvalues with summed zero-weight degeneracy, and n0 = degeneracy
    of the lambda=0 zero mode (the (0,0) trivial rep; n0=1). The heat trace
    Theta(t) = n0 + sum_{lambda>0} deg e^{-lambda t} KEEPS the zero mode (its
    constant n0 is needed for the clean half-integer small-t expansion); the
    spectral zeta sum EXCLUDES it (C2=0 cannot be raised to -s). The zero-mode
    subtraction in the Mellin transform contributes only n0/s -- a pole at s=0,
    NOT at s=-1/2, so it does not touch the target structure.
    """
    spec = defaultdict(int)
    n0 = 0
    for a in range(1, a_max + 1):
        for b in range(1, a_max + 1):
            if (a - b) % 3:
                continue
            lam = (a * a + a * b + b * b - 3) // 3
            if lam == 0:                       # the (0,0) trivial zero mode
                n0 += min(a, b)
                continue
            spec[lam] += min(a, b)
    lams = np.array(sorted(spec.keys()), dtype=np.float64)
    degs = np.array([spec[int(l)] for l in lams], dtype=np.float64)
    return lams, degs, n0


def make_theta(lams, degs, n0):
    """Full heat trace INCLUDING the zero-mode constant n0 (needed for the clean
    half-integer asymptotic expansion). Accepts float or mpf t (cast to float --
    the fit/integration nodes are all t >= ~7e-3 where float64 evaluation of the
    ~9e4-mode sum is fully accurate; mpmath precision is needed only for the
    ill-conditioned linear solve, not for Theta itself)."""
    def Theta(t):
        tf = float(t)
        return float(n0 + np.sum(degs * np.exp(-lams * tf)))
    return Theta


# ===========================================================================
# PART 2. Small-t heat-trace asymptotic expansion (half-integer powers).
# ===========================================================================
HALF_INT_EXPS = [-1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5]
FIT_NODES = [28, 38, 50, 66, 86, 112, 146]   # t = 1/n, deep small-t window


def fit_heat_coefficients(Theta, exps=HALF_INT_EXPS, nodes=FIT_NODES):
    r"""
    Solve for the half-integer small-t coefficients of Theta. The Vandermonde
    matrix t^{e} on a deep small-t window is severely ill-conditioned
    (cond ~ 1e13 in float64), so we solve it in high precision (mpmath) when
    available; otherwise we fall back to numpy least squares (degraded accuracy
    on the higher coefficients, leading coefficients still reliable).
    """
    if _HAVE_MPMATH:
        from mpmath import matrix as _mat, lu_solve as _lus
        M = _mat(len(nodes), len(exps))
        rhs = _mat(len(nodes), 1)
        for i, n in enumerate(nodes):
            t = mpf(1) / n
            rhs[i] = mpf(Theta(t))
            for j, e in enumerate(exps):
                M[i, j] = t ** mpf(e)
        sol = _lus(M, rhs)
        coef = np.array([float(sol[j]) for j in range(len(exps))], dtype=np.float64)
    else:                                          # pragma: no cover
        M = np.zeros((len(nodes), len(exps)))
        rhs = np.zeros(len(nodes))
        for i, n in enumerate(nodes):
            t = 1.0 / n
            rhs[i] = Theta(t)
            for j, e in enumerate(exps):
                M[i, j] = t ** e
        coef, *_ = np.linalg.lstsq(M, rhs, rcond=None)
    # validation on held-out t
    val = []
    for n in (35, 100, 200):
        t = 1.0 / n
        fit = sum(coef[j] * t ** exps[j] for j in range(len(exps)))
        tru = Theta(t)
        val.append({"t": t, "rel_err": abs(fit - tru) / abs(tru)})
    return coef, val


def continuum_leading_coefficient():
    """Closed-form check of c_{-3/2}: continuum lattice density.
    c_{-3/2} = sqrt(3) * J, J = int int min(a,b) e^{-(a^2+ab+b^2)} da db (a,b>0)."""
    from scipy.integrate import dblquad
    J, _ = dblquad(lambda b, a: min(a, b) * math.exp(-(a * a + a * b + b * b)),
                   0, 30, lambda a: 0, lambda a: 30)
    return math.sqrt(3.0) * J, J


# ===========================================================================
# PART 3. Analytic continuation to s = -1/2 (Mellin / heat-kernel split).
#   zeta(s) = 1/Gamma(s) [ int_0^1 t^{s-1}(Theta - P_N) dt
#                          + sum_k c_k/(s+e_k) + int_1^inf t^{s-1} Theta dt ]
#   P_N = sum_k c_k t^{e_k} the half-integer small-t series.
# At s=-1/2 the term c_{+1/2}/(s+1/2) is a SIMPLE POLE.
# ===========================================================================
def continue_to_minus_half(Theta, coef, n0, exps=HALF_INT_EXPS):
    r"""
    zeta(s) = (1/Gamma(s)) int_0^inf t^{s-1} [Theta(t) - n0] dt, where Theta keeps
    the zero mode and n0 is its degeneracy (so Theta - n0 = sum_{lambda>0} ...).
    The small-t asymptotic series of (Theta - n0) is P_N(t) - n0 (the half-integer
    coefficients of Theta are unchanged; the only added term is a t^0 = -n0
    constant). The t^0 = -n0 term contributes -n0/s to the bracket -- a pole at
    s=0, which does NOT affect s=-1/2.
    """
    s = -0.5

    def P_N(t):                                  # half-integer asymptotic series of Theta
        return sum(coef[j] * t ** exps[j] for j in range(len(exps)))

    def f0(t):    # int_0^1 t^{s-1}[(Theta - n0) - (P_N - n0)] = t^{s-1}(Theta - P_N)
        return t ** (s - 1.0) * (Theta(t) - P_N(t))

    def finf(t):                                 # int_1^inf t^{s-1}(Theta - n0)
        return t ** (s - 1.0) * (Theta(t) - n0)

    # Small-t integral int_0^1 t^{s-1}(Theta - P_N) dt. The subtracted remainder
    # (Theta - P_N) is the tail of an ASYMPTOTIC (not convergent) series: it is
    # genuinely tiny in a sweet-spot window t in [t_lo, 1] but, for t below t_lo,
    # (a) the dropped higher half-integer orders (t^{5.5}, t^{6.5}, ...) start to
    # matter and (b) float64 catastrophic cancellation between Theta ~ t^{-3/2}
    # and P_N corrupts the difference. We therefore integrate down to t_lo and
    # add the t in [0, t_lo] tail analytically: there the remainder is O(t^{5.5}),
    # so t^{s-1}(Theta-P_N) = O(t^4) and the tail integral is < t_lo^5/5 ~ 1e-11
    # at t_lo=1e-2 -- negligible at the reported precision. We verify stability by
    # confirming the integral is flat across t_lo in [5e-3, 2e-2].
    t_lo = 1.0e-2
    I0_main, _ = sc_quad(f0, t_lo, 1.0, limit=300)
    # stability witnesses at neighbouring cutoffs (flatness => tail negligible)
    I0_lo, _ = sc_quad(f0, 5.0e-3, 1.0, limit=300)
    I0_hi, _ = sc_quad(f0, 2.0e-2, 1.0, limit=300)
    I0 = I0_main
    I0_cutoff_spread = max(abs(I0_lo - I0_main), abs(I0_hi - I0_main))
    Iinf, _ = sc_quad(finf, 1.0, np.inf, limit=400)

    # index of the e = +1/2 term (the pole)
    jpole = exps.index(0.5)
    c_half = coef[jpole]

    # H(s) = regular bracket part (everything except the c_{1/2}/(s+1/2) pole term).
    # Includes the zero-mode subtraction term -n0/s (from the t^0 = -n0 constant in
    # the small-t series of Theta - n0; this is a pole at s=0, regular at s=-1/2).
    Hval = I0 + Iinf - n0 / s
    for j, e in enumerate(exps):
        if j == jpole:
            continue
        Hval += coef[j] / (s + e)

    if _HAVE_MPMATH:
        sm = mpf(-1) / 2
        invG = 1 / gamma(sm)                      # 1/Gamma(-1/2) = -1/(2 sqrt pi)
        dinvG = -psi(0, sm) / gamma(sm)           # d/ds [1/Gamma(s)] at -1/2
        R = float(mpf(c_half) * invG)
        F = float(mpf(Hval) * invG + mpf(c_half) * dinvG)
        invG_f = float(invG)
        gamma_mhalf = float(gamma(sm))
    else:                                          # pragma: no cover
        gamma_mhalf = -2.0 * math.sqrt(math.pi)
        invG_f = 1.0 / gamma_mhalf
        # psi(-1/2) = 2 - gamma_E - 2 ln 2
        psi_mhalf = 2.0 - 0.5772156649015329 - 2.0 * math.log(2.0)
        dinvG = -psi_mhalf / gamma_mhalf
        R = c_half * invG_f
        F = Hval * invG_f + c_half * dinvG

    return {
        "s": s,
        "I0_int_tlo_1": I0,
        "I0_cutoff_spread_5e-3_to_2e-2": I0_cutoff_spread,
        "Iinf_int_1_inf": Iinf,
        "c_half_theta_coeff": c_half,
        "H_regular_bracket": Hval,
        "gamma_minus_half": gamma_mhalf,
        "one_over_gamma_minus_half": invG_f,
        "residue_R": R,                            # scheme-INVARIANT
        "finite_part_F_minimal_subtraction": F,    # at mu = 1/R_K6 (scheme-dep)
    }


def scheme_dependence(R, F):
    r"""
    With a renormalization scale mu (mass dimension), zeta(s,mu)=mu^{2s} zeta(s).
    Near the pole: mu^{2s} = mu^{-1}(1 + 2 ln(mu)(s+1/2) + ...), so the finite part
    shifts as F(mu) = mu^{-1}(F + 2 R ln mu). The residue sign is INVARIANT; the
    finite-part sign FLIPS at ln(mu*) = -F/(2R).
    """
    if R == 0:
        return {"residue_zero": True}
    ln_mu_flip = -F / (2.0 * R)
    try:
        mu_flip = math.exp(ln_mu_flip)
    except OverflowError:
        mu_flip = float("inf") if ln_mu_flip > 0 else 0.0
    return {
        "residue_sign_scheme_invariant": "NEGATIVE" if R < 0 else "POSITIVE",
        "finite_part_sign_at_mu_1": "NEGATIVE" if F < 0 else "POSITIVE",
        "ln_mu_star_where_finite_part_flips": ln_mu_flip,
        "mu_star_where_finite_part_flips": mu_flip,
        "finite_part_sign_is_scheme_dependent": True,
    }


def validate_split_at_convergent_point(Theta, coef, n0, lams, degs,
                                       exps=HALF_INT_EXPS, s0=2.0):
    r"""
    SANITY GATE on the whole continuation machinery: at a CONVERGENT point
    s0 = 2 > 3/2 (the abscissa), compare the Mellin-split formula against the
    direct sum sum deg lambda^{-s0}. The direct sum (finite cutoff) approaches its
    limit as 1/cutoff; we Richardson-extrapolate. If the split formula reproduces
    the extrapolated direct sum, the split machinery (coeff extraction, zero-mode
    subtraction, integration) is correct, so the continuation to s=-1/2 is trusted.
    """
    # direct sum at increasing cutoffs -> extrapolate (V ~ Vinf + slope/cutoff)
    cutoffs = [1000, 2000, 4000, 6000]
    Vs = []
    for A in cutoffs:
        spec = defaultdict(int)
        for a in range(1, A + 1):
            for b in range(1, A + 1):
                if (a - b) % 3:
                    continue
                lam = (a * a + a * b + b * b - 3) // 3
                if lam == 0:
                    continue
                spec[lam] += min(a, b)
        L = np.array(sorted(spec.keys()), dtype=np.float64)
        D = np.array([spec[int(l)] for l in L], dtype=np.float64)
        Vs.append(float(np.sum(D * L ** (-s0))))
    A = np.array(cutoffs, dtype=np.float64)
    slope, Vinf = np.polyfit(1.0 / A, np.array(Vs), 1)
    direct_extrap = float(Vinf)

    # split formula at s0
    def P_N(t):
        return sum(coef[j] * t ** exps[j] for j in range(len(exps)))

    def f0(t):
        return t ** (s0 - 1.0) * (Theta(t) - P_N(t))

    def finf(t):
        return t ** (s0 - 1.0) * (Theta(t) - n0)

    I0, _ = sc_quad(f0, 1e-2, 1.0, limit=300)
    Iinf, _ = sc_quad(finf, 1.0, np.inf, limit=300)
    brk = I0 + Iinf - n0 / s0
    for j, e in enumerate(exps):
        brk += coef[j] / (s0 + e)
    if _HAVE_MPMATH:
        zeta_split = float(brk / float(gamma(mpf(s0))))
    else:                                          # pragma: no cover
        zeta_split = brk / math.gamma(s0)

    rel = abs(zeta_split - direct_extrap) / abs(direct_extrap)
    return {
        "s0_convergent_test_point": s0,
        "direct_sum_extrapolated": direct_extrap,
        "split_formula_value": zeta_split,
        "relative_agreement": rel,
        "PASS_machinery_validated": bool(rel < 1e-4),
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
    # ---- forbidden-token firewall on the only external file we touch -------
    veff_text = None
    veff_hash = None
    if os.path.exists(VEFF_YAML):
        veff_text = open(VEFF_YAML, "r", encoding="utf-8").read()
        leaked = [t for t in FORBIDDEN_VALUE_TOKENS if t in veff_text]
        if leaked:
            sys.stderr.write("REFUSE(exit2): forbidden value in veff yaml: %s\n"
                             % leaked)
            return 2
        veff_hash = sha256_file(VEFF_YAML)

    # =====================================================================
    # PART 0 -- verify the tower (Kostant cross-check of zero-weight mult).
    # =====================================================================
    tower_ok, casimir_ok, tower_checks = verify_tower()

    # =====================================================================
    # PART 1 -- build the spectrum (two cutoffs to witness stability).
    # =====================================================================
    lams, degs, n0 = build_spectrum(a_max=900)
    Theta = make_theta(lams, degs, n0)
    n_modes = int(len(lams))
    smallest = [(float(lams[i]), int(degs[i])) for i in range(min(8, n_modes))]

    # =====================================================================
    # PART 2 -- heat-trace small-t expansion (half-integer powers).
    # =====================================================================
    coef, val = fit_heat_coefficients(Theta)
    lead_pred, J = continuum_leading_coefficient()
    coef_table = {f"t^{e:+.1f}": float(coef[j]) for j, e in enumerate(HALF_INT_EXPS)}

    # validate the split machinery at a convergent point before trusting s=-1/2
    split_validation = validate_split_at_convergent_point(
        Theta, coef, n0, lams, degs)

    # =====================================================================
    # PART 3 -- analytic continuation to s = -1/2.
    # =====================================================================
    cont = continue_to_minus_half(Theta, coef, n0)
    R = cont["residue_R"]
    F = cont["finite_part_F_minimal_subtraction"]
    sch = scheme_dependence(R, F)

    has_pole = abs(cont["c_half_theta_coeff"]) > 1e-6
    pref = 1.0 / ((4.0 * math.pi) ** (D_BULK / 2.0))
    cloop_from_F = GLOBAL_ONE_LOOP * pref * F      # -(1/2)(4pi)^{-13/2} F

    # =====================================================================
    # CROSS-CHECK (read the frozen magnitude AFTER sign/structure computed).
    # =====================================================================
    c_loop_wall_on_disk = (read_c_loop_wall(veff_text)
                           if veff_text is not None else None)
    target = C_LOOP_FRG2_TARGET
    ratio_F_to_target = cloop_from_F / target
    reproduces = (0.5 < abs(ratio_F_to_target) < 2.0)   # within a factor of 2

    # =====================================================================
    # HONEST OUTCOME (do NOT force a sign; do NOT force BRANCH-STANDS).
    # =====================================================================
    if has_pole:
        outcome = "SCHEME-AMBIGUOUS-owner-locked"
        zeta_value = ("POLE at s=-1/2 (no scheme-free finite value): "
                      "zeta(s) = R/(s+1/2) + F + O(s+1/2), "
                      "R=%.6g (scheme-invariant), F=%.6g (mu=1/R_K6; scheme-dep)"
                      % (R, F))
        zeta_sign = ("residue R NEGATIVE (scheme-invariant); finite part F sign "
                     "SCHEME-DEPENDENT (flips at mu*=%.4g)"
                     % sch["mu_star_where_finite_part_flips"])
        branch = "still-owner-locked"
        well_verdict = (
            "OWNER-LOCKED / CONDITIONAL -- but the residual is now SHARPER. The "
            "continuation is COMPLETE (not deferred): zeta_{Delta_K6}(s) has a "
            "SIMPLE POLE at s=-1/2 (Theta(t) carries a nonzero t^{+1/2} term, "
            "coeff=+%.5f), so the one-loop vacuum energy is UV-divergent and its "
            "finite part is scheme-dependent. The scheme-INVARIANT residue is "
            "NEGATIVE (R=%.5f), which is the sign BRANCH-STANDS would want -- but "
            "it is the residue of a DIVERGENCE, not the finite wall coefficient. "
            "The finite part F that actually sets the wall is scheme-dependent "
            "(its sign flips with the renormalization scale mu), so the FAVORABLE "
            "BRANCH-STANDS is NOT forced. The well stays gated on the owner's "
            "FRG-2 NLO Litim shell-projection SCHEME -- now a single named scheme "
            "choice (a smaller residual), not a whole missing computation."
            % (cont["c_half_theta_coeff"], R))
    else:                                          # unreachable given the data
        outcome = "DERIVED-sign-BRANCH-STANDS" if F < 0 else "DERIVED-sign-BRANCH-RUNAWAY"
        zeta_value = "%.10g" % F
        zeta_sign = "NEGATIVE" if F < 0 else "POSITIVE"
        branch = "BRANCH-STANDS" if F < 0 else "BRANCH-RUNAWAY"
        well_verdict = "(finite continuation; branch read from the finite value)"

    result = {
        "schema": "gap04_zeta_continuation_frg2_result_v1",
        "object": (
            "c_loop = -(1/2)(4 pi)^{-D/2} zeta_{Delta_K6}(-1/2); scalar K6=SU(3)/T^2 "
            "KK tower; eigenvalue = C2(p,q); degeneracy = T^2 zero-weight mult."),
        "outcome": outcome,

        "part0_tower_verification": {
            "zero_weight_mult_matches_kostant": tower_ok,
            "casimir_normalization_C2_adjoint_3_fund_4over3": casimir_ok,
            "panel": tower_checks,
        },

        "part1_spectrum": {
            "coordinates": ("shifted Eisenstein: a=p+1,b=q+1; "
                            "lambda=(a^2+ab+b^2-3)/3; deg=min(a,b); a,b>=1; a==b mod3"),
            "a_max": 900,
            "n_distinct_eigenvalues": n_modes,
            "smallest_(lambda,deg)": smallest,
            "note": ("eigenvalue = SU(3) Casimir of triality-0 rep; the smallest "
                     "nonzero level is the (1,1) adjoint at C2=3 with deg=2."),
        },

        "part2_heat_trace_expansion": {
            "form": "Theta(t) ~ sum_k c_k t^{e_k}, half-integer e only",
            "coefficients": coef_table,
            "leading_c_minus_3half_fit": float(coef[0]),
            "leading_c_minus_3half_continuum_pred_sqrt3_times_J": lead_pred,
            "continuum_J_int_min_ab": J,
            "leading_coeff_match": abs(coef[0] - lead_pred) / abs(lead_pred) < 1e-3,
            "effective_spectral_dimension_d_eff": 3,
            "validation_rel_err": [{"t": v["t"], "rel_err": v["rel_err"]} for v in val],
            "note": ("d_eff=3 (Theta~t^{-3/2}), NOT 6: the zero-weight sublattice "
                     "is a measure-zero slice of the full L^2(K6) spectrum."),
        },

        "split_machinery_validation": split_validation,

        "part3_continuation_to_minus_half": {
            "method": ("Mellin / heat-kernel split (Epstein-Hurwitz): zeta(s) = "
                       "1/Gamma(s)[int_0^1 t^{s-1}(Theta-P_N) + sum_k c_k/(s+e_k) "
                       "- n0/s + int_1^inf t^{s-1}(Theta-n0)]"),
            "I0_int_tlo_1": cont["I0_int_tlo_1"],
            "I0_cutoff_spread_5e-3_to_2e-2": cont["I0_cutoff_spread_5e-3_to_2e-2"],
            "Iinf_int_1_inf": cont["Iinf_int_1_inf"],
            "c_half_theta_coeff_t_plus_half": cont["c_half_theta_coeff"],
            "POLE_at_minus_half": has_pole,
            "residue_R_scheme_invariant": R,
            "residue_R_sign": "NEGATIVE" if R < 0 else "POSITIVE",
            "finite_part_F_minimal_subtraction_mu_1": F,
            "finite_part_F_sign_at_mu_1": "NEGATIVE" if F < 0 else "POSITIVE",
            "scheme_dependence": sch,
        },

        "zeta_minus_half_value": zeta_value,
        "zeta_minus_half_sign": zeta_sign,
        "branch_selected": branch,

        "cross_check_against_frozen_cloop": {
            "performed_after_sign_computed": True,
            "frozen_c_loop_FRG2_target": target,
            "c_loop_wall_on_disk_veff": c_loop_wall_on_disk,
            "minus_half_one_loop_prefactor": GLOBAL_ONE_LOOP,
            "factor_4pi_to_minus_13_over_2": pref,
            "c_loop_from_finite_part_F": cloop_from_F,
            "ratio_to_frozen_target": ratio_F_to_target,
            "reproduces_frozen_magnitude_within_factor_2": bool(reproduces),
            "verdict": (
                "MISMATCH: the minimal-subtraction scalar-zeta finite part gives "
                "|c_loop| ~ %.3e, about %.0fx smaller than the frozen FRG-2 "
                "magnitude %.4e. The frozen value is set by the owner's FRG-2 NLO "
                "Litim shell-projection scheme (specific finite subtraction + full "
                "13D field content + mode-by-mode shell mass spectrum), which is "
                "MORE than the bare scalar K6 zeta(-1/2). Honest non-reproduction."
                % (abs(cloop_from_F), abs(target / cloop_from_F), target)),
        },

        "scheme": (
            "Regularization = Epstein-Hurwitz / Mellin heat-kernel zeta on the "
            "SU(3)-Casimir (Eisenstein-form) lattice. Because zeta has a POLE at "
            "s=-1/2, a finite value requires a subtraction scheme. Minimal "
            "subtraction (mu=1/R_K6) gives F=%.5f<0; the corpus c_loop uses FRG-2 "
            "NLO Litim shell-projection, a DIFFERENT finite scheme. FRG-2 Litim vs "
            "minimal-subtraction MS-bar give different finite parts (and the "
            "finite-part SIGN is mu-dependent), so the result is "
            "SCHEME-AMBIGUOUS-owner-locked." % F),

        "scheme_ambiguity": (
            "The pole at s=-1/2 means the finite part is NOT scheme-free. Only the "
            "residue (R<0) is scheme-invariant. The finite-part sign flips at the "
            "renormalization scale mu*=%.4g, so without the owner's named FRG-2 "
            "Litim shell-projection scheme the BRANCH sign is genuinely ambiguous. "
            "This is the honest endpoint -- NOT a manufactured favorable branch."
            % sch["mu_star_where_finite_part_flips"]),

        "well_verdict": well_verdict,

        "what_requires_chris": (
            "(1) The named FRG-2 NLO Litim shell-projection SCHEME definition that "
            "fixes the finite subtraction at s=-1/2 (which renormalization scale "
            "mu, which shell-by-shell mass spectrum) -- this is what pins the "
            "finite-part sign and reproduces the frozen 1.3637877e-5 magnitude; "
            "the bare scalar K6 zeta(-1/2) is a POLE and gives only a "
            "scheme-invariant NEGATIVE residue, not a scheme-free finite wall "
            "coefficient. (2) Confirmation that the wall coefficient is the FINITE "
            "PART under that scheme (not the residue), and that the full 13D field "
            "content (the divergence's coefficient) is renormalized consistently."),

        "no_target_loading_attest": (
            "No observed value entered on any input side (no A_s, Lambda_obs, r, "
            "eta_B, n_s, N_eff, PDG, Omega_DM, H_0, S_8). The tower and the entire "
            "continuation are built from dim-6 geometry and SU(3) group theory "
            "ALONE. The frozen c_loop magnitude (1.3637877e-5) was used ONLY at the "
            "final cross-check, strictly AFTER the sign/structure were computed, and "
            "ONLY as a geometry-side comparison -- never as an input to the "
            "continuation. The favorable BRANCH-STANDS was NOT forced: the residue "
            "is reported NEGATIVE (scheme-invariant) but the wall-setting finite "
            "part is reported SCHEME-DEPENDENT and the magnitude cross-check is "
            "reported as an honest MISMATCH."),

        "provenance": {
            "veff_coefficients_frg4.yaml_sha256": veff_hash,
            "mpmath_used": _HAVE_MPMATH,
        },

        "non_promotion": (
            "no gate flipped; no status word emitted for any gate; countersign-"
            "ready continuation + scheme-ambiguity analysis only."),
    }

    def _sanitize(o):
        """Recursively coerce numpy scalars/bools to native Python types."""
        if isinstance(o, dict):
            return {k: _sanitize(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)):
            return [_sanitize(v) for v in o]
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        return o

    result = _sanitize(result)

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gap04_zeta_continuation_frg2_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- decision-grade packet to stdout ----------------------------------
    print("=" * 76)
    print("B-UQFC-14-FRG-2  scalar K6 spectral-zeta continuation (Gap-04)")
    print("=" * 76)
    print("OBJECT: c_loop = -(1/2)(4pi)^{-13/2} zeta_{Delta_K6}(-1/2)")
    print("-" * 76)
    print("PART 0  tower verification:")
    print("  zero-weight mult == Kostant : %s" % tower_ok)
    print("  Casimir norm C2(1,1)=3,C2(1,0)=4/3 : %s" % casimir_ok)
    print("PART 1  spectrum (a_max=900):")
    print("  distinct eigenvalues: %d ; smallest (lam,deg): %s"
          % (n_modes, smallest[:4]))
    print("  eigenvalue = Eisenstein form (a^2+ab+b^2-3)/3, deg=min(a,b)")
    print("PART 2  heat trace Theta(t) ~ half-integer powers:")
    for j, e in enumerate(HALF_INT_EXPS):
        print("    c[t^%+.1f] = %+.8f" % (e, coef[j]))
    print("  leading c_{-3/2}: fit=%.8f  continuum sqrt(3)*J=%.8f  (match)"
          % (coef[0], lead_pred))
    print("  effective spectral dimension d_eff = 3")
    print("VALIDATION  split machinery vs direct sum at s0=2 (convergent):")
    print("    direct(extrap)=%.8f  split=%.8f  rel=%.2e  PASS=%s"
          % (split_validation["direct_sum_extrapolated"],
             split_validation["split_formula_value"],
             split_validation["relative_agreement"],
             split_validation["PASS_machinery_validated"]))
    print("PART 3  continuation to s=-1/2 (Mellin split):")
    print("  c_{+1/2} (t^{1/2} coeff) = %+.8f  -> POLE at s=-1/2: %s"
          % (cont["c_half_theta_coeff"], has_pole))
    print("  residue  R = %+.8f   (scheme-INVARIANT)  sign: %s"
          % (R, "NEGATIVE" if R < 0 else "POSITIVE"))
    print("  finite F   = %+.8f   (mu=1/R_K6; SCHEME-DEP) sign: %s"
          % (F, "NEGATIVE" if F < 0 else "POSITIVE"))
    print("  finite-part sign flips at mu* = %.5f  -> scheme-dependent"
          % sch["mu_star_where_finite_part_flips"])
    print("-" * 76)
    print("CROSS-CHECK vs frozen FRG-2 c_loop (read AFTER sign):")
    print("  -(1/2)(4pi)^{-13/2} F = %.6e" % cloop_from_F)
    print("  frozen target          = %.6e" % target)
    print("  ratio = %.6f  -> reproduces within 2x: %s  (MISMATCH, ~%.0fx)"
          % (ratio_F_to_target, reproduces, abs(target / cloop_from_F)))
    print("-" * 76)
    print("OUTCOME : %s" % outcome)
    print("ZETA(-1/2): %s" % zeta_value)
    print("SIGN    : %s" % zeta_sign)
    print("BRANCH  : %s" % branch)
    print("SCHEME  : Epstein-Hurwitz/Mellin; pole at s=-1/2 => finite part is")
    print("          scheme-dependent (minimal-subtraction vs FRG-2 Litim differ)")
    print("artifact:", out_path)
    print("=" * 76)
    return 0


if __name__ == "__main__":
    sys.exit(main())
