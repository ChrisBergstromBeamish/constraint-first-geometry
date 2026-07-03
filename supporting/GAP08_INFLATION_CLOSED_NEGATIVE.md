# Inflation σ-slope — why λ² = 1/6 is retired as a forced prediction

**Status:** the λ²=1/6 inflation branch is **retired** as a *forced geometric prediction*. The frozen 13-dimensional internal geometry does contain a valid, target-blind lever for the inflaton slope — but that lever gives 8/3, 4, or 22/9, never 1/6. The value 1/6 arises only from a separate normalization convention, not from the geometry. This note records the exact linear algebra, verified in exact rational arithmetic. The branch-independent tensor-to-scalar falsifier r ∈ [3.5, 36]×10⁻³ (LiteBIRD-testable) is unaffected and remains the honest claim.

## The lever

Parametrize the internal metric by factor log-radii β = (β_K, β_S, β_Y), with factor dimensions (d_K, d_S, d_Y) = (6, 2, 1). K₆ and S² are positively curved (R > 0); the S¹_Y/ℤ₂ factor is flat (R = 0). In the 4D Einstein frame the internal-curvature potential is

> V_curv = C_K e^(−a_K·β) + C_S e^(−a_S·β),  with  a_K = (8, 2, 1),  a_S = (6, 4, 1).

This potential is **not** invariant under factor-volume breathing, so the frozen action genuinely distinguishes K₆-only vs S²-only vs uniform breathing. That is a valid, target-blind lever on the inflaton slope — which means the slope cannot be certified as an untouchable constant; it is set by which breathing direction is lightest.

## Verified numbers (exact rational arithmetic)

- Canonical 4D moduli kinetic metric G_ij = d_i δ_ij + d_i d_j/2 = [[24,6,3],[6,4,1],[3,1,3/2]]; inverse G⁻¹ = [[5/66,−1/11,−1/11],[−1/11,9/22,−1/11],[−1/11,−1/11,10/11]].
- Curvature-wall slopes λ²_a = aᵀ G⁻¹ a:  **λ²_K = 8/3**,  **λ²_S = 4**,  cross term a_Kᵀ G⁻¹ a_S = 2.  Uniform 9D breathing: **λ²_uniform = 22/9**.  **None equals 1/6.**
- Radion normalization K_σσ(d) = d(d+2)/2 gives K_σσ(6) = 24 (a genuine coefficient); the geometric slope is λ²_geom(d) = 2(d+2)/d, so λ²_geom(6) = 8/3. The often-quoted relation λ² := 4/K coincides with the geometric slope only if 8/(d(d+2)) = 2(d+2)/d, i.e. (d+2)² = 4, i.e. d = 0 or −4 — no positive dimension. So λ² = 1/6 is a *declared convention*, not a geometric invariant.
- Curvature-flat direction v₀ = (−1, −1, 10) satisfies a_K·v₀ = 0 and a_S·v₀ = 0 (one curvature-flat direction, lifted by boundary / Wilson / loop terms — so not by itself a proven inflaton).
- Curvature Hessian M = G⁻¹(V_K a_K a_Kᵀ + V_S a_S a_Sᵀ) has eigenvalues {0, (4V_K/3 + 2V_S) ∓ (2/3)√(4V_K² − 3V_K V_S + 9V_S²)}.

## Why 1/6 is retired

K_σσ = 24 is a real d = 6 radion coefficient, but λ² = 1/6 additionally requires the convention λ² := 4/K, which is not the geometric slope for any positive dimension. The geometry's actual curvature slopes are 8/3 (K₆), 4 (S²), and 22/9 (uniform). The value 1/6 appears nowhere in the geometry itself; as a "forced geometric CMB prediction" it does not hold.

## The honest ceiling on any replacement

A full three-modulus effective potential would read

> V_eff(β, θ_W) = C_K e^(−a_K·β) + C_S e^(−a_S·β) + B e^(−b·β) + W cos(θ_W) e^(−w·β) + L e^(−ℓ·β).

The curvature sector (a_K, a_S) is exact. The remaining exponent 3-vectors (b, w, ℓ) and their coefficients are **not** recoverable from the single-field projection V(σ) = c_KK e^(−4σ) + c_bdry e^(−2σ) + c_Wilson cos θ_W e^(−4σ) + c_loop e^(−6σ): a single-field projection cannot reconstruct a 3-vector, and its σ-normalization differs from the log-radius β. The one-loop coefficient c_loop is itself undetermined in sign, since it depends on the retained compact spectrum. Supplying b, w, ℓ by hand would be fabrication, so no replacement inflaton slope is asserted here.

The physical slope, once those inputs exist, is λ² = āᵀ G⁻¹ ā with ā_i = (Σ_m V_m a_{m,i}) / (Σ_m V_m) — mechanically computable, but only after the missing term-physics (the orbifold fixed-point term, the Hosotani/Wilson term, and the Casimir supertrace over the retained spectrum) is derived from first principles.

## Bottom line

- The inflaton slope is a real, target-blind lever, and the geometry's curvature slopes are 8/3, 4, and 22/9 — not 1/6.
- λ² = 1/6 was a normalization convention, not a derived prediction; it is retired.
- No replacement inflaton slope is claimed; that would require deriving the full three-modulus term structure, which is left open and named as open.
- The branch-independent falsifier r ∈ [3.5, 36]×10⁻³ is unaffected and stands.
