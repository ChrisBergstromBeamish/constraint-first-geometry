# (3) THE FIVE "TEST IT YOURSELF" PROMPTS — A REFEREE TOOL

All four manuscripts embed the **same five copy-paste prompts** (a referee can run each in a
calculator or any competent AI). They are a *referee convenience tool*, not a result-claim.
**DRAFT — pending countersign (see `00_REFEREE_AID_README.md` §0).**

The five prompts live at:
- **TOE_FINAL_merged.md** — "Test it yourself — five prompts you can paste into any AI"
- **Fable_GUT_merged.md** — §"Test it yourself — five copy-paste checks"
- **Fable_Forces_merged.md** — §0.4.1 "Test It Yourself — Five Prompts You Can Run in Any AI"
- **Fable_Quantum_merged.md** — §19B.5 "Test it yourself … five prompts"

(Minor sector-specific routing differs between docs — e.g. the GUT homes Prompt 1 in its own
Appendix O while the Quantum doc cites the GUT as the sibling — but the prompts and expected
values are identical.)

---

## THE HONEST CAVEAT THAT GOVERNS ALL FIVE (read before any green check)

The prompts split into two kinds, and **the kind controls what a green check is allowed to
mean** — this caveat is printed in every manuscript and must travel with the tool:

- **Type A (Prompts 1–3) — reproduce-known:** the geometry must return the **same answer with or
  without** it. The geometry only re-labels the textbook ledger object-for-object; it does **not**
  change the physics and does **not** claim to replace general relativity or Maxwell. A green
  check is an **equivalence/consistency** demonstration recorded at CONDITIONAL/Diagnostic grade —
  **never** a proof of the theory.
- **Type B (Prompts 4–5) — geometry-necessary-but-standard-verifiable:** these check the
  geometry's outputs for a genuine **Standard-Model free parameter** the SM cannot derive
  (δ_CKM; the generation count), for **consistency with independent data**. A sub-1σ match is a
  **non-falsification, never a confirmation** — a null result *would* have been a falsifier; a
  sub-1σ pull is consistency-with-data only.

**Do not read any green check as a status promotion. A referee should treat the whole tool as
"the construction is checkable and self-consistent," not as "the construction is correct."**

---

## PROMPT 1 — Charged-shell field energy (Type A)

> You are a careful physicist with a calculator. A thin spherical shell carries total charge
> Q = 1.00000 C at radius R_s = 5.00000 m. Two concentric Gaussian surfaces sit at r_1 = 1.00000 m
> and r_2 = 10.0000 m. Using only standard Einstein–Maxwell electrostatics, compute the
> electromagnetic field energy stored in the spherical region between r_1 and r_2 for this
> configuration (shell between the two surfaces), with the field given by the vacuum Coulomb law
> E(r) = Q/(4πε₀r²) for r > R_s and zero for r < R_s, energy density u = ε₀E²/2, and
> ε₀ = 8.8541878128×10⁻¹² F/m. Give the result to six significant figures in joules. Then state
> the closed form you used.

**Expected:** U_EM,12 = **4.49378×10⁸ J**, from U = Q²/(8πε₀)·(1/R_s − 1/r₂). By hand:
Q²/(8πε₀) = 4.49378×10⁹ J·m; (1/5 − 1/10) = 0.100000; product = 4.49378×10⁸ J. The geometry side
(the ×,⊕,⊗ ledger) returns identical digits because it re-labels the bookkeeping, not the physics.
**Guardrail:** stop at U_EM; do not also reproduce Δm to six figures — Δm = U_EM/c² inherits
U_EM's precision and the 5.00079×10⁻⁹-style figure is a round-then-square artifact, not a
discrepancy. **Home:** GUT Appendix O.4 / O.2.
**Honest framing:** consistency/equivalence at CONDITIONAL grade; does **not** claim to replace GR.

---

## PROMPT 2 — One-line anomaly cancellation (Type A)

> You are a particle physicist checking gauge-anomaly cancellation by hand for one Standard Model
> generation. Take the quarks of one generation: a color-triplet left-handed quark doublet
> (multiplicity 3 from color) of weak-hypercharge Y = +1/6, and the left-handed lepton doublet of
> Y = −1/2. For the mixed SU(2)²–U(1) (and gravitational–U(1)) anomaly, the relevant trace over the
> left-handed weak doublets is the sum of their hypercharges weighted by multiplicity. Compute
> 3·(1/6) + (−1/2) and state whether it vanishes. Show the one line.

**Expected:** 3·(1/6) − 1/2 = 0 (3·(1/6) = 1/2; 1/2 − 1/2 = 0). The geometry inherits this because
its index output *is* one SM generation per family. **Home:** GUT Appendix E′ — Anomaly Closure
(Gate 5); Forces §8.6.4; Quantum §7 cubic rows.
**Honest framing:** shows *consistency* ("inherited, not arranged"), not that the geometry is the
sole origin of the SM.

---

## PROMPT 3 — Weak-field reductions to Newton and Coulomb (Type A)

