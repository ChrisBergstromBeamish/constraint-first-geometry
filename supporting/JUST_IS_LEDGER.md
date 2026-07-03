# What the geometry forces, and what it measures — a triage of the free numbers

A recurring intuition about this program is that *a clean, simple number probably has a geometric origin, while a messy one (say 534323424.343) genuinely just is what it is.* This note tests that intuition against every free number in the framework and states where it holds and where it fails.

**Result up front:** the intuition is **strongly confirmed for discrete / topological quantities** — counts, groups, dimensions, indices, and simple curvature or radion ratios — which the framework already derives from the geometry. It is **unreliable for continuous measured magnitudes** — couplings, masses, mixings, and the cosmological constant — where the record contains three concrete cautionary cases. A refined principle is given at the end.

---

## A. Discrete / topological numbers — clean *and* geometric origin found

| Number | Value | Geometric origin | Status |
|---|---|---|---|
| Family count N_ν | **3** | \|χ(K₆, E)\| = 3 (spin-ℂ index / Euler characteristic) | forced by the geometry — the clearest case |
| Gauge group | SU(3)×SU(2)×U(1)/ℤ₆ | K₆ = SU(3)/T² carrier plus the shape; the ℤ₆ center-lock | group content forced; the discrete quotient sub-choice open |
| Dimension / split | D = 13, n = (6, 2, 1) | the frozen shape (selected, and structurally clean integers) | shape-anchored |
| Born exponent | p = **2** | pinned by "no preferred absolute" | structural |
| Curvature / radion ratios | κ = 1/6, λ²_K = **8/3** = 2(d+2)/d | DeWitt moduli metric with dimension d = 6 | forced by the geometry |

**Pattern:** every place the geometry *forces* a number, it is an integer, an index, or a simple ratio of dimensions — exactly the intuition.

## B. The continuous anchors — mostly measured

| Number | Value | Clean? | Geometric-origin result | Status |
|---|---|---|---|---|
| **M_Pl** | a scale | dimensionful | Buckingham-π requires at least one dimensionful anchor — a scale cannot come from pure number | genuine anchor (the one that must exist) |
| **α_i(M_Z) / α_GUT** | α_s ≈ 0.118, α_GUT⁻¹ ≈ 25–40 | the *unification* is clean; the *value* not obviously | value not yet shown geometric | measured anchor (α_GUT value is a live candidate) |
| **y_t** | 0.9665 | ≈ 1 at leading order; the precise value is not clean | leading ~1; the top-Yukawa infrared quasi-fixed point is a real RG-attractor mechanism | measured, with a live reduction candidate |
| **\|V_us\|** | 0.22436 | clean-ish (Cabibbo ≈ 13°) | tested and missed: the only mixing-angle-blind geometric magnitude is 1/√3 = 0.5774, off by more than 500σ; coset invariants miss by 90–690σ | measured anchor — a counterexample to the intuition |
| **Λ** | ~10⁻¹²² M_Pl⁴ | messy and tiny | no cancellation mechanism known (Weinberg-open) | measured / genuinely "just is" |

## C. A retired "clean" number — clean but not geometric

| Number | Was described as | Reality |
|---|---|---|
| λ² = **1/6** | "clean, Planck-dead-center" | equals the convention λ² := 4/K, not the geometry; the geometric slope is **8/3**. Retired. Clean did not mean geometric — it was bookkeeping. |

## D. Floor values — dimensionful or asserted

ħ, k_B, the Bekenstein constant, cΛ_YM, a minimum length ℓ_min, and a sub-unit density ρ < 1 are dimensionful or asserted, not clean dimensionless targets. These sit in the genuine "just is" tier.

## E. Declared-open structural bits — mixed

A neutrino-sector sign bit σ_ν = +1 is discrete and a candidate for geometric forcing (three routes agree it is the same bit); a right-handed scale M_R is a scale and hence measured; the Born measure axioms are axioms.

---

## Three cautionary cases, all observed within the framework

1. **Convention artifact.** λ² = 1/6 looked clean but was the normalization λ² := 4/K; the geometry gives 8/3. *A clean number can come from a normalization choice, not from the geometry.*
2. **Clean but misses.** \|V_us\| (clean-ish Cabibbo angle) versus the geometry's clean invariant 1/√3: off by more than 500σ. *A clean observed number need not equal the geometry's clean values.*
3. **Cheap rationals.** For the frozen moduli metric G and integer curvature walls, every single-wall slope aᵀ G⁻¹ a is automatically a simple rational; the geometry produces many (8/3, 4, 22/9, 32/11, 24, 30/11, …). *Matching one of many to data is weak evidence without a selector that is blind to the target.*

## Refined principle

> A clean "just-is" number is a **hypothesis** of geometric origin, not a proof. It is confirmed only when a **target-blind selector** — an index, a symmetry-forced eigenvector, a specific curvature wall, a dimension count — forces *that specific* value independently of the fact that it matches data. The intuition is reliable for discrete / topological quantities (which the framework already derives: N_ν = 3 = χ, the gauge group, the dimension, p = 2) and unreliable for continuous magnitudes (M_Pl, α, y_t, \|V_us\|, Λ), which are mostly measured anchors — the one clean-ish continuous case, \|V_us\|, was tested and missed.

## Candidates still worth investigating (ranked)

1. **y_t (top Yukawa)** — strongest, because the RG infrared quasi-fixed point is a real mechanism tied to α_3; if it genuinely attracts, y_t would reduce from five anchors to four. (Tested at one and two loops in this release — it does not currently reduce; see the insight page.)
2. **α_GUT value** — is the unification coupling a clean geometric ratio or a measured one?
3. **σ_ν = +1** — a discrete bit, plausibly index-forcible.
4. **\|V_us\| revisited** — only if a non-coset mechanism exists; the simple-invariant route already missed, and re-nominating an invariant chosen to match the target would defeat the point.

**Genuinely "just is" (stop looking):** M_Pl (a scale) and Λ (tiny and Weinberg-open) — the honest measured anchors.
