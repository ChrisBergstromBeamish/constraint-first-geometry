<!--
================================================================================
INDEX–UV-WALL OBSTRUCTION THEOREM  —  standalone math result
Authored 2026-06-15 (document_writing vertical). Voice-matched to the CFCA method
(METHOD_CFCA_June_14.md) and the TOE_FINAL status vocabulary.

DISCIPLINE (no-target-loading). This file states a STRUCTURAL obstruction as a
clean standalone theorem. It does NOT adopt the spectral-action UV-completion
axiom B-UQFC-14-UV-1; it does NOT call B-UQFC-14-UV-1 closed; it does NOT claim
global stability. The current geometry does not "globally stabilize itself" —
the theorem's content is the opposite: it explains why global stabilization is
UV-HARD, i.e. why no positive shrinking-volume UV wall is derivable from the
currently banked geometry without an additional, separately named UV-completion
axiom. It is a standalone result; it does NOT edit the manuscript or the diff.
================================================================================
-->

# The Index–UV-Wall Obstruction Theorem

*A standalone structural result. It states why a positive shrinking-volume UV wall is **not derivable** from the currently banked $K_6^{W\text{-rig}} \times S^2 \times S^1_Y$ geometry — not that the geometry runs away, and not that $\Lambda$ is solved.*

**Status (CFCA terminal-state vocabulary).** This theorem is **closed-by-computation** as stated: it is an arithmetic-and-index implication, fully banked by the runs cited in §3. It is *about* an OPEN object (`B-UQFC-14-UV-1`), but it is itself not that object: the theorem asserts an **absence-of-derivation**, and it certifies that this absence is **structural, not accidental**. Adopting it advances no gate; in particular it does **not** close `B-UQFC-14-UV-1`, which remains `precisely-OPEN-behind-named-object` (owner: Chris).

---

## 1. Statement (Chris's)

> **Theorem (Index–UV-Wall Obstruction).** In the current $K_6^{W\text{-rig}} \times S^2 \times S^1_Y$ geometry, the same spin-$c$ three-family index that generates the chiral matter spectrum forces $n_F > n_B$, hence
> $$\mathrm{Str}[\mathbf{1}] \;=\; n_B - n_F \;=\; 35 - 90 \;=\; -55 \;<\; 0.$$
> Therefore the leading full-spectrum spectral-action coefficient $a_0$ has the **non-stabilizing sign**, and **no positive shrinking-volume UV wall follows from the currently banked geometry without an additional UV-completion axiom.**

In one line: *the geometry's own index, which is load-bearing for the matter content, is the very thing that denies the leading spectral coefficient the sign a derived UV wall would require.* The obstruction is sourced by the same integer that does the corpus's most-celebrated work; it is not an unrelated pathology.

---

## 2. Assumptions (made explicit)

The theorem is conditional on exactly the following, each banked and named. Nothing else is used; in particular **no measured constant**, no committed `c_loop` magnitude, and no observed $\Lambda$ enters on any input side.

