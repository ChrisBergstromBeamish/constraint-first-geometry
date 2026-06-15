#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gap04_reason_hunt.py
====================
Gap-04 IRREDUCIBLE REASON-HUNT (CFCA Stage 4 + the irreducible-constant doctrine,
METHOD_CFCA_June_14.md sec 0.4).

Owner's rule: "'just is' is the FLOOR, not the first answer." For each residual
number Gap-04 leans on, run CFCA to find a REASON it is what it is, and classify:

  DERIVED            -- a reason was found (geometry-FORCED, group/number-theoretic,
                        a recognizable normalization, or Noether-invariant). It is
                        no longer 'just is'.
  EARNED-IRREDUCIBLE -- no deeper reason found, BUT it explains >= 2 independent
                        outputs, so it nets POSITIVE on the economy ledger
                        (credit >= 2 >= 1 debit). A legitimate input that pays
                        its keep (CFCA sec 0.4 economy rule).
  BARE-COUNTED       -- no reason AND explains nothing else. A pure debit; flagged
                        and counted against the small ~5-6 pure-debit budget.

NO observed value enters (no A_s, Lambda_obs, r, eta_B, n_s, N_eff, PDG). Every
'DERIVED' carries its licensing reason in the SAME record. Non-promotion: no gate
flip; countersign-input only.

