# NARRATIVE FRAME — The Fable Series, Site Release

**Status of THIS file:** READER-FACING FRONT-MATTER DRAFT ONLY. Everything below is
*narrative scaffolding* for the landing page and per-article on-ramps. It states **zero new
physics**, advances **no status**, changes **no number**, and introduces **no gate**. The four
frozen manuscripts and their §V truth table, terminal states, economy headline, Gap-04 close-out,
and T1/T2/T3/T1′ are preserved exactly and are never restated as anything other than what the
documents already say. Reader-facing additions live here, in clearly-marked front-matter, and never
inside the technical body. The hook is **integrity, not hype.**

> **A discipline note up front (honesty gate).** This frame was asked to find the site's iframes and
> placeholder references and report them honestly. The honest finding:
> - **No iframes.** The release now ships HTML files — the landing page (`index.html`), the four
>   article HTML renders under `articles/` (plus their Markdown sources and canonical PDF downloads),
>   and three directory-index pages (`articles/`, `scripts/`, `supporting/`) — alongside the Python
>   scripts, their JSON/CSV outputs, and the Markdown supporting docs. **None of that HTML contains an
>   iframe.** The only active element anywhere is the MathJax `<script>` loaded from a CDN in the four
>   article renders (math typesetting). There is nothing else to embed and nothing embedded. I will not
>   invent an iframe that does not exist.
> - **Placeholder references DO exist — and they are honest ones, not site stubs.** `bg10_four_fix.py`
>   carries explicit `TODO(physics: Chris, F⁺-chamber derivation)` markers with `None` for the four
>   deferred baryogenesis inputs (Y_ν, M_N, Dirac_δ_CP, T_RH); `lambda_L1L3_radstab.py` and its
>   output JSON carry `"lambda_1_placeholder": "PRESERVED-NOT-UPGRADED"`. These are the manuscripts'
>   **own disclosed deferred soft-spots** (BG-10 at 0/4; Λ's surviving L1–L3 lane), surfaced in code
>   exactly as the papers surface them in prose. They are part of the honest content, not gaps to
>   paper over — and the narrative below treats them as such.

---

## THE PREMISE (the stakes)

Can the universe's deepest numbers — why there are exactly three families of matter, how the four
forces split, the tilt of the early universe, the weight of the vacuum — be **derived from one
geometry**, rather than measured and shrugged at? This series makes that bet on a single
thirteen-dimensional shape, four measured numbers in, and asks the reader to watch the shape return
twenty-two-plus independent quantities back out. But the real stakes are not the answer; they are the
**discipline**: a method bound to a record that would rather report an honest failure than a flattering
success — and that, on camera, refused the flattering answer four times and published the one place it
genuinely broke.

---

## THE CHARACTER (whose wagon we hitch to, and why we trust them)

We do not ask the reader to bond with a theory. We ask them to bond with a **way of being honest under
temptation** — embodied by three figures the reader can identify with because each one is brave in the
one way that costs something:

- **The honest author**, who built the cage before theorizing and wrote each claim's obituary in
  advance — naming, for every open item, the experiment and the year that could kill it. The author's
  signature move is the hardest one in science: *say where you are wrong, first, in public, before
  anyone forces you to.* (No byline is finalized; the author block is honestly absent pending entity
  formation — stated, not hidden.)

- **The self-skeptical method (CFCA)** — the real protagonist. It is the detective's eye (eliminate the
  impossible), the naturalist's patience (assemble before theorizing), and the physicist's imagination
  (interrogate the assumption hiding *inside* your own surviving explanation). We trust it because it has
  a track record of refusing to flatter the thing that built it: it tested the theory's deepest hope
  against the cosmological constant, **watched it fail, proved the failure inevitable, and published the
  refutation**; and it **retracted its own baryogenesis closure within a day** of claiming it, under its
  own audit, and left the gap loudly open. A method that publicly reverses *itself* — and gets deeper
  each time — is showing you its evidence chain, not asking for your faith.

- **The AI co-investigator**, the tireless second pair of eyes that ran the eliminations, froze the
  hashes before the comparison, and held the min-rule against the temptation to round up — a partner in
  the discipline, never an oracle that outranks the record.

**Why the reader can trust them:** because the thing they are selling is the *courage to be wrong in
public*. Every page routes its own weakest links to the top, attaches a falsifier to every open claim,
and pins the headline to the worst row, never the best. The min-rule makes self-flattery a structural
drafting bug. That is something a reader can identify with and check — not a personality to admire.

---

## THE JOURNEY (the 4-paper arc as a quest — each paper a trial)

The four papers form a hierarchy, and read as a quest each is a distinct trial of the same discipline:

