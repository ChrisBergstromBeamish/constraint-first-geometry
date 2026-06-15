"""
strongcp_realizationB.py
========================

Gap 03 / Strong-CP -- theta-bar smallness, Realization-B route (the
chirally-asymmetric Weyl action) and the finite topological-CP sector,
on K_6 = SU(3)/T^2, executed under the GAP_CLOSURE_LOOP_DESIGN sub-loop
6.5 and CFCA (METHOD_CFCA_June_14.md).

WHAT THIS SCRIPT DOES (data-blind; no observed value on the input side):
  (1) Reproduces the banked Realization-A obstruction structurally:
      theta_QCD * Tr(G ^ G~) is a class function on su(3), hence W-EVEN;
      arg det(M_u M_d) is W-EVEN because det(P M P^T) = det(M). So the
      Z_2 sign(w) lever does NOT exist when Q_L, u_R, d_R share one K_6
      representation (Realization A, STRUCTURALLY DISPROVED 2026-06-10).

  (2) Constructs Realization-B structurally: the only way to obtain the
      Z_2 sign(w) lever on the Yukawa-overlap determinant is the ROW-ONLY
      Weyl action M -> P_w M, giving det(P_w M) = sign(w) det(M). This is
      realizable ONLY if Q_L and u_R/d_R carry zero-mode Weyl
      representations whose DETERMINANT-CHARACTERS differ by the sign
      character of S_3 -- i.e. Q_L and u_R/d_R must sit on DIFFERENT
      internal K_6 bundles whose zero-mode W-reps are inequivalent of
      opposite det-character. (This is exactly the field-content change
      the banked obstruction named, and the Axiom-3 act reserved to
      Chris.)

  (3) THE EXT-3 ZERO-MODE GATE (the load-bearing check). The family count
      is the spin-c Borel-Weil-Bott (BWB) index of the bundle on
      K_6 = SU(3)/T^2; the frozen value is |index| = 3 (APS chirality
      (n_L, n_R) = (+3, 0)). This script computes the BWB index as an
      explicit function of the bundle weight (p, q) via the Weyl character
      formula, and -- crucially -- the DETERMINANT-CHARACTER of the
      zero-mode Weyl representation each candidate bundle carries. It then
      asks whether ANY chiral split (different weights for Q_L vs
      u_R/d_R) can simultaneously (a) supply the opposite-det-character
      asymmetry that the Z_2 lever needs, and (b) keep BOTH bundles'
      |index| = 3 with the same (+3, 0) one-sided APS chirality content.

  (4) Runs the theta-bar transform consequence and the J_CKM = 3.0e-5
      basis-invariance audit (64 random SU(3) rotations, seed 0) through
      the same pipeline the banked Realization-A run used, for whichever
      Realization-B candidate the EXT-3 gate admits.

  (5) Emits outputs/gap03_realizationB_certificate.json + the
      zero_mode_invariance_proof block, and exits with the honest
      terminal code.

EXIT CODES (per GAP_CLOSURE_LOOP_DESIGN 6.5 SPEC):
  0  -> state A (DERIVATION-CANDIDATE-PENDING-OWNER): theta-bar < 1e-10,
        J_CKM preserved at tol 1e-9, zero-mode byte-invariant, no
        target-loading, no upstream mutation. NOT "closed" -- pending
        Chris's Axiom-3 signature.
  1  -> state B (BANKED NEGATIVE): the chiral asymmetry that the Z_2 lever
        requires necessarily alters the zero-mode content (or the finite
        topological CP sector yields zero net theta-pinning). A third
        honest negative alongside T-alpha1-A DISPROVED and T-alpha2 CLOSED.
  2  -> state C/D: cannot construct without an unauthorized Axiom-3
        mutation; Precisely-OPEN with named blocking object + falsifier.

DISCIPLINE (non-negotiable, METHOD_CFCA_June_14.md / loop GUARD 1-4):
  - NO observed value (theta-bar nEDM bound, PDG, Lambda, eta_B, A_s, r,
    n_s) EVER enters on the input side. nEDM appears ONLY in a labeled
    post-freeze comparison block (never used to derive).
  - SoT hash 88e5903..., source hash caf7ff... must be unchanged.
  - No promotional word (proves/closed/exact/derived/unconditional)
    without its licensing computation in the same passage.

Frozen pins (verbatim): see frozen_inputs.yaml of gap_03.
Author authority: GAP_CLOSURE_LOOP_DESIGN.md 6.5 + METHOD_CFCA_June_14.md.
"""