| # | Assumption | What it fixes | Authority / hash |
|---|---|---|---|
| **A1** | **The geometry.** The spectral triple lives over $M_4 \times K_6 \times S^2 \times S^1_Y/\mathbb{Z}_2$ with $K_6 = SU(3)/T^2$ (the flag manifold, $\dim 6$). | The fixed background whose breathing $\mathrm{Vol}(K_6)\!\to\!0$ ray is the collapse direction. | Frozen geometry registry; $\mathrm{Scal}(K_6)\cdot\mathrm{Vol}(K_6)=12\pi^3$. |
| **A2** | **The spin-$c$ index $=-3$.** The Borel–Weil–Bott / spin-$c$ index of the corpus's own Dirac operator $D_{K_6}^{\mathrm{spin}^c}$ on the active line bundle is $\mathrm{ind}\,D = -3$. | Forces exactly **3** unpaired chiral families, **no mirror partners**. | Active bundle R1.4, hash `0fd19c9ae0c1`; spin-$c$ index $-3$ (banked topological integer). |
| **A3** | **The full gauge-fixed tower $n_B = 35$.** The bosonic content of the gauge-fixed BV/BRST fluctuation complex inside $D_\sigma^2$ totals $n_B = 35$ real dof: graviton $2$ + gauge $2\times 12 = 24$ + moduli $(3{+}1{+}1)=5$ + Higgs $4$. | The bosonic side of the supertrace. | Nine-row field ledger; `gap04_full_supertrace_residue.py`. |
| **A4** | **The Chamseddine–Connes framing, $a_0 \propto \mathrm{Str}[\mathbf{1}]$.** The UV functional is the spectral action $S_\sigma[f] = \mathrm{Str}\, f(D_\sigma^2/\Lambda^2)$; in its large-$\Lambda$ heat expansion the **leading** Seeley–DeWitt coefficient is the cosmological/volume term $a_0$, and on the full graded tower its multiplicity weight is the graded dimension $\mathrm{Str}[\mathbf{1}] = n_B - n_F$. | Ties the leading coefficient's sign to the supertrace integer. | Chamseddine–Connes spectral action; `uv1_frozen_functional.py` FREEZE 2/3. |
| **A5** | **The Weyl-rigid projection.** The Weyl-rigid / $T^2$-invariant Cartan slice ($u \in [1/2,3/2]^3$) restricts the $K_6$ spectrum to the zero-weight $d_{\mathrm{eff}}=3$ tower; it acts as a **spectral restriction** of $D_\sigma^2$, **not** as new degrees of freedom, and **bounds shape, not volume** (so it imposes no kinematic floor on the collapse ray). | Keeps the tower a projection, not a dof injection, and leaves $\mathrm{Vol}\!\to\!0$ admissible. | `14D_PARENT_SELECTOR_GEOMETRY.md`; `gap04_chamber_exclusion.py`. |

**On the matter side of the count.** Under A2, the chiral dof are the spin-$c$ sections themselves: $|{\mathrm{ind}}| = 3$ families $\times\ 15$ Weyl per generation $\times\ 2 = 90 = n_F$. These have **no degenerate bosonic partner** — that is the whole force of "no mirror" — so they cannot be paired off against the $n_B=35$ bosons. This is the assumption that makes $\mathrm{Str}[\mathbf 1]\neq 0$ unavoidable rather than incidental.

---

## 3. Proof

The chain is short, and each link is a banked computation, not a model choice.