- **Trial I — Can the shape build the world? (Paper 1, GUT.)** The hero's strongest banked claim, and
  the only one making a *certificate* claim. Four anchors in; nineteen-plus flavor observables and three
  families out — the families counted like a rubber band's winding, with no dial. The load-bearing
  trial: is the F⁺ chamber a derivation or disguised curve-fitting? It is asked to be wrong on a napkin.

- **Trial II — Do the four forces come from the one shape? (Paper 2, Forces.)** The least-over-claimed
  trial. Four explicit maps route gravity and the strong, weak, and electromagnetic forces out of the
  single frozen coset, with **zero new dials** between five strengths — two of them (e, G_F) not
  predictions but identities that break against measurement if the geometry is wrong. It re-closes no
  gate; it inherits and is honest about it.

- **Trial III — Does it survive being made real? (Paper 3, Quantum.)** The trial where unification
  usually dies — quantization, where ghosts, anomalies, and mirror fermions surface. The paper runs all
  four forces through a seventeen-gate stress-test and **prints its own weakest link as the headline
  (Σ = AUDIT)** by the min-rule, eight rows held open on purpose. The bravest cover page in the series.

- **The Capstone — Was the whole quest honest? (TOE_FINAL.)** The state-of-the-programme ledger and the
  tie-breaker. Its §V truth table places every gap in exactly one terminal state with a falsifier
  attached, carries the Λ honest-FAIL and the four-branch inflation table rather than one flattering
  band, and makes zero promotions. It is the place the quest is graded — in public, against an
  append-only record.

Read end to end, the arc is one sentence: *fix what cannot move, eliminate what cannot survive,
interrogate the assumption hiding inside what remains, keep only what every honest observer would have
to keep — and publish, to the experiment and the year, every place you are not yet forced.*

---

## READER-FACING FRONT-MATTER — PER ARTICLE

*(Premise + hook + "here is what you're about to watch happen." Humble and honest; preserves all frozen
content exactly. Goes in front-matter only.)*

### Paper 1 — Fable_GUT — *A Compact Grand Unified Theory Candidate by Constraint Selection*

This is the load-bearing one — the only paper here that makes a certificate-grade claim, and the place
the whole programme either stands or falls. The premise is audacious and simple: take one small frozen
shape, feed in **four measured numbers**, and read the gauge sector and nineteen-plus flavor observables
back off the geometry — including the most arbitrary-looking fact in physics, *why there are exactly
three families of matter*, which comes out as an integer the shape counts, with no dial to turn it to
two or four. More answers than questions is the fingerprint of a theory that is **constrained, not
curve-fitted.**

Here is what you're about to watch happen: the paper hands a hostile reviewer its ten most vulnerable
points *first*, and dares you to break the load-bearing one — is the F⁺ flavor chamber a real derivation,
or compressed Yukawa fitting? You can check the discipline in five minutes by hand (the anomaly witness
3·(1/6) − 1/2 = 0; the Einstein–Maxwell field-energy reproduction to six significant figures). Six hard
sectors are declared **excluded, not failed**, fenced by a binding rule that no required gate may be
closed by hiding its difficulty in the excluded row. Read it as a candidate cornered by constraints, not
a finished proof of nature — and check it at every gate.

### Paper 2 — Fable_Forces — *13D Four-Force Interface from the Constraint-Selected Geometry*

The premise of the second trial is the most falsifiable sentence in the series: **the four forces are the
symmetries of one small frozen shape.** Take the six-dimensional flag manifold the first paper froze, and
let the strong, weak, electromagnetic, and gravitational forces each fall out as an explicit projection of
that one geometry — with **zero new dials** between the five force strengths. Two of them, the electric
charge e and the weak Fermi constant G_F, are not predictions at all but **identities**: an identity that
disagreed with experiment would prove the geometry wrong on the spot.

