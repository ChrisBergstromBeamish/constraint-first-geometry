#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
c_loop_NLO_match.py
===================
THE NAMED PRODUCER. The FRG-2 NLO Litim shell-projection producer of the finite
c_loop (the e^{-6 sigma} KK-Casimir wall coefficient) that the corpus REFERENCES
(z_renormalized_c_loop.py's RETAINED_MODES comment: "matches c_loop_NLO_match.py
spectrum") but does NOT contain. This file BUILDS that producer from first
principles, target-blind, on canonical literature-justified grounds.

It supersedes the partial reconstruction in gap04_litim_scheme_branch.py by
constructing the actual NLO Litim THRESHOLD-FUNCTION shell projection over the
five FRG-2 retained-mode shell masses (not the unbounded bare K6 Casimir tower),
and it carries the relative-one-loop-sign analysis to its honest endpoint.

================================================================================
THE INTEGRITY CRUX (read twice)
================================================================================
There is a KNOWN TARGET the producer "should" reproduce: c_loop = +1.3637877e-5.
CHOOSING O1/O2/O3 TO HIT THAT TARGET IS REVERSE-FITTING AND IS FORBIDDEN. Every
O1/O2/O3 choice below is made on PRINCIPLED, canonical, literature-justified
grounds (Litim 2001 PRD 64 105007 threshold functions l_n^d; the canonical FRG
effective-potential / heat-kernel one-loop insertion; the corpus-pinned matching
scale). All choices are COMMITTED in STEPS 1-3 BEFORE the target value is read.
The target enters ONLY at STEP 4 as an INDEPENDENT validator.

A sign is DERIVED-validated ONLY IF a non-reverse-fit principled construction
BOTH gives the sign AND reproduces the magnitude (within the factor-2 fold band).
NEVER force the favorable BRANCH-STANDS.

--------------------------------------------------------------------------------
PROVENANCE / WHY THIS REPLACES AN EARLIER DRAFT
--------------------------------------------------------------------------------
An earlier c_loop_NLO_match.py asserted that the relative-sign / BRANCH-STANDS
reading is "DERIVED and does NOT require Chris," claiming to BREAK the owner-lock
the corpus explicitly recorded. A held countersign and an independent rebuild
found that claim does NOT hold, on four grounds documented below (integration
direction skipped; finite part scheme-dependent; prior producer read the SAME
scheme as RUNAWAY; the no-flip convention is selected by reference to the stored
target's known + sign, which is circular). This version keeps the EXEMPLARY
magnitude handling (honest, non-reverse-fit) and CORRECTS the sign claim to the
corpus's standing owner-must-rule position. See STEP 3.

================================================================================
THE THREE OWNER-NAMED PIECES -- PRINCIPLED CHOICES (committed target-blind)
================================================================================
O1  SPECTRAL CUTOFF / SHELL-PROJECTION SCALE k.
    CHOICE: k = mu_match = M_13 (the corpus matching scale). In dimensionless
    M_13^2 units k^2 = 1, so the Litim threshold variable per retained mode is
        w_i = m_i^2 / k^2 = m_i^2   (m_i^2 the FRG-2 LO shell masses).
    JUSTIFICATION (corpus-pinned, NOT target-tuned): z_renormalized_c_loop.py
    evaluates every Z_i(mu_match) at EXACTLY mu_match = M_13, and the veff
    coefficient c_loop_Z is reported "at mu_match". The shell projection that
    feeds that re-weighting is therefore the projection AT k = mu_match. This is
    the ONLY scale the corpus actually fixes. The shell projection acts on the
    FIVE RETAINED-MODE shell masses (sigma_K6, rho_S2, chi_Y, theta_W, b_orb_sc)
    -- a FINITE set fixed by FRG-2 LO geometry/group theory -- NOT on the bare K6
    Casimir tower (whose Litim sum is UNBOUNDED in the cutoff, the
    gap04_litim_scheme_branch demonstration; and whose smallest eigenvalue
    C2 >= 2 is never retained at the frozen k_R_K6^2 = 0.01). Using the finite
    retained-mode shell -- not the divergent tower -- is what makes the NLO shell
    projection a single finite number at fixed k, and it is corpus-read (the same
    five modes z_renorm uses), not chosen to hit 1.36e-5.

O2  NLO THRESHOLD FUNCTION / FINITE SUBTRACTION.
    CHOICE: the canonical Litim optimised BOSONIC threshold function for the
    effective-potential (vacuum-energy) flow,
        l_0^d(w; eta) = (2/d) * (1 - eta/(d+2)) * 1/(1 + w),
    assembled into the one-loop vacuum-energy coefficient via the canonical FRG
    effective-potential-flow prefactor
        c_d = (1/2) * (4 pi)^{-d/2} / Gamma(d/2 + 1)   ( == 2 v_d / d ),
    so that
        c_loop = c_d * sum_i g_i * (1 - eta/(d+2)) / (1 + w_i)
               = (1/2)(4 pi)^{-d/2} * sum_i g_i * l_0^d(w_i; eta).
    JUSTIFICATION (Litim 2001; canonical FRG EP flow): l_0^d is THE optimised
    dimensionless scalar threshold function; v_d = [2^{d+1} pi^{d/2} Gamma(d/2)]^{-1}
    is the standard FRG loop-momentum measure; c_d = 2 v_d/d is the standard EP-flow
    prefactor. The identity 2 v_d/d == (1/2)(4pi)^{-d/2}/Gamma(d/2+1) is VERIFIED in
    code so the (2/d) of l_0 and the 1/Gamma of c_d are not double-counted.
    DIMENSION d: the shell projection runs over the COMPACT internal space, so
    d = total_compact_dimension = 9 (K6 6 + S^2 2 + S^1_Y 1; frozen_inputs.yaml
    geometry.total_compact_dimension = 9).
    HONESTY GUARD (per the held countersign): d = 9 is a SELECTION, not a
    derivation -- the corpus's OWN gilkey/zeta producers use the BULK
    (4 pi)^{-13/2} one-loop prefactor for the 13D log-det. And the threshold-
    function ASSEMBLY (where the (2/d) and the 1/Gamma sit) is itself ambiguous
    at fixed d. We therefore REPORT the d=13 alternative and the four internally-
    canonical assembly placements as an explicit AMBIGUITY BAND, and we do NOT
    claim a unique canonical magnitude.

O3  NLO RUNNING.
    CHOICE: eta = 1/(24 pi^2) per real scalar (the corpus C_ETA_LITIM), entering
    the threshold via the canonical (1 - eta/(d+2)) Litim NLO factor.
    JUSTIFICATION: Litim 2001 PRD 64 105007 Eq. (38); hard-coded in
    z_renormalized_c_loop.py. Sub-percent correction; agreed.

================================================================================
THE SIGN (the load-bearing Gap-04 deliverable) -- honest endpoint
================================================================================
The branch (BRANCH-STANDS vs BRANCH-RUNAWAY) is decided by the RELATIVE one-loop
sign of c_a4 vs the c_loop wall, which equals sign(int_a4)/sign(int_loop), where
int_loop is the SIGN OF c_loop's UNDERLYING heat-kernel density.

  * int_a4 = +(1/36) R_K6 R_S2 with R_K6 = +30, R_S2 = +2 -> POSITIVE,
    convention-invariant, manifest (gilkey_a4_cross_terms.py).
  * int_loop (the sign of c_loop's underlying density) is NOT banked anywhere in
    the corpus -- gilkey_a4_cross_terms.py records this EXPLICITLY as the
    owner-must-rule item (the CONVENTION_FREEZE slot for the a_4 sector is
    unfilled). It is NOT pinned by the principled construction. FOUR independent
    reasons the construction does NOT fix int_loop's sign:

      (i)  INTEGRATION DIRECTION. The Wetterich EP flow partial_t u_k > 0 is the
           INSTANTANEOUS flow (bosonic, manifestly positive). But the accumulated
           vacuum-energy contribution integrates UV -> IR, i.e. t = log k DECREASING
           (dt < 0), so the accumulated DELTA-u carries the OPPOSITE sign to
           partial_t u. "partial_t u > 0" therefore does NOT fix the accumulated-
           density sign. (This is the specific flaw in the earlier draft.)
      (ii) SCHEME DEPENDENCE OF THE FINITE PART. The bare spectral zeta has a POLE
           at s = -1/2 (gap04_zeta_continuation_frg2.py): the residue sign is
           scheme-invariant (NEGATIVE) but the FINITE PART that actually sets the
           wall flips sign with the renormalization scale mu (at mu* ~ 0.061).
           The wall-setting sign is genuinely scheme-dependent.
      (iii) PRIOR-RECONSTRUCTION DISAGREEMENT. gap04_litim_scheme_branch.py read
           the SAME Litim scheme family's leading order as BRANCH-RUNAWAY (the
           opposite, UNFAVORABLE branch). Two corpus reconstructions already
           disagree with a STANDS reading.
      (iv) CIRCULARITY. Selecting "the self-consistent convention is the one in
           which stored c_loop = +1.36e-5 needs no -(1/2) flip" uses the target's
           KNOWN + sign to fix the construction -- a no-target-loading violation
           ON THE SIGN side. Forbidden.

ENDPOINT: the relative sign is CONSTRUCTION/CONVENTION-DEPENDENT. Equally
principled readings give opposite branches (int_loop > 0 -> RUNAWAY;
int_loop < 0 -> STANDS). This is exactly the owner-must-rule situation the corpus
recorded. We default HOLD; we do NOT force BRANCH-STANDS and we do NOT claim the
sign is derived.

NON-PROMOTION: no gate flip; no status word emitted for any gate. exit 0 on an
honest resolution; exit 2 if an input is unreadable or a forbidden token leaks.
This file is STAGED here; promotable to the corpus gap_04/src ONLY if validated
+ owner-signed. Validation FAILS (magnitude mismatch + sign owner-locked), so it
is NOT promotable as a sign-derivation.
"""

import hashlib
import json
import math
import os
import sys

# ---------------------------------------------------------------------------
# Paths. The frozen magnitude is read ONLY at STEP 4 (post-hoc validator).
# ---------------------------------------------------------------------------
FA = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
      r"physics_Journal_and_patents/Final_physics_articles/scripts/gap_04")
FROZEN_YAML = os.path.join(FA, "frozen_inputs.yaml")
ZRENORM_SRC = os.path.join(FA, "src", "z_renormalized_c_loop.py")
GILKEY_SRC = os.path.join(FA, "src", "gilkey_a4_cross_terms.py")
VEFF_YAML = os.path.join(FA, "outputs", "veff_coefficients_frg4.yaml")

PI = math.pi
FOUR_PI_SQ = (4.0 * PI) ** 2
D_BULK = 13                 # full bulk dimension (gilkey/zeta one-loop prefactor)
D_COMPACT = 9               # K6(6) + S^2(2) + S^1_Y(1); the shell-projection dim
GLOBAL_ONE_LOOP = -0.5

# Frozen FRG-2 c_loop magnitude -- VALIDATOR target ONLY (read at STEP 4).
C_LOOP_FRG2_TARGET = 1.3637877214788921e-05

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
# Retained shell masses -- the FIVE FRG-2 LO retained modes, read off
# z_renormalized_c_loop.py's RETAINED_MODES seeds and recovered as EXACT
# rationals over (4 pi)^2. These VALUES are the FRG-2 LO coefficients
# (geometry/group-forced), fixed BEFORE any c_loop value is seen.
# ===========================================================================
SEED_SIGMA = 0.009498860966469166      # -> 3/2 / (4 pi)^2  (c_KK universality)
SEED_THETA = 4.875756906074309e-05     # -> Wilson harmonic / (4 pi)^2
SEED_BORB = 0.012665147955292222       # -> 2   / (4 pi)^2  (|c_bdry|)

RETAINED_MODES = [
    {"name": "sigma_K6", "g_dof": 1, "m2": SEED_SIGMA},
    {"name": "rho_S2",   "g_dof": 1, "m2": SEED_SIGMA},
    {"name": "chi_Y",    "g_dof": 1, "m2": SEED_SIGMA},
    {"name": "theta_W",  "g_dof": 1, "m2": SEED_THETA},
    {"name": "b_orb_sc", "g_dof": 1, "m2": SEED_BORB},
]
ETA_LITIM = 1.0 / (24.0 * PI * PI)      # O3 (Litim 2001 Eq. 38)


# ===========================================================================
# O2 building blocks -- Litim threshold + canonical EP-flow prefactor.
# ===========================================================================
def v_d(d):
    """Standard FRG loop-momentum measure v_d = [2^{d+1} pi^{d/2} Gamma(d/2)]^{-1}."""
    return 1.0 / (2.0 ** (d + 1) * PI ** (d / 2.0) * math.gamma(d / 2.0))


def c_d_EPflow(d):
    """Canonical FRG effective-potential-flow prefactor c_d = 2 v_d / d
       == (1/2)(4 pi)^{-d/2} / Gamma(d/2 + 1)."""
    return 2.0 * v_d(d) / d


def l0_litim(w, d, eta):
    """Litim optimised bosonic threshold function l_0^d(w; eta)
       = (2/d)(1 - eta/(d+2)) / (1 + w)  (Litim 2001)."""
    return (2.0 / d) * (1.0 - eta / (d + 2.0)) / (1.0 + w)


def c_loop_principled(d, eta):
    """The PRINCIPLED FRG-2 NLO Litim shell-projection c_loop (committed O1/O2/O3):
        c_loop = (1/2)(4 pi)^{-d/2} * sum_i g_i * l_0^d(w_i; eta)
               = c_d * sum_i g_i * (1 - eta/(d+2)) / (1 + w_i),  w_i = m_i^2.
    Returns (c_loop, threshold_core_sum)."""
    half_pref = 0.5 * (4.0 * PI) ** (-d / 2.0)
    s = sum(m["g_dof"] * l0_litim(m["m2"], d, eta) for m in RETAINED_MODES)
    return half_pref * s, s


def assembly_band(d, eta):
    """Four internally-canonical threshold-assembly placements at FIXED d, used to
    expose the assembly ambiguity HONESTLY (per the held countersign). Each is a
    defensible reading of "where the (2/d) and 1/Gamma live"; they are NOT all
    correct simultaneously, and reporting the spread is the honest CFCA move."""
    core_full = sum(m["g_dof"] * (2.0 / d) * (1.0 - eta / (d + 2.0)) / (1.0 + m["m2"])
                    for m in RETAINED_MODES)              # core carries (2/d)
    core_bare = sum(m["g_dof"] * (1.0 - eta / (d + 2.0)) / (1.0 + m["m2"])
                    for m in RETAINED_MODES)              # core without (2/d)
    half = 0.5 * (4.0 * PI) ** (-d / 2.0)
    plain = (4.0 * PI) ** (-d / 2.0)
    return {
        # A: EP-flow prefactor c_d on the (2/d)-free core (folds (2/d) into c_d).
        "A_EPflow_c_d_times_core_bare": c_d_EPflow(d) * core_bare,
        # B: COMMITTED O2 -- (1/2)(4pi)^{-d/2} * sum l_0^d (l_0 carries its own (2/d)).
        "B_half_times_core_full":       half * core_full,
        # C: (1/2)(4pi)^{-d/2} on the (2/d)-free core.
        "C_half_times_core_bare":       half * core_bare,
        # D: plain heat-kernel (4pi)^{-d/2} on the (2/d)-free core.
        "D_plain_times_core_bare":      plain * core_bare,
    }


# ===========================================================================
# The a_4 relative-sign / branch logic (geometry-forced; target-blind).
# ===========================================================================
def a4_and_relative_sign():
    R_K6_0, R_S2_0 = 30.0, 2.0
    a4_prefactor = 1.0 / 36.0
    hk_norm_13 = (4.0 * PI) ** (-D_BULK / 2.0)
    int_a4 = a4_prefactor * R_K6_0 * R_S2_0            # POSITIVE, convention-invariant
    c_a4_genuine_minus_half = GLOBAL_ONE_LOOP * hk_norm_13 * int_a4   # NEGATIVE (= -5.97e-8)
    return {
        "int_a4_sign": "POSITIVE",
        "int_a4_value": int_a4,
        "c_a4_under_genuine_minus_half": c_a4_genuine_minus_half,   # -5.97e-8
        "abs_c_a4": abs(c_a4_genuine_minus_half),
        "relative_sign_rule": (
            "relative sign(c_a4)/sign(c_loop) = sign(int_a4)/sign(int_loop). "
            "int_a4 = +(1/36)R_K6 R_S2 is POSITIVE & convention-invariant. "
            "int_loop (sign of c_loop's UNDERLYING density) is NOT banked; the "
            "branch rides entirely on it."),
        "int_loop_status_NOT_pinned": {
            "i_integration_direction": (
                "Wetterich partial_t u > 0 is INSTANTANEOUS; accumulated UV->IR "
                "(dt<0) carries OPPOSITE sign -> does NOT fix accumulated-density "
                "sign."),
            "ii_scheme_dependence": (
                "bare zeta has POLE at s=-1/2; residue NEGATIVE (invariant) but "
                "finite part FLIPS with mu (mu*~0.061) -> wall sign scheme-dep."),
            "iii_prior_disagreement": (
                "gap04_litim_scheme_branch read SAME scheme family leading order "
                "as BRANCH-RUNAWAY (opposite branch)."),
            "iv_circularity": (
                "choosing the no-flip convention by reference to stored c_loop=+ "
                "uses the target's sign -> circular, forbidden."),
        },
        "branch_if_int_loop_POSITIVE": (
            "c_a4 SAME relative sign as c_loop. With genuine -(1/2) on positive "
            "int_a4, c_a4 = -5.97e-8 < 0; growth-8 operator dominates growth-6 "
            "c_loop wall at the -sigma corner -> V -> -inf -> BRANCH-RUNAWAY."),
        "branch_if_int_loop_NEGATIVE": (
            "c_a4 OPPOSITE relative sign to c_loop -> c_a4 = +5.97e-8 > 0, a "
            "positive wall -> the -sigma well stands -> BRANCH-STANDS."),
    }


def main():
    for p in (FROZEN_YAML, ZRENORM_SRC, GILKEY_SRC, VEFF_YAML):
        if not os.path.exists(p):
            sys.stderr.write("REFUSE(exit2): missing input %s\n" % p)
            return 2

    frozen_text = open(FROZEN_YAML, "r", encoding="utf-8").read()
    zrenorm_src = open(ZRENORM_SRC, "r", encoding="utf-8").read()
    gilkey_src = open(GILKEY_SRC, "r", encoding="utf-8").read()
    veff_text = open(VEFF_YAML, "r", encoding="utf-8").read()

    for name, txt in (("frozen_inputs.yaml", frozen_text),
                      ("z_renormalized_c_loop.py", zrenorm_src),
                      ("gilkey_a4_cross_terms.py", gilkey_src),
                      ("veff_coefficients_frg4.yaml", veff_text)):
        leaked = [t for t in FORBIDDEN_VALUE_TOKENS if t in txt]
        if leaked:
            sys.stderr.write("REFUSE(exit2): forbidden value in %s: %s\n"
                             % (name, leaked))
            return 2

    # =====================================================================
    # STEP 1 -- commit O1/O2/O3 + verify the corpus pins (target-blind).
    # =====================================================================
    seeds_in_src = (str(SEED_SIGMA) in zrenorm_src
                    and str(SEED_THETA) in zrenorm_src
                    and str(SEED_BORB) in zrenorm_src)
    mu_match_pinned = ("MU_MATCH_GEV" in zrenorm_src
                       and "Z_at_mu_match" in zrenorm_src)
    num_sigma = SEED_SIGMA * FOUR_PI_SQ
    num_borb = SEED_BORB * FOUR_PI_SQ
    sigma_is_three_halves = abs(num_sigma - 1.5) < 1e-12
    borb_is_two = abs(num_borb - 2.0) < 1e-12
    eta_in_src = ("24.0 * math.pi * math.pi" in zrenorm_src)
    identity_ok = all(
        abs(c_d_EPflow(d) - 0.5 * (4.0 * PI) ** (-d / 2.0) / math.gamma(d / 2.0 + 1.0))
        < 1e-15 * abs(c_d_EPflow(d))
        for d in (9, 13))

    O1 = ("k = mu_match = M_13 (corpus-pinned: z_renorm evaluates Z at mu_match); "
          "w_i = m_i^2 in M_13^2 units; projection over the FIVE FRG-2 retained "
          "shell masses (finite), NOT the unbounded bare K6 Casimir tower.")
    O2 = ("Litim optimised bosonic threshold l_0^d(w;eta)=(2/d)(1-eta/(d+2))/(1+w) "
          "assembled with canonical EP-flow prefactor c_d=2 v_d/d "
          "=(1/2)(4pi)^{-d/2}/Gamma(d/2+1); d = total_compact_dimension = 9. "
          "d=9 is a SELECTION (corpus gilkey/zeta use bulk 13); band reported.")
    O3 = ("eta = 1/(24 pi^2) per real scalar (Litim 2001 Eq. 38), via the NLO "
          "factor (1 - eta/(d+2)). Sub-percent.")

    # =====================================================================
    # STEP 2 -- compute the principled c_loop (magnitude + sign), target-blind.
    # =====================================================================
    c_loop_d9, core_d9 = c_loop_principled(D_COMPACT, ETA_LITIM)
    c_loop_d13, core_d13 = c_loop_principled(D_BULK, ETA_LITIM)
    band_d9 = assembly_band(D_COMPACT, ETA_LITIM)
    band_d13 = assembly_band(D_BULK, ETA_LITIM)

    c_loop_committed = c_loop_d9
    c_loop_committed_sign = "POSITIVE" if c_loop_committed > 0 else "NEGATIVE"
    sign_robust_positive = (c_loop_d9 > 0 and c_loop_d13 > 0
                            and all(v > 0 for v in band_d9.values())
                            and all(v > 0 for v in band_d13.values()))

    # =====================================================================
    # STEP 3 -- the relative one-loop sign + branch (do NOT force STANDS).
    # The relative sign rides on int_loop (sign of c_loop's underlying density),
    # which is NOT banked and is scheme-dependent (four reasons above). Equally
    # principled readings give opposite branches. We report the leading-order
    # reading (the UNFAVORABLE one) honestly and decline to break the owner-lock.
    # =====================================================================
    a4 = a4_and_relative_sign()
    leading_order_branch = "BRANCH-RUNAWAY"   # assembled coeff positive -> int_loop+ reading
    branch_selected = "still-owner-locked"
    relative_sign_derived = False             # construction/convention-dependent

    # =====================================================================
    # STEP 4 -- VALIDATE against the frozen magnitude (read NOW, post-hoc).
    # =====================================================================
    target = C_LOOP_FRG2_TARGET
    ratio_committed = c_loop_committed / target
    reproduces_committed = (0.5 < abs(ratio_committed) < 2.0)
    ratio_band = {}
    for tag, val in list(band_d9.items()):
        ratio_band["d9_" + tag] = val / target
    for tag, val in list(band_d13.items()):
        ratio_band["d13_" + tag] = val / target
    any_in_fold = any(0.5 < abs(r) < 2.0 for r in ratio_band.values())
    nearest = min(ratio_band.values(), key=lambda r: abs(math.log(abs(r))))
    magnitude_reproduces_without_reverse_fit = bool(reproduces_committed)

    # =====================================================================
    # OUTCOME (honest; do NOT force the favorable branch).
    # =====================================================================
    outcome = "CONSTRUCTION-DEPENDENT-sign-owner-must-rule"
    magnitude_validation = (
        "Committed principled c_loop (O1+O2+O3, EP-flow d=9) = %.6e, ratio to "
        "target = %.4f -> OUTSIDE the factor-2 fold (does NOT reproduce). The + "
        "SIGN of the assembled coefficient is reproduced (robustly: sum of "
        "positive terms x positive prefactor), but the magnitude is NOT "
        "reproduced under the committed canonical normalization. Across the four "
        "internally-canonical assemblies x {d=9,d=13} the ratio spans %.2e..%.2f "
        "(>~10^4); the target sits inside this wide band but NO single principled "
        "prescription lands cleanly in [0.5,2.0] (nearest = %.3f, just outside). "
        "Hitting 1.36e-5 exactly would require hand-picking the assembly = "
        "reverse-fit, which is FORBIDDEN and DECLINED."
        % (c_loop_committed, ratio_committed,
           min(abs(r) for r in ratio_band.values()),
           max(abs(r) for r in ratio_band.values()), abs(nearest)))

    well_verdict = (
        "OWNER-LOCKED / CONDITIONAL. The FRG-2 NLO Litim shell-projection is now "
        "constructed from first principles target-blind: O1 (k=mu_match, w_i=m_i^2 "
        "over the five FRG-2 retained shell masses), O2 (Litim l_0^d threshold + "
        "canonical EP-flow prefactor c_d=2 v_d/d, d=9), O3 (eta=1/(24 pi^2)). The "
        "assembled c_loop is POSITIVE (robustly) but its MAGNITUDE does NOT "
        "reproduce 1.3637877e-5 under the committed canonical normalization "
        "(ratio 0.039); across equally-principled assemblies the magnitude is "
        "unpinned (>~10^4 span), so the magnitude is genuinely owner-locked and "
        "we DECLINE to reverse-fit it. The load-bearing DELIVERABLE -- the "
        "relative one-loop SIGN of c_a4 vs c_loop that decides STANDS vs RUNAWAY "
        "-- is NOT derived: it rides on the sign of c_loop's UNDERLYING density, "
        "which the corpus records as NOT banked (gilkey_a4_cross_terms.py: "
        "owner-must-rule) and which is NOT pinned by the construction for four "
        "independent reasons -- (i) the Wetterich partial_t u > 0 is "
        "instantaneous, the accumulated UV->IR contribution carries the opposite "
        "sign; (ii) the bare zeta has a POLE at s=-1/2 and the finite part flips "
        "with mu; (iii) the prior gap04_litim_scheme_branch read the SAME scheme "
        "family as BRANCH-RUNAWAY; (iv) selecting the no-flip convention by "
        "reference to the stored + target is circular. Equally principled "
        "readings give opposite branches (int_loop>0 -> RUNAWAY; int_loop<0 -> "
        "STANDS). The leading-order reading is the UNFAVORABLE RUNAWAY. We "
        "DEFAULT HOLD and do NOT force BRANCH-STANDS. The relative sign is "
        "CONSTRUCTION-DEPENDENT = owner-must-rule (Chris).")

    result = {
        "schema": "c_loop_NLO_match_result_v1",
        "object": (
            "c_loop = (1/2)(4 pi)^{-d/2} sum_i g_i l_0^d(w_i; eta) -- the FRG-2 NLO "
            "Litim shell-projection over the five retained shell masses; the "
            "e^{-6 sigma} KK-Casimir wall coefficient."),
        "outcome": outcome,

        "step1_principled_choices_committed_target_blind": {
            "O1_spectral_cutoff_scale": O1,
            "O2_NLO_threshold_prescription": O2,
            "O3_NLO_running": O3,
            "corpus_pins": {
                "O1_mu_match_pinned_in_zrenorm": bool(mu_match_pinned),
                "O1_retained_seeds_match_zrenorm": bool(seeds_in_src),
                "O2_EPflow_identity_2vd_over_d_eq_half_4pi_minus_d2_over_Gamma":
                    bool(identity_ok),
                "O3_eta_1_over_24pi2_in_zrenorm": bool(eta_in_src),
                "shell_mass_sigma_numerator_is_3_over_2": bool(sigma_is_three_halves),
                "shell_mass_borb_numerator_is_2": bool(borb_is_two),
            },
            "shell_masses_M13_2_units": {m["name"]: m["m2"] for m in RETAINED_MODES},
            "eta_litim": ETA_LITIM,
        },

        "step2_principled_c_loop_target_blind": {
            "c_loop_committed_EPflow_d9": c_loop_committed,
            "c_loop_committed_sign": c_loop_committed_sign,
            "threshold_core_sum_d9": core_d9,
            "c_loop_EPflow_d13": c_loop_d13,
            "threshold_core_sum_d13": core_d13,
            "assembly_band_d9": band_d9,
            "assembly_band_d13": band_d13,
            "sign_robustly_positive_across_band": bool(sign_robust_positive),
        },

        "step3_relative_sign_and_branch": {
            "a4_and_relative_sign": a4,
            "leading_order_reading": leading_order_branch,
            "leading_order_note": (
                "assembled c_loop coefficient POSITIVE -> if int_loop inherited "
                "positive, c_a4 keeps sign -> c_a4 < 0 -> RUNAWAY. Reported "
                "honestly; NOT forced to STANDS."),
            "relative_sign_derived": relative_sign_derived,
            "branch_selected": branch_selected,
            "why_not_derived": (
                "the relative sign rides on the sign of c_loop's UNDERLYING "
                "density (int_loop), which the corpus records as NOT banked "
                "(owner-must-rule) and which is scheme-dependent (zeta pole at "
                "s=-1/2; finite part flips with mu; instantaneous Wetterich flow "
                "sign != accumulated-density sign; prior reconstruction read "
                "RUNAWAY). Choosing the no-flip convention by reference to the "
                "stored + target is circular/forbidden."),
        },

        "step4_magnitude_validation_post_hoc": {
            "performed_after_sign_and_structure": True,
            "frozen_c_loop_FRG2_target": target,
            "committed_ratio_to_target": ratio_committed,
            "committed_reproduces_within_factor_2": bool(reproduces_committed),
            "ratio_band_all_principled_assemblies": ratio_band,
            "any_assembly_in_fold": bool(any_in_fold),
            "nearest_ratio": nearest,
            "magnitude_reproduces_without_reverse_fit":
                magnitude_reproduces_without_reverse_fit,
            "verdict": magnitude_validation,
        },

        "cloop_magnitude": (
            "committed principled (EP-flow d=9) = %.6e (POSITIVE); magnitude "
            "owner-locked / unpinned across equally-principled assemblies "
            "(~10^4 span); does NOT reproduce 1.36e-5 without reverse-fit."
            % c_loop_committed),
        "cloop_sign": ("POSITIVE for the assembled coefficient (robust). The "
                       "underlying-density sign that the BRANCH needs is NOT "
                       "pinned (scheme-dependent / not banked)."),
        "relative_sign": (
            "CONSTRUCTION-DEPENDENT. sign(c_a4)/sign(c_loop)=sign(int_a4)/sign(int_loop); "
            "int_a4=+ (manifest) but int_loop (c_loop underlying density sign) is "
            "NOT banked and scheme-dependent. int_loop>0 -> RUNAWAY; int_loop<0 -> "
            "STANDS. NOT derived."),
        "branch_selected": branch_selected,
        "well_verdict": well_verdict,

        "magnitude_validation": magnitude_validation,

        "reverse_fit_attestation": (
            "O1/O2/O3 were committed in STEPS 1-3 (this docstring + code) BEFORE "
            "the target 1.3637877e-5 was read at STEP 4. The shell masses are the "
            "corpus FRG-2 LO rationals (3/2/(4pi)^2, 2/(4pi)^2, Wilson/(4pi)^2), "
            "geometry/group-forced; none equals the target or a simple multiple. "
            "The committed canonical normalization (EP-flow d=9) MISMATCHES the "
            "target (ratio 0.039); the closer assembly (d9 C ~ 2.06) is DECLINED "
            "(it is not THE canonical placement and choosing it to land nearer the "
            "target would be reverse-fit). The hard-coded target does NOT enter "
            "STEPS 1-3. MAGNITUDE side is genuinely target-blind. The SIGN side is "
            "explicitly NOT claimed derived precisely BECAUSE deriving it would "
            "require selecting the no-flip convention by reference to the target's "
            "known + sign -- the circular reverse-fit we refuse. (An earlier draft "
            "made exactly that circular selection and claimed STANDS as derived; "
            "this version corrects it to owner-must-rule.)"),

        "what_requires_chris": (
            "(SIGN -- the load-bearing deliverable) The sign of c_loop's "
            "UNDERLYING heat-kernel density (int_loop) -- the unfilled "
            "CONVENTION_FREEZE slot for the a_4 sector -- which fixes the relative "
            "one-loop sign of c_a4 vs c_loop and hence the branch (STANDS vs "
            "RUNAWAY). This is owner-must-rule per gilkey_a4_cross_terms.py and is "
            "NOT broken here. "
            "(MAGNITUDE / O1 / O2) The exact NLO threshold-assembly placement and "
            "the shell-projection dimension (d=9 compact vs d=13 bulk) that pin "
            "the magnitude to 1.3637877e-5 -- unpinned across equally-principled "
            "choices. (O3 is sub-percent and agreed.)"),

        "no_target_loading_attest": (
            "No observed value entered on any input side (no A_s, Lambda_obs, r, "
            "eta_B, n_s, N_eff, PDG, Omega_DM, H_0, S_8). The construction is built "
            "from frozen geometry + SU(3)/T^2 group theory + the corpus FRG-2 LO "
            "coefficients (exact rationals over (4 pi)^2) + Litim 2001 threshold "
            "functions ALONE. The frozen magnitude 1.3637877e-5 was read ONLY at "
            "STEP 4 (post-hoc validator), strictly AFTER O1/O2/O3, the c_loop "
            "magnitude+sign, the relative-sign analysis, and the branch logic were "
            "fixed -- and ONLY as a comparison, never as an input. The favorable "
            "BRANCH-STANDS was NOT forced: the leading-order reading is the "
            "UNFAVORABLE RUNAWAY, the magnitude is reported as an honest mismatch, "
            "and the relative sign is reported CONSTRUCTION-DEPENDENT = "
            "owner-must-rule. The SIGN was NOT derived via the target's known + "
            "sign (which would be no-target-loading on the sign side)."),

        "provenance": {
            "frozen_inputs.yaml": sha256_file(FROZEN_YAML),
            "z_renormalized_c_loop.py": sha256_file(ZRENORM_SRC),
            "gilkey_a4_cross_terms.py": sha256_file(GILKEY_SRC),
            "veff_coefficients_frg4.yaml": sha256_file(VEFF_YAML),
        },
        "non_promotion": (
            "no gate flipped; no status word emitted for any gate. STAGED "
            "producer; promotable to gap_04/src ONLY if validated + owner-signed. "
            "Validation FAILS (magnitude mismatch + sign owner-locked), so NOT "
            "promotable as a sign-derivation."),
    }

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "c_loop_NLO_match_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- decision-grade packet to stdout ----------------------------------
    print("=" * 78)
    print("c_loop_NLO_match.py -- FRG-2 NLO Litim shell-projection (the named producer)")
    print("=" * 78)
    print("OBJECT: c_loop = (1/2)(4pi)^{-d/2} sum_i g_i l_0^d(w_i;eta)  [e^{-6 sigma} wall]")
    print("-" * 78)
    print("STEP 1  principled O1/O2/O3 (committed BEFORE target):")
    print("  O1 k=mu_match, w_i=m_i^2, FIVE retained shell masses (corpus-pinned)")
    print("     mu_match pinned in z_renorm : %s ; seeds match : %s"
          % (mu_match_pinned, seeds_in_src))
    print("     shell num 3/2: %s ; num 2: %s" % (sigma_is_three_halves, borb_is_two))
    print("  O2 Litim l_0^d + EP-flow c_d=2v_d/d, d=9 (SELECTION; band reported)")
    print("     EP-flow identity 2v_d/d==(1/2)(4pi)^-d/2/Gamma : %s" % identity_ok)
    print("  O3 eta=1/(24pi^2) in z_renorm : %s" % eta_in_src)
    print("-" * 78)
    print("STEP 2  principled c_loop (target-blind):")
    print("  committed (EP-flow d=9) : %+.6e  [%s]" % (c_loop_committed, c_loop_committed_sign))
    print("  threshold core sum d=9  : %.6f" % core_d9)
    print("  assembly band d=9       : %s" % {k: "%.3e" % v for k, v in band_d9.items()})
    print("  assembly band d=13      : %s" % {k: "%.3e" % v for k, v in band_d13.items()})
    print("  sign robustly positive  : %s" % sign_robust_positive)
    print("-" * 78)
    print("STEP 3  relative sign + branch (NOT forced):")
    print("  int_a4 POSITIVE (manifest) ; int_loop (c_loop underlying density) NOT banked")
    print("  int_loop>0 -> RUNAWAY ; int_loop<0 -> STANDS  (scheme-dependent, 4 reasons)")
    print("  leading-order reading   : %s (UNFAVORABLE)" % leading_order_branch)
    print("  relative_sign_derived   : %s" % relative_sign_derived)
    print("  branch_selected         : %s" % branch_selected)
    print("-" * 78)
    print("STEP 4  magnitude validation (read AFTER sign/structure):")
    print("  frozen target           : %.6e" % target)
    print("  committed ratio         : %.4f  (in fold: %s)"
          % (ratio_committed, reproduces_committed))
    print("  nearest principled ratio: %.3f  (just outside [0.5,2.0])" % abs(nearest))
    print("  reproduces w/o reverse-fit : %s" % magnitude_reproduces_without_reverse_fit)
    print("-" * 78)
    print("OUTCOME : %s" % outcome)
    print("BRANCH  : %s" % branch_selected)
    print("artifact:", out_path)
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
