# (2) FAST-VERIFIABILITY — THE CHECKS A REFEREE CAN RUN IN AN AFTERNOON

The series is built so a time-boxed referee does not need a weekend. Three of the four
manuscripts print an explicit "afternoon" / "minutes-not-weeks" box. The two sharpest by-hand
checks are below, each with its exact in-document home, followed by the broader afternoon menu.
**DRAFT — pending countersign (see `00_REFEREE_AID_README.md` §0).**

The honest framing the manuscripts attach to every fast check travels with each item below:
**a reproduce-known check returns the same number with or without the geometry — it is a
consistency/equivalence demonstration, NOT a proof of the theory, and explicitly does NOT
claim to replace general relativity or Maxwell.**

---

## CHECK 1 — The by-hand anomaly witness: 3·(1/6) − 1/2 = 0 (~30 seconds, no tools)

**What it checks:** whether the geometry's particle list balances the gauge-anomaly ledger
exactly. One subtraction a referee can do on a napkin.

**The one line:**
- One generation of left-handed quarks: color-triplet quark doublet (multiplicity 3 from color)
  with weak-hypercharge Y = +1/6.
- Left-handed lepton doublet: Y = −1/2.
- Mixed SU(2)²–U(1) (and gravitational–U(1)) trace = Σ (multiplicity × Y) over left-handed
  doublets = **3·(1/6) + (−1/2) = 1/2 − 1/2 = 0.** Exact rational arithmetic, no error bars.

**Where it lives (authority):**
- **GUT:** Appendix E′ — Anomaly Closure (Gate 5). The one-line witness is the fastest by-hand
  entry point; the *full* closure is the six-ledger set including the mod-2 Witten condition
  (GUT §6.5 / Appendix E′).
- **Forces:** §8.6.4 (the live electroweak anomaly witness). If the hypercharge lattice were off
  by a single step, this subtraction would fail and the charge table (§8.2) would break with it.
- **Quantum:** the cubic rows (SU(3)³, ΣY³) are worked in §7 / object-ledger Row 5; the linear
  witness above is inherited from Paper 1.
- **TOE_FINAL:** the afternoon-checks box, check 2, reading the frozen q = 6Y row of §0.

**Honest framing (verbatim sense):** shows *consistency* — "inherited, not arranged" — that the
geometry's particle content balances the SM's own cancellation. It does **not** show the geometry
is the *sole* origin of the SM list (it is one of six anomaly ledgers).

---

## CHECK 2 — Einstein–Maxwell conservation ledger: U_EM = 4.49378×10⁸ J to 6 sig figs (~5 minutes)

**What it checks:** whether the geometry's ×,⊕,⊗ bookkeeping reproduces the *exact* textbook
electromagnetic field energy, object-for-object, on a hand-auditable charged shell. This is the
GUT manuscript's "reduces-to-known-physics" equivalence certificate, **Appendix O**.

**The configuration (GUT Appendix O.1):** a thin spherical shell carries total charge
Q = 1.00000 C at radius R_s = 5.00000 m. Two concentric Gaussian surfaces sit at r₁ = 1.00000 m
and r₂ = 10.0000 m. Field E(r) = Q/(4πε₀r²) for r > R_s, zero for r < R_s; energy density
u = ε₀E²/2; ε₀ = 8.8541878128×10⁻¹² F/m.

**The by-hand arithmetic (GUT Appendix O.2 / O.5):**
- Closed form: U = Q²/(8πε₀) · (1/R_s − 1/r₂).
- Prefactor: Q²/(8πε₀) = **4.49378×10⁹ J·m**.
- Geometric factor: (1/5 − 1/10) = **0.100000**.
- Product: **U_EM,12 = 4.49378×10⁸ J** (six significant figures).

**The equivalence certificate (GUT Appendix O.4 — Same-Output Equivalence Table):**

| Quantity | Traditional GR/Maxwell ledger | The ×,⊕,⊗ ledger | Difference | Match |
|---|---|---|---|---|
| U_EM,12 | 4.49378×10⁸ J | 4.49378×10⁸ J | 0 | Yes |
| Δm_EM,12 | 5.00000×10⁻⁹ kg | 5.00000×10⁻⁹ kg | 0 | Yes |

The boxed result appears at GUT Appendix O.2 (`U^GR_EM,12 = 4.49378×10⁸ J`), O.3
(`U^×⊕⊗_EM,12 = 4.49378×10⁸ J`), and O.6 (the final equivalence theorem:
`U^GR = U^×⊕⊗ = 4.49378×10⁸ J`). The two methods compute the same quantities from the same
inputs; the value of the decomposition is *auditability* (every possible disagreement must
localize to a different ×-region, ⊕-rule, or ⊗-actor), not numerical novelty.