Here is what you're about to watch happen: this is the least-over-claimed paper of the four, and it says so.
It re-closes no gate — every certificate is owned upstream by Paper 1, and if a Paper 1 gate downgrades, the
rows here downgrade with it, automatically. It declares its four weakest links *before* any physics (chiefly
the gravity interface's honest dependence on a frozen volume modulus). The attack-first target is named for
you: the composite map π_QED ∘ π_weak — if that is not a real map from the frozen geometry, the whole routing
collapses. It is "sharp enough to be wrong on a napkin, and it tells you exactly where."

### Paper 3 — Fable_Quantum — *13D Unified Quantum Force Completion*

The premise here is the one most unification programmes never survive: **writing down the forces is the easy
half.** The hard half is making them survive *quantization* — where ghosts fail to cancel, anomalies survive,
and mirror fermions the world does not contain show up, none of it visible until you actually quantize. So
this paper runs all four forces through a **seventeen-gate stress-test** and does the bravest thing a theory
can do on its own cover: it prints its **weakest link as the headline.**

Here is what you're about to watch happen: the aggregate tier is the **minimum** over all seventeen gates, so
no strong result can hide a weak one — and the paper ships at **Σ = AUDIT, on purpose**, because the
Yang-Mills mass gap (a Clay Millennium problem), asymptotic safety, and strong CP genuinely sit open inside
its scope, and the min-rule forbids it from claiming more. Eight AUDIT rows are routed to the very top for a
hostile reader. You will see the discipline tested against temptation in the strong-CP row — the single most
tempting line to "complete" — checked against the live record and **deliberately left open**. Read the
headline correctly: AUDIT is the honest floor a weakest-link rule forces, not a verdict that the work is
sloppy. A theory that printed its average instead of its minimum would be the one to distrust.

### Capstone — TOE_FINAL — *The Fable TOE: The Complete Statement*

The premise of the capstone is the whole series in one breath: **one thirteen-dimensional shape, four
measured numbers, and a rule that the theory must publish every place it is wrong** — and so far it has
passed every test it could run, published in full the one place it failed, and named each test it hasn't yet
run. Four measured numbers go in; **twenty-two-plus independent quantities** come out — the economy headline,
the fingerprint of a theory that is constrained, not fitted. It even ships a test rigged to come out negative
(PCM-12), so you can check that the discipline is real and not just claimed.

Here is what you're about to watch happen: this is the ledger where the programme grades its own homework in
public, with a fixed vocabulary, and **catches itself** — you will watch it reverse four of its own optimistic
errors, numbered #2 through #5, and get *deeper* each time. The hardest number in physics — the cosmological
constant — it tested its deepest idea against, **failed honestly, and published the refutation**; Λ remains
Weinberg-open and no observed-Λ comparison is made anywhere. If you read only one thing, read §V — the truth
table — where every one of the eighteen gaps lands in exactly one of four terminal states (closed-by-
computation, closed-at-decision-grade, conditional-behind-a-named-gate, precisely-OPEN-with-a-falsifier-
attached), with its kill-condition attached. Gap-04 is honestly **CLOSED at decision grade, not
certificate grade** — its scoped close-out cleared the operative bound by 35× (weakest variant) / 2.4×10³
(central), with the residual c_loop named and proved unable to threaten the well, and the global-UV question
explicitly **delegated**, not claimed. Of eighteen gaps, fourteen are deliberately OPEN — because an open gap
with a named kill-condition is a *specification*, not an admission. This is a state-of-the-programme ledger,
not a finality claim. *The pitch in one breath: this might actually be it — and it tells you, to the
experiment, exactly where it isn't yet.*

---

## NARRATIVE SPINE FOR THE LANDING PAGE

**Open on the stakes, not the claim.** The deepest numbers in the universe have always been *measured and
shrugged at.* This series asks whether they can be **derived from one shape** — and binds itself to a rule
that would rather report failure than fool itself.

**Act 1 — The bet (the economy).** One thirteen-dimensional shape. Four measured numbers in. Twenty-two-plus
independent quantities out. *More answers than questions* — the signature of a theory that is constrained,
not curve-fitted. (And a control rigged to come out negative, so you can check the discipline is real.)

**Act 2 — The character we trust (the discipline that refuses to flatter itself).** Meet the method that
catches its own optimism in public: it tested its deepest hope against the cosmological constant and
**published the refutation**; it **retracted its own baryogenesis closure within a day**. The honesty is
mechanical, not rhetorical — every claim wears a status label, the headline is pinned to the *weakest* row,
and self-flattery is a structural drafting bug. *This is the courage to be wrong in public.*

**Act 3 — The quest (four trials).** Four papers, four trials of the same discipline: *Can the shape build
the world?* (GUT) → *Do the four forces come from the one shape?* (Forces) → *Does it survive being made
real?* (Quantum, Σ = AUDIT on the cover) → *Was the whole quest honest?* (the capstone ledger). Each trial
routes its own weakest links to the top and names the experiment that could end it.

**Act 4 — The calendar of ways to die (the falsifier timeline).** Between now and ~2035 the world hands the
series repeated chances to die — m_W (2027), LiteBIRD r (2030+), proton-lifetime reach (~2035), nEDM on θ̄,
dark-matter direct detection, the baryon window η_B. Each is a published bound with a date.

**Close on the invitation, not the verdict.** *The series does not ask to be believed. It hands you its
weakest links first, attaches a kill-condition to every open claim, names the year each one could die — and
invites you to check it at every gate.* The honest thing it has not done is also stated plainly: nothing is
submitted, the author block is pending, and the deferred soft-spots (Gap-04 c_loop, Λ, BG-10, θ̄, the eight
AUDIT rows) are disclosed by the documents themselves. **Read on — and check us at every gate.**