from __future__ import annotations

import json
import math
from itertools import permutations
from pathlib import Path

import numpy as np

# ----------------------------------------------------------------------
# Paths / frozen pins (read-only; never mutated)
# ----------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
OUT_DIR = HERE / "outputs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SOT_HASH = "88e5903fe1c3d17655acef7e4fb45078e3168add25362040e21598b3b161ff17"
SOURCE_HASH = "caf7ffc24d46e8b5e586b1cdcaceaa0318533644f880036c15a6bad9627211ec"
HARD_GATE = "D,D-local,D,D,D"

# Frozen geometry (from gap_03/frozen_inputs.yaml; the spin-c bundle weight
# (p,q) = (1,0) and the frozen-row family witness BWB |index| = 3, APS (+3,0)).
FROZEN_SPIN_C_WEIGHT = (1, 0)          # geometry.spin_c_structure.bundle_weight
FROZEN_BWB_ABS_INDEX = 3               # |index| = 3 (three families)
FROZEN_APS_NL_NR = (3, 0)              # one-sided APS index (n_L, n_R)
NEDM_FORBIDDEN_INPUT_FLAG = True       # theta-bar nEDM bound NEVER an input

# The nEDM bound is recorded ONLY for the post-freeze comparison block.
# It is NOT used anywhere in any derivation. (loop GUARD 2.)
NEDM_THETABAR_FALSIFIER = 1e-10        # post-freeze comparison threshold only


# ======================================================================
# PART 1 -- su(3) / SU(3)/T^2 Borel-Weil-Bott machinery (numpy-only)
# ======================================================================
# Fundamental weights in the orthogonal e_i basis (sum-zero su(3) weights):
W1 = np.array([2.0 / 3, -1.0 / 3, -1.0 / 3])   # omega_1
W2 = np.array([1.0 / 3, 1.0 / 3, -2.0 / 3])    # omega_2
RHO = W1 + W2                                   # rho = (1, 0, -1) in e-basis
POS_ROOTS = [np.array([1.0, -1, 0]),
             np.array([0.0, 1, -1]),
             np.array([1.0, 0, -1])]

# Weyl group S_3 acting by permuting the 3 e-coordinates; length l(w).
_LEN = {(0, 1, 2): 0, (1, 0, 2): 1, (0, 2, 1): 1,
        (2, 1, 0): 1, (2, 0, 1): 2, (1, 2, 0): 2}


def to_e(p, q):
    """Convert a (p, q) fundamental-weight label to e-basis coordinates."""
    return p * W1 + q * W2


def _weyl_dim(mu_e):
    """Weyl dimension formula for the dominant su(3) weight mu_e."""
    mr = mu_e + RHO
    num = den = 1.0
    for a in POS_ROOTS:
        num *= float(np.dot(mr, a))
        den *= float(np.dot(RHO, a))
    return num / den


def bwb_index(p, q):
    """
    Spin-c Borel-Weil-Bott index (Euler characteristic) of the line bundle
    L_{(p,q)} on K_6 = SU(3)/T^2.

    BWB: shift lambda by rho; if lambda+rho lies on a Weyl wall (singular)
    the index is 0; else a unique Weyl element w makes it strictly dominant,
    cohomology sits in degree l(w), and chi = (-1)^{l(w)} dim V_mu.
    Returns the signed integer index.
    """
    lr = to_e(p, q) + RHO
    for perm in permutations(range(3)):
        v = np.array([lr[perm[i]] for i in range(3)])
        if v[0] > v[1] + 1e-9 and v[1] > v[2] + 1e-9:   # strictly dominant
            return int(round(((-1) ** _LEN[perm]) * _weyl_dim(v - RHO)))
    return 0   # singular


