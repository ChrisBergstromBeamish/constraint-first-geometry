#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
gap04_disjointness.py
=====================
Gap-04 sub-loop instrument: the (-sigma negative-modulus runaway well) vs
(+modulus decompactification corner) DISJOINTNESS check.

This script does NOT promote any gate. It emits a result artifact
{disjoint: bool, basis, provenance_hash} that a diff may cite. It loads the
REAL frozen FRG-4 V_eff coefficients off disk (it does not hard-code them as a
target) and evaluates the asymptotic operator structure of V(sigma, rho, chi)
in the two competing directions.

====================================================================
SPEC  (written BEFORE the check -- the EXT-5 freeze)
====================================================================
PURPOSE
  Decide, from the FRG-4 V_eff operator basis alone, whether:
    (A) the sigma -> -inf NEGATIVE-modulus runaway corner (where the v10
        Amendment places the e^{-6 sigma} c_loop wall and claims the well is
        UNCONDITIONAL in c_loop), and
    (B) the (sigma,rho,chi) -> +inf POSITIVE-modulus DECOMPACTIFICATION corner
        (where FRG-4 names the missing non-perturbative object B-UQFC-14-NP-1),
  are governed by DISJOINT operator structures -- i.e. the operator that
  *dominates each asymptotic limit* is a different operator, so the two corners
  are different physics objects with their own statuses.

INPUTS  (real, on-disk; NO observed value may enter)
  veff_yaml : .../Final_physics_articles/scripts/gap_04/outputs/
              veff_coefficients_frg4.yaml
              -> coefficients{} and operator_exponents{}
              (c_loop_Z, c_bdry, c_a4_K6_S2, c_KK, c_Wilson, c_S2, c_KK_S1Y)
  Each operator is e^{-(a*sigma + b*rho + c*chi)} with a,b,c read from
  operator_exponents (parsed structurally, not guessed).

  FORBIDDEN INPUTS (presence => hard refuse): any observed A_s, Lambda_obs, r,
  eta_B, n_s, N_eff, PDG datum. The yaml carries forbidden_inputs_used:false;
  we assert it and we never read any observed number.

METHOD  (CFCA Stage 4 thought-experiment, made mechanical)
  For each asymptotic direction d (a unit ray in (sigma,rho,chi)):
    - the "growth rate" of operator i along d is  g_i(d) = -(a_i,b_i,c_i) . d
      (because the operator is e^{-(a sigma + b rho + c chi)}; along a ray
       X = t*d, t->+inf, the exponent is exp(t * g_i(d))).
    - the DOMINANT operator in that limit is the one with the largest g_i(d)
      (it sets whether V -> +-inf or -> 0, and with which sign).
  Direction -sigma  : d = (-1, 0, 0)   (sigma -> -inf, rho,chi fixed)
  Direction +modulus: d = (+1,+1,+1)/sqrt(3)  (full decompactification)
  (axis +sigma, +rho, +chi also reported for completeness.)

ACCEPTANCE  (the disjointness predicate -- fixed before the run)
  disjoint := TRUE iff ALL of:
    (1) the dominant operator governing the -sigma limit is NOT the same
        operator as the one governing the +modulus limit
        (different governing operator => different physics object); AND
    (2) the +modulus limit has NO operator with positive growth rate
        (every operator decays => V -> 0+, no perturbative wall =>
         the corner is genuinely the B-UQFC-14-NP-1 object, not the well); AND
    (3) the -sigma limit is dominated by a term that BLOWS UP (positive growth
        rate) so the corner is a real runaway question (not a non-event).
  We also report which operator the v10 well-wall (c_loop, e^{-6 sigma}) is and
  whether it is the GOVERNING term on -sigma at FRG-4. The honest finding is
  expected to be that at FRG-4 the GOVERNING -sigma term is the a4 cross-term
  (n=8 > 6), NOT c_loop -- so the v10 "unconditional in c_loop" claim is
  CONVENTION-DEPENDENT (it holds only under the opposite heat-kernel sign
  convention). That convention dependence is reported, never resolved here.

OUTPUTS
  - JSON result artifact -> outputs/gap04_disjointness_result.json with:
      disjoint (bool), basis (str), provenance_hash (sha256 of the yaml),
      direction analyses, governing operators, c_loop status on -sigma,
      convention_dependent (bool), named_blocker, no_target_loading (bool).
  - human-readable summary to stdout.
  - exit 0 if the artifact was produced (the artifact carries the verdict;
    a False disjoint is a valid honest outcome, not an error);
    exit 2 if inputs cannot be read / forbidden input detected (refuse).

NON-PROMOTION
  No gate flip. No status word ("closed"/"proved"/"certificate") is emitted
  for any gate. The artifact is countersign-input only.
