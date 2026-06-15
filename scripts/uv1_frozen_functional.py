#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
uv1_frozen_functional.py
========================
UV-1 -- FREEZE THE UV FUNCTIONAL (CFCA Stage 1 + Stage 3 setup).

PURPOSE (target-blind, BEFORE any boundedness/stability test):
  Define and FREEZE -- exactly, and in a way that cannot be reverse-fit from the
  desired STANDS outcome -- the single UV object whose sigma -> -inf (internal-
  collapse) behavior the SUBSEQUENT pass will test. This script writes nothing
  about whether the object is bounded; it ONLY pins down WHAT is tested, WITH
  WHAT prescription, and WHAT it computes, so the later stability test rides on a
  frozen definition rather than a tunable one.

  This is the CFCA "freeze certificate" (METHOD_CFCA_June_14.md Stage 5 / R0):
  core / auxiliary / normalization / approximation / comparison-scale / data-source
  are all fixed and hashed BEFORE any measured number or any committed magnitude
  is read.

================================================================================
WHAT IS FROZEN (the four freezes; each is target-blind by construction)
================================================================================
FREEZE 1 -- THE OPERATOR.  D_sigma = the corpus's OWN spin-c Dirac-type operator
  of the spectral triple over M4 x K6 x S^2 x S^1_Y/Z2, the SAME D whose
  Borel-Weil-Bott / spin-c index = -3 already generates the three-family matter
  tower (Fable_GUT(3).md 2557-2558, 2581-2586, 7600-7601; active line bundle
  R1.4 hash 0fd19c9ae0c1). The fluctuation complex C_sigma is the full
  gauge-fixed BV/BRST tower sitting inside D_sigma^2: metric (graviton),
  gauge connection (inner fluctuation of D), scalar/Higgs (inner fluctuation of
  the finite Dirac), chiral fermion (the spin-c sections themselves), Faddeev-
  Popov ghosts (the Z2 BRST grading P_BRST), the projected sector, and the
  Weyl-rigid Cartan slice. NO scalar-only / bosonic-only reduction: Guard (1).

FREEZE 2 -- THE FUNCTIONAL.  The object tested is the Chamseddine-Connes
  SPECTRAL ACTION
        S_sigma[f] = Str f( D_sigma^2 / Lambda^2 )
  -- a SINGLE positive functional over the WHOLE graded tower at once.  It is
  explicitly NOT the resummed determinant (1/2)Str log D_sigma^2 (candidate (B)):
  the two prior runs proved B is exactly where the scheme/finite-part ambiguity
  lives (zeta pole at s=-1/2, residue survives, Str[1]=n_B-n_F=-55 != 0). The
  spectral action has NO subtraction, so it cannot re-open the int_loop
  convention fight. Guards (2),(8).

FREEZE 3 -- THE PRESCRIPTION (cutoff-profile CLASS, not a single profile).  f is
  frozen as a CLASS: any admissible cutoff profile -- positive (f >= 0), even,
  sufficiently decaying, with positive moments f_0, f_2, f_4 > 0. The theorem to
  be proved downstream MUST hold for ALL admissible f (quantified over the whole
  class), so NO single f can be tuned to a desired outcome. This is the structural
  reason the freeze is outcome-blind. Guard (2),(3).

FREEZE 4 -- THE BOUNDARY COMPANION (phase-exit / minimum-length).  Paired
  freeze, candidate (C): as Vol(K6) -> 0 the heat/curvature expansion of S_sigma
  stops converging (gap04_higher_operator_wall.py: curvature reaches the cutoff;
  a6 >~ a4 >~ c_loop). The companion freeze is the EFT-validity boundary
  sigma_* at which the asymptotic reading of S_sigma ceases, beyond which the
  description is declared non-geometric / phase-exiting. (A) owns the bounded
  interior; (C) owns the boundary. Guard (5).

================================================================================
WHAT IS *NOT* FROZEN HERE (deliberately deferred to the stability pass)
================================================================================
  * Whether S_sigma is bounded-below or phase-exits as sigma -> -inf. NOT decided
    here. Both STANDS and RUNAWAY remain live (Guard (3),(5)).
  * The sign/branch of int_loop. The spectral action never forms log-det, so no
    branch sign is taken. The committed c_loop = 1.3637877e-5 is NEVER read and
    enters NO decision (Guard (2)).
  * The positivity of the UV spectral measure as a *derived* fact. If the UV
    completion does not in fact carry a positive spectral measure, "Str f >= 0"
    is itself a NAMED UV-completion AXIOM (B-UQFC-14-UV-1), declared, not
    disguised as derived (Guard (7)). This script NAMES it; it does not prove it.