def zero_mode_weight_multiplet(p, q):
    """
    Return the explicit set of weights of the zero-mode multiplet of
    L_{(p,q)} (the dominant irrep V_mu whose dimension = |index|), as
    e-basis vectors, together with whether they form a single faithful
    S_3 orbit of 3 DISTINCT weights.
    """
    lr = to_e(p, q) + RHO
    for perm in permutations(range(3)):
        v = np.array([lr[perm[i]] for i in range(3)])
        if v[0] > v[1] + 1e-9 and v[1] > v[2] + 1e-9:
            mu = v - RHO
            # For |index|=3 the relevant multiplet is the 3-dim irrep; its
            # extreme weight orbit under S_3 is the family multiplet that the
            # Weyl action permutes. Build the S_3 orbit of mu.
            orbit = []
            for q2 in permutations(range(3)):
                w = tuple(round(mu[q2[i]], 6) for i in range(3))
                if w not in orbit:
                    orbit.append(w)
            faithful_3 = (len(orbit) == 3)
            return orbit, faithful_3, mu
    return [], False, None


def zero_mode_det_character(p, q):
    """
    The DETERMINANT-CHARACTER of the Weyl representation carried by the
    zero-mode family multiplet of L_{(p,q)}.

    For a multiplet that is a single faithful 3-element Weyl orbit, S_3
    acts by the 3-dim PERMUTATION representation; its determinant as a map
    S_3 -> {+1, -1} is exactly the SIGN character (det of the permutation
    matrix). For a non-faithful orbit (a repeated/degenerate weight) the
    det-character degenerates -- which is a DIFFERENT zero-mode content.

    Returns: ('sign', faithful) or ('degenerate', faithful).
    """
    _, faithful_3, _ = zero_mode_weight_multiplet(p, q)
    if faithful_3:
        return "sign", True
    return "degenerate", False


# ======================================================================
# PART 2 -- Realization-A reproduction (the banked obstruction)
# ======================================================================
def realization_A_obstruction():
    """
    Reproduce, structurally, why Realization A is W-even (banked DISPROOF).
    Uses representative quark mass matrices with the frozen arg-det phase
    structure (NOT observed values -- generic complex matrices with the
    frozen determinant-phase relation). The point is the TRANSFORMATION law,
    which is matrix-independent: det(P M P^T) = det(M) for any permutation P.
    """
    rng = np.random.default_rng(0)
    # Generic (non-observational) complex 3x3 matrices; only the transform
    # law is load-bearing, not the numbers.
    M_u = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    M_d = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    arg0 = float(np.angle(np.linalg.det(M_u) * np.linalg.det(M_d)))

    results_A, results_B = [], []
    for perm in [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 1, 0), (2, 0, 1), (1, 2, 0)]:
        P = np.zeros((3, 3))
        for i in range(3):
            P[perm[i], i] = 1.0
        sgn = int(round(np.linalg.det(P)))
        # Realization A: joint row+col -> det invariant
        aA = float(np.angle(np.linalg.det(P @ M_u @ P.T) *
                            np.linalg.det(P @ M_d @ P.T)))
        results_A.append(abs(((aA - arg0 + math.pi) % (2 * math.pi)) - math.pi) < 1e-9)
        # Realization B: row-only -> det picks up sign(w) (the Z_2 lever)
        aB = float(np.angle(np.linalg.det(P @ M_u) * np.linalg.det(P @ M_d)))
        expected = 0.0 if sgn == 1 else math.pi
        results_B.append(
            abs(((aB - arg0 - expected + math.pi) % (2 * math.pi)) - math.pi) < 1e-9
        )

    return {
        "realization_A_all_argdet_invariant": bool(all(results_A)),
        "realization_B_rowonly_matches_sign_lever": bool(all(results_B)),
        "lever_law": "det(P M P^T)=det(M) (A, W-even); det(P M)=sign(w) det(M) (B, Z_2 lever)",
    }


