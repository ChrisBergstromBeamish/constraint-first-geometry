# Falsifiers — the open claims and how to kill each

Every entry below is a **ready-to-open GitHub issue**: copy the title and body, apply the labels. Two groups: **(A) checks you can run now** (by hand, by script, or against existing data), and **(B) dated experimental falsifiers** — the world's scheduled chances to prove this wrong.

Each entry states the **locus** (where it lives), **how to check**, **pass vs. break**, and **cost if broken**. Sorted cheapest-first within each group.

---

## A. Checks you can run now

### 1 — The anomaly witness (30-second, by hand)
**Labels:** `falsification`, `gauge-sector`, `good-first-attack`, `cost:fatal`
**Locus:** GUT, Appendix E′; Forces §8.6.4; Quantum §7.
**Check:** For one Standard-Model generation, evaluate the mixed `SU(2)²–U(1)` trace over left-handed doublets: `3·(1/6) + (−1/2) = 1/2 − 1/2 = 0`. Exact rational arithmetic, no error bars. Then perturb the hypercharge lattice by one step and confirm it *fails*.
**Pass:** closes to exactly 0. **Break:** does not close as claimed → the charge assignments are wrong.
**Cost if broken:** **Fatal** — the construction dies at the gauge sector.

### 2 — The counting claim (the crux)
**Labels:** `falsification`, `over-determination`, `high-priority`, `cost:fatal`
**Locus:** GUT §§ on the flavor chamber; capstone over-determination table; `scripts/`.
**Check:** Enumerate the declared **inputs** (the four anchors). Enumerate the claimed **independent outputs**. Verify (a) each output is *not* algebraically derivable from the inputs or from another output, and (b) each was *frozen before* its measured comparison (check the hash/freeze records). 
**Pass:** outputs materially exceed inputs and are independent + frozen. **Break:** any output is secretly an input, derivable from another output, or tuned after seeing data.
**Cost if broken:** **Fatal** — the over-determination claim collapses to curve-fitting; the whole case fails. *This is the single highest-value review in the repository.*

### 3 — Hidden input / smuggled tuning
**Labels:** `falsification`, `over-determination`, `cost:fatal`
**Locus:** anywhere in the corpus.
**Check:** Find a fifth numerical input that functions as a degree of freedom but is presented as an output, or any place a value was adjusted after comparison with data.
**Pass:** none found. **Break:** exhibit one.
**Cost if broken:** **Fatal** — deflates the output-to-input ratio that the entire claim rests on.

### 4 — Reproduction failure
**Labels:** `reproduction`, `cost:downgrades-gate`
**Locus:** `scripts/reproduce_all.py`, `scripts/MANIFEST.md`.
**Check:** Run `python scripts/reproduce_all.py` under the documented environment lock. 
**Pass:** all scripts `PASS` or `REFUSED-by-design`. **Break:** any genuine `FAIL` (non-zero exit) that is not refused-by-design.
**Cost if broken:** the affected gate drops from claimed certificate to diagnostic, on the spot.

### 5 — The Einstein–Maxwell field-energy ledger (5-minute)
**Labels:** `falsification`, `consistency-check`, `cost:downgrades-gate`
**Locus:** GUT, Appendix O.
**Check:** A thin shell `Q = 1 C` at `R_s = 5 m` gives `U_EM = Q²/(8πε₀)·(1/R_s − 1/r₂) = 4.49378×10⁸ J` (6 s.f.); confirm the geometry's `×,⊕,⊗` bookkeeping returns the identical digits. *(Guardrail: stop at `U_EM`; a round-then-square artifact in `Δm = U_EM/c²` is not a discrepancy.)*
**Pass:** identical to 6 s.f. **Break:** digits differ. *Note: this is a reproduce-known consistency check — agreement does not prove the theory; disagreement breaks the bookkeeping claim.*

### 6 — The CKM phase (consistency, Type-B)
**Labels:** `falsification`, `flavor`, `cost:downgrades-claim`
**Locus:** GUT §7.6 (holonomy / CKM).
**Check:** The order-three holonomy yields a compared phase `+60.0°` (after the standard Wolfenstein convention alignment; **compare the aligned +60.0, not the raw −120**). Compare against PDG `γ = 65.5°` and compute the pull at ~10% structural precision (~0.79σ).
**Pass:** sub-σ consistency. **Break:** a corrected alignment or value puts it many σ away. *Consistency, not confirmation; a null would have falsified it.*

