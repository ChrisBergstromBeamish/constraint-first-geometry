# How to Break This

This repository exists to be attacked. The request is not "believe this" — it is **"try to break this, and tell us exactly where it broke."** A genuine refutation is the most valuable contribution you can make, and it will be logged, credited, and acted on in [`ERRATA.md`](ERRATA.md).

This guide tells you where to push, how to file what you find, and the shared vocabulary that lets a finding be acted on rather than argued about.

---

## 1. Where to push (cheapest first)

| Attack | Effort | What breaks if you succeed |
|---|---|---|
| **Anomaly witness** — verify `3·(1/6) − 1/2 = 0` for one generation; perturb the hypercharge lattice | 30 s | **Fatal** — the gauge sector |
| **The counting claim** — show the 22+ outputs are not independent, or were not frozen before comparison | ~1 h | **Fatal** — the over-determination claim, the whole case |
| **Hidden input / smuggled tuning** — find a fifth number that functions as an input but is presented as an output | ~1 h | **Fatal** — the over-determination claim |
| **Reproduction** — run `scripts/reproduce_all.py`; produce a `FAIL` that is not `REFUSED-by-design` | minutes | The affected gate drops from certificate to diagnostic |
| **A graded result** — show a "certified" result is actually decision-grade or open | varies | That claim is downgraded in `ERRATA.md` |
| **A dated falsifier** — a measurement lands outside a frozen band (see [`FALSIFIERS.md`](FALSIFIERS.md)) | wait for data | The named sector falls |

The two that take the spine are the **anomaly witness** and the **counting claim**. If you only have an hour, spend it on the counting claim.

## 2. What counts as a finding (and what doesn't)

A finding must have a **specific locus** — the place it lives and the exact mismatch.

- ✅ **A finding:** "Trace *X* in Forces §8.6.4 evaluates to *Z*, not the claimed *W*; here is the arithmetic." / "Output *A* in Table 1 is algebraically `f(input B)`, so it is not independent; here is the derivation." / "`scripts/reproduce_all.py` returns `FAIL` on script *N* with this traceback."
- ❌ **Not a finding (yet):** "I don't believe it." / "Independent researchers can't do this." / "This is too good to be true." These may be *priors* — and they may even be right — but they are not bugs anyone can fix or refute. Convert them into a locus.

If you can't yet name a locus but smell a problem, open a **discussion**, not an issue. Issues are for specific, checkable claims.

## 3. Speak the grading vocabulary

So findings can be acted on precisely, use the same four terminal states the corpus uses. Every claim sits in exactly one:

- **Certified** — established by a closed proof or a reproducible computation.
- **Decision-grade** — the best available computation supports it, but it is not a closed proof. (Weaker than certified, and labelled as such.)
- **Open** — an honestly unsolved problem, carrying a named falsifier.
- **Refuted** — tested and failed. (Yes, the corpus contains these on purpose — see the cosmological-constant entry.)

**The min-rule:** the grade of any composite is the *minimum* over its parts. If you show one load-bearing component is weaker than claimed, the whole aggregate drops to that level. Pointing at the weakest link is therefore not nitpicking — it is the highest-leverage move in the system.

## 4. How to file

Use the issue templates in `.github/ISSUE_TEMPLATE/`:

- **Falsification attempt** — you checked a specific claim and it failed.
- **Reproduction failure** — a script behaves differently than documented.
- **Hidden input / tuning** — you believe an "output" is actually an input or was tuned to data.

Include: the **locus** (paper + section, or script + line), the **claim** you are challenging, the **check you ran**, **expected vs. found**, and a **severity** (fatal / downgrades-a-gate / cosmetic).

## 5. What happens when you find something

1. The finding is reproduced by a maintainer.
2. It is entered in [`ERRATA.md`](ERRATA.md) with your attribution, dated, with a severity.
3. The construction is either **fixed**, the affected claim is **downgraded** to its true grade, or — if it's a spine-breaker — the central claim is **withdrawn**. All three outcomes are recorded publicly.

There is no outcome in which a confirmed error is quietly dropped. That guarantee is the whole point of doing this in the open.

## 6. Rules of engagement

- **Adversarial is welcome; uncivil is not.** Attack the work as hard as you like; address people decently. (See `CODE_OF_CONDUCT.md`.)
- **No appeals to authority in either direction.** "A PhD would never accept this" and "a computer did this so it must be wrong" are both noise. Only the locus matters.
- **Credit is shared generously.** Anyone who finds a real flaw is named. Anyone who verifies a non-trivial result is named.

*A construction that hands you the fastest way to kill it, and survives, has earned the hour. That's the deal.*