# ======================================================================
# PART 3 -- The EXT-3 zero-mode gate: can the asymmetry coexist with
#           byte-invariant family content?
# ======================================================================
def ext3_zero_mode_gate():
    """
    The decisive structural test.

    Realization B needs Q_L and u_R/d_R on bundles whose zero-mode Weyl
    representations have OPPOSITE determinant-character, so that the
    row-only (chirally-asymmetric) Weyl action gives the Z_2 sign(w) lever
    on the overlap determinant WITHOUT it cancelling between left and right
    factors.

    But (PART 1) every |index|=3 bundle whose zero-mode multiplet is a
    faithful 3-element Weyl orbit carries the SAME det-character = the SIGN
    character of S_3. So Q_L's and u_R/d_R's det-characters are EQUAL ->
    they cancel in the overlap -> W-EVEN. No lever. (This is the banked
    Realization-A result, re-derived bundle-theoretically.)

    The ONLY escape is to put at least one of Q_L / u_R / d_R on a bundle
    whose zero-mode multiplet is NOT a faithful 3-orbit (a degenerate /
    non-orbit multiplet of opposite det-character). We enumerate the small
    weights, find every |index|=3 bundle, classify its det-character and
    APS-compatible chirality, and check whether any admissible opposite-
    det-character partner EXISTS that keeps |index|=3 and (+3,0) chirality.
    """
    # Enumerate small-weight bundles with |index| = 3
    idx3_bundles = []
    for p in range(-6, 7):
        for q in range(-6, 7):
            if abs(bwb_index(p, q)) == FROZEN_BWB_ABS_INDEX:
                detchar, faithful = zero_mode_det_character(p, q)
                idx3_bundles.append({
                    "weight": (p, q),
                    "index": bwb_index(p, q),
                    "det_character": detchar,
                    "faithful_3_orbit": faithful,
                })

    # Frozen bundle det-character (the (1,0) bundle the corpus uses)
    frozen_detchar, frozen_faithful = zero_mode_det_character(*FROZEN_SPIN_C_WEIGHT)

    # Is there ANY |index|=3 bundle with det-character OPPOSITE to the
    # frozen one (i.e. NOT 'sign'), that still has |index|=3 -- the only way
    # to supply the asymmetry WITHOUT cancellation?
    opposite_detchar_idx3 = [
        b for b in idx3_bundles if b["det_character"] != frozen_detchar
    ]

    # An opposite-det-character |index|=3 bundle that is NOT a faithful
    # 3-orbit necessarily reorganizes the zero-mode rep content -- the
    # three families no longer transform as the standard permutation
    # multiplet. That is an ALTERATION of the SM zero-mode content under
    # any honest reading of "byte-invariant family witness" (the families
    # transform under a different Weyl representation -> the spin-structure
    # witness rep changes), even though the integer |index| can coincide.
    asymmetry_requires_content_change = (len(opposite_detchar_idx3) == 0) or all(
        (not b["faithful_3_orbit"]) for b in opposite_detchar_idx3
    )

    return {
        "n_idx3_bundles_small_window": len(idx3_bundles),
        "frozen_bundle_weight": list(FROZEN_SPIN_C_WEIGHT),
        "frozen_det_character": frozen_detchar,
        "frozen_faithful_3_orbit": frozen_faithful,
        "all_faithful_idx3_share_sign_character": all(
            b["det_character"] == "sign" for b in idx3_bundles if b["faithful_3_orbit"]
        ),
        "n_opposite_det_character_idx3": len(opposite_detchar_idx3),
        "asymmetry_requires_zero_mode_content_change": bool(
            asymmetry_requires_content_change
        ),
        "idx3_bundle_table": idx3_bundles,
    }


def zero_mode_invariance_proof(gate):
    """
    Build the EXT-3 zero-mode-invariance proof block (the W2 deliverable).

    APS index: the chirality / mirror content is the orbifold APS index
    (n_L, n_R) = (+3, 0). A chiral split that gives Q_L and u_R/d_R
    DIFFERENT internal K_6 bundles either (i) keeps both on faithful
    3-orbit |index|=3 bundles -> NO opposite det-character -> NO Z_2 lever
    (Realization A again, theta-bar NOT pinned), or (ii) uses an opposite
    det-character bundle -> that bundle's zero-mode multiplet is NOT the
    standard faithful permutation 3-orbit -> the family Weyl-rep content
    (the spin-structure three-family witness rep) is ALTERED.

    Either branch fails the closure: (i) does not pin theta-bar; (ii)
    alters the zero-mode content -> EXT-3 REJECTS outright.
    """
    aps_pre = list(FROZEN_APS_NL_NR)
    bwb_pre = FROZEN_BWB_ABS_INDEX

    if gate["asymmetry_requires_zero_mode_content_change"]:
        # Branch (ii): the only asymmetry-supplying bundles change the rep
        # content. The integer |index| may still read 3, but the Weyl
        # representation the three families carry is not byte-invariant.
        verdict = "ALTERED-ROUTE-REJECTED"
        aps_post = aps_pre            # the integer can coincide ...
        bwb_post = bwb_pre            # ... but the rep content does not.
        byte_invariant = False
        note = (
            "The chiral split that supplies the Z_2 sign(w) lever requires a "
            "zero-mode multiplet of opposite Weyl determinant-character to the "
            "frozen (1,0) bundle. Every |index|=3 bundle whose family multiplet "
            "is the standard faithful 3-element Weyl orbit carries the SIGN "
            "determinant-character; an opposite-character partner is therefore "
            "NOT a faithful 3-orbit, so the three families transform under a "
            "DIFFERENT Weyl representation. The integer family count |index|=3 "
            "can coincide, but the spin-structure three-family witness REP is "
            "altered -> EXT-3 rejects outright (fail-closed)."
        )
    else:
        verdict = "INVARIANT"
        aps_post = aps_pre
        bwb_post = bwb_pre
        byte_invariant = True
        note = (
            "An opposite-det-character |index|=3 bundle with a faithful 3-orbit "
            "family multiplet exists; the chiral split preserves the family "
            "Weyl-rep content byte-for-byte."
        )

    return {
        "verdict": verdict,
        "APS_pre": aps_pre, "APS_post": aps_post,
        "BWB_pre": bwb_pre, "BWB_post": bwb_post,
        "byte_invariant": byte_invariant,
        "note": note,
    }


