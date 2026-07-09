# Site architecture — `constraint-first-geometry`

A map of the public site (`physics.magflowmeters.com`) as mirrored in this repository, plus the
source/artifact tiers. Regenerated 2026-07-09.

## How the repo is laid out
- **`site/`** — a faithful mirror of the live public site (all current sections, `.html`; pages are
  self-contained with inline CSS). Excludes only the `/old/` archive (superseded snapshots, not part of the
  current architecture).
- **`papers/`** — the long-form papers as Markdown sources (`*.md`) + rendered `*.pdf` (GUT, TOE, Quantum,
  Forces, Particles). These are the citable artifacts; the browsable HTML lives under `site/articles/`.
- **top-level docs** — `README.md`, `CHANGELOG.md`, `CITATION.cff`, `HASHES.sha256`, `VERSION`, `LICENSE`, etc.
- **`audit/`, `examples/`, `scripts/`, `supporting/`** — reproduction tooling and supplementary material.

## The site, by section

**Entry & method**
- `/` — home; the one-shape thesis and the start-here callouts.
- `/process/` — the constraint-first method (how the shape is derived, not guessed).
- `/AI-testing/` — the flagship advocacy page: **Part 1** makes the case to an external AI reviewer (verifiable
  claims + `fable_reviewer_documents.zip` to reproduce + `fable_solver_packet.zip` to use it); **Part 2** makes
  the case to a human (the overwhelming list of independent hits). `ai-review-exhibit.html` = the full prior
  AI-review record, linked as a supporting exhibit.
- `/paying/` — what "paying" (anchoring to a measured ruler) means.

**The two anchoring layers (building blocks)**
- `/building-blocks/` — how every result rests on two layers: observed phenomena + shape/scale/granularity.
- `/observables/` — the full registry of measured phenomena the physics is tested against.
- `/shape/`, `/scale/`, `/granularity/` — the three deep roots (high-level, with links to full depth).

**The requirement gates (SOURCE OF TRUTH)**
- `/gates/` — the 33-gate scoreboard; **the canonical status of every closure**. Board: 33 resolved at +0 / 0
  anchored at +1 / 0 open. `/gates/dossiers/` — the per-gate full-depth dossiers.
- `/residuals/` — the attack list (named open residuals shown under reached terminals).
- `/walls/` — the wall register (deeper technical closure paths; **derived from the gates**, propagate-outward).
- `/anchors/` — per-gate anchor ledgers (which measured/axiom anchors each gate rests on).
- `/closure/` — the closure system (terminals, wall-routing).

**The theories**
- `/forces/`, `/quantum/`, `/gut/`, `/toe/`, `/particles/` — the theory pages (`/v2/` = current where present).
- `/articles/` — the full papers, dossiers, and closure compendiums as browsable HTML (Markdown sources in
  `papers/`).

**Cosmology, foundations & extras**
- `/early-universe/` (+ `/tests/`) — the cosmic-timeline reconstruction (44 checkpoints: 30 agree / 0 disagree
  / 14 indeterminate) and its blind-prediction tests.
- `/tests/` — the standalone tests (incl. the quantum-computer and NASA-grade GR calculators).
- `/consciousness/`, `/emergent-separability/` — interpretive sections.
- `/layer2/`, `/supplemental/`, `/supporting/`, `/scripts/` — second-layer roots and supporting material.
- `/v1/` — the earlier public version (kept for reference).

## Editing / propagation rules
- **`/gates/` (ledger + dossiers) is the source of truth.** All other pages are DERIVED — a discrepancy is
  fixed by propagating *from* the gates outward, never the reverse.
- Closures are **never downgraded** (upgrade-only; a reached terminal stays closed with residuals shown).
- Public pages are plain physics; internal-process vocabulary stays off-page.