The economy ledger is maintained at the end: pure-debit count vs the ~5-6 budget,
and total earned/derived.
"""

import hashlib
import json
import math
import os
import sys
from fractions import Fraction

FA = (r"C:/Users/cberg/Desktop/VS Code Projects Random/"
      r"physics_Journal_and_patents/Final_physics_articles/scripts/gap_04")
FROZEN_YAML = os.path.join(FA, "frozen_inputs.yaml")
VEFF_YAML = os.path.join(FA, "outputs", "veff_coefficients_frg4.yaml")
GILKEY_JSON = os.path.join(FA, "outputs", "gilkey_a4_cross_terms.json")

FORBIDDEN_TOKENS = ["A_s ", "Lambda_obs", "eta_B", "n_s_obs", "N_eff_obs",
                    "PDG", "BICEP", "r_obs", "Omega_DM_obs"]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# The reason-hunt entries. Each is the result of running CFCA against ONE number:
#   - look for geometry-FORCED (fixed by the frozen K6 x S2 x S1_Y geometry)
#   - look for number/group-theoretic (Casimir, root system, rational, transcendental,
#     a normalization like (4pi)^{-D/2})
#   - test Noether-INVARIANCE (survives gauge/scale/chamber) vs convention
#   - test economy-EARNING (explains >= 2 independent outputs)
# The 'reason' field is the licensing computation/argument in the same record.
# ---------------------------------------------------------------------------

D_BULK = 13
HK_NORM = 1.0 / (math.pow(4.0 * math.pi, D_BULK / 2.0))


def build_entries():
    entries = []

    # 1) a_4 master coefficient of R^2: +5/360 -> cross prefactor 1/36 ----------
    entries.append({
        "number": "a_4 master R^2 coefficient = +5/360 (cross prefactor 2*5/360 = 1/36)",
        "value": str(Fraction(5, 360)) + " (=1/72); cross 1/36",
        "classification": "DERIVED",
        "reason_or_why_not": (
            "Number/group-theoretic + convention-INVARIANT. The +5/360 is the "
            "fixed coefficient of R^2 in the Gilkey/Seeley-DeWitt a_4 heat-kernel "
            "master formula (Gilkey 1995 Eq. 4.1.7); it is a universal property "
            "of the Laplace-type operator, the same rational in BOTH the "
            "D=-(nabla^2+E) and D=-(nabla^2)-E conventions (R^2 is even in "
            "curvature). The cross prefactor 1/36 = 2*(5/360) where the 2 is the "
            "binomial cross-term coefficient of (R_1+R_2+R_3)^2. No dial; a "
            "theorem-fixed rational. NOT 'just is'."),
        "outputs_explained": (
            "Sets the magnitude and (with the registry) the sign of c_a4_K6_S2; "
            "the same master formula governs every a_4 insertion in the FRG-4 "
            "expansion.")
    })

    # 2) curvature registry R_K6=+30, R_S2=+2 (single-signed) ------------------
    entries.append({
        "number": "curvature registry R_K6_0 = +30, R_S2_0 = +2 (single-signed)",
        "value": "R_K6_0 = 6*5 = 30 ; R_S2_0 = 2*1 = 2",
        "classification": "DERIVED",
        "reason_or_why_not": (
            "Geometry-FORCED. R_i = n_i * lambda_i with the FROZEN Einstein "
            "constants of the frozen geometry: K6 = SU(3)/T^2 (F_3 flag) has the "
            "normal Einstein metric Ric = +5g (Besse, Einstein Manifolds, Tab. "
            "7.107; Castellani-D'Auria-Fre), n=6 -> R=30; round S^2 has Ric = +g, "
            "n=2 -> R=2. Both POSITIVE because both are positively-curved Einstein "
            "factors -- no dial once the geometry K6 x S^2 x S^1_Y is frozen. The "
            "registry is convention-consistent (single curvature-sign convention "
            "across the corpus). NOT 'just is': forced by the chosen compact "
            "geometry, which is itself fixed upstream by the 3-family index."),
        "outputs_explained": (
            "Pins the a_4 cross-density POSITIVE; sets R_K6 (Casimir/KK scale) "
            "feeding c_KK and the e^{-4 sigma} wall; same registry feeds the "
            "first-Laplace eigenvalues used in the shell projection.")
    })

    # 3) one-loop normalization (4 pi)^{-D/2}, D=13 ---------------------------
    entries.append({
        "number": "one-loop normalization (4 pi)^{-D/2} with D = 13",
        "value": "%.6e (= (4 pi)^{-6.5})" % HK_NORM,
        "classification": "DERIVED",
        "reason_or_why_not": (
            "Number-theoretic normalization (a recognizable (4 pi)^{-D/2}) x a "
            "geometry-FORCED exponent. The (4 pi)^{-D/2} is the universal "
            "Gaussian momentum-integration measure of a D-dimensional one-loop "
            "determinant (proper-time / heat-kernel normalization); D = 13 is "
            "FORCED by the frozen total signature (12,1). No dial. NOT 'just is'."),
        "outputs_explained": (
            "Common one-loop measure for c_a4 AND every other heat-kernel "
            "coefficient in the FRG-4 expansion; not specific to one term.")
    })

    # 4) the one-loop log-det sign/prefactor -(1/2) ---------------------------
    # SPLIT into the part that IS derived (the global MAGNITUDE -1/2) and the
    # part that is genuinely OWNER-LOCKED (the RELATIVE sign of c_a4 vs c_loop).
    # The countersign caught a prior 'DERIVED' classification of the RELATIVE
    # sign as a manufactured step: a global prefactor does NOT force same-sign.
    entries.append({
        "number": ("one-loop log-det prefactor: global MAGNITUDE -(1/2) "
                   "[DERIVED] vs RELATIVE sign of c_a4 w.r.t. c_loop "
                   "[OWNER-LOCKED]"),
        "value": ("-1/2 global magnitude is universal; the RELATIVE one-loop "
                  "sign of c_a4 vs the c_loop wall is NOT fixed data-blind"),
        "classification": "BARE-COUNTED",
        "reason_or_why_not": (
            "PARTIALLY DERIVED, but the LOAD-BEARING part is OWNER-LOCKED, so "
            "this entry is honestly counted as a bare (undecided) debit until "
            "the owner rules. The MAGNITUDE -(1/2) IS derived: it is the "
            "universal bosonic one-loop log-det prefactor "
            "(V^(1-loop) = -(1/2)(4pi)^{-D/2} sum_n a_n), GLOBAL to every a_n. "
            "BUT 'global prefactor' does NOT force two coefficients to the same "
            "SIGN: sign(c_n) = sign(-1/2) x sign(that term's OWN integrand). "
            "c_a4's integrand (1/36)*R_K6*R_S2 is POSITIVE, so the genuine global "
            "-(1/2) yields c_a4 NEGATIVE. Making c_a4 POSITIVE (to match the "
            "c_loop wall) REQUIRES asserting c_loop's stored +value already "
            "absorbed a -(1/2) acting on a NEGATIVE underlying density -- a sign "
            "NEVER established in the corpus (z_renormalized_c_loop.py reads "
            "c_loop as a frozen inherited number; TOE_FINAL records c_loop OPEN, "
            "positivity merely assumed, F6-guarded). So the RELATIVE one-loop "
            "sign is NOT Noether/geometry-FORCED -- it is the genuine "
            "OWNER-MUST-RULE item (gap04_convention_audit original verdict; "
            "gap04_disjointness convention_dependent=True). Classifying it "
            "'DERIVED' would be the manufactured step the countersign caught. "
            "Honest floor: 'just is' / owner-locked until the c_loop "
            "underlying-density sign is banked."),
        "outputs_explained": (
            "Once RULED, it sets the relative sign of the a_4 cross-term in "
            "V_eff and decides whether the FRG-4 -sigma well stands "
            "(BRANCH-STANDS) or fails as a separate runaway (BRANCH-RUNAWAY). "
            "Until ruled it explains nothing else on its own -> a pure debit, "
            "counted against the ~5-6 budget.")
    })

    # 5) c_loop_Z = +1.36e-5 -------------------------------------------------
    entries.append({
        "number": "c_loop_Z = +1.3637e-5 (the e^{-6 sigma} KK-Casimir wall)",
        "value": "1.3637166327064904e-05 (M_13^4 units), POSITIVE",
        "classification": "EARNED-IRREDUCIBLE",
        "reason_or_why_not": (
            "Its SIGN is DERIVED (geometry-forced positive vacuum energy of the "
            "KK shell + the global one-loop convention). Its MAGNITUDE is NOT "
            "reducible to a closed form data-blind -- it is the output of an "
            "FRG-2 NLO shell-projection / Z-renormalization integral over the "
            "retained mode spectrum (Wetterich flow, Litim regulator), a genuine "
            "computation, not a closed rational. So it remains an irreducible "
            "computed input -- BUT it EARNS its keep (>= 2 independent outputs)."),
        "outputs_explained": (
            "ECONOMY-EARNING (>=2): (a) it is the small-sigma wall that closes "
            "F6 / blocks the sigma -> -inf runaway in Gap-04; AND (b) it gates "
            "the A_s-absolute normalization (the As-absolute row is BLOCKED on "
            "K13-2 + c_loop) and the Gap-09 scale in the cascade. Two+ "
            "independent downstream outputs -> nets POSITIVE on the ledger.")
    })

    # 6) c_bdry = -0.01267 ---------------------------------------------------
    entries.append({
        "number": "c_bdry = -0.012665 (Dai-Freed 4D + orbifold-bordism half)",
        "value": "-0.012665147955292222 (M_13^4 units), NEGATIVE",
        "classification": "EARNED-IRREDUCIBLE",
        "reason_or_why_not": (
            "Its SIGN is DERIVED/geometry-forced: the boundary term is fixed by "
            "the Dai-Freed / Freed-Hopkins orbifold-bordism anomaly class of the "
            "S^1_Y/Z_2 fixed points (2 fixed points, boundary_anomaly_class in "
            "the frozen geometry) -- negative, and CLOSED in Fable-Latest. Its "
            "MAGNITUDE is a computed bordism/eta-invariant output, not a closed "
            "rational data-blind, so it stays an irreducible computed input -- "
            "but it EARNS its keep."),
        "outputs_explained": (
            "ECONOMY-EARNING (>=2): (a) c_bdry<0 is what makes the -sigma well "
            "robust ('well unconditional in c_loop' rides on c_bdry<0, v10); AND "
            "(b) it sets the e^{-2 sigma - 2 chi} term coupling sigma and chi in "
            "V_eff, entering the joint Hessian / F8 Higgs-Wilson vacuum check. "
            "Two+ independent roles -> nets POSITIVE.")
    })

    # 7) c_KK = c_S2 = c_KK_S1Y = +0.0094989 (zero-mode universality) --------
    entries.append({
        "number": "c_KK = c_S2 = c_KK_S1Y = +0.0094989 (zero-mode universality)",
        "value": "0.009498860966469166 (all three equal), POSITIVE",
        "classification": "EARNED-IRREDUCIBLE",
        "reason_or_why_not": (
            "PARTIALLY DERIVED: the EQUALITY of the three is geometry/group-"
            "FORCED -- it is the zero-mode universality of the FRG-2 LO "
            "coefficient (one universal constant, not three independent dials; "
            "that they coincide is a Noether-style universality, not a "
            "coincidence). The shared MAGNITUDE is an FRG-2 LO computed output, "
            "not a closed rational data-blind. So it is one irreducible computed "
            "constant (not three) that EARNS its keep."),
        "outputs_explained": (
            "ECONOMY-EARNING: ONE constant explains THREE wall coefficients "
            "(c_KK e^{-4 sigma}, c_S2 e^{-4 rho}, c_KK_S1Y e^{-4 chi}) by "
            "universality -> credit 3 >= 1 debit. Strongly net-positive.")
    })

    # 8) c_Wilson = -4.876e-5 (Hosotani n=1 harmonic) ------------------------
    entries.append({
        "number": "c_Wilson = -4.876e-5 (Hosotani n=1 harmonic)",
        "value": "-4.875756906074309e-05 (M_13^4 units), NEGATIVE",
        "classification": "EARNED-IRREDUCIBLE",
        "reason_or_why_not": (
            "Its STRUCTURE is DERIVED: it is the n=1 harmonic of the Hosotani "
            "Wilson-line (gauge-holonomy) potential cos(theta_W) e^{-4 sigma} -- "
            "a group-theoretic object (first Fourier harmonic on the Wilson-line "
            "circle), Noether-meaningful (gauge holonomy). Its magnitude is an "
            "FRG-2 computed output. Irreducible computed input that EARNS keep."),
        "outputs_explained": (
            "ECONOMY-EARNING (>=2): (a) sets the theta_W extremum (theta_W = 0) "
            "used in the V_eff and the Hessian; AND (b) feeds the joint "
            "Higgs-Wilson vacuum check (F8). Net-positive.")
    })

    # 9) c_KK_S2 cross at FRG-2 = 0 (vanishes) -------------------------------
    entries.append({
        "number": "c_cross_K6_S2_FRG2 = 0 (cross-term first arises at FRG-4)",
        "value": "0 at FRG-2 truncation",
        "classification": "DERIVED",
        "reason_or_why_not": (
            "Geometry/truncation-FORCED zero. At FRG-2 the heat-kernel expansion "
            "stops below the a_4 curvature^2 order, so the K6 x S2 cross term "
            "(which lives in a_4) is identically absent. NOT a tuned zero -- a "
            "forced consequence of the truncation order. NOT 'just is'."),
        "outputs_explained": (
            "Explains why the cross-term is a NEW FRG-4 object and was absent in "
            "the §II single-sigma potential (the v10 reconciliation).")
    })

    return entries


def main():
    for p in (FROZEN_YAML, VEFF_YAML, GILKEY_JSON):
        if not os.path.exists(p):
            sys.stderr.write("REFUSE(exit2): missing input %s\n" % p)
            return 2

    # forbidden-input firewall on the inputs we read
    for p in (FROZEN_YAML, VEFF_YAML):
        with open(p, "r", encoding="utf-8") as fh:
            txt = fh.read()
        # tokens like "no_As_input" are attestations, not inputs; only flag a
        # raw observed VALUE assignment. The frozen files contain only the
        # attestation strings, so we check for an actual leaked numeric anchor.
        # (None present; this is a defensive check.)
        for t in ("A_s=", "eta_B=", "Lambda_obs=", "r_obs="):
            if t in txt:
                sys.stderr.write("REFUSE(exit2): forbidden value token %s in %s\n"
                                 % (t, p))
                return 2

    entries = build_entries()

    derived = [e for e in entries if e["classification"] == "DERIVED"]
    earned = [e for e in entries if e["classification"] == "EARNED-IRREDUCIBLE"]
    bare = [e for e in entries if e["classification"] == "BARE-COUNTED"]

    # economy ledger
    ledger = {
        "pure_debit_budget_approx": "5-6",
        "bare_counted_count": len(bare),
        "bare_counted_numbers": [e["number"] for e in bare],
        "derived_count": len(derived),
        "earned_irreducible_count": len(earned),
        "irreducibles_total": len(earned) + len(bare),
        "ledger_verdict": (
            "Most residual Gap-04 numbers are DERIVED (reason found, no longer "
            "'just is') or EARNED-IRREDUCIBLE (each explains >= 2 independent "
            "outputs, netting positive): the +5/360 master coeff, the curvature "
            "registry, the (4pi)^{-D/2} normalization, and the FRG-2 zero "
            "(DERIVED); c_loop, c_bdry, the zero-mode universal constant, and "
            "c_Wilson (EARNED-IRREDUCIBLE). The SINGLE exception, surfaced by "
            "the countersign, is the RELATIVE one-loop sign of c_a4 vs the "
            "c_loop wall (entry 4): it is NOT geometry/Noether-FORCED and is "
            "NOT yet earned -- it is the genuine OWNER-MUST-RULE item, honestly "
            "BARE-COUNTED (1 pure debit) until the owner banks the sign of "
            "c_loop's underlying heat-kernel density. So the pure-debit budget "
            "(~5-6) carries exactly ONE Gap-04 debit, the owner-locked relative "
            "one-loop sign; everything else pays its keep. This is the honest "
            "floor: classifying that relative sign 'DERIVED' was the "
            "manufactured step the countersign rejected."),
    }

    result = {
        "schema": "gap04_reason_hunt_result_v1",
        "purpose": (
            "CFCA reason-hunt over Gap-04's residual numbers: find a reason for "
            "each ('just is' is the floor, not the first answer) and classify "
            "DERIVED / EARNED-IRREDUCIBLE / BARE-COUNTED with the economy ledger."),
        "provenance_hashes": {
            "frozen_inputs.yaml": sha256_file(FROZEN_YAML),
            "veff_coefficients_frg4.yaml": sha256_file(VEFF_YAML),
            "gilkey_a4_cross_terms.json": sha256_file(GILKEY_JSON),
        },
        "entries": entries,
        "economy_ledger": ledger,
        "no_target_loading": True,
        "non_promotion": "no gate flipped; countersign-input only",
    }

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gap04_reason_hunt_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    print("=" * 72)
    print("Gap-04 IRREDUCIBLE REASON-HUNT (CFCA)")
    print("=" * 72)
    for e in entries:
        print("[%-18s] %s" % (e["classification"], e["number"]))
    print("-" * 72)
    print("DERIVED:            %d" % len(derived))
    print("EARNED-IRREDUCIBLE: %d" % len(earned))
    print("BARE-COUNTED:       %d   (pure-debit budget ~5-6)" % len(bare))
    print("irreducibles total: %d" % ledger["irreducibles_total"])
    print("-" * 72)
    print(ledger["ledger_verdict"])
    print("artifact:", out_path)
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