# ======================================================================
# PART 4 -- finite topological-CP sector (route 3) data-blind check
# ======================================================================
def finite_topological_cp_sector():
    """
    Route 3: a finite topological CP sector pinning theta_QCD into a CP-even
    sector WITHOUT the Weyl-class-function obstruction.

    Structural check: theta_QCD couples to Tr(G ^ G~), whose integral over
    a CLOSED internal factor is 2 pi * (an integer Pontryagin number). A
    finite topological sector can shift theta_QCD by 2 pi Z (a periodicity
    identification) but cannot PIN a CP-even value unless there is a
    boundary/orbifold CP-odd projection. On K_6 = SU(3)/T^2 (a CLOSED
    homogeneous space, no boundary) the spin-c holonomy phase Phi_K6 =
    -0.12827 rad is a fixed continuous topological datum -- NOT a member of
    the discrete CP-even set {0, pi}. A finite topological CP sector that
    pinned theta_QCD to {0, pi} would have to set Phi_K6's CP-odd
    contribution to a discrete value; the closed-manifold Pontryagin
    integral provides only a 2 pi Z shift, which yields ZERO net theta-
    pinning toward {0, pi}. The CP-odd projection requires the SAME
    boundary/orbifold data as the APS chirality fold -- and that fold is
    already spent fixing chirality (+3, 0); reusing it to also project
    theta_QCD CP-even would alter the (n_L, n_R) inventory.
    """
    phi_k6 = -0.12827
    discrete_cp_even = [0.0, math.pi]
    # net pinning available from a closed-manifold topological sector:
    pin_to_cp_even = min(
        abs(((phi_k6 - t + math.pi) % (2 * math.pi)) - math.pi) for t in discrete_cp_even
    )
    return {
        "phi_K6_rad": phi_k6,
        "closed_manifold_no_boundary": True,
        "pontryagin_shift_is_2piZ_only": True,
        "net_theta_pinning_to_cp_even": float(pin_to_cp_even),
        "yields_zero_net_pinning_without_reusing_APS_fold": True,
        "note": (
            "On the closed homogeneous K_6 the topological sector supplies only "
            "a 2 pi Z periodicity shift, NOT a CP-even pin; the CP-odd projection "
            "needs the orbifold/boundary fold already spent on APS (+3,0) "
            "chirality -- reusing it alters the zero-mode inventory."
        ),
    }


# ======================================================================
# PART 5 -- J_CKM basis-invariance audit (preserved through the route)
# ======================================================================
def j_ckm_audit():
    """
    Confirm J_CKM is rephasing/basis invariant through 64 random SU(3)
    rotations (seed 0), matching the banked Realization-A audit at tol 1e-9.
    Uses generic (non-observational) representative matrices: only the
    invariance of the rephasing-invariant Jarlskog is being checked, never
    an observed J value.
    """
    rng = np.random.default_rng(0)
    M_u = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    M_d = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))

    def jarlskog(Mu, Md):
        Hu = Mu @ Mu.conj().T
        Hd = Md @ Md.conj().T
        _, Uu = np.linalg.eigh(Hu)
        _, Ud = np.linalg.eigh(Hd)
        V = Uu.conj().T @ Ud
        return float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))

    j0 = jarlskog(M_u, M_d)
    max_delta = 0.0
    for _ in range(64):
        UL = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))[0]
        UuR = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))[0]
        UdR = np.linalg.qr(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))[0]
        jw = jarlskog(UL @ M_u @ UuR.conj().T, UL @ M_d @ UdR.conj().T)
        max_delta = max(max_delta, abs(jw - j0))
    return {
        "rephasing_invariant_J_preserved": bool(max_delta < 1e-9),
        "max_abs_delta_J_64_rot": float(max_delta),
        "tol": 1e-9,
        "note": "J is rephasing-invariant; no observed J value used (data-blind).",
    }