### 7 — Three families from the index
**Labels:** `falsification`, `topology`, `cost:downgrades-claim`
**Locus:** GUT, Appendix E (spin-c / Borel–Weil–Bott index).
**Check:** Verify the index on `K₆ = SU(3)/T²` evaluates to `χ = −3` (an integer, no tunable dial), consistent with LEP `N_ν = 2.984 ± 0.008`.
**Pass:** index = −3. **Break:** the index computation gives a different integer, or is shown to be tunable.

### 8 — The cosmological-constant self-refutation (audit the failure)
**Labels:** `audit`, `published-failure`, `cost:already-refuted`
**Locus:** TOE §III; Λ supertrace line.
**Check:** The corpus *claims its own candidate Λ cancellation failed* (supertrace ratio 0.58 at k=0; theorem refuted). Verify the failure is real and that **no** comparison to the observed Λ is smuggled in as a partial success.
**Pass (for the method):** the failure is honestly carried as `refuted`, Λ left Weinberg-open. **Break (of the honesty):** find a place the failure is quietly softened into a win.

### 9 — The fermion mass spectrum from two anchors
**Labels:** `falsification`, `flavor`, `cost:downgrades-claim`
**Locus:** GUT Appendix J/K; particle-closure companion §Stage-3.
**Check:** From only `y_t` and `|V_us|`, the construction returns the quark / charged-lepton / neutrino masses, CKM + PMNS, `v`, and `m_h = 123.82 ± 1.8 GeV` (0.48σ). Re-derive and check pulls. **Known open:** the up-quark mass sits at ~4.4σ — confirm or sharpen this tension.
**Pass:** pulls as claimed (most <1σ). **Break:** a mass lands many σ off, or an anchor turns out to be doing more work than declared.

### 10 — Gap-04 grade
**Labels:** `audit`, `grading`, `cost:downgrades-gate`
**Locus:** TOE §II; supporting Gap-04 close-out docs.
**Check:** Gap-04 is claimed **CLOSED at decision grade, not certificate grade** (operative bound cleared 35× at the weakest variant), with the global-UV question delegated. Verify it is not presented anywhere as certificate-grade.
**Pass:** consistently decision-grade. **Break:** find it claimed as certificate-grade.

---

## B. Dated experimental falsifiers (the calendar)

Each row is a published-measurement chance to break a frozen prediction. Finding the first one that fails is a complete review on its own.

### 11 — Inflation: LiteBIRD tensor-to-scalar ratio
**Labels:** `falsifier:dated`, `cosmology`, `cost:sector-falls`
**Locus:** TOE §IV.
**Prediction (frozen):** `n_s ∈ [0.9643, 0.9679]`, `r ∈ [3.5, 10]×10⁻³` (operative branch; four-branch union up to `36×10⁻³`).
**Falsifier:** LiteBIRD (~2030+) measures `r` below the band, or `n_s` outside it.

### 12 — Proton decay
**Labels:** `falsifier:dated`, `cost:sector-falls`
**Prediction:** pre-registered dimension-six `QQQL` channel.
**Falsifier:** a proton-decay detection above the registered rate (next-gen reach, ~2035).

### 13 — Neutron electric dipole moment (strong-CP)
**Labels:** `falsifier:dated`, `open-gap`, `cost:sector-falls`
**Prediction:** `θ̄` is left **underived** (open).
**Falsifier:** an nEDM corresponding to `θ̄ > 10⁻¹⁰` turns the underived status into a refutation.

### 14 — Dark matter direct detection (inverted)
**Labels:** `falsifier:dated`, `cost:sector-falls`
**Prediction:** minimal candidate `σ_SI ~ 10⁻⁵⁵–10⁻⁶⁰ cm²` (null forecast).
**Falsifier:** **any** positive direct-detection signal at conventional WIMP scales falsifies the minimal candidate.

### 15 — Baryon asymmetry
**Labels:** `falsifier:dated`, `open-gap`, `cost:sector-falls`
**Prediction:** `η_B` held **open** at a 0-of-4 fix ledger.
**Falsifier:** `η_B` outside `[6.0, 6.2]×10⁻¹⁰` at 3σ once the fixes are attempted.

### 16 — Neutrino ordering / atmospheric octant
**Labels:** `falsifier:dated`, `flavor`, `cost:downgrades-claim`
**Prediction:** normal ordering; lower-octant `θ₂₃` (diagnostic grade).
**Falsifier:** DUNE / JUNO establish inverted ordering, or the wrong octant once resolved.

### 17 — W boson mass
**Labels:** `falsifier:dated`, `cost:downgrades-row`
**Prediction:** the corpus `m_W` comparison row.
**Falsifier:** an updated `m_W` (2027) outside the comparison band.

---

*See [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to file, and [`ERRATA.md`](ERRATA.md) for what's already been found.*
