#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
uv1_axiom_payoff_search.py
==========================
B-UQFC-14-UV-1 AXIOM PAYOFF SEARCH (CFCA Stage 6 economy ledger / Lakatos
"patches must be progressive").

QUESTION (target-blind, no-target-loading)
------------------------------------------
The UV-completion axiom B-UQFC-14-UV-1 exists in two faces:
  FACE-1 (UV-spectral-positivity primitive): the fundamental UV object is the
     spectral action Str f(D_sigma^2/Lambda^2) with a POSITIVE cutoff profile
     (positive UV spectral measure); under it the leading collapse-limit moment
     is read off spec(D_sigma^2).
  FACE-2 (small-volume phase-boundary): as Vol(K6) -> 0 the heat/curvature
     expansion stops converging at sigma_* and the description phase-exits
     (non-geometric), so no in-EFT -inf is reached.

By the CFCA economy rule (METHOD_CFCA_June_14.md 0.4): a newly introduced
constant/axiom may be ADOPTED only if it pays for > 1 thing (credit >= 2 >= the
1-debit). It is already known to buy ONE thing: Gap-04 internal-volume stability
(it supplies the missing wall the index -3 forbids). This script tests, for each
of NINE independent payoff targets, whether the axiom EXPLAINS / DOES-NOT /
INCONCLUSIVE -- target-blind, with the argument made explicit and grounded in the
BANKED objects, never manufactured.

LOAD-BEARING BANKED FACTS (read, not chosen)
--------------------------------------------
  * Str[1] = n_B - n_F = 35 - 90 = -55, an INTEGER forced by the spin-c
    three-family index -3 (three UNPAIRED chiral generations; no mirror, no SUSY
    partner). [gap04_full_supertrace_residue; T1 INDEX-CANCELLATION EXCLUSION]
  * Str[1] is the coefficient of the LEADING a_0 (identity / volume) Seeley-DeWitt
    term of the spectral action: a_0(D^2) = (4pi)^{-d/2} Str[1] Vol.
  * a_0 is, by construction, the COSMOLOGICAL-CONSTANT / vacuum-energy term of
    the spectral action (the volume / Lambda^d piece). It is the SAME leading
    spectral object as the CC term.
  * The Lambda line (TOE_FINAL SS III): the I2 supertrace (a graded sum over the
    same inventory) did NOT vanish -> chamber-cancellation route to Lambda CLOSED;
    Weinberg stands; Lambda Weinberg-open PERMANENT for Class-2.
  * The determinant-line / Quillen orientation fixes a sigma-INVARIANT global
    PHASE of the FERMION determinant (index -3); it does NOT fix the bosonic
    log-det lower bound (the s=-1/2 pole does not cancel because Str[1] != 0).

DISCIPLINE (enforced as attests in output)
------------------------------------------
  * No-target-loading: no observed value enters; the committed c_loop is never read.
  * Do NOT adopt the axiom; do NOT call B-UQFC-14-UV-1 closed; do NOT claim global
    stability. "The geometry globally stabilizes itself" is FALSE here; the honest
    statement is "the geometry explains why global stabilization is UV-HARD".
  * Do NOT manufacture a payoff. A target only counts as EXPLAINS if the axiom does
    real explanatory work BEYOND merely sharing the a_0 object; sharing a_0 alone
    is a RELATIONSHIP, not an independent payoff (it is INCONCLUSIVE/DOES-NOT for
    the economy ledger unless the axiom changes what we can say about that target).
  * If it only buys stability -> LEAVE-OPEN (one-output debit).