**Honest framing (GUT Appendix O.0 / O.7):** this is *illustrative same-output equivalence*. It
recovers the standard Einstein–Maxwell accounting object-for-object; it does **NOT** replace GR,
it adds **no** new closure gate, and it is **not** used to support any claim of scoped-GUT
certificate completeness.

**Inoculation note (do not over-run this check):** stop at U_EM. Do **not** also reproduce a Δm
to six figures independently — Δm = U_EM/c² *inherits* U_EM's precision; the corpus
5.00079×10⁻⁹-style figure quoted elsewhere is a round-then-square artifact, not a discrepancy.
The falsifiable claim is U_EM to six figures only. (GUT pass-5 note; mirrored as a guardrail in
the Quantum Prompt-2 box.)

---

## CHECK 3 — The economy / over-determination count (~5 minutes, in-document)

**What it checks:** that there are more independent outputs than inputs — the signature of a
*constrained* theory, not a *fitted* one.

- Count the inputs: **four MEASURED anchors** — M_Pl, α_i(M_Z), y_t, |V_us| (TOE_FINAL §0; GUT
  §1.3.1 / R1.8).
- Count the independent banked outputs: **22+** (TOE_FINAL §I ledger); **19+ frozen observables
  plus v, m_h, M_U** in the GUT (§1.3.1, worked in §8).
- The anti-fitting control is *registered*, not asserted: **PCM-12** is a blind-negative case
  built to come out *negative* (TOE_FINAL §I / §0; GUT Objection 1). The over-determination
  inequality (independent observables > calibration inputs) is machine-checked in exact
  arithmetic by `certificates/G09_flavor/` (GUT).
- **No-target-loading rule:** observed values (Λ_obs, A_s, r, η_B) are never read as inputs; the
  comparison happens after the freeze, on the far side of the wall (TOE_FINAL §VI Rule 4).

---

## CHECK 4 — The graviton polarization count: 10 − 4 − 4 = 2 (~minutes, in-document, Paper 3)

**What it checks:** that the linearized graviton construction returns the textbook
transverse-traceless mode count. In 4D de Donder gauge: 10 metric components − 4 (gauge) − 4
(residual) = **2** transverse-traceless modes. Flagged CERTIFICATE-tier at the linearized level
(Quantum §8.4.3–§8.6). The section states plainly what it does **not** cover (the interacting,
nonperturbative graviton — routed to the AUDIT row UQF-9).

A companion free-field check (Quantum §5.5): on the free / perturbative-overlap sector the
canonical and BV/path-integral formulations agree (brackets, spectrum, gauge-invariant
correlators, tree-level S-matrix) by the standard 4D theorems.

---

## THE PUBLISHED "AFTERNOON" BOXES (each manuscript's own, for cross-reference)

- **TOE_FINAL — "How a skeptical referee can check this in an afternoon":** four checks that take
  minutes — (1) the economy count + PCM-12 blind-negative; (2) the one by-hand arithmetic witness
  3·(1/6) − 1/2 = 0; (3) where the textbook reductions live (pointer — note: TOE_FINAL makes NO
  in-doc GR/Maxwell reduction and does not claim one; the reductions are EXTERNAL, in the
  siblings); (4) the calendar of falsifiers (§IV). **Honesty disclosure carried verbatim: this
  document makes no in-doc GR/Maxwell reduction.**
- **GUT — "How fast can a skeptic check this?":** the Appendix-O.4 six-sig-fig field-energy check
  and the one-line anomaly cancellation, named as the first two of five copy-paste prompts.
- **Forces — §0.4 fast-check scoreboard:** a routing index to the landing points (Newtonian limit
  §6.6.9; Coulomb/Gauss §9.6.3/§9.6.5; anomaly witness §8.6.4; derived identities e and G_F),
  each with a "time to check" column and an honest grade column.
- **Quantum — "A fast check, before you commit the hour":** the graviton 10−4−4=2 count and the
  canonical↔path-integral overlap, both deliberately the *easy, checkable* end of the claim.

**Bottom line for an afternoon referee:** Checks 1 and 2 are decisive entry points — both are
exact, both have a single named home, and both come with the honest "consistency/equivalence,
not proof; does not replace GR/Maxwell" framing already attached in-document.