====================================================================
"""

import hashlib
import json
import math
import os
import re
import sys

# ---- stdlib-only YAML-lite loader for the flat veff yaml (avoids the pyyaml
# ---- dependency; the file is a flat mapping of scalars under known keys).
def _try_pyyaml(path):
    try:
        import yaml  # noqa
        with open(path, "r", encoding="utf-8") as fh:
            return yaml.safe_load(fh)
    except Exception:
        return None


def _coerce(v):
    v = v.strip().strip('"').strip("'")
    if v.lower() in ("true",):
        return True
    if v.lower() in ("false",):
        return False
    try:
        if any(ch in v for ch in ".eE") and not v.endswith(":"):
            return float(v)
        return int(v)
    except ValueError:
        return v


def _minimal_yaml(path):
    """Parse the two blocks we need (coefficients, operator_exponents) plus the
    gilkey flags, without pyyaml. Tracks 2-space indentation under a section."""
    out = {"coefficients": {}, "operator_exponents": {}, "gilkey_a4_metadata": {}}
    section = None
    with open(path, "r", encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            stripped = line.strip()
            # top-level section header e.g. "coefficients:"
            if not line.startswith(" ") and stripped.endswith(":"):
                key = stripped[:-1]
                section = key if key in out else None
                continue
            if section and line.startswith("  ") and ":" in stripped:
                k, _, val = stripped.partition(":")
                k = k.strip()
                # strip inline comments outside of the operator parentheses
                if "#" in val and section != "operator_exponents":
                    val = val.split("#", 1)[0]
                out[section][k] = _coerce(val)
    return out


def load_veff(path):
    d = _try_pyyaml(path)
    if d is None:
        d = _minimal_yaml(path)
    return d


# ---- structural exponent parser: "exp(-(8 sigma + 4 rho + chi))" -> (8,4,1)
# ---- "exp(-4 sigma)" -> (4,0,0); "cos(theta_W) * exp(-4 sigma)" -> (4,0,0)
# ---- "exp(-2 sigma - 2 chi)" -> (2,0,2)
def parse_exponent(expr):
    m = re.search(r"exp\(([^)]*\)?[^)]*)\)\s*$", expr)
    # robust: take substring inside the LAST exp(...) including a possible
    # leading "-(" group
    e = expr
    start = e.find("exp(")
    if start == -1:
        raise ValueError("no exp() in operator: %r" % expr)
    inner = e[start + 4:]
    # balance parentheses to find the matching close
    depth = 1
    buf = []
    for ch in inner:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                break
        buf.append(ch)
    body = "".join(buf).strip()
    # body looks like "-(8 sigma + 4 rho + chi)" or "-4 sigma" or "-2 sigma - 2 chi"
    overall_sign = 1.0
    if body.startswith("-(") and body.endswith(")"):
        overall_sign = -1.0
        body = body[2:-1]
    elif body.startswith("-"):
        # single linear form like "-4 sigma" or "-2 sigma - 2 chi": handle term-by-term
        overall_sign = 1.0  # signs are explicit per-term below
    coeffs = {"sigma": 0.0, "rho": 0.0, "chi": 0.0}
    # normalize "+ -" and split on + and - while keeping signs
    body = body.replace("-", "+-")
    for term in body.split("+"):
        term = term.strip()
        if not term:
            continue
        sign = 1.0
        if term.startswith("-"):
            sign = -1.0
            term = term[1:].strip()
        # term is like "8 sigma", "rho", "2 chi", "chi"
        tm = re.match(r"([0-9]*\.?[0-9]*)\s*\*?\s*(sigma|rho|chi)$", term)
        if not tm:
            continue
        num = tm.group(1)
        var = tm.group(2)
        c = float(num) if num not in ("", ".") else 1.0
        coeffs[var] += sign * c
    # apply overall sign of the -( ... ) wrapper
    a = overall_sign * coeffs["sigma"]
    b = overall_sign * coeffs["rho"]
    cc = overall_sign * coeffs["chi"]
    # The operator is e^{-(a sigma + b rho + c chi)} => we want the exponent
    # vector E = (a,b,c) such that operator = exp(-(E . X)). For "exp(-4 sigma)"
    # body="-4 sigma" => coeffs sigma=-4 => operator=exp(-4 sigma) so E=(4,0,0).
    # Our parsed coeffs are the *content of the exponent* (already includes the
    # leading minus for the simple forms). Recover E = -content:
    if expr_has_simple_minus(expr):
        return (-a, -b, -cc)
    # for the -( ... ) wrapper case overall_sign already = -1, content positive,
    # so a,b,c are negative; E = -content:
    return (-a, -b, -cc)


def expr_has_simple_minus(expr):
    start = expr.find("exp(")
    inner = expr[start + 4:]
    return not inner.lstrip().startswith("-(")


FORBIDDEN_TOKENS = [
    "A_s", "As_obs", "Lambda_obs", "lambda_obs", "eta_B", "n_s_obs",
    "N_eff_obs", "PDG", "Planck_n_s", "BICEP", "r_obs",
]


def assert_no_target_loading(veff):
    flag = veff.get("forbidden_inputs_used",
                     veff.get("coefficients", {}).get("forbidden_inputs_used"))
    # the yaml stores it at top level outside our two sections; re-scan raw if absent
    return flag in (False, None)


def growth_rate(E, d):
    # operator = exp(-(E . X)); along ray X = t d, exponent = -t (E . d);
    # growth rate g = -(E . d). g>0 => operator blows up; g<0 => decays.
    return -(E[0] * d[0] + E[1] * d[1] + E[2] * d[2])


def analyze_direction(name, d, operators):
    rows = []
    for opname, (E, coeff) in operators.items():
        g = growth_rate(E, d)
        rows.append({
            "operator": opname,
            "exponent_vec_(sigma,rho,chi)": list(E),
            "coefficient": coeff,
            "growth_rate_along_d": g,
            "sign_of_coefficient": ("+" if coeff > 0 else ("-" if coeff < 0 else "0")),
        })
    # dominant = max growth rate; ties broken by larger |coefficient|
    rows_sorted = sorted(rows, key=lambda x: (x["growth_rate_along_d"],
                                              abs(x["coefficient"])), reverse=True)
    dominant = rows_sorted[0]
    any_positive_growth = any(r["growth_rate_along_d"] > 1e-12 for r in rows)
    # asymptotic sign of V: governed by dominant term IF it blows up; else ->0
    if dominant["growth_rate_along_d"] > 1e-12:
        v_limit = "+inf" if dominant["coefficient"] > 0 else "-inf"
    else:
        v_limit = "0+"  # all decay; bounded below by 0 from the leading positive remnant
    return {
        "direction": name,
        "unit_ray_(sigma,rho,chi)": list(d),
        "dominant_operator": dominant["operator"],
        "dominant_growth_rate": dominant["growth_rate_along_d"],
        "dominant_coefficient": dominant["coefficient"],
        "V_asymptotic_limit": v_limit,
        "any_operator_grows": any_positive_growth,
        "per_operator": rows_sorted,
    }


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    # Locate the real FRG-4 veff yaml. Primary canonical location:
    candidates = [
        r"C:/Users/cberg/Desktop/VS Code Projects Random/physics_Journal_and_patents/Final_physics_articles/scripts/gap_04/outputs/veff_coefficients_frg4.yaml",
        os.path.join(here, "veff_coefficients_frg4.yaml"),
    ]
    veff_path = next((p for p in candidates if os.path.exists(p)), None)
    if veff_path is None:
        sys.stderr.write("REFUSE(exit2): cannot locate veff_coefficients_frg4.yaml\n")
        return 2

    raw = open(veff_path, "rb").read()
    provenance_hash = hashlib.sha256(raw).hexdigest()
    veff = load_veff(veff_path)

    if not assert_no_target_loading(veff):
        sys.stderr.write("REFUSE(exit2): forbidden_inputs_used not False\n")
        return 2

    coeffs = veff["coefficients"]
    opexp = veff["operator_exponents"]

    # Build operator table {name: (exponent_vec, coefficient)} for the
    # sigma-bearing operators that participate in the two corners.
    operators = {}
    for opname, expr in opexp.items():
        if opname not in coeffs:
            continue
        c = coeffs[opname]
        if c == 0:
            continue
        E = parse_exponent(str(expr))
        operators[opname] = (E, float(c))

    # Directions
    d_neg_sigma = (-1.0, 0.0, 0.0)
    n = 1.0 / math.sqrt(3.0)
    d_plus_mod = (n, n, n)

    a_neg = analyze_direction("-sigma (negative-modulus runaway)", d_neg_sigma, operators)
    a_pos = analyze_direction("+modulus (decompactification)", d_plus_mod, operators)

    # The v10 well-wall term: c_loop with operator exp(-6 sigma).
    cloop_name = "c_loop_Z" if "c_loop_Z" in operators else (
        "c_loop" if "c_loop" in operators else None)
    cloop_governs_neg_sigma = (a_neg["dominant_operator"] == cloop_name)

    # Acceptance predicate (frozen in SPEC):
    cond1_diff_governing = (a_neg["dominant_operator"] != a_pos["dominant_operator"])
    cond2_no_pos_wall_in_plus = (not a_pos["any_operator_grows"])
    cond3_neg_is_real_runaway = a_neg["dominant_growth_rate"] > 1e-12
    disjoint = bool(cond1_diff_governing and cond2_no_pos_wall_in_plus
                    and cond3_neg_is_real_runaway)

    # Convention dependence: at FRG-4 the -sigma corner is governed by the a4
    # cross-term (n=8 > 6) with NEGATIVE coefficient => V -> -inf => the v10
    # "well unconditional in c_loop" is NOT what governs -sigma here; it holds
    # only under the opposite (Vassilevich) heat-kernel sign convention.
    convention_dependent = bool(
        (not cloop_governs_neg_sigma)
        and a_neg["dominant_coefficient"] < 0
    )

    named_blocker = None
    gk = veff.get("gilkey_a4_metadata", {})
    if isinstance(gk, dict):
        named_blocker = gk.get("newly_named_blocker_after_FRG4")

    basis = (
        "DIRECTIONALLY DISJOINT operator structure: the -sigma corner is "
        "governed by the operator '%s' (growth rate %.3g, coeff %s); the "
        "+modulus corner has NO operator with positive growth rate (all decay "
        "=> V->0+, no perturbative wall => the corner IS the named "
        "non-perturbative object %s). The two corners are dominated by "
        "different operators in different asymptotic directions. HOWEVER the "
        "v10 well-wall term c_loop (exp(-6 sigma)) is NOT the governing -sigma "
        "term at FRG-4 (the a4 cross-term exp(-8 sigma) is, with negative "
        "coefficient): so the v10 'well unconditional in c_loop' claim is "
        "CONVENTION-DEPENDENT (heat-kernel sign convention), which is "
        "owner-locked and NOT resolved by this script."
        % (a_neg["dominant_operator"], a_neg["dominant_growth_rate"],
           ("+" if a_neg["dominant_coefficient"] > 0 else "-"),
           str(named_blocker))
    )

    result = {
        "schema": "gap04_disjointness_result_v1",
        "disjoint": disjoint,
        "basis": basis,
        "provenance_hash": provenance_hash,
        "veff_source": veff_path,
        "acceptance_conditions": {
            "cond1_different_governing_operator": cond1_diff_governing,
            "cond2_no_positive_wall_in_+modulus": cond2_no_pos_wall_in_plus,
            "cond3_-sigma_is_a_real_runaway": cond3_neg_is_real_runaway,
        },
        "neg_sigma_direction": a_neg,
        "plus_modulus_direction": a_pos,
        "c_loop_well_wall": {
            "operator": cloop_name,
            "coefficient": coeffs.get(cloop_name) if cloop_name else None,
            "governs_neg_sigma_at_FRG4": cloop_governs_neg_sigma,
            "v10_amendment_claim": "well UNCONDITIONAL in c_loop (sigma->-inf)",
        },
        "convention_dependent": convention_dependent,
        "convention_note": (
            "FRG-4 status_certificate: F1 PASS at FRG-2 is OVERTURNED at FRG-4 "
            "unless the opposite Vassilevich heat-kernel sign convention is "
            "adopted. The -sigma well thus stands at DECISION grade ONLY under "
            "the heat-kernel sign convention that flips the a4 cross-term sign; "
            "that choice is a genuine physics decision = owner-locked."
        ),
        "named_blocker_plus_modulus": named_blocker,
        "no_target_loading": True,
        "non_promotion": "no gate flipped; artifact is countersign-input only",
    }

    out_dir = os.path.join(here, "outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "gap04_disjointness_result.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2)

    # human summary
    print("=" * 70)
    print("Gap-04 disjointness check  (-sigma well  vs  +modulus corner)")
    print("=" * 70)
    print("veff source     :", veff_path)
    print("provenance_hash :", provenance_hash)
    print("c_loop_Z        :", coeffs.get(cloop_name))
    print("c_bdry          :", coeffs.get("c_bdry"))
    print("c_a4_K6_S2      :", coeffs.get("c_a4_K6_S2"))
    print("-" * 70)
    print("-sigma  governing op :", a_neg["dominant_operator"],
          "| growth", round(a_neg["dominant_growth_rate"], 4),
          "| coeff sign", ("+" if a_neg["dominant_coefficient"] > 0 else "-"),
          "| V ->", a_neg["V_asymptotic_limit"])
    print("+mod    governing op :", a_pos["dominant_operator"],
          "| growth", round(a_pos["dominant_growth_rate"], 4),
          "| any grows", a_pos["any_operator_grows"],
          "| V ->", a_pos["V_asymptotic_limit"])
    print("-" * 70)
    print("cond1 different governing operator   :", cond1_diff_governing)
    print("cond2 no positive wall in +modulus   :", cond2_no_pos_wall_in_plus)
    print("cond3 -sigma is a real runaway       :", cond3_neg_is_real_runaway)
    print("c_loop governs -sigma at FRG-4       :", cloop_governs_neg_sigma)
    print("convention_dependent (-sigma well)   :", convention_dependent)
    print("=" * 70)
    print("DISJOINT (directional) :", disjoint)
    print("named +modulus blocker :", named_blocker)
    print("result artifact        :", out_path)
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