> You are a physicist auditing whether a higher-dimensional unification proposal reproduces
> textbook low-energy physics. (a) For gravity: state the weak-field, slow-motion (Newtonian)
> limit of general relativity as a field equation for the gravitational potential Φ sourced by
> mass density ρ, with Newton's constant G. (b) For electrostatics: state Gauss's law in
> differential form and the resulting Coulomb field of a point charge Q in vacuum. Write both
> standard results explicitly.

**Expected:** (a) ∇²Φ = 4πGρ; (b) ∇·E = ρ/ε₀, giving E = Q/(4πε₀r²). The geometry claims only to
*land on these same equations*. **Home (companion file):** Forces gravity ladder §6.6, electrostatics
§9.6; the GUT's own Appendix O reduction is the electromagnetic one only.
**Honest framing:** these are **interface claims** — "recovers GR's weak-field limit, does **not**
replace GR"; reproducing a limit is a necessary consistency check, not a proof of the parent
geometry. The gravity interface is additionally conditional on the volume-modulus freeze (declared
soft spot WL-1, Forces §0.2).

---

## PROMPT 4 — CKM CP phase (Type B) — δ_CKM, 0.79σ

> You are a flavor physicist. The Standard Model does not predict the CKM CP-violating phase
> δ_CKM (the Cabibbo–Kobayashi–Maskawa phase, equivalently the unitarity-triangle angle γ); it is
> a free parameter fixed only by measurement. (1) Confirm that in the Standard Model this phase is
> an input, not a derived quantity. (2) Given a theoretical proposal that the phase emerges from an
> order-three geometric holonomy equal to −2π/3 = −120° (raw), which after the standard Wolfenstein
> phase-convention alignment corresponds to a compared value of +60.0°, evaluate the consistency of
> +60.0° against the measured PDG value of 65.5° for γ. Report the discrepancy in units of the
> experimental standard deviation (the "pull"), assuming roughly 10% structural precision on the
> prediction, and state whether +60.0° is consistent with data at that level.

**Expected:** SM cannot derive δ_CKM (genuine free parameter). Raw holonomy −2π/3 = −120°;
Wolfenstein-aligned +60.0° vs PDG 65.5° → **0.79σ pull** (σ ≈ 6–7° at ~10% structural precision;
(65.5 − 60.0)/6.9 ≈ 0.79; in-doc band δ_CKM = 60.0° ± 7.0°). **Convention guardrail (load-bearing):**
compare the Wolfenstein-aligned +60.0°, NOT the raw −120° — comparing −120° to 65.5° is a false
~185° mismatch. **Home:** GUT §7.6 table + Appendices I/J.
**Honest framing:** agreement at 0.79σ is **consistency with data at the stated precision** — it
does **not** prove the theory; a null result would have been a falsifier, a sub-1σ pull is a
non-falsification, not a confirmation.

---

## PROMPT 5 — Exactly three generations (Type B) — topological index −3

> You are a model-building physicist. (1) Confirm that the Standard Model does not explain why
> there are exactly three generations of matter — the number 3 is an empirical input, not derived
> from SM principles. (2) A theoretical proposal obtains the generation number as a topological
> index (a spin-ℂ / Borel–Weil–Bott index on the internal flag manifold K_6 = SU(3)/T², evaluating
> to −3, i.e. three chiral families), an integer that cannot be continuously tuned. Treating the
> family count as fixed by topology rather than by hand, verify that the value "exactly three" is
> consistent with experiment: state what the LEP measurement of the number of light neutrino
> species (N_ν ≈ 2.984 ± 0.008 from the Z invisible width) and the absence of fourth-generation
> discoveries imply about the allowed number of standard chiral generations.

**Expected:** SM does not predict the generation count; the geometry's topological index
χ(K_6, E) = −3 → exactly three chiral families, **forced (not a dial)**; LEP N_ν ≈ 3 and null
fourth-generation searches are consistent with exactly three, and the index-changing deformation
that would give two or four families is excluded by the LEP N_ν bound. **Home:** GUT §1.3.1,
§3.4–§3.5, Appendix E, and the Objection-4 rebuttal.
**Honest framing:** this is **consistency with the observed count**, recorded at CONDITIONAL grade
— not a from-nothing proof that nature must have three. **Minimality holds only inside the declared
search category** — a reviewer who supplies a natural excluded competitor triggers a documented
downgrade to "category-relative diagnostic."

---

## HOW A REFEREE SHOULD USE THIS TOOL

- **Prompts 1–3 (Type A)** answer the reader's deepest fear — *"does this ever touch known
  physics?"* — in minutes. A green check means the new machinery has not quietly changed the
  textbook physics. It is **load-bearing for consistency, never for correctness.**
- **Prompts 4–5 (Type B)** are the falsifiable teeth: each targets a genuine SM free parameter the
  SM cannot derive. They could have come out wrong (a null is a falsifier); they came out at
  0.79σ and at the LEP-consistent count of three. **Sub-1σ is consistency, not proof.**
- **Each prompt carries its own honest-framing line in the source; do not strip it.** No QC prompt
  exists — by design (the no-target-loading rule forbids any QC number from feeding the physics
  claims).

**The honest one-sentence summary for an editor:** the five-prompt tool lets a referee confirm, in
an afternoon, that the construction is checkable and self-consistent against known physics and
against two genuine SM free parameters — it is **evidence of discipline and consistency, and is
explicitly not offered as evidence that the theory is correct.**