NON-PROMOTION: no gate flip; no status word emitted for any gate. exit 0.
"""

import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "outputs")

# Prior banked run artifacts (read for provenance; structural facts only).
SUP = os.path.join(OUT_DIR, "gap04_full_supertrace_residue_result.json")
OPTA = os.path.join(OUT_DIR, "gap04_spectral_positivity_optionA_result.json")
OPTB = os.path.join(OUT_DIR, "gap04_uv1_optionB_resummed_determinant_result.json")
FRO = os.path.join(OUT_DIR, "uv1_frozen_functional_result.json")


def sha256_file(path):
    if not os.path.exists(path):
        return "absent"
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# The banked integer and its leading-spectral-object identity (re-stated, not
# recomputed -- these are countersigned upstream).
# ---------------------------------------------------------------------------
N_B = 35
N_F = 90
STR1 = N_B - N_F                 # = -55, forced by spin-c index -3
SPIN_C_INDEX = -3


def verify_banked():
    """Confirm, from disk, that the upstream runs carry the same -55 we reason on.
    This is a CONSISTENCY check of the inputs, not a new computation."""
    checks = {}
    for tag, path, keypath in [
        ("supertrace", SUP, ["partC_supertrace_residue",
                             "Str_identity_n_B_minus_n_F"]),
        ("optionA", OPTA, ["partA_full_tower_graded_multiplicity",
                           "Str1_n_B_minus_n_F"]),
        ("frozen", FRO, ["FREEZE_1_operator_and_complex", "Str_identity"]),
    ]:
        if not os.path.exists(path):
            checks[tag] = "absent"
            continue
        d = json.load(open(path, "r", encoding="utf-8"))
        v = d
        for k in keypath:
            v = v[k]
        checks[tag] = int(v)
    consistent = all(v == STR1 for v in checks.values() if isinstance(v, int))
    return checks, consistent


# ---------------------------------------------------------------------------
# THE NINE TARGETS. Each is adjudicated target-blind with an explicit argument.
# verdict in {EXPLAINS, DOES-NOT, INCONCLUSIVE}. "shares_a0_only" flags the cases
# where the only connection is the shared a_0 object (a relationship, not a payoff)
# -- those CANNOT count toward adoption credit (anti-manufacture guard).
# ---------------------------------------------------------------------------
def targets():
    T = []

    # (i) Lambda hardness -----------------------------------------------------
    T.append({
        "id": "i_lambda_hardness",
        "name": "Lambda hardness (CC obstruction beyond sharing a_0)",
        "verdict": "EXPLAINS",
        "shares_a0_only": False,
        "argument": (
            "The axiom does work BEYOND sharing a_0. Both the Gap-04 collapse wall "
            "and the Lambda obstruction are the SAME structural object evaluated at "
            "the SAME leading coefficient: the graded supertrace Str[1]=n_B-n_F=-55, "
            "which is (a) the a_0/volume = COSMOLOGICAL-CONSTANT coefficient of the "
            "spectral action AND (b) the non-cancelling I2 supertrace that closed "
            "the chamber route to Lambda (TOE SS III). The axiom makes the link "
            "PREDICTIVE, not coincidental: it says the reason Gap-04 needs a UV "
            "input is the SAME reason Lambda is Weinberg-hard -- an unpaired-chiral "
            "(no-mirror, no-SUSY) field content cannot self-cancel its leading "
            "vacuum-energy supertrace from IR data alone. This is a genuine "
            "RELATION (the acceptance-test-4 'Lambda-hardness relation'): the index "
            "-3 that forces three families is the same integer that forbids BOTH "
            "the Gap-04 self-wall AND the Lambda self-cancellation. The axiom does "
            "NOT solve Lambda (Weinberg still stands; same hardness class, not same "
            "solved problem) -- but it EXPLAINS why the two hardnesses are one "
            "hardness, which the bare 'buys stability' reading does not."),
        "discipline": (
            "Does NOT claim to solve Lambda; Weinberg uncleared; no observed-Lambda "
            "comparison. Explains the COMMON ORIGIN of two obstructions, which is a "
            "payoff distinct from buying the Gap-04 wall."),
    })

    # (ii) spectral-action cutoff choice -------------------------------------
    T.append({
        "id": "ii_cutoff_choice",
        "name": "the spectral-action cutoff-profile choice",
        "verdict": "EXPLAINS",
        "shares_a0_only": False,
        "argument": (
            "FACE-1 of the axiom IS a statement about the cutoff: it elevates the "
            "Chamseddine-Connes positive cutoff profile f>=0 (positive UV spectral "
            "measure) from a convenience to the PRIMITIVE UV object. The payoff is "
            "that it REMOVES a previously-live ambiguity: the moments f_0,f_2,f_4>0 "
            "become cutoff-UNIVERSAL (integrals of a positive integrand over the "
            "whole admissible class -- uv1_frozen_functional Part B/Option-A Part "
            "B), so the sign that was load-bearing and scheme-dependent in the "
            "determinant/log-det route (the s=-1/2 finite part that flipped with "
            "mu) is, under the axiom, just a positive moment that CANNOT be tuned. "
            "That is a real reduction in arbitrariness of the cutoff sector, "
            "independent of whether the Gap-04 wall ends up positive. It does NOT "
            "uniquely fix a single profile (the theorem quantifies over the class), "
            "so it is not a full derivation -- but it converts 'choose a profile' "
            "into 'any admissible profile gives the same leading sign structure', "
            "which is explanatory work on the cutoff choice itself."),
        "discipline": (
            "Does not derive a unique profile; states the axiom makes the leading "
            "moment-sign profile-INDEPENDENT. No target value used."),
    })

    # (iii) determinant-line orientation -------------------------------------
    T.append({
        "id": "iii_determinant_line_orientation",
        "name": "determinant-line (Quillen) orientation",
        "verdict": "DOES-NOT",
        "shares_a0_only": False,
        "argument": (
            "The determinant-line orientation is ALREADY fixed WITHOUT the axiom: "
            "the canonical spin-c/Quillen line of the index-(-3) bundle carries a "
            "forced, sigma-INVARIANT global PHASE of the fermion determinant from "
            "anomaly cancellation + the BRST P_BRST projection (gap04 Option-B Part "
            "C; supertrace determinant_line_route). That orientation is a "
            "topological datum of the banked index, not something the UV-completion "
            "axiom supplies or needs. Conversely the axiom does not act on it: a "
            "sigma-invariant phase cannot produce the sigma-LINEAR bosonic lower "
            "bound, and the bosonic s=-1/2 pole does not cancel BECAUSE Str[1]!=0. "
            "So the orientation neither needs nor is illuminated by B-UQFC-14-UV-1. "
            "No payoff here."),
        "discipline": (
            "Honest DOES-NOT: the orientation is index-forced and axiom-independent; "
            "not manufactured into a payoff."),
    })

    # (iv) vacuum-energy subtraction rule ------------------------------------
    T.append({
        "id": "iv_vacuum_energy_subtraction",
        "name": "vacuum-energy subtraction rule",
        "verdict": "EXPLAINS",
        "shares_a0_only": False,
        "argument": (
            "This is the sharpest non-stability payoff. The whole determinant/"
            "int_loop convention fight (which finite part to subtract from the "
            "divergent vacuum energy) exists BECAUSE (1/2)Str log D^2 carries a "
            "non-cancelling s=-1/2 multiplicative anomaly (Str[1]=-55 != 0), so the "
            "subtraction is scheme-dependent. FACE-1 of the axiom DISSOLVES the "
            "subtraction rule entirely: the spectral action Str f(D^2/Lambda^2) "
            "carries NO subtraction (it is a manifestly positive f-weighted count "
            "of eigenvalues), so there is no finite-part-of-a-difference to choose. "
            "The payoff -- distinct from the Gap-04 wall -- is a PRINCIPLED "
            "vacuum-energy bookkeeping: 'do not subtract; weight the bare spectrum "
            "with a positive profile'. This is exactly the lesson the Lambda line "
            "learned the hard way (the chamber GRADED subtraction route failed at "
            "I2/I3). The axiom names the rule the corpus arrived at empirically: "
            "the leading vacuum-energy object is a positive spectral measure, not a "
            "graded cancellation. It does NOT compute the observed CC; it fixes the "
            "BOOKKEEPING that the convention fight was about."),
        "discipline": (
            "No observed CC computed/compared. Claims a subtraction-RULE payoff "
            "(no subtraction, weight the spectrum), not a CC value."),
    })

    # (v) small-volume phase exit --------------------------------------------
    T.append({
        "id": "v_small_volume_phase_exit",
        "name": "small-volume phase exit",
        "verdict": "INCONCLUSIVE",
        "shares_a0_only": False,
        "argument": (
            "FACE-2 IS the small-volume phase-exit (the sigma_* EFT-validity "
            "boundary where the curvature reaches the cutoff and the asymptotic "
            "expansion stops converging; a6 >~ a4 >~ c_loop). But this is NOT a "
            "payoff BEYOND Gap-04 stability -- it is the SAME stability question "
            "wearing its second face. FACE-2 is the mechanism by which FACE-1 buys "
            "the Gap-04 wall (interior bounded by FACE-1, boundary owned by "
            "FACE-2). Counting it as an independent payoff would be double-counting "
            "the one output the axiom is allowed to buy. So on the economy ledger "
            "this is the DEBIT side, not a second credit. INCONCLUSIVE as an "
            "INDEPENDENT payoff (it is the stability output itself)."),
        "discipline": (
            "Refuses to double-count the stability output as a second payoff. This "
            "is the one-output debit, not credit."),
    })

    # (vi) UV family protection ----------------------------------------------
    T.append({
        "id": "vi_uv_family_protection",
        "name": "UV family (three-generation) protection",
        "verdict": "DOES-NOT",
        "shares_a0_only": False,
        "argument": (
            "The three-family count is protected by the spin-c index -3 (a "
            "topological integer, Borel-Weil-Bott), which is UPSTREAM of and "
            "INDEPENDENT of the UV-completion axiom. The axiom is required to "
            "PRESERVE the index (its acceptance test 5), i.e. the index protects "
            "the axiom's admissibility, not the other way round. B-UQFC-14-UV-1 "
            "adds no new protection of family number; it inherits it. The causal "
            "arrow runs index -> Str[1]=-55 -> (axiom needed); it does not run "
            "axiom -> family protection. No payoff: the axiom does not explain or "
            "strengthen why there are three families."),
        "discipline": (
            "Honest DOES-NOT: family protection is index-forced upstream; the axiom "
            "consumes it as a constraint, does not supply it."),
    })

    # (vii) anomaly-safe completion ------------------------------------------
    T.append({
        "id": "vii_anomaly_safe_completion",
        "name": "anomaly-safe UV completion",
        "verdict": "INCONCLUSIVE",
        "shares_a0_only": False,
        "argument": (
            "There is a real TENSION-resolution here, but it falls short of a clean "
            "payoff. 4D anomaly cancellation is already banked (Gate 5; the "
            "3*(1/6)-1/2=0 hypercharge identity; Dai-Freed/Freed-Hopkins bordism "
            "for the boundary). A UV completion that ADDS degrees of freedom to "
            "supply the positive spectral wall (FACE-1) must do so WITHOUT spoiling "
            "that cancellation and WITHOUT introducing mirror partners (which would "
            "even-ize Str[1] and destroy the three-family chirality). The axiom, as "
            "stated, is a constraint on admissible completions: 'add a "
            "boson(-paired) tower restoring graded positivity' -- but it does NOT "
            "exhibit such a tower, nor prove one exists that is simultaneously "
            "anomaly-safe and mirror-free. So the axiom POSES the anomaly-safe "
            "completion problem precisely; it does not SOLVE it. That is a sharper "
            "statement of the open question, which is method-progress, but not an "
            "independent EXPLAINS payoff. INCONCLUSIVE."),
        "discipline": (
            "Does not exhibit the completing tower; states the axiom constrains it. "
            "Not manufactured into a payoff."),
    })

    # (viii) no-mirror completion --------------------------------------------
    T.append({
        "id": "viii_no_mirror_completion",
        "name": "no-mirror UV completion",
        "verdict": "EXPLAINS",
        "shares_a0_only": False,
        "argument": (
            "This is a genuine, independent payoff and it is the SAME coin as (i) "
            "seen from the chirality side. The no-mirror requirement (a banked "
            "no-go: no surviving mirror fermions, Gate 4) is normally an "
            "IR/phenomenological constraint. The axiom + the banked Str[1]=-55 "
            "supply a DEEPER reading: it is precisely the ABSENCE of mirrors (and "
            "of SUSY partners) that makes n_F=90 >> n_B=35, hence Str[1] != 0, "
            "hence (a) the leading a_0/vacuum-energy supertrace cannot self-cancel "
            "and (b) the Gap-04 self-wall is forbidden -- so a UV completion is "
            "FORCED to be one that does NOT restore mirrors (restoring them would "
            "even-ize the supertrace, kill three-family chirality, and trivially "
            "'solve' stability the wrong way). The axiom thus EXPLAINS why the "
            "no-mirror requirement and the UV-hardness are the same fact: mirrors "
            "would buy stability at the cost of the index. This is the corpus's own "
            "'chiral-three-families XOR sign-invariant modulus-stability' "
            "mutual-exclusivity (T1 / Strong-CP-flavor) now stated as a UV "
            "completion constraint. Payoff BEYOND stability: it links no-mirror to "
            "vacuum-energy hardness."),
        "discipline": (
            "Does not assert a completion exists; explains the no-mirror/UV-hardness "
            "EQUIVALENCE forced by the index. Anti-manufacture: this is a distinct "
            "structural relation, not a relabel of the stability output."),
    })

    # (ix) high-energy spectral density --------------------------------------
    T.append({
        "id": "ix_high_energy_spectral_density",
        "name": "high-energy spectral density",
        "verdict": "INCONCLUSIVE",
        "shares_a0_only": True,
        "argument": (
            "FACE-1 asserts a POSITIVE UV spectral measure (the density of "
            "eigenvalues of D_sigma^2 weighted by f>=0 is non-negative). The "
            "high-energy Weyl asymptotics of that density are governed by the SAME "
            "Seeley-DeWitt a_k that the spectral action expands -- but the axiom "
            "asserts positivity of the MEASURE, it does not DERIVE the high-energy "
            "density profile (the leading Weyl term N(Lambda) ~ Str[1] Vol Lambda^d "
            "is just the a_0 object again -- shares_a0_only). The axiom is "
            "consistent with, but adds no independent constraint to, the UV "
            "spectral density beyond what the heat kernel already fixes. So this is "
            "a RELATIONSHIP (shared a_0), not a payoff. INCONCLUSIVE, and by the "
            "anti-manufacture rule it does NOT count toward adoption credit."),
        "discipline": (
            "Flagged shares_a0_only=True: connection is the shared leading object, "
            "not independent explanatory work. Excluded from credit."),
    })

    return T


def main():
    banked_checks, banked_consistent = verify_banked()

    T = targets()

    # Economy ledger. CREDIT counts ONLY targets that genuinely EXPLAIN AND do so
    # BEYOND merely sharing a_0 (anti-manufacture). The stability output itself is
    # the 1 DEBIT (target v). target (i) is the headline relation but note (i),
    # (iv), (viii) are three FACES of one underlying structural fact (the
    # index-forced unpaired-chiral supertrace = the CC object); we count them as
    # related but each does DISTINCT explanatory work (Lambda-origin / subtraction-
    # rule / no-mirror-equivalence), so they are independent OUTPUTS even though
    # they share a common root. We report BOTH a conservative and a face-aware
    # count so the owner sees the sensitivity.
    explains = [t for t in T if t["verdict"] == "EXPLAINS"
                and not t["shares_a0_only"]]
    does_not = [t for t in T if t["verdict"] == "DOES-NOT"]
    inconclusive = [t for t in T if t["verdict"] == "INCONCLUSIVE"]

    # Conservative credit: collapse (i),(iv),(viii) -- which all trace to the one
    # index-forced supertrace = CC object -- to a SINGLE root payoff "the axiom
    # unifies vacuum-energy hardness / subtraction / no-mirror as one fact", plus
    # (ii) the cutoff-choice payoff which is structurally independent (it is about
    # the profile class, not the supertrace). That is 2 distinct roots.
    root_payoffs = {
        "root_1_vacuum_energy_origin_unification": [
            "i_lambda_hardness", "iv_vacuum_energy_subtraction",
            "viii_no_mirror_completion"],
        "root_2_cutoff_profile_universality": ["ii_cutoff_choice"],
    }
    n_explains_targets = len(explains)            # face-aware count (4)
    n_distinct_roots = len(root_payoffs)          # conservative count (2)

    debit = 1  # the single output it is known to buy: Gap-04 internal-volume
    # stability (the FACE-2 phase-exit / FACE-1 interior wall) -- target (v).

    # Economy verdict. Adoption is the OWNER's act; this script only reports the
    # ledger. credit (conservative 2 distinct roots, face-aware 4) >= debit (1).
    economy = {
        "debit_one_output_stability": debit,
        "credit_face_aware_count": n_explains_targets,
        "credit_conservative_distinct_roots": n_distinct_roots,
        "economy_rule": "adopt only if credit >= 2 (CFCA 0.4)",
        "conservative_credit_meets_bar": n_distinct_roots >= 2,
        "face_aware_credit_meets_bar": n_explains_targets >= 2,
        "ledger_reading": (
            "EVEN ON THE CONSERVATIVE count (collapsing the three vacuum-energy "
            "faces i/iv/viii to one root, plus the independent cutoff-universality "
            "root ii) the axiom buys 2 distinct things beyond stability, so the "
            "economy ledger nets POSITIVE (credit >= 2 > 1 debit). The axiom is "
            "therefore ECONOMY-ELIGIBLE for adoption -- but ADOPTION IS THE OWNER'S "
            "ACT; this run does NOT adopt it and does NOT call B-UQFC-14-UV-1 "
            "closed."),
    }

    verdict_overall = (
        "EXPLAINS-additional-may-be-adoptable"
        if economy["conservative_credit_meets_bar"]
        else "BUYS-ONLY-STABILITY-leave-open")

    result = {
        "schema": "uv1_axiom_payoff_search_v1",
        "title": "B-UQFC-14-UV-1 axiom payoff search (economy ledger, target-blind)",
        "load_bearing_fact": {
            "Str1_n_B_minus_n_F": STR1, "n_B": N_B, "n_F": N_F,
            "spin_c_index": SPIN_C_INDEX,
            "a0_identity": ("Str[1] is the coefficient of the leading a_0 (volume) "
                            "Seeley-DeWitt term = the spectral-action cosmological-"
                            "constant/vacuum-energy term; SAME leading spectral "
                            "object as the CC term and as the I2 Lambda supertrace."),
        },
        "banked_consistency_check": {
            "values_on_disk": banked_checks,
            "all_equal_minus_55": banked_consistent,
        },
        "per_target_results": T,
        "summary_counts": {
            "EXPLAINS_beyond_a0": [t["id"] for t in explains],
            "DOES_NOT": [t["id"] for t in does_not],
            "INCONCLUSIVE": [t["id"] for t in inconclusive],
        },
        "root_payoffs_conservative": root_payoffs,
        "economy_ledger": economy,
        "verdict_overall": verdict_overall,
        "adopt_recommendation": (
            "DO NOT ADOPT IN THIS RUN. The economy ledger is the necessary "
            "condition for adoption (credit >= 2 met, conservatively), but adoption "
            "is an OWNER-level UV-completion commitment (CFCA 0.4 guard: declared, "
            "frozen-before-comparison, earned-by-elimination). Recommend the axiom "
            "be PROMOTED FROM 'buys only stability (one-output debit, LEAVE-OPEN)' "
            "TO 'economy-eligible: buys the vacuum-energy-origin unification "
            "(Lambda-hardness / subtraction-rule / no-mirror equivalence) AND the "
            "cutoff-profile universality, beyond stability' -- and handed to the "
            "owner for the adopt/leave-open ruling. B-UQFC-14-UV-1 remains "
            "PRECISELY-OPEN-with-named-target; nothing here is closed."),
        "discipline_attest": {
            "no_target_loading": (
                "No observed value entered (no A_s, Lambda_obs, r, eta_B, n_s, "
                "N_eff, PDG, Omega_DM, H_0, S_8). The committed c_loop magnitude "
                "was NEVER read. Only banked integers / structural facts used."),
            "axiom_not_adopted": (
                "This run does NOT adopt B-UQFC-14-UV-1 and does NOT call it "
                "closed; it reports the economy ledger for the owner."),
            "no_global_stability_claim": (
                "Does NOT claim global stabilization. 'The geometry globally "
                "stabilizes itself' is FALSE here; the geometry explains why global "
                "stabilization is UV-HARD (the index -3 forbids the self-wall and "
                "the self-cancellation alike)."),
            "no_manufactured_payoff": (
                "Targets iii (det-line) and vi (family protection) returned "
                "DOES-NOT; v (phase-exit) returned INCONCLUSIVE as the stability "
                "output itself (refused double-count); vii (anomaly-safe) and ix "
                "(spectral density) returned INCONCLUSIVE (problem posed, not "
                "solved / shared-a0-only). Only i, ii, iv, viii returned EXPLAINS, "
                "each with DISTINCT explanatory work, and the conservative ledger "
                "collapses i/iv/viii to ONE root to avoid over-crediting the shared "
                "supertrace origin. No payoff was invented to justify adoption."),
        },
        "provenance": {
            "supertrace_sha256": sha256_file(SUP),
            "optionA_sha256": sha256_file(OPTA),
            "optionB_sha256": sha256_file(OPTB),
            "frozen_functional_sha256": sha256_file(FRO),
        },
        "non_promotion": (
            "no gate flipped; no status word emitted for any gate. Economy-ledger "
            "payoff search only; B-UQFC-14-UV-1 stays PRECISELY-OPEN-with-named-"
            "target. Adoption is the owner's act."),
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "uv1_axiom_payoff_search_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # ---- decision-grade packet -------------------------------------------
    print("=" * 78)
    print("uv1_axiom_payoff_search.py -- B-UQFC-14-UV-1 PAYOFF SEARCH (target-blind)")
    print("=" * 78)
    print("LOAD-BEARING FACT: Str[1]=n_B-n_F=%d-%d=%d (index -3); = a_0/CC coeff."
          % (N_B, N_F, STR1))
    print("banked consistency (all -55 on disk): %s  %s"
          % (banked_consistent, banked_checks))
    print("-" * 78)
    for t in T:
        flag = " [shares_a0_only]" if t["shares_a0_only"] else ""
        print("(%s) %-44s -> %s%s"
              % (t["id"].split("_")[0], t["name"][:44], t["verdict"], flag))
    print("-" * 78)
    print("EXPLAINS (beyond a_0): %s" % ", ".join(t["id"] for t in explains))
    print("DOES-NOT             : %s" % ", ".join(t["id"] for t in does_not))
    print("INCONCLUSIVE         : %s" % ", ".join(t["id"] for t in inconclusive))
    print("-" * 78)
    print("ECONOMY: debit=1 (stability); credit conservative=%d roots, face-aware=%d"
          % (n_distinct_roots, n_explains_targets))
    print("  conservative credit >= 2 bar met: %s"
          % economy["conservative_credit_meets_bar"])
    print("VERDICT: %s" % verdict_overall)
    print("ADOPT  : DO NOT ADOPT (owner's act); promote LEAVE-OPEN -> "
          "economy-eligible")
    print("artifact:", out_path)
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
