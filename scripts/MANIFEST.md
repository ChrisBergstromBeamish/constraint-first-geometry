# SCRIPTS MANIFEST — Fable / TOE_FINAL verification bundle

> **Reader-facing front-matter (this block only).** This manifest is an honest
> index of the 21 Fable verification scripts and their output artifacts. Each
> script is **target-blind** (no observed value enters on the input side) and runs
> under the corpus's CFCA discipline (`../supporting/METHOD_CFCA_June_14.md`).
> A green run is a *consistency / structural* check, **not** a proof of the theory.
> Several scripts are **stubs-that-refuse**: their deliverable is a fail-closed
> refusal that routes an owner-only physics act to Chris. Nothing here promotes a
> status; the Return-YAML is the only instrument of promotion. The FROZEN
> scientific content (the §V truth table, the decision-grade closures, the
> economy headline, the Gap-04 CLOSED-SCOPED / GLOBAL-UV-DELEGATED close-out, and
> the T1/T2/T3/T1' rows) lives unchanged in the source manuscripts and the
> supporting docs; this manifest only points at it.
>
> **Counts:** 21 Python scripts, 24 output artifacts (`outputs/`).

---

## How to read this

- **Script** — the file under `scripts/`.
- **What it computes / verifies** — one honest line.
- **Output(s)** — the artifact(s) under `scripts/outputs/` it writes (or `—` if
  it is a refusal stub that writes a skeleton, or shares an output).

---

## Gap-04 — σ-well / `c_loop` modulus stabilization (the UV-wall lane)

| Script | What it computes / verifies | Output(s) |
|---|---|---|
| `gap04_disjointness.py` | From the FRG-4 V_eff operator basis alone, checks that the −σ negative-modulus runaway corner and the +modulus decompactification corner are governed by **disjoint** dominant operators (different physics objects, different statuses). Loads frozen coefficients; no observed value enters. | `gap04_disjointness_result.json` |
| `gap04_convention_audit.py` | Heat-kernel sign-convention audit: decomposes the sign of the a₄ cross-term into one-loop prefactor × cross-density and asks whether the corpus's own frozen conventions pin it (vs a free choice). | `gap04_convention_audit_result.json` |
| `gap04_oneloop_consistency.py` | Applies the corpus's genuine single one-loop log-det convention to the frozen a₄ cross-term; reports c_a4 = −5.97e-08 (negative) without forcing a "well-stands" outcome; shows why the relative-sign-vs-`c_loop` question stays owner-locked. | `gap04_oneloop_consistency_result.json` |
| `gap04_cloop_density_sign.py` | Tries to derive (or precisely gate) the sign of `c_loop`'s underlying heat-kernel density — the single deciding fact for the owner-lock. Honest endpoint: gated on the named open object (no first-principles producer exists in-corpus). | `gap04_cloop_density_sign_result.json` |
| `gap04_cloop_casimir_firstprinciples.py` | "Elegant path": checks two flagged scalar-Casimir scripts to see if either is a genuine first-principles producer of the e^{−6σ} wall coefficient. Verifies object identity before trusting it; endpoint = machinery-different-object, owner-locked. | `gap04_cloop_casimir_firstprinciples_result.json` |
| `gap04_zeta_continuation_frg2.py` | Analytically continues the scalar K₆=SU(3)/T² spectral zeta ζ_{Δ_K6}(s) to s=−1/2 via Mellin / Epstein-Hurwitz; finds a **simple pole at s=−1/2** (residue scheme-invariant negative; finite part scheme-dependent). The bare `c_loop` is UV-divergent. | `gap04_zeta_continuation_frg2_result.json` |
| `gap04_litim_scheme_branch.py` | Reconstructs the FRG-2 NLO Litim shell-projection scheme from corpus definitions; computes the Litim-regularized finite `c_loop` and the relative one-loop sign; states exactly what is recoverable vs owner-supplied. | `gap04_litim_scheme_branch_result.json` |
| `c_loop_NLO_match.py` | The named producer: builds the FRG-2 NLO Litim threshold-function shell projection over the five retained-mode shell masses, target-blind; supersedes the partial reconstruction; corrects an earlier over-claimed sign reading back to owner-must-rule. | `c_loop_NLO_match_result.json` |
| `gap04_intloop_principle_check.py` | Tests five candidate physical/geometric principles (reflection positivity, a₆ UV-completion consistency, etc.) for whether any fixes the sign of `int_loop` for the frozen geometry without the full Λ resolution. Honest per-principle verdicts. | `gap04_intloop_principle_check_result.json` |
| `gap04_full_supertrace_residue.py` | **T1 — highest-yield test.** Enumerates the complete field content on K₆^{W-rig}×S²×S¹_Y/ℤ₂, computes each species' s=−1/2 pole-residue contribution, forms the supertrace. Finds Str[1] = n_B−n_F = 35−90 = −55 ≠ 0 (no index cancellation; residue survives). | `gap04_full_supertrace_residue_result.json` |
| `gap04_higher_operator_wall.py` | Builds the complete operator tower at the −σ corner, identifies the fastest operator within EFT validity (a₆ ~ e^{−12σ}), and tests whether the runaway corner even lies inside EFT validity. Phase-exit boundary σ\* = ½ln30 ≈ 1.70. | `gap04_higher_operator_wall_result.json` |
| `gap04_chamber_exclusion.py` | Kinematic-floor test: asks, per prior banked constraint (W-rig projector, flux quantization, three-family APS index), whether any already forbids unbounded K₆ shrinking. Honest endpoint: **no kinematic floor** (Weyl-rigidity bounds shape, not volume). | `gap04_chamber_exclusion_result.json` |
| `gap04_reason_hunt.py` | Irreducible reason-hunt: for each residual Gap-04 number, runs CFCA to classify DERIVED / EARNED-IRREDUCIBLE / BARE-COUNTED and maintains the economy ledger (pure-debit count vs the ~5–6 budget). | `gap04_reason_hunt_result.json` |

## B-UQFC-14-UV-1 — the named UV-completion axiom (freeze + stability routes)

| Script | What it computes / verifies | Output(s) |
|---|---|---|
| `uv1_frozen_functional.py` | CFCA freeze certificate: pins and hashes the single UV object to be tested — the Chamseddine-Connes spectral action S_σ[f]=Str f(D_σ²/Λ²) over the full gauge-fixed BV/BRST tower — **before** any stability test or committed magnitude is read. Takes no branch. | `uv1_frozen_functional_result.json` |
| `gap04_spectral_positivity_optionA.py` | OPTION A proof attempt: is the full-tower spectral action bounded below by a positive, σ-growing wall as Vol(K₆)→0? Closed-form spectral-positivity statement required; finite-order coefficients are consistency checks only. | `gap04_spectral_positivity_optionA_result.json` |
| `gap04_uv1_optionB_resummed_determinant.py` | OPTION B: is the one-loop functional determinant W_σ=½Str log D_σ² bounded below as σ→−∞ under the frozen prescription? The route the freeze flags as "where the ambiguity lives." Honest endpoint of B alone. | `gap04_uv1_optionB_resummed_determinant_result.json` |
| `uv1_axiom_payoff_search.py` | CFCA economy ledger (Stage 6): tests, for nine independent payoff targets, whether the UV-1 axiom EXPLAINS / DOES-NOT / INCONCLUSIVE — target-blind. Per the >1-payoff rule (credit ≥ 2 ≥ 1 debit). | `uv1_axiom_payoff_search_result.json` |

## Other gaps (each a self-contained sub-loop instrument)

| Script | What it computes / verifies | Output(s) |
|---|---|---|
| `strongcp_realizationB.py` | **Gap-03 / Strong-CP.** Reproduces the Realization-A obstruction structurally; constructs Realization-B (row-only Weyl action); runs the EXT-3 zero-mode Borel-Weil-Bott index gate (|index|=3, APS (+3,0)) and the determinant-character test; the chiral-split field-content change is the Axiom-3 act reserved to Chris. | `gap03_realizationB_certificate.json`, `zero_mode_invariance_proof.json` |
| `lambda_L1L3_radstab.py` | **Gap-05 / Λ.** Builds the three surviving relocation constructions (L1 discrete symmetry, L2 non-perturbative wall, L3 boundary sequestering) and applies the 122-orders-of-magnitude radiative-stability burden test. Chamber route stays CLOSED; Weinberg's no-go stands. | `lambda_L1L3_radstab_result.json` |
| `inflation_sigma_map_read.py` | **Gap-08 / inflation.** The frozen σ-map read: the single named gate separating the operative inflation branch (T6/T_u/D6/D_u) and the four r-bands + union falsifier. If the σ-map yaml is absent the gate is reported PENDING (precisely-OPEN, Chris rules intent). | `inflation_sigma_map_read_result.json` |
| `bg10_four_fix.py` | **Gap-10 / baryogenesis (stub-that-refuses).** Orchestrates the four named fixes; **cannot** produce an η_B without Chris's signed 7-input F⁺ manifest, so it refuses (exit 2) and emits an all-null countersign-ready skeleton + the pre-registered falsifier window η_B ∈ [6.0,6.2]e-10. The stub IS the deliverable. | `bg10_manifest_skeleton.json`, `bg10_open_package.json`, `bg10_eta_B_prediction.csv` |

---

## Output artifacts without a one-to-one script in this bundle

All 24 artifacts under `outputs/` are accounted for above. Note the many-to-one
and shared cases:

- `bg10_four_fix.py` → `bg10_manifest_skeleton.json`, `bg10_open_package.json`,
  `bg10_eta_B_prediction.csv` (the η_B prediction CSV is a frozen-window/skeleton
  artifact, **not** a produced η_B value — the lane refuses).
- `strongcp_realizationB.py` → `gap03_realizationB_certificate.json`,
  `zero_mode_invariance_proof.json`.

---

## Honest notes (no fabrication)

- **No iframes** appear in any script or output in this bundle (searched; none found).
- The only `placeholder` token in the bundle is in `lambda_L1L3_radstab.py` /
  `lambda_L1L3_radstab_result.json`, where `"lambda_1_placeholder":
  "PRESERVED-NOT-UPGRADED"` is a deliberate **non-promotion marker** (it records
  that L1 was preserved, not silently upgraded), not an unfinished stub.
- The `TODO(physics: Chris, …)` tokens in `bg10_four_fix.py` are the **owner-locked
  input slots** that the refusal stub leaves null by design — they mark the 7 F⁺
  inputs only Chris can supply, not incomplete code.
- No script reads an observed value (A_s, Λ_obs, r, n_s, N_eff, PDG, η_B,
  Ω_DM, H₀, S₈) on its input side; committed magnitudes (e.g. `c_loop` =
  1.3637877e-5) enter only as post-hoc cross-checks where stated.