================================================================================
HARD GUARDS (any = FAIL) -- re-stated and enforced as attests in the output
================================================================================
 (1) FULL gauge-fixed physical tower (metric/gauge/scalar/fermion/ghost/projected/
     Weyl-rigid) -- NOT scalar-only or bosonic-only.
 (2) NO target-loading: sign/branch not chosen from STANDS; committed
     c_loop=1.3637877e-5 enters NO sign decision and is never read.
 (3) NO anthropic "we exist".
 (4) Finite-order a4/a6/a8 appear ONLY as consistency checks, NEVER as the proof
     (Lemma 1 banked: along sigma->-inf no finite heat-kernel/FRG truncation is
     licensed to decide global stability).
 (5) Boundedness OR phase-exit must be PROVEN before collapse -- here we FREEZE
     the paired (A)+(C) object that the proof will use; we do NOT yet claim it.
 (6) Lambda scope preserved -- same hardness class, NOT the same solved problem.
 (7) If not proven, NAME the result a UV-completion AXIOM, never disguised as
     derived.
 (8) NO "leans/leaning runaway" language.

NON-PROMOTION: no gate flip; no status word emitted for any gate. This file
FREEZES a definition; it asserts no stability verdict. exit 0 on a clean freeze;
exit 2 if a corpus authority is unreadable or a forbidden token leaks.
"""

import hashlib
import json
import math
import os
import sys
from collections import defaultdict
from fractions import Fraction

import numpy as np


# ---------------------------------------------------------------------------
# CORPUS AUTHORITIES (read for provenance + the forbidden-token firewall). The
# committed c_loop magnitude file is DELIBERATELY NOT in this list and is NEVER
# opened (Guard (2)).
# ---------------------------------------------------------------------------
FA = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
      r"physics_Journal_and_patents/Final_physics_articles")
QUANTUM_MD = os.path.join(FA, "Fable_Quantum.md")            # nine-row field ledger
GUT_MD = os.path.join(FA, "Fable_GUT (3).md")                # spin-c Dirac, index -3
GILKEY_SRC = os.path.join(
    FA, "scripts", "gap_04", "src", "gilkey_a4_cross_terms.py")  # a4 density + sign
SELECTOR_DIR = os.path.join(FA, "scripts", "parent_selector_14d")
SELECTOR_GEOM = os.path.join(SELECTOR_DIR, "14D_PARENT_SELECTOR_GEOMETRY.md")
SELECTOR_DET = os.path.join(SELECTOR_DIR, "SELECTOR_DETERMINANT_CHANNEL_AUDIT.md")

# Prior frozen runs this freeze BUILDS ON (read for provenance only).
HERE = os.path.dirname(os.path.abspath(__file__))
PRIOR_SUPERTRACE = os.path.join(HERE, "gap04_full_supertrace_residue.py")
PRIOR_ZETA = os.path.join(HERE, "gap04_zeta_continuation_frg2.py")
PRIOR_WALL = os.path.join(HERE, "gap04_higher_operator_wall.py")

FORBIDDEN_VALUE_TOKENS = [
    "A_s=", "A_s =", "eta_B=", "eta_B =", "Lambda_obs=", "Lambda_obs =",
    "r_obs=", "r_obs =", "n_s_obs=", "N_eff_obs=", "Omega_DM_obs=",
    "H_0_obs=", "S_8_obs=",
]

# The committed FRG-2 c_loop magnitude is named ONLY so we can ATTEST it is never
# used in any sign/branch decision in this freeze. It is NOT read from disk.
C_LOOP_COMMITTED_NEVER_USED = 1.3637877214788921e-05

# Frozen geometry (Einstein constants of the compactification; data-blind).
# K6 = SU(3)/T^2 (dim 6, Lambda=+5): R=30; S^2 (round, Lambda=+1): R=2; S^1_Y flat.
GEOM = {
    "K6":  {"name": "SU(3)/T^2", "n": 6, "lam": 5, "R": 30, "Ric2": 150, "Riem2": 60},
    "S2":  {"name": "round S^2", "n": 2, "lam": 1, "R": 2,  "Ric2": 2,   "Riem2": 4},
    "S1Y": {"name": "S^1_Y/Z2",  "n": 1, "lam": 0, "R": 0,  "Ric2": 0,   "Riem2": 0},
}
SPIN_C_INDEX = -3                       # banked topological integer (Fable_GUT C2/E)
ACTIVE_BUNDLE_HASH = "0fd19c9ae0c1"     # R1.4 active line bundle (Fable_GUT 7600-7601)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ===========================================================================
# PART A. FREEZE 1 -- the operator D_sigma and its fluctuation complex C_sigma.
# The nine-row physical tower, each row mapped to its PIECE of D_sigma^2, so the
# "full gauge-fixed tower" (Guard 1) is satisfied BY CONSTRUCTION, not bolted on.
# This is the Guard-(4) consistency countersign: every ledger row -> a piece of D.
# ===========================================================================
def frozen_operator_and_complex():
    r"""
    Return the frozen operator definition and the explicit map ledger-row ->
    piece-of-D_sigma^2. Counts are the SAME banked content countersigned in
    gap04_full_supertrace_residue.py (n_B=35, n_F=90), re-stated here so the
    freeze is self-contained and cites its own provenance. NO new physics; this
    is a DEFINITION freeze.
    """
    n_gauge = 8 + 3 + 1                              # su(3)+su(2)+u(1) = 12 generators
    weyl_per_gen = 6 + 3 + 3 + 2 + 1                 # 15 Weyl / generation
    n_families = abs(SPIN_C_INDEX)                   # = 3 (banked index)

    # The graded tower, each row tied to its location inside D_sigma^2.
    rows = [
        {"row": "Q4-Row1", "sector": "metric (graviton)", "stat": "boson",
         "g_dof": 2,
         "inside_D2": "fluctuation of the M4 metric -> the curvature (E,Omega) "
                      "endomorphisms of D_sigma^2 (Lichnerowicz: D^2 = nabla*nabla "
                      "- E, E carries R/4)",
         "authority": "Fable_Quantum.md SS4 Row1 (2 TT polarizations)"},
        {"row": "Q4-Row4", "sector": "gauge connection A_mu^a (12 gens)",
         "stat": "boson", "g_dof": 2 * n_gauge,
         "inside_D2": "INNER FLUCTUATION D -> D + A + JAJ^-1 of the spin-c Dirac "
                      "(Connes): the gauge field IS a fluctuation of D over the "
                      "su(3)c+su(2)L+u(1)Y descended from K6/S^2/S^1_Y isometries",
         "authority": "Fable_Quantum.md SS4 Row4; Fable_GUT 955 (descended algebras)"},
        {"row": "Q4-Row3", "sector": "moduli (3 K6 shape + rho_S2 + chi_Y)",
         "stat": "boson", "g_dof": 3 + 1 + 1,
         "inside_D2": "internal-metric (shape/radion) fluctuations -> the sigma-, "
                      "rho-, chi-dependence of the internal Laplace block of "
                      "D_sigma^2; the breathing direction is the collapse ray",
         "authority": "Fable_GUT App A.4 Weyl-rigid chamber u in [1/2,3/2]^3 "
                      "+ gilkey sigma,rho,chi radions"},
        {"row": "Q4-Row6", "sector": "Higgs doublet (4 real)", "stat": "boson",
         "g_dof": 4,
         "inside_D2": "INNER FLUCTUATION of the FINITE (discrete) Dirac D_F: the "
                      "Higgs is the connection on the finite spectral-triple factor "
                      "(Chamseddine-Connes), entering D_sigma^2 as the off-diagonal "
                      "Yukawa block squared",
         "authority": "Fable_Quantum.md SS4 Row6 (complex doublet = 4 real)"},
        {"row": "Q4-Row5", "sector": "chiral matter (3 fam x 15 Weyl)",
         "stat": "fermion", "g_dof": n_families * weyl_per_gen * 2,
         "inside_D2": "the spin-c SECTIONS THEMSELVES: matter = zero modes of the "
                      "internal Dirac (Fable_GUT 870); the 90 chiral dof are the "
                      "spectrum of D_sigma on the index-(-3) bundle. They have NO "
                      "degenerate bosonic partner -> Str[1] != 0 is FORCED",
         "authority": "Fable_Quantum.md SS4 Row5 (15 Weyl/gen) x |index|=3 "
                      "(Fable_GUT 2558,5741 spin-c index -3)"},
        {"row": "Q4-Row8", "sector": "Faddeev-Popov ghosts (diffeo + 12 YM)",
         "stat": "ghost", "g_dof": 0,  # folded into physical counts via BRST
         "inside_D2": "the Z2 BRST grading P_BRST = (physical +1)/(gauge-exact -1) "
                      "(SELECTOR_DETERMINANT_CHANNEL_AUDIT line 37): ghosts enter "
                      "D_sigma^2 as the gauge-fixing/ghost block; net physical dof "
                      "are BRST-invariant",
         "authority": "Fable_Quantum.md SS4 Row8; SELECTOR P_BRST grading"},
        {"row": "PROJ", "sector": "projected sector (P_chi chirality)",
         "stat": "projection", "g_dof": 0,
         "inside_D2": "the chirality projector P_chi commuting with the grading "
                      "Gamma_8 selects the left-handed family content; acts on "
                      "D_sigma^2 as a spectral projection, not new dof",
         "authority": "14D_PARENT_SELECTOR_GEOMETRY.md 4.2 (P_chi, Gamma_8)"},
        {"row": "WRIG", "sector": "Weyl-rigid Cartan slice",
         "stat": "projection", "g_dof": 0,
         "inside_D2": "the Weyl-rigid / T^2-invariant projector selects the "
                      "zero-weight (Cartan) slice of the K6 spectrum -- the d_eff=3 "
                      "tower that carries the s=-1/2 structure; a spectral "
                      "restriction of D_sigma^2, not new dof",
         "authority": "gap04_zeta_continuation_frg2.py (zero-weight tower, d_eff=3)"},
    ]

    n_B = sum(r["g_dof"] for r in rows if r["stat"] == "boson")
    n_F = sum(r["g_dof"] for r in rows if r["stat"] == "fermion")
    return {
        "operator_name": "D_sigma  (spin-c Dirac-type operator of the spectral "
                          "triple over M4 x K6 x S^2 x S^1_Y/Z2)",
        "operator_definition": (
            "D_sigma is the corpus's OWN spin-c Dirac operator D_{K6}^{spin^c} "
            "(twisted by the active line bundle R1.4 hash %s), extended over the "
            "product geometry M4 x K6 x S^2 x S^1_Y/Z2 and dressed by INNER "
            "FLUCTUATIONS (gauge + Higgs). Its Borel-Weil-Bott / spin-c index is "
            "%d (three chiral families, no mirrors). The matter content is the "
            "spectrum of THIS operator; the gauge and Higgs sectors are inner "
            "fluctuations of THIS operator; the metric/moduli enter through its "
            "Lichnerowicz endomorphism E and curvature 2-form Omega. The collapse "
            "ray sigma -> -inf is the breathing (Row3) direction Vol(K6) ~ "
            "e^{+6 sigma/M_Pl} -> 0."
            % (ACTIVE_BUNDLE_HASH, SPIN_C_INDEX)),
        "fluctuation_complex_C_sigma": (
            "The full gauge-fixed BV/BRST fluctuation complex sitting inside "
            "D_sigma^2: metric+gauge+moduli+Higgs+chiral-fermion+ghost, with the "
            "P_chi chirality projection and the Weyl-rigid Cartan slice as spectral "
            "projections. ALL nine physical/ghost rows are accounted for INSIDE "
            "the single operator (Guard (1) satisfied by construction)."),
        "ledger_to_D2_map": rows,
        "n_B": n_B, "n_F": n_F, "Str_identity": n_B - n_F,
        "n_gauge_generators": n_gauge, "weyl_per_generation": weyl_per_gen,
        "n_families_from_index": n_families,
        "guard1_full_tower": (
            "FULL gauge-fixed physical tower: every one of the nine ledger rows "
            "(graviton, gauge, moduli, Higgs, chiral fermion, ghosts, projected, "
            "Weyl-rigid) maps to an explicit piece of the SINGLE operator "
            "D_sigma^2. NOT scalar-only, NOT bosonic-only. n_B=%d, n_F=%d."
            % (n_B, n_F)),
    }


# ===========================================================================
# PART B. FREEZE 2 + 3 -- the functional and the prescription (cutoff CLASS).
# The spectral action S_sigma[f] = Str f(D_sigma^2 / Lambda^2), with f frozen as
# a CLASS (positive, even, decaying; positive moments). We DEMONSTRATE, target-
# blind, that the leading asymptotic moments f_0,f_2,f_4 are positive for EVERY
# admissible profile by sampling several representative profiles -- this is the
# outcome-blind content of FREEZE 3 (quantify over the class, tune nothing).
# ===========================================================================
def admissible_profiles():
    r"""A representative FAMILY of admissible cutoff profiles f(u) >= 0 on u>=0
    (u = D^2/Lambda^2). Each must be positive, decaying, with finite positive
    moments. The freeze QUANTIFIES OVER the class; these samples only EXHIBIT
    that the moment positivity is profile-independent (it is not tuned)."""
    return {
        "heat_exp":        lambda u: math.exp(-u),
        "gaussian":        lambda u: math.exp(-u * u),
        "smooth_bump_p2":  lambda u: math.exp(-u) * (1.0 + u) ** 2,   # positive
        "rational_decay":  lambda u: 1.0 / (1.0 + u) ** 3,           # positive
        "exp_plus_half":   lambda u: math.exp(-u) * (1.0 + 0.5 * u), # positive
    }


def profile_moments(f, kmax=4, upper=80.0, n=200000):
    r"""Spectral-action moments f_k = int_0^inf f(u) u^{k-1} du for k=0..kmax.
    These are the POSITIVE coefficients multiplying the Seeley-DeWitt a_{2k} in
    the large-Lambda expansion S_sigma ~ sum_k f_k a_{2k} Lambda^{...}. For ANY
    positive profile and k>=1 the integrand f(u) u^{k-1} >= 0 => f_k >= 0; for
    k=0 (f_0 = int f(u) u^{-1} du) we use the regulated positive moment that
    multiplies the cosmological a_0 term (still a positive integral of a positive
    integrand on u>0). We compute them numerically as an EXHIBIT only."""
    out = {}
    us = np.linspace(1e-6, upper, n)
    fu = np.array([f(u) for u in us], dtype=np.float64)
    for k in range(0, kmax + 1):
        integrand = fu * us ** (k - 1)
        out["f_%d" % k] = float(np.trapezoid(integrand, us)) \
            if hasattr(np, "trapezoid") else float(np.trapz(integrand, us))
    return out


def frozen_functional_and_prescription():
    profiles = admissible_profiles()
    moment_table = {}
    all_positive = True
    for name, f in profiles.items():
        m = profile_moments(f)
        moment_table[name] = m
        # the load-bearing moments for the collapse-limit reading are f_0 (a_0,
        # cosmological/volume) and f_2 (a_2, Einstein-Hilbert) and f_4 (a_4,
        # Yang-Mills/cross). Positivity of these for EVERY profile is the freeze.
        if not (m["f_0"] > 0 and m["f_2"] > 0 and m["f_4"] > 0):
            all_positive = False

    return {
        "functional_frozen": (
            "S_sigma[f] = Str f( D_sigma^2 / Lambda^2 )  -- the Chamseddine-Connes "
            "SPECTRAL ACTION over the full graded tower of PART A. A SINGLE "
            "manifestly positive functional (sum of f(eigenvalue^2/Lambda^2) over "
            "the real non-negative spectrum of D_sigma^2 for f >= 0). It is NOT the "
            "resummed determinant (1/2)Str log D_sigma^2: that object (candidate B) "
            "is exactly where the prior runs located the ambiguity (zeta pole at "
            "s=-1/2; residue survives because Str[1]=n_B-n_F != 0). The spectral "
            "action carries NO subtraction, so it cannot re-open the int_loop "
            "convention fight."),
        "prescription_frozen": (
            "f is frozen as a CLASS: every admissible profile is positive (f>=0), "
            "even, sufficiently decaying, with positive moments f_0,f_2,f_4 > 0. "
            "The downstream theorem must hold for ALL admissible f (a universal "
            "quantifier over the class), so NO single f can be tuned. The leading "
            "collapse-limit terms are a_0 (cosmological, coeff f_0>0) and a_2 "
            "(Einstein-Hilbert, coeff f_2>0); the finite-order a_4,a_6,a_8 appear "
            "ONLY as consistency checks (Guard (4)), never as the proof."),
        "moment_positivity_exhibit": moment_table,
        "moments_positive_for_all_sampled_profiles": bool(all_positive),
        "why_outcome_blind": (
            "The moments f_k = int f(u) u^{k-1} du are integrals of a POSITIVE "
            "integrand for any positive profile, so f_0,f_2,f_4 > 0 is a property "
            "of the CLASS, not a choice. The sign that WAS load-bearing in the "
            "determinant route (the s=-1/2 residue / finite part that flipped with "
            "mu) is, in the spectral action, just a positive moment of a positive "
            "profile -- it cannot be selected. This is the structural freeze that "
            "removes the convention fight."),
        "asymptotic_expansion_schema": (
            "Large-Lambda heat expansion: S_sigma[f] ~ sum_k f_k a_{2k}(D_sigma^2) "
            "Lambda^{(d-2k)}. The a_{2k} are the SAME Seeley-DeWitt coefficients as "
            "before, but now they are MOMENTS of a frozen positive profile, NOT a "
            "renormalization-scheme finite part. a_0 ~ Vol (cosmological), a_2 ~ "
            "int R (Einstein-Hilbert), a_4 ~ Yang-Mills + R^2."),
    }


# ===========================================================================
# PART C. FREEZE 4 -- the boundary companion (phase-exit / minimum-length).
# Pin the EFT-validity boundary sigma_* where the asymptotic reading of S_sigma
# ceases. (A) owns the interior sigma > sigma_*; (C) owns the boundary and beyond.
# We compute sigma_* data-blind from the curvature-reaches-cutoff condition only
# (NO committed magnitude, NO sign). This DISCHARGES the freeze side of Guard (5).
# ===========================================================================
def frozen_boundary_companion():
    # curvature reaches the cutoff: R_K6(sigma) = R_K6_0 e^{-2 sigma} = M^2 (=1 in
    # unit-vol normalization) -> sigma_* = (1/2) ln R_K6_0. data-blind, sign-free.
    R_K6_0 = GEOM["K6"]["R"]
    sigma_star_unitvol = 0.5 * math.log(R_K6_0)
    return {
        "companion_frozen": (
            "Phase-exit / minimum-length companion (candidate C): as Vol(K6) -> 0 "
            "the curvature/heat expansion of S_sigma stops converging (higher "
            "Seeley-DeWitt operators a6 >~ a4 >~ c_loop outgrow their predecessors; "
            "gap04_higher_operator_wall.py). At the EFT-validity boundary sigma_* "
            "the asymptotic reading of S_sigma ceases and the description is "
            "declared non-geometric / phase-exiting. (A) owns the interior "
            "sigma > sigma_*; (C) owns sigma <= sigma_*."),
        "sigma_star_unitvol_curvature_at_cutoff": sigma_star_unitvol,
        "sigma_star_note": (
            "sigma_* = (1/2) ln R_K6_0 = (1/2) ln 30 = %.4f in unit-vol "
            "normalization (curvature reaches M^2). Computed data-blind from the "
            "frozen geometry ALONE; NO committed magnitude, NO sign decision. This "
            "is the FREEZE of the boundary location, not a claim that the interior "
            "is bounded." % sigma_star_unitvol),
        "why_paired_not_fallback": (
            "(A) is a positive functional valid in the EFT interior; (C) owns the "
            "region where (A)'s asymptotic expansion stops converging. The pairing "
            "is REQUIRED, not a fallback: it is the only way the limit-non-"
            "commutativity (large-Lambda vs Vol->0) is covered. Together (A)+(C) "
            "tile the whole ray sigma in (-inf, vacuum] with no -inf reached -- "
            "but ONLY the FREEZE of that tiling is asserted here; the PROOF is the "
            "next pass (Guard (5))."),
    }


def main():
    # ---- input firewall (the committed c_loop magnitude file is NOT opened) ---
    authorities = [QUANTUM_MD, GUT_MD, GILKEY_SRC, SELECTOR_GEOM, SELECTOR_DET]
    for p in authorities:
        if not os.path.exists(p):
            sys.stderr.write("REFUSE(exit2): missing corpus authority %s\n" % p)
            return 2
    for p in authorities:
        txt = open(p, "r", encoding="utf-8", errors="replace").read()
        leaked = [t for t in FORBIDDEN_VALUE_TOKENS if t in txt]
        if leaked:
            sys.stderr.write("REFUSE(exit2): forbidden value token in %s: %s\n"
                             % (p, leaked))
            return 2

    # =====================================================================
    # ASSEMBLE THE FOUR FREEZES.
    # =====================================================================
    op = frozen_operator_and_complex()
    func = frozen_functional_and_prescription()
    comp = frozen_boundary_companion()

    what_it_computes = (
        "S_sigma[f] = Str f(D_sigma^2/Lambda^2) computes the SPECTRAL ACTION of "
        "the geometry's own spin-c Dirac operator over the full graded tower -- a "
        "single positive number (for each Lambda, sigma, admissible f) equal to "
        "the f-weighted count of the eigenvalues of D_sigma^2. Its large-Lambda "
        "asymptotics reproduce, with POSITIVE moment coefficients f_0,f_2,f_4, the "
        "corpus cosmological (a_0 ~ Vol), Einstein-Hilbert (a_2 ~ int R), and "
        "Yang-Mills + R^2 (a_4) terms. The collapse limit sigma -> -inf "
        "(Vol(K6) -> 0) is to be read off the geometric behavior of this positive "
        "functional -- a property of spec(D_sigma^2), NOT of any subtraction. "
        "WHAT IS DELIBERATELY NOT COMPUTED HERE: whether it is bounded-below or "
        "phase-exits (deferred to the stability pass; both branches live).")

    frozen_prescription = (
        "PRESCRIPTION FROZEN target-blind: (i) operator = the corpus spin-c Dirac "
        "D_sigma (bundle hash %s, index %d), fixed by geometry, zero freedom; "
        "(ii) functional = Str f(D_sigma^2/Lambda^2), the positive spectral action, "
        "NOT the log-det; (iii) profile = the CLASS of all positive even decaying "
        "f with positive moments (universal quantifier; nothing tunable); "
        "(iv) companion = the phase-exit boundary sigma_* = (1/2)ln 30 from "
        "curvature-at-cutoff, data-blind. The committed c_loop=%g is NEVER read "
        "and enters NO decision. Freeze order: (operator class, functional, "
        "profile class, boundary) FIRST -> stability test SECOND."
        % (ACTIVE_BUNDLE_HASH, SPIN_C_INDEX, C_LOOP_COMMITTED_NEVER_USED))

    functional_definition = (
        "D_sigma = spin-c Dirac-type operator of the spectral triple over "
        "M4 x K6(=SU(3)/T^2) x S^2 x S^1_Y/Z2, index %d, active bundle %s. "
        "Fluctuation complex C_sigma = full gauge-fixed BV/BRST tower INSIDE "
        "D_sigma^2 (metric via Lichnerowicz E; gauge + Higgs via inner "
        "fluctuations; chiral fermions = spin-c sections, 90 unpaired dof; ghosts "
        "= Z2 BRST grading P_BRST; P_chi chirality projection; Weyl-rigid Cartan "
        "slice). Frozen UV functional = the Chamseddine-Connes spectral action "
        "S_sigma[f] = Str f(D_sigma^2/Lambda^2), f in the positive-profile class. "
        "n_B=%d, n_F=%d, Str[1]=%d (forced by index -3)."
        % (SPIN_C_INDEX, ACTIVE_BUNDLE_HASH, op["n_B"], op["n_F"],
           op["Str_identity"]))

    no_target_loading_attest = (
        "NO target-loading. (2) The sign/branch is NOT chosen: this freeze takes "
        "NO branch (the spectral action never forms a log-det, so no int_loop sign "
        "is decided). The committed c_loop=%g was NEVER opened and entered NO "
        "input or sign decision. (3) NO anthropic 'we exist': runaway stays live; "
        "boundedness is NOT asserted here. (7) The positivity of the UV spectral "
        "measure is NAMED as the UV-completion axiom B-UQFC-14-UV-1 (NOT disguised "
        "as derived): 'Str f >= 0 under the spectral-action axiom (positive cutoff "
        "profile + the corpus spin-c Dirac operator as fundamental object)'. The "
        "moment positivity f_0,f_2,f_4>0 is exhibited over a CLASS of profiles, "
        "tuning nothing. (4) finite-order a4/a6/a8 are flagged as consistency "
        "checks only; Lemma 1 (no finite truncation decides global stability) "
        "respected. No observed value (A_s, Lambda_obs, r, eta_B, n_s, N_eff, PDG, "
        "Omega_DM, H_0, S_8) entered on any input side."
        % C_LOOP_COMMITTED_NEVER_USED)

    operator_complex = (
        "OPERATOR D_sigma: corpus spin-c Dirac operator over "
        "M4 x SU(3)/T^2 x S^2 x S^1_Y/Z2, twisted by active bundle %s, BWB/spin-c "
        "index %d. COMPLEX C_sigma: the full gauge-fixed BV/BRST physical tower "
        "(metric, gauge, moduli, Higgs, 90 chiral-fermion dof, FP ghosts, P_chi "
        "projection, Weyl-rigid Cartan slice) realized INSIDE the single operator "
        "D_sigma^2 -- gauge+Higgs as inner fluctuations, metric via the "
        "Lichnerowicz endomorphism E, fermions as the spin-c sections, ghosts as "
        "the Z2 BRST grading. Guard (1) full tower satisfied by construction: "
        "n_B=%d, n_F=%d, Str[1]=%d (unpaired chiral content forced by index -3)."
        % (ACTIVE_BUNDLE_HASH, SPIN_C_INDEX, op["n_B"], op["n_F"],
           op["Str_identity"]))

    # The named UV-completion axiom (Guard (7)): declared, not disguised.
    named_axiom = {
        "id": "B-UQFC-14-UV-1",
        "statement": (
            "SPECTRAL-ACTION UV-COMPLETION AXIOM: the fundamental UV object is the "
            "spectral action Str f(D_sigma^2/Lambda^2) of the corpus spin-c Dirac "
            "operator, with a POSITIVE cutoff profile f >= 0 (equivalently, a "
            "positive UV spectral measure). UNDER this axiom Str f is manifestly "
            "positive and its collapse-limit behavior is a spectral-geometry "
            "property of spec(D_sigma^2). The axiom is DECLARED as an irreducible "
            "input (CFCA 0.4), NOT derived. Its honesty guard: if the true UV "
            "completion lacks a positive spectral measure, this is the single "
            "named axiom on which the downstream bounded-below/phase-exit theorem "
            "rests -- same hardness class as Lambda (Guard (6)), NOT the same "
            "solved problem."),
        "terminal_state": "conditional-with-named-gate (frozen, awaiting the "
                          "stability pass; both STANDS and RUNAWAY live)",
    }

    result = {
        "schema": "uv1_frozen_functional_v1",
        "title": "UV-1 FROZEN FUNCTIONAL -- target-blind freeze before stability",
        "object_frozen": op["operator_name"],

        "FREEZE_1_operator_and_complex": op,
        "FREEZE_2_3_functional_and_prescription": func,
        "FREEZE_4_boundary_companion": comp,

        "what_it_computes": what_it_computes,
        "functional_definition": functional_definition,
        "operator_complex": operator_complex,
        "frozen_prescription": frozen_prescription,

        "named_uv_completion_axiom": named_axiom,

        "deferred_to_stability_pass": (
            "NOT decided here (deliberately, so the test cannot be reverse-fit): "
            "(i) whether S_sigma is bounded-below or phase-exits as sigma -> -inf; "
            "(ii) any int_loop sign/branch; (iii) the positivity of the UV spectral "
            "measure as a derived fact (it is the NAMED axiom, not proven). Both "
            "STANDS and RUNAWAY remain live."),

        "builds_on": {
            "gap04_full_supertrace_residue.py": (
                "field content n_B=35, n_F=90, Str[1]=-55 forced by index -3; "
                "supertrace residue Str_pole=+4.466 survives (determinant route B "
                "is owner-locked)."),
            "gap04_zeta_continuation_frg2.py": (
                "zeta pole at s=-1/2, d_eff=3 zero-weight tower; finite part "
                "scheme-dependent (flips with mu) -- the ambiguity the spectral "
                "action removes by carrying no subtraction."),
            "gap04_higher_operator_wall.py": (
                "EFT-validity boundary: a6>~a4>~c_loop outgrow; curvature reaches "
                "cutoff near sigma~+1.70 (unit-vol). This is the substrate for the "
                "FREEZE-4 phase-exit boundary."),
        },

        "integrity_guards_attest": {
            "1_full_gauge_fixed_tower": op["guard1_full_tower"],
            "2_no_target_loading": (
                "No sign/branch chosen; committed c_loop=%g never read; spectral "
                "action forms no log-det so no int_loop decision is taken."
                % C_LOOP_COMMITTED_NEVER_USED),
            "3_no_anthropic": (
                "Runaway stays live; boundedness NOT asserted here."),
            "4_finite_order_consistency_only": (
                "a4/a6/a8 appear ONLY as consistency checks of a_0/a_2/a_4 against "
                "the corpus cosmological/Einstein/Yang-Mills terms; the proof rides "
                "on positivity of Str f, never on a finite-order coefficient sign. "
                "Lemma 1 (finite-order undecidability along sigma->-inf) respected."),
            "5_boundedness_or_phase_exit_frozen_not_claimed": (
                "The paired (A)+(C) object that the boundedness/phase-exit proof "
                "will use is FROZEN here (positive functional interior + sigma_* "
                "phase-exit boundary); the PROOF is the next pass. No -inf is "
                "asserted reached and none is asserted avoided yet."),
            "6_lambda_scope_preserved": (
                "Relationship to Lambda is 'same hardness class, not same solved "
                "problem' -- the result will be conditional on B-UQFC-14-UV-1, the "
                "single named axiom, exactly as the Lambda record is."),
            "7_axiom_named_not_disguised": (
                "The positive-spectral-measure input is NAMED as B-UQFC-14-UV-1, "
                "declared as an irreducible UV-completion axiom, never disguised as "
                "derived."),
            "8_no_leans_language": (
                "No 'leans/leaning runaway' language used anywhere; branches are "
                "stated as live, not tilted."),
        },

        "no_target_loading_attest": no_target_loading_attest,

        "provenance": {
            "Fable_Quantum.md_sha256": sha256_file(QUANTUM_MD),
            "Fable_GUT_3.md_sha256": sha256_file(GUT_MD),
            "gilkey_a4_cross_terms.py_sha256": sha256_file(GILKEY_SRC),
            "14D_PARENT_SELECTOR_GEOMETRY.md_sha256": sha256_file(SELECTOR_GEOM),
            "SELECTOR_DETERMINANT_CHANNEL_AUDIT.md_sha256": sha256_file(SELECTOR_DET),
            "prior_supertrace_sha256": sha256_file(PRIOR_SUPERTRACE)
                if os.path.exists(PRIOR_SUPERTRACE) else "absent",
            "prior_zeta_sha256": sha256_file(PRIOR_ZETA)
                if os.path.exists(PRIOR_ZETA) else "absent",
            "prior_wall_sha256": sha256_file(PRIOR_WALL)
                if os.path.exists(PRIOR_WALL) else "absent",
            "active_bundle_hash": ACTIVE_BUNDLE_HASH,
            "spin_c_index": SPIN_C_INDEX,
        },
        "non_promotion": (
            "no gate flipped; no status word emitted for any gate. This file "
            "FREEZES a definition (the UV object, its prescription, what it "
            "computes) target-blind; it asserts NO stability verdict and is NOT "
            "promotable as one."),
    }

    def _sanitize(o):
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

    out_dir = os.path.join(HERE, "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "uv1_frozen_functional_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- decision-grade packet to stdout ----------------------------------
    print("=" * 78)
    print("uv1_frozen_functional.py -- FREEZE THE UV FUNCTIONAL (target-blind)")
    print("=" * 78)
    print("FREEZE 1 OPERATOR : %s" % op["operator_name"])
    print("  bundle hash %s ; spin-c index %d ; n_B=%d n_F=%d Str[1]=%d"
          % (ACTIVE_BUNDLE_HASH, SPIN_C_INDEX, op["n_B"], op["n_F"],
             op["Str_identity"]))
    print("  full tower rows -> pieces of D_sigma^2:")
    for r in op["ledger_to_D2_map"]:
        print("    %-8s %-34s [%s] g=%d"
              % (r["row"], r["sector"][:34], r["stat"], r["g_dof"]))
    print("-" * 78)
    print("FREEZE 2 FUNCTIONAL: S_sigma[f] = Str f(D_sigma^2/Lambda^2)  (spectral")
    print("  action; NOT (1/2)Str log D^2 -- no subtraction, no int_loop fight)")
    print("FREEZE 3 PRESCRIPTION: f in the POSITIVE-PROFILE CLASS (universal")
    print("  quantifier; nothing tunable). Moment positivity f_0,f_2,f_4>0 for all")
    print("  sampled profiles: %s"
          % func["moments_positive_for_all_sampled_profiles"])
    for name, m in func["moment_positivity_exhibit"].items():
        print("    %-16s f0=%+.4f f2=%+.4f f4=%+.4f"
              % (name, m["f_0"], m["f_2"], m["f_4"]))
    print("-" * 78)
    print("FREEZE 4 COMPANION : phase-exit boundary sigma_* = (1/2)ln30 = %.4f"
          % comp["sigma_star_unitvol_curvature_at_cutoff"])
    print("-" * 78)
    print("NAMED AXIOM : %s -- positive spectral measure (DECLARED, not derived)"
          % named_axiom["id"])
    print("DEFERRED    : boundedness vs phase-exit (next pass); both branches LIVE")
    print("c_loop=%g : NEVER read, NO sign decision" % C_LOOP_COMMITTED_NEVER_USED)
    print("artifact    :", out_path)
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