**Step 1 — Index $\Rightarrow$ three unpaired families, no mirror.**
By A2, $\mathrm{ind}\,D_{K_6}^{\mathrm{spin}^c} = -3$. An index is the *signed* count of zero modes, $\dim\ker D - \dim\ker D^\dagger$; a nonzero value is a topological integer that no continuous deformation, and no choice of admissible cutoff, can cancel. Its magnitude $|-3| = 3$ is the number of net chiral families; its sign is the statement that these are unpaired left-handed sections with **no mirror** right-handed partners. *(This is exactly the corpus's three-family witness; here we only use that it is a fixed integer.)*

**Step 2 — No mirror $\Rightarrow n_F = 90 > n_B = 35$.**
The $3$ unpaired families carry $3 \times 15 \times 2 = 90$ chiral fermionic dof (A2). Because they are unpaired (Step 1), they admit no degenerate bosonic partners to cancel against. The bosonic tower is the full gauge-fixed BV/BRST content, $n_B = 35$ (A3). Hence
$$ n_F = 90 \;>\; 35 = n_B. $$

**Step 3 — $\Rightarrow \mathrm{Str}[\mathbf{1}] = -55$.**
The graded dimension (supertrace of the identity over the full tower) is
$$ \mathrm{Str}[\mathbf{1}] \;=\; n_B - n_F \;=\; 35 - 90 \;=\; -55 \;\neq\; 0. $$
This is a single banked integer, **forced** by the index of Step 1; it is not a fitted or tunable quantity.

**Step 4 — $\Rightarrow$ leading coefficient $a_0 \propto (n_B - n_F) < 0$.**
In the Chamseddine–Connes framing (A4), the large-$\Lambda$ heat expansion is
$$ S_\sigma[f] \;\sim\; \sum_{k\ge 0} f_k\, a_{2k}(D_\sigma^2)\, \Lambda^{\,d-2k}, $$
whose **leading** term ($k=0$) is the cosmological/volume term $a_0 \sim \mathrm{Vol}$, weighted on the full graded tower by the graded multiplicity $\mathrm{Str}[\mathbf{1}]$. The profile moment $f_0$ is positive for every admissible cutoff profile (it is the integral of a positive integrand), so the **sign of the leading full-spectrum coefficient is the sign of $\mathrm{Str}[\mathbf{1}]$**. By Step 3 that sign is negative:
$$ a_0 \;\propto\; (n_B - n_F) \;=\; -55 \;<\; 0. $$

**Step 5 — $\Rightarrow$ no positive leading UV wall is derivable from the banked geometry.**
A "positive shrinking-volume UV wall" is, by definition, a *derived* positive leading contribution to the effective potential along $\mathrm{Vol}(K_6)\!\to\!0$ that walls off the collapse. The leading full-spectrum spectral coefficient is the natural candidate for that contribution, and Step 4 fixes its sign to be **non-stabilizing**. The Weyl-rigid projection (A5) supplies no rescue: it bounds shape, not volume, so it imposes no kinematic floor that could substitute for the missing positive leading term. Therefore **no positive leading UV wall follows from the currently banked geometry**. Any positive wall must instead be *supplied* — by a separately declared input that asserts a positive UV spectral measure (the named axiom `B-UQFC-14-UV-1`), which this geometry does **not** itself force. $\qquad\blacksquare$

**Banked runs and scripts (provenance).**

- **T1 — Index-cancellation exclusion** (Steps 1–3): $\mathrm{Str}[\mathbf 1] = 35 - 90 = -55 \neq 0$, forced by spin-$c$ index $-3$. Script `gap04_full_supertrace_residue.py`; run **`wovps8huo`** (supertrace), countersigned. The supertrace residue $\mathrm{Str}_{\mathrm{pole}} = +4.466$ survives precisely because $\mathrm{Str}[\mathbf 1]\neq 0$.
- **EFT-boundary companion** (frames where the asymptotic reading of $a_0,a_2,a_4,\dots$ even applies): `gap04_higher_operator_wall.py`; run **`wito6mc0z`** (EFT boundary), countersigned. The curvature reaches the cutoff at the phase-exit boundary $\sigma_* = \tfrac12\ln 30 \approx 1.70$, beyond which the heat expansion stops converging.
- **No-kinematic-floor** (Step 5, A5): $\sigma\!\to\!-\infty$ is admissible; Weyl rigidity bounds shape not volume. Script `gap04_chamber_exclusion.py`; run **`wg206lpk7`** (no floor), countersigned.
- **UV-1 axiom-level route** (Step 4, the $a_0$ identification): run **`wq91wo0x0`** — all three independent routes hit the same leading object $a_0 = -55$, and $a_0$ is the **same leading spectral object** as the cosmological-constant term (see §5). Freeze script `uv1_frozen_functional.py` (FREEZE 1–4), exit 0; banked $n_B=35,\ n_F=90,\ \mathrm{Str}[\mathbf 1]=-55$, spin-$c$ index $-3$, bundle hash `0fd19c9ae0c1`.

Every step is an index/arithmetic implication over frozen content. No measured number, no committed `c_loop`, and no observed $\Lambda$ entered any input.

---

## 4. Scope — what this theorem does **not** claim

The result is deliberately narrow. It is an *absence-of-derived-wall* statement, certified to be structural. It is **not** any of the following, and the discipline is to say so out loud:

1. **It does not claim the geometry runs away.** The negative leading sign denies a *derived positive* wall; it does **not** assert that the potential is unbounded below or that $\mathrm{Vol}\!\to\!0$ is actually reached. Both STANDS (a wall exists, supplied by the UV completion) and RUNAWAY remain live. The theorem rules out one *route to a conclusion*, not the conclusion.
2. **It does not solve, bound, or predict $\Lambda$.** No observed $\Lambda$ is compared against anything. The relation to $\Lambda$ (§5) is one of *shared hardness class and shared spectral source*, not of solution.
3. **It does not adopt, nor close, `B-UQFC-14-UV-1`.** The spectral-action UV-completion axiom (positive UV spectral measure) is **named, not assumed and not proven** here. It remains `precisely-OPEN-behind-named-object` (owner: Chris). This theorem is what makes that object *necessary* — it is the proof that the gap cannot be filled from the banked geometry alone.
4. **It does not depend on a finite-order coefficient sign.** Per the corpus's Lemma 1, no finite heat-kernel / FRG truncation is licensed to decide *global* stability along $\sigma\!\to\!-\infty$. The proof rides only on the **leading** graded multiplicity $\mathrm{Str}[\mathbf 1]$ and the positivity of the profile moment — never on $a_4, a_6, a_8$, which appear (if at all) only as consistency checks.

**The one positive claim it does make** is the structural one: the absence of a derived shrinking-volume wall is **not an accident of incomplete computation** and **not a convention artifact**. It is forced by a topological integer (the index) flowing through a fixed framing ($a_0 \propto \mathrm{Str}[\mathbf 1]$). Closing the same integer differently would require changing the matter content — which A2 forbids, since the index is the three-family witness. *That* is the sense in which the missing wall is structural: you cannot get the wall for free without giving up the families.

---

## 5. Relation to $\Lambda$ — same $a_0$ source

The cosmological-constant problem and the shrinking-volume-wall question are **not the same problem**, but in this geometry they draw on the **same leading spectral object**. The cosmological term in the spectral action *is* $a_0 \sim \mathrm{Vol}$, graded by $\mathrm{Str}[\mathbf 1]$ — the very coefficient whose sign Step 4 fixes to $-55$. So:

- The leading spectral-action coefficient that a derived UV wall would need on the *positive* side is the **same** $a_0$ whose graded weight controls the vacuum-energy / cosmological-constant line.
- The UV-1 axiom-level route (run `wq91wo0x0`) records that all three independent routes land on this one object, $a_0 = -55$. The obstruction therefore inherits **exactly the hardness class** of $\Lambda$: a sign/normalization that the banked geometry does not force, that a positive UV spectral measure would supply, and that is left as the single named axiom.
- This is the corpus's standing posture on $\Lambda$, mirrored: the chamber/grading route to $\Lambda$ is closed as an honest FAIL because the grading is coefficient-blind ($\mathrm{Str}[\mathbf 1]\neq 0$, the I2 supertrace) — the *same* $\mathrm{Str}[\mathbf 1] = -55$ that obstructs the wall here. One integer obstructs both a grading-based $\Lambda$ cancellation and a geometry-derived UV wall.

The honest reading is the irreducible-constant doctrine (CFCA §0.4): where the geometry stops forcing the answer, the missing piece is **named as a declared input**, not smuggled in as derived. The shrinking-volume UV wall and the observed $\Lambda$ both sit on the far side of that same named input — `B-UQFC-14-UV-1` — and this theorem is the proof that the input is *required*, because the index will not let the leading coefficient have the stabilizing sign on its own.

---

### One-paragraph summary

The spin-$c$ index $-3$ that delivers three chiral families with no mirror forces $n_F = 90 > n_B = 35$, hence $\mathrm{Str}[\mathbf 1] = -55 < 0$; in the Chamseddine–Connes framing the leading coefficient obeys $a_0 \propto \mathrm{Str}[\mathbf 1]$, so $a_0$ carries the non-stabilizing sign, and **no positive shrinking-volume UV wall is derivable from the banked geometry** without a separately named UV-completion axiom (`B-UQFC-14-UV-1`, OPEN, owner: Chris). This rules out a *route*, not a *conclusion*: it does not claim runaway, does not solve $\Lambda$, and does not close the axiom — it proves that the missing wall is **structural**, sourced by the same integer that draws the cosmological-constant line.