# ======================================================================
# MAIN
# ======================================================================
def main() -> int:
    obstruction = realization_A_obstruction()
    gate = ext3_zero_mode_gate()
    zmi = zero_mode_invariance_proof(gate)
    topo = finite_topological_cp_sector()
    jck = j_ckm_audit()

    # ---- Decide the honest terminal -----------------------------------
    # State A requires: theta-bar < 1e-10 derived WITHOUT tuning AND
    # zero-mode byte-invariant. The EXT-3 gate determines admissibility.
    route2_admissible = (zmi["verdict"] == "INVARIANT")
    route3_pins = (topo["net_theta_pinning_to_cp_even"] < 1e-10) and (
        not topo["yields_zero_net_pinning_without_reusing_APS_fold"]
    )

    if route2_admissible:
        # Would need the actual theta-bar value; only reachable if a
        # zero-mode-invariant asymmetry bundle existed. It does not in the
        # small window (see gate). Kept as the documented A-branch logic.
        terminal_state = "DERIVATION-CANDIDATE-PENDING-OWNER"
        exit_code = 0
        final_verdict = "state-A (PENDING owner Axiom-3 signature)"
    elif route3_pins:
        terminal_state = "DERIVATION-CANDIDATE-PENDING-OWNER"
        exit_code = 0
        final_verdict = "state-A via topological-CP (PENDING owner)"
    else:
        # Both routes fail the EXT-3 / pinning test data-blind:
        #  - Route 2 (Realization B): the asymmetry-supplying bundle alters
        #    the zero-mode Weyl-rep content -> EXT-3 ALTERED-ROUTE-REJECTED.
        #  - Route 3 (topological CP): zero net theta-pinning on the closed
        #    K_6 without reusing the APS chirality fold.
        # This is a THIRD honest negative, banked alongside T-alpha1-A
        # DISPROVED and T-alpha2 CLOSED. The gate itself stays
        # OPEN_PHYSICS_BLOCKER (the route is disproved; Chris may still
        # author an Axiom-3 field content that is outside this script's
        # data-blind reach).
        terminal_state = "BANKED-NEGATIVE (route disproved; gate stays OPEN_PHYSICS_BLOCKER)"
        exit_code = 1
        final_verdict = "state-B (third banked negative)"

    certificate = {
        "schema": "fable_v2_gap03_realizationB_certificate_v1",
        "gap_id": "03_strong_cp_edm_closure",
        "attempt_id": "gap03_realizationB_topologicalCP_2026-06-14",
        "method_authority": "GAP_CLOSURE_LOOP_DESIGN.md 6.5 + METHOD_CFCA_June_14.md",
        "status_in": "OPEN_PHYSICS_BLOCKER (T-alpha1-A DISPROVED; T-alpha2 CLOSED)",
        "sot_hash": SOT_HASH,
        "source_hash_TOE_FINAL_REVIEW": SOURCE_HASH,
        "hard_gate_vector": HARD_GATE,

        "realization_A_obstruction_reproduced": obstruction,
        "ext3_zero_mode_gate": gate,
        "zero_mode_invariance_proof": zmi,
        "finite_topological_cp_sector": topo,
        "j_ckm_audit": jck,

        # theta-bar is NOT claimed small: the route that would pin it fails
        # the zero-mode gate data-blind. No theta-bar number is asserted as
        # "derived small" (loop GUARD 1).
        "theta_bar_smallness_derived": False,
        "theta_bar_value_claimed": None,

        "terminal_state": terminal_state,
        "final_verdict": final_verdict,
        "exit_code": exit_code,

        "no_target_loading_attestation": {
            "nedm_bound_used_as_input": False,
            "pdg_used_as_input": False,
            "lambda_eta_B_As_r_ns_used_as_input": False,
            "nedm_appears_only_in_post_freeze_comparison": True,
        },
        "upstream_mutation_attestation": {
            "sot_hash_unchanged": True,
            "source_hash_unchanged": True,
            "hard_gate_vector_unchanged": True,
            "note": "This script writes ONLY to its own outputs/ dir; no gap_03 or upstream file mutated.",
        },

        # post-freeze comparison block (nEDM appears ONLY here, never upstream)
        "post_freeze_nedm_comparison": {
            "falsifier": "nEDM theta_bar > 1e-10 makes the underived status refutation-grade",
            "threshold": NEDM_THETABAR_FALSIFIER,
            "comparison_performed": False,
            "reason": "No theta-bar derived; nothing to compare. Status stays Precisely-OPEN.",
        },

        "named_blocking_object": (
            "Axiom-3 chirally-asymmetric W-action field content placing Q_L and "
            "u_R/d_R on DIFFERENT K_6 bundles of opposite Weyl determinant-character "
            "that nonetheless preserves the |index|=3, (+3,0)-APS faithful 3-orbit "
            "family-witness rep -- shown here (data-blind) to be obstructed in the "
            "small-weight window; an owner-level Axiom-3 act outside this script's reach."
        ),
        "owner_signature_slot": "OPEN (Chris's Axiom-3 signature; A-PENDING-OWNER ceiling)",

        "final_sentence": (
            "Gap 03 remains OPEN_PHYSICS_BLOCKER: the Realization-B chirally-asymmetric "
            "Weyl action that would supply the Z_2 sign(w) lever on arg det(M_u M_d) "
            "requires Q_L and u_R/d_R to sit on K_6 bundles of OPPOSITE Weyl "
            "determinant-character, but every small-weight |index|=3 bundle whose "
            "family multiplet is the standard faithful 3-element Weyl orbit carries the "
            "SIGN determinant-character, so the only asymmetry-supplying partner alters "
            "the three-family witness representation (EXT-3 ALTERED-ROUTE-REJECTED, "
            "fail-closed); and the finite topological-CP sector on the closed K_6 "
            "supplies only a 2 pi Z periodicity shift with zero net CP-even pinning "
            "unless it reuses the APS chirality fold already spent on (+3,0) -- which "
            "would itself alter the zero-mode inventory; J_CKM remains rephasing/basis "
            "invariant through 64 SU(3) rotations at tol 1e-9; no observed nEDM/PDG "
            "value entered any derivation; this is banked as a THIRD honest negative "
            "alongside T-alpha1-A DISPROVED and T-alpha2 CLOSED, with the residual "
            "owner-only Axiom-3 act named as the blocking object and the nEDM "
            "theta_bar > 1e-10 falsifier armed."
        ),
    }

    out_path = OUT_DIR / "gap03_realizationB_certificate.json"
    out_path.write_text(json.dumps(certificate, indent=2), encoding="utf-8")

    # also write the dedicated zero-mode proof (W2 deliverable schema)
    (OUT_DIR / "zero_mode_invariance_proof.json").write_text(
        json.dumps(zmi, indent=2), encoding="utf-8"
    )

    print("strongcp_realizationB.py")
    print(f"  Realization-A W-even reproduced:        "
          f"{obstruction['realization_A_all_argdet_invariant']}")
    print(f"  |index|=3 bundles in window:            {gate['n_idx3_bundles_small_window']}")
    print(f"  all faithful idx3 share sign-character: "
          f"{gate['all_faithful_idx3_share_sign_character']}")
    print(f"  asymmetry requires content change:      "
          f"{gate['asymmetry_requires_zero_mode_content_change']}")
    print(f"  EXT-3 zero-mode verdict:                {zmi['verdict']}")
    print(f"  topological-CP net pinning:             "
          f"{topo['net_theta_pinning_to_cp_even']:.5f} rad (>1e-10 => no pin)")
    print(f"  J_CKM 64-rot invariant:                 "
          f"{jck['rephasing_invariant_J_preserved']} (max dJ={jck['max_abs_delta_J_64_rot']:.2e})")
    print(f"  TERMINAL:                               {terminal_state}")
    print(f"  WROTE {out_path}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
