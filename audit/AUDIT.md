# COMPLETENESS + EXACT-PATH AUDIT — Fable GUT/ToE corpus

**Date:** 2026-06-15
**Auditor scope:** 4 manuscripts (.md + .html renders) + supporting docs (METHOD_CFCA, GAP_CLOSURE_LOOP_DESIGN, INDEX_UV_WALL_OBSTRUCTION_THEOREM, UV_COMPLETION_CANDIDATE_MAP, submission_package/companion_detail/*).
**Discipline applied:** Completeness is the gate. FROZEN scientific content verified PRESENT and UNCHANGED (not edited by this audit). Honesty-first: where nothing was found, this report says so rather than inventing findings.

Base dir: `C:/Users/cberg/Desktop/VS Code Projects Random/physics_Journal_and_patents/Fable_Version/`

---

## FROZEN-CONTENT INTEGRITY CHECK (must survive cleanup unchanged)

All FROZEN anchors were located and confirmed present/intact. **Cleanup agents MUST NOT touch these:**

| Frozen item | Where (verified present) |
|---|---|
| §V truth table (18 gaps / 30 instruments / 4 terminal states) | `TOE_FINAL_merged.md` (front-matter routes to it; "Read §V before judging completeness") |
| Economy headline "Four measured numbers go in. Twenty-two-plus…" | `TOE_FINAL_merged.md` line 27 (also line 13 BIG IDEA) |
| Gap-04 close-out: **CLOSED-SCOPED / GLOBAL-UV-DELEGATED** | `TOE_FINAL_merged.md` lines 400, 402, 418, 420 (canonical frozen block) |
| T1 / T2 / T3 banked structural theorems | `TOE_FINAL_merged.md` lines 406–408; `rendered/UV_COMPLETION_CANDIDATE_MAP.md` lines 82–84 |
| T1′ — INDEX-UV-LAMBDA UNIFICATION (banked, axiom NOT adopted) | `TOE_FINAL_merged.md` line 410; `rendered/TOE_FINAL_June_14_diff.md` lines 96–112 |
| Decision-grade closures / status vocabulary / four terminal states | TOE §II / §V; `METHOD_CFCA_June_14.md` |
| Λ-1 placeholder PRESERVED-NOT-UPGRADED (frozen technical term) | `Fable_Quantum_merged.md` 641, 892, 9203; `GAP_CLOSURE_LOOP_DESIGN.md` 380 |

Reader-facing additions are correctly confined to CLEARLY-MARKED front-matter (e.g. TOE_FINAL "reader-optimized statement", "adds the reader on-ramp", BIG IDEA, WHY THIS MATTERS, HOW TO READ) and to the explicitly-marked HTML comment blocks in METHOD_CFCA/INDEX_UV_WALL. **No reader copy was found inside the technical body.**

---

## (1) IFRAMES / EMBEDDED INTERACTIVE ELEMENTS THAT BREAK IN PDF

**Finding: NO iframes, embeds, videos, audio, forms, buttons, or onclick handlers in any .md or .html file.** (Honest negative — none fabricated.)

The ONLY embedded/active element across all four HTML renders is a **MathJax `<script>` loaded from a CDN**:

| File | Line | Element | PDF impact |
|---|---|---|---|
| `rendered/TOE_FINAL_merged.html` | 5, 13 | `<script>` MathJax config + `<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">` | Requires network at render time. If PDF is generated from this HTML without network access, math will not typeset. PDFs already exist in `rendered/` so this was resolved at build; flag only if re-rendering offline. |
| `rendered/Fable_Forces_merged.html` | 5, 13 | same MathJax pair | same |
| `rendered/Fable_Quantum_merged.html` | 5, 13 | same MathJax pair | same |
| `rendered/Fable_GUT_merged.html` | 5, 8 | same MathJax pair | same |

No `<img>`, no data-URIs, no other `src=`/`href="http`/`@import` external resources. The single in-body hyperlink (`rendered/Fable_Quantum_merged.html` line 404) is the companion-paper link covered in §3.

**Non-issue noise (NOT iframes):** `Fable_GUT_merged.md:3828` `"<object name>": "<sha256-12 hash>"` is a JSON-schema placeholder string inside a hash-manifest example, not an HTML `<object>`.

---

## (2) INTERNAL / INCOMPLETE REFERENCES (TODO / TBD / placeholder / "see above-below" / "Chris will" / bare [ref])

**Finding: NO authorial TODO/FIXME/placeholder/TKTK in any of the four manuscript bodies.** Every literal-string hit resolves to FROZEN technical content or a legitimate status token. Itemized so cleanup agents do **NOT** "fix" frozen content:

### 2a. Manuscript bodies — all hits are frozen technical content (DO NOT EDIT)
| File:line | Text | Why it is NOT a placeholder |
|---|---|---|
| `TOE_FINAL_merged.md:78` | "...inputs = data/values still to be supplied" | Definition of a truth-table status category (CONDITIONAL row). Frozen §V vocabulary. |
| `Fable_Quantum_merged.md:641,892,9203` | "$\Lambda$-1 placeholder … preserved as a placeholder" | Frozen scientific term for the deferred cosmological-constant mechanism (Paper 4 reserve). Intentional. |
| `Fable_Quantum_merged.md:5647` | "predicted shift TBD" | Scorecard cell honestly marking an uncomputed quantity (the FROZEN honesty mechanism). Decision-grade, not authorial. |
| `Fable_Quantum_merged.md:6752–6755` | proton-decay rows "TBC" | Scorecard status cells (To Be Confirmed by experiment), with named experiments (Super-K/DUNE). Frozen. |
| `Fable_GUT_merged.md:4222` | "no row is a placeholder" | Certificate-completeness assertion — the OPPOSITE of a placeholder. |
| `Fable_GUT_merged.md:4030` | `pending_post_rebuild` (Appendix N hash) | Frozen status token: illustrative example explicitly "does not close Gates 1–10". Intentional, disclosed. |
| `Fable_GUT_merged.md:9853,10188,10289` | "Yukawas … inserted as free parameters / inputs to be inserted later" | Describes a REJECTED modeling branch (counter-result), not an author TODO. |
| `Fable_Quantum_merged.md:542,6349` | "exactly what is not yet done" / "not yet done" | Honest gap statements (the paper grading its own homework). Frozen. |
| many `… as above` / `see below` (GUT tables 5975/6216/6217/6232–6237; Quantum 2356/6752–6755; GUT:412 "see below") | All resolve to in-table anchors (DECISION block, adjacent scorecard rows). Anchors ARE resolvable. |

### 2b. "Chris will" / "awaiting Chris" — present, but ONLY in internal status docs (expected, not a manuscript defect)
These are legitimate blocking-condition / countersign-queue records in the referee-aid and design layer, NOT placeholders in the published manuscript body:
- `submission_package/companion_detail/00_REFEREE_AID_README.md:34` "Chris's countersign" + §0 blocking conditions — this layer's PURPOSE is to disclose what is pending.
- `rendered/GAP_CLOSURE_LOOP_DESIGN.md:446` `TODO(physics: Chris, F⁺-chamber derivation)` and "Chris-decision" — inside a DESIGN SPEC describing what a manifest *template* must contain. Internal design doc, not reader manuscript.
- `rendered/UV_COMPLETION_CANDIDATE_MAP.md` / `INDEX_UV_WALL_OBSTRUCTION_THEOREM.md` "(owner: Chris)" — owner field on an OPEN named object. Correct.

**Cleanup guidance:** None of the §2 items should be edited. If a public-facing release wants to suppress the internal "Chris"/countersign-queue language, that is an editorial scoping decision (defer to principal author) — it is NOT a completeness defect, and the manuscript bodies themselves are clean.

---

## (3) RELATIVE / SHORT PATHS THAT SHOULD BE EXACT FULL URLs FOR EXTERNAL REVIEW

The corpus already establishes the canonical host: **`https://physics.magflowmeters.com/gut/…`**
(confirmed live in `Fable_GUT_merged.md:3968` → `/gut/scripts/`; `Fable_Quantum_merged.md:367` → `/gut/quantum_forces/quantum_forces.md`).

The manuscripts deliberately invoke many project artifacts **by name as "EXTERNAL artifacts of record"** (see `Fable_GUT_merged.md:16707` — "invoked by name and not reproduced here"). Those bare `.md`/`.json` names (e.g. `selector_results.json`, `HANDOFF_*`, `UQC_04_strong_CP.md`, `restructure_plan.md`) are intentional named provenance anchors, NOT broken links — they do not each need a URL. The items below are the ones that ARE rendered as clickable/dereferenceable references and therefore benefit from an exact full URL for an external reviewer:

| File:line | Current form | Issue | Recommended exact URL |
|---|---|---|---|
| `Fable_Quantum_merged.md:367` and `rendered/Fable_Quantum_merged.html:404` | `[Four-Force Interface paper](https://physics.magflowmeters.com/gut/quantum_forces/quantum_forces.md)` | Link target is a raw `.md` (downloads/renders as plaintext, not a reader page). Path-precision only — host is already correct. | Point to the published render, e.g. `https://physics.magflowmeters.com/gut/quantum_forces/` (landing) or the `.html`. Leave host as-is. |
| `Fable_GUT_merged.md:3968` | `https://physics.magflowmeters.com/gut/scripts/` | Already exact. No change. | (keep) |
| `Fable_Quantum_merged.md:727,5151,5827` | `quantum_forces_build/quantum_forces.md` (bare relative) | If externalized, should resolve to the live Paper-2 URL. Currently an internal repo path. | `https://physics.magflowmeters.com/gut/quantum_forces/quantum_forces.md` |

See the canonical exact-path map below for the full intended URL for every supporting doc.

---

## CANONICAL EXACT-PATH MAP (supporting doc → intended physics.magflowmeters.com URL)

Host root: `https://physics.magflowmeters.com/`. The corpus already uses the `/gut/` prefix for the series; supporting docs map under `/gut/` subpaths consistent with the established `/gut/scripts/` and `/gut/quantum_forces/` examples.

### Manuscripts (4)
| Local file | Intended URL |
|---|---|
| `TOE_FINAL_merged.md` / `rendered/TOE_FINAL_merged.html` | `https://physics.magflowmeters.com/gut/toe/TOE_FINAL_merged.html` |
| `Fable_GUT_merged.md` / `rendered/Fable_GUT_merged.html` | `https://physics.magflowmeters.com/gut/paper1/Fable_GUT_merged.html` |
| `Fable_Forces_merged.md` / `rendered/Fable_Forces_merged.html` | `https://physics.magflowmeters.com/gut/forces/Fable_Forces_merged.html` |
| `Fable_Quantum_merged.md` / `rendered/Fable_Quantum_merged.html` | `https://physics.magflowmeters.com/gut/quantum/Fable_Quantum_merged.html` |

### Supporting / method docs
| Local file | Intended URL |
|---|---|
| `METHOD_CFCA_June_14.md` | `https://physics.magflowmeters.com/gut/method/METHOD_CFCA.html` |
| `rendered/GAP_CLOSURE_LOOP_DESIGN.md` | `https://physics.magflowmeters.com/gut/gap04/GAP_CLOSURE_LOOP_DESIGN.html` |
| `rendered/INDEX_UV_WALL_OBSTRUCTION_THEOREM.md` | `https://physics.magflowmeters.com/gut/gap04/INDEX_UV_WALL_OBSTRUCTION_THEOREM.html` |
| `rendered/UV_COMPLETION_CANDIDATE_MAP.md` | `https://physics.magflowmeters.com/gut/gap04/UV_COMPLETION_CANDIDATE_MAP.html` |
| `rendered/GAP04_IRREDUCIBLES_PHILOSOPHY_CLOSURE.md` | `https://physics.magflowmeters.com/gut/gap04/GAP04_IRREDUCIBLES_PHILOSOPHY_CLOSURE.html` |
| `rendered/GAP04_REVIEWER_DEFENSE_NOTE.md` | `https://physics.magflowmeters.com/gut/gap04/GAP04_REVIEWER_DEFENSE_NOTE.html` |

### Public scripts / reproducibility bundle (already canonical in corpus)
| Artifact | Intended URL |
|---|---|
| Scripts mirror (`reproduce_all.py`, build/hash/verify utils) | `https://physics.magflowmeters.com/gut/scripts/` |
| `reproduce_all.py` | `https://physics.magflowmeters.com/gut/scripts/reproduce_all.py` |
| Paper-2 source (`quantum_forces.md`) | `https://physics.magflowmeters.com/gut/quantum_forces/quantum_forces.md` |

### Referee-aid layer (submission_package/companion_detail/*) — INTERNAL by design
These are explicitly a "referee/editor convenience layer … NOT SUBMITTED … blocked on Chris countersign" (`00_REFEREE_AID_README.md` §0). They are NOT public-release targets in their current state. If/when cleared, map under:
| Local file | Intended URL (only if cleared for release) |
|---|---|
| `submission_package/companion_detail/00_REFEREE_AID_README.md` | `https://physics.magflowmeters.com/gut/referee/00_REFEREE_AID_README.html` |
| `submission_package/companion_detail/00_SERIES_SPINE.md` | `https://physics.magflowmeters.com/gut/referee/00_SERIES_SPINE.html` |
| `submission_package/companion_detail/01_READING_ORDER_AND_ON_RAMP.md` | `https://physics.magflowmeters.com/gut/referee/01_READING_ORDER_AND_ON_RAMP.html` |
| `submission_package/companion_detail/02_FAST_VERIFIABILITY_AFTERNOON_CHECKS.md` | `https://physics.magflowmeters.com/gut/referee/02_FAST_VERIFIABILITY_AFTERNOON_CHECKS.html` |
| `submission_package/companion_detail/02_REFEREE_FAST_PATH.md` | `https://physics.magflowmeters.com/gut/referee/02_REFEREE_FAST_PATH.html` |
| `submission_package/companion_detail/03_TEST_IT_YOURSELF_FIVE_PROMPTS.md` | `https://physics.magflowmeters.com/gut/referee/03_TEST_IT_YOURSELF_FIVE_PROMPTS.html` |
| `submission_package/companion_detail/04_REPRODUCIBILITY_FREEZE_AND_CODE.md` | `https://physics.magflowmeters.com/gut/referee/04_REPRODUCIBILITY_FREEZE_AND_CODE.html` |
| `submission_package/companion_detail/05_WHAT_TO_ATTACK_FIRST.md` | `https://physics.magflowmeters.com/gut/referee/05_WHAT_TO_ATTACK_FIRST.html` |
| `submission_package/companion_detail/01_VENUE_FIT_HONEST.md` | `https://physics.magflowmeters.com/gut/referee/01_VENUE_FIT_HONEST.html` |
| `submission_package/companion_detail/VENUE_FIT_AND_READINESS_ASSESSMENT_2026-06-13.md` | `https://physics.magflowmeters.com/gut/referee/VENUE_FIT_AND_READINESS_ASSESSMENT.html` |

---

## SUMMARY FOR CLEANUP AGENTS

1. **iframes/interactive:** none to remove. Only action: ensure MathJax renders/PDFs are network-resolved (already done — PDFs exist in `rendered/`). If re-rendering offline, vendor MathJax locally or keep CDN with network.
2. **placeholders/TODOs:** none in manuscript bodies. Do NOT "fix" frozen status tokens (TBD/TBC/`pending_post_rebuild`/Λ-1 placeholder). The only literal `TODO(...)` lives in an internal design spec (`GAP_CLOSURE_LOOP_DESIGN.md:446`), not in any manuscript.
3. **paths:** host is correct everywhere it appears (`physics.magflowmeters.com/gut/...`). Only path-precision fixes: (a) the Quantum companion link points at a raw `.md`; (b) bare `quantum_forces_build/quantum_forces.md` relative paths if externalized. Apply the exact-path map above.
4. **DISCIPLINE:** Do not edit the FROZEN-CONTENT INTEGRITY table items. Reader-facing copy stays in marked front-matter only.
