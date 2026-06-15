# DEPLOY MANIFEST — physics.magflowmeters.com

**Date:** 2026-06-15
**Staging root:** `C:/tmp/physics_site_release/`
**Target host root:** `https://physics.magflowmeters.com/`
**Total payload:** 77 files, 67,395,567 bytes (64.27 MB).

> **Self-contained:** the staged root **becomes** the public site root. Every link on
> the landing page resolves to a file inside this upload, with **exactly one** external
> dependency by design: `/gut/nasa/`, the independent NASA-facing GUT companion (an
> owner-designated public companion that survives the archive of the old gated site).
> The landing has **no dependence** on the old `/gut/` article / method / scripts tree —
> those paths have been repointed to in-upload `/articles/`, `/supporting/`, and
> `/scripts/` files.

> **Scope of this document (operations only).** This manifest is a deploy/migration
> map. It states **zero physics**, edits **no frozen content**, and changes **no
> number**. The FROZEN scientific content — the §V truth table, every decision-grade
> closure, the economy headline ("Four measured numbers go in. Twenty-two-plus…"),
> the Gap-04 **CLOSED-SCOPED / GLOBAL-UV-DELEGATED** close-out, and **T1/T2/T3/T1′** —
> was verified present and intact in the staged articles and supporting docs, and is
> preserved exactly. The four article bodies (`articles/*.html`, `articles/*.md`) and
> the canonical article PDFs (`articles/*.pdf`) are byte-frozen and untouched. Reader-facing
> copy lives only in clearly-marked front-matter (`index.html`, the directory-index pages
> `articles/index.html` / `scripts/index.html` / `scripts/outputs/index.html` /
> `supporting/index.html`, the runner header of `scripts/reproduce_all.py`, and the
> front-matter blocks of `NARRATIVE_FRAME.md`, `AUDIT.md`, `supporting/INDEX.md`,
> `scripts/MANIFEST.md`, and the per-doc front-matter blocks).

---

## 0. Honest findings (completeness gate)

- **iframes / embeds / video / audio / forms / `<object>` / `<source>`:** **NONE**
  anywhere in the release (searched all `.html`, including the four new directory-index
  pages). Honest negative — none fabricated. The only active element in any HTML is the
  **MathJax `<script>` loaded from a CDN** in the four article renders (math
  typesetting; needs network at view time). The landing and the four index pages use
  inline CSS only, no scripts.
- **Placeholder references:** the only **reader-facing site placeholder** is in
  `index.html` (§5 QC): `Will be added July 16` for the provisional-patent link — a
  deliberate, dated front-matter marker. All other `placeholder`/`TODO`/`TBD`/`TBC`
  tokens in the release are **FROZEN scientific status terms** (the Λ-1 placeholder
  PRESERVED-NOT-UPGRADED; "predicted shift TBD"; the owner-locked
  `TODO(physics: Chris, …)` slots in `bg10_four_fix.py`) and were **NOT** altered.
- **Internal links (self-contained):** **every** root-relative link in `index.html`
  resolves to a file or directory-index inside this upload (verified file-by-file — see
  §3). The four article cards now link the in-upload `/articles/*.html` (primary),
  `/articles/*.md` (source), and `/articles/*.pdf` (canonical) directly — the old
  `/gut/<article>` "canonical" links, which would 404/gate once the old tree is archived,
  have been **removed**. The scripts/supporting section links the in-upload
  `/scripts/reproduce_all.py`, `/scripts/MANIFEST.md`, all nine `/supporting/*.md`, and
  the directory indexes. The **only** external link is `/gut/nasa/` (independent
  companion; see §4).
- **Reproducibility driver added:** `scripts/reproduce_all.py` is a new self-contained
  runner that executes all 21 staged scripts in turn and prints PASS / REFUSED-by-design
  / FAIL per script plus a summary. It removes the prior dependence on
  `/gut/scripts/reproduce_all.py`. Verified: it discovers 21 scripts, reports **19 PASS,
  2 REFUSED-by-design** (`bg10_four_fix.py` exit 2 = owner-locked refusal;
  `strongcp_realizationB.py` exit 1 = banked honest-negative, gate stays OPEN), **0 FAIL**,
  and exits 0. It exits 1 only on a genuine failure (unexpected exit or uncaught exception).
- **Stale meta-note resolved (now corrected):** `NARRATIVE_FRAME.md`'s honesty-gate
  bullet previously said "There are no HTML files anywhere in `physics_site_release/`."
  That described an earlier staging snapshot and is now false. It has been **corrected**
  in-place (front-matter self-description, not frozen science) to state accurately that
  the release ships HTML articles + landing + index pages, with canonical PDFs as
  downloads, and that none of that HTML contains an iframe.

---

## 1. Tree (file counts per directory)

```
physics_site_release/                      4 files at root
├── index.html                             (landing — reader front-matter only)
├── AUDIT.md
├── NARRATIVE_FRAME.md
├── DEPLOY_MANIFEST.md                      (this file)
├── articles/                             13 files  (4 articles × {.html,.md,.pdf} + index.html)
│   ├── index.html                          (directory index of the 4 articles)
│   ├── GUT.html / GUT.md / GUT.pdf         (GUT.pdf ~40 MB)
│   ├── Forces.html / Forces.md / Forces.pdf
│   ├── Quantum.html / Quantum.md / Quantum.pdf
│   └── TOE.html / TOE.md / TOE.pdf
├── scripts/                              24 files  (21 .py + reproduce_all.py + MANIFEST.md + index.html)
│   └── outputs/                          25 files  (24 artifacts: .json × 23, .csv × 1; + index.html)
└── supporting/                           11 files  (INDEX.md + 9 supporting docs + index.html)
```

Counts reconcile with the in-bundle manifests: `scripts/MANIFEST.md` ("21 Python
scripts, 24 output artifacts" — the new `reproduce_all.py` is the driver over those 21,
not one of the 21) and `supporting/INDEX.md` ("9 supporting documents").
Total tree: **77 files, 64.27 MB** (the size jump vs the prior 7.83 MB is the four
canonical article PDFs, dominated by `GUT.pdf` at ~40 MB).

---

## 2. Migration plan (owner-decision steps)

Run on the `physics.magflowmeters.com` document root (host `public_html/`).

1. **Archive the current (gated) site.** Move everything currently under
   `public_html/*` to `public_html/old/` (preserve, do not delete) — full rollback
   point. The old gated site is archived to `/old`; it is no longer the landing.
   - Guard: do **not** sweep `public_html/old/` into itself; create it first, then
     move siblings. Verify the move with a directory listing before step 3.

2. **Keep ONLY `/gut/nasa/` as an independent public companion.** The NASA-facing GUT
   companion at `https://physics.magflowmeters.com/gut/nasa/` is the one
   owner-designated path that must survive the archive. Carry **just** `/gut/nasa/`
   across intact (or re-establish it) at `public_html/gut/nasa/`. The **rest** of the
   old `/gut/` tree (the old article / method / scripts renders) is archived into
   `/old` with everything else — the new landing no longer references it, so nothing on
   the landing 404s when it is gone. (This is the change from the prior plan, which kept
   the whole `/gut/` tree; the landing is now self-contained except for `/gut/nasa/`.)

3. **Upload the staged root as the new site root.** Copy the entire contents of
   `C:/tmp/physics_site_release/` to `public_html/` so that:
   - `index.html` becomes the site landing page,
   - `/articles/` (incl. the four `.pdf` downloads), `/scripts/`
     (+`/scripts/outputs/`), `/supporting/`, `/AUDIT.md`, `/NARRATIVE_FRAME.md`,
     `/DEPLOY_MANIFEST.md` sit at the document root.

4. **Directory-index check (already satisfied in-upload).** `index.html` links four
   trailing-slash paths — `/articles/`, `/scripts/`, `/scripts/outputs/`,
   `/supporting/`. Each now ships its own `index.html` listing page in this upload, so
   they resolve **without** relying on server autoindex. No autoindex configuration is
   required for the landing's links to work.

5. **Smoke test after upload** (see §5 checklist).

---

## 3. Staged file → target URL map (every staged file)

Host root for all rows: `https://physics.magflowmeters.com/`.
"Resolves in upload" = a root-relative link in `index.html` points here and the file
is in this upload.

### Root (4)
| Staged file | Target URL | Linked from index.html |
|---|---|---|
| `index.html` | `/` (and `/index.html`) | — (it is the landing) |
| `AUDIT.md` | `/AUDIT.md` | yes — footer "completeness & exact-path audit" |
| `NARRATIVE_FRAME.md` | `/NARRATIVE_FRAME.md` | yes — footer "narrative frame" |
| `DEPLOY_MANIFEST.md` | `/DEPLOY_MANIFEST.md` | no (ops doc; not reader-linked) |

### articles/ — 4 articles, three formats each + index (13)
| Staged file | Target URL | Linked from index.html |
|---|---|---|
| `articles/index.html` | `/articles/` | yes — "directory index of all four articles" |
| `articles/GUT.html` | `/articles/GUT.html` | yes — Paper 1 "Read (HTML)" |
| `articles/GUT.md` | `/articles/GUT.md` | yes — Paper 1 "Markdown source" |
| `articles/GUT.pdf` | `/articles/GUT.pdf` | yes — Paper 1 "PDF" (~40 MB) |
| `articles/Forces.html` | `/articles/Forces.html` | yes — Paper 2 "Read (HTML)" |
| `articles/Forces.md` | `/articles/Forces.md` | yes — Paper 2 "Markdown source" |
| `articles/Forces.pdf` | `/articles/Forces.pdf` | yes — Paper 2 "PDF" |
| `articles/Quantum.html` | `/articles/Quantum.html` | yes — Paper 3 "Read (HTML)" |
| `articles/Quantum.md` | `/articles/Quantum.md` | yes — Paper 3 "Markdown source" |
| `articles/Quantum.pdf` | `/articles/Quantum.pdf` | yes — Paper 3 "PDF" |
| `articles/TOE.html` | `/articles/TOE.html` | yes — TOE "Read (HTML)" |
| `articles/TOE.md` | `/articles/TOE.md` | yes — TOE "Markdown source" |
| `articles/TOE.pdf` | `/articles/TOE.pdf` | yes — TOE "PDF" |

The four `.pdf` files are the **canonical typeset scientific artifacts**, copied
byte-for-byte (MD5-verified) from the source render dir
(`…/physics_Journal_and_patents/Fable_Version/rendered/`): `TOE.pdf` ←
`TOE_FINAL_merged.pdf`, `Forces.pdf` ← `Fable_Forces_merged.pdf`, `Quantum.pdf` ←
`Fable_Quantum_merged.pdf`, `GUT.pdf` ← `Fable_GUT_merged.pdf`.

### scripts/ — driver + manifest + index + 21 reproducibility scripts (24)
| Staged file | Target URL |
|---|---|
| `scripts/index.html` | `/scripts/`  *(linked: "Browse the bundled scripts"; in-upload directory index)* |
| `scripts/reproduce_all.py` | `/scripts/reproduce_all.py`  *(linked: top-level driver, runs all 21)* |
| `scripts/MANIFEST.md` | `/scripts/MANIFEST.md`  *(linked: "Scripts manifest")* |
| `scripts/bg10_four_fix.py` | `/scripts/bg10_four_fix.py` |
| `scripts/c_loop_NLO_match.py` | `/scripts/c_loop_NLO_match.py` |
| `scripts/gap04_chamber_exclusion.py` | `/scripts/gap04_chamber_exclusion.py` |
| `scripts/gap04_cloop_casimir_firstprinciples.py` | `/scripts/gap04_cloop_casimir_firstprinciples.py` |
| `scripts/gap04_cloop_density_sign.py` | `/scripts/gap04_cloop_density_sign.py` |
| `scripts/gap04_convention_audit.py` | `/scripts/gap04_convention_audit.py` |
| `scripts/gap04_disjointness.py` | `/scripts/gap04_disjointness.py` |
| `scripts/gap04_full_supertrace_residue.py` | `/scripts/gap04_full_supertrace_residue.py` |
| `scripts/gap04_higher_operator_wall.py` | `/scripts/gap04_higher_operator_wall.py` |
| `scripts/gap04_intloop_principle_check.py` | `/scripts/gap04_intloop_principle_check.py` |
| `scripts/gap04_litim_scheme_branch.py` | `/scripts/gap04_litim_scheme_branch.py` |
| `scripts/gap04_oneloop_consistency.py` | `/scripts/gap04_oneloop_consistency.py` |
| `scripts/gap04_reason_hunt.py` | `/scripts/gap04_reason_hunt.py` |
| `scripts/gap04_spectral_positivity_optionA.py` | `/scripts/gap04_spectral_positivity_optionA.py` |
| `scripts/gap04_uv1_optionB_resummed_determinant.py` | `/scripts/gap04_uv1_optionB_resummed_determinant.py` |
| `scripts/gap04_zeta_continuation_frg2.py` | `/scripts/gap04_zeta_continuation_frg2.py` |
| `scripts/inflation_sigma_map_read.py` | `/scripts/inflation_sigma_map_read.py` |
| `scripts/lambda_L1L3_radstab.py` | `/scripts/lambda_L1L3_radstab.py` |
| `scripts/strongcp_realizationB.py` | `/scripts/strongcp_realizationB.py` |
| `scripts/uv1_axiom_payoff_search.py` | `/scripts/uv1_axiom_payoff_search.py` |
| `scripts/uv1_frozen_functional.py` | `/scripts/uv1_frozen_functional.py` |

### scripts/outputs/ — 24 artifacts (23 JSON + 1 CSV) + index (25)
`scripts/outputs/index.html` → `/scripts/outputs/` (in-upload directory index; linked
from `index.html` as "browse the output artifacts"). The 24 artifacts all map under
`/scripts/outputs/<name>`:
`bg10_eta_B_prediction.csv`, `bg10_manifest_skeleton.json`, `bg10_open_package.json`,
`c_loop_NLO_match_result.json`, `gap03_realizationB_certificate.json`,
`gap04_chamber_exclusion_result.json`, `gap04_cloop_casimir_firstprinciples_result.json`,
`gap04_cloop_density_sign_result.json`, `gap04_convention_audit_result.json`,
`gap04_disjointness_result.json`, `gap04_full_supertrace_residue_result.json`,
`gap04_higher_operator_wall_result.json`, `gap04_intloop_principle_check_result.json`,
`gap04_litim_scheme_branch_result.json`, `gap04_oneloop_consistency_result.json`,
`gap04_reason_hunt_result.json`, `gap04_spectral_positivity_optionA_result.json`,
`gap04_uv1_optionB_resummed_determinant_result.json`, `gap04_zeta_continuation_frg2_result.json`,
`inflation_sigma_map_read_result.json`, `lambda_L1L3_radstab_result.json`,
`uv1_axiom_payoff_search_result.json`, `uv1_frozen_functional_result.json`,
`zero_mode_invariance_proof.json`.

### supporting/ — index page + INDEX.md + 9 supporting docs (11)
All nine supporting docs are now **directly linked from `index.html`** (the orphan is
closed). The directory also ships its own index page.
| Staged file | Target URL | Linked from index.html |
|---|---|---|
| `supporting/index.html` | `/supporting/` | yes — "/supporting/" + "directory index" |
| `supporting/INDEX.md` | `/supporting/INDEX.md` | yes — "supporting/INDEX.md" |
| `supporting/00_SERIES_SPINE.md` | `/supporting/00_SERIES_SPINE.md` | yes — "series spine" |
| `supporting/01_READING_ORDER_AND_ON_RAMP.md` | `/supporting/01_READING_ORDER_AND_ON_RAMP.md` | yes — "reading order & on-ramp" |
| `supporting/02_FAST_VERIFIABILITY_AFTERNOON_CHECKS.md` | `/supporting/02_FAST_VERIFIABILITY_AFTERNOON_CHECKS.md` | yes — "afternoon checks" |
| `supporting/03_TEST_IT_YOURSELF_FIVE_PROMPTS.md` | `/supporting/03_TEST_IT_YOURSELF_FIVE_PROMPTS.md` | yes — "test-it-yourself prompts" |
| `supporting/05_WHAT_TO_ATTACK_FIRST.md` | `/supporting/05_WHAT_TO_ATTACK_FIRST.md` | yes — "what to attack first" |
| `supporting/METHOD_CFCA_June_14.md` | `/supporting/METHOD_CFCA_June_14.md` | yes — "METHOD — CFCA" |
| `supporting/INDEX_UV_WALL_OBSTRUCTION_THEOREM.md` | `/supporting/INDEX_UV_WALL_OBSTRUCTION_THEOREM.md` | yes — "Index–UV-wall obstruction theorem" |
| `supporting/GAP04_REVIEWER_DEFENSE_NOTE.md` | `/supporting/GAP04_REVIEWER_DEFENSE_NOTE.md` | yes — "Gap-04 reviewer defense note" |
| `supporting/UV_COMPLETION_CANDIDATE_MAP.md` | `/supporting/UV_COMPLETION_CANDIDATE_MAP.md` | yes — "UV-completion candidate map" |

---

## 4. External dependency: ONE link only — `/gut/nasa/` (independent companion)

The landing is now self-contained. There is exactly **one** `index.html` link that
points outside this upload:

| index.html link | Status |
|---|---|
| `/gut/nasa/` | The independent NASA-facing GUT companion — an owner-designated public companion that survives the archive of the old gated site (migration §2). Intentionally **not** mirrored in this upload; it is its own resource. |

### What the old `/gut/…` links became (repointed to in-upload paths)

The prior staging linked the four papers and the supporting docs through the old
live-server `/gut/` tree (with in-upload "mirrors" beside them). Because that tree is
now archived to `/old` at deploy, every such link has been **repointed** to the
in-upload file (the `/gut/<article>` "canonical" links were **removed**, not kept as a
fallback):

| Old `index.html` link (`/gut/…`, now removed) | Now points to (in-upload, resolves) |
|---|---|
| `/gut/paper1/Fable_GUT_merged.html` | `/articles/GUT.html` (+ `/articles/GUT.md`, `/articles/GUT.pdf`) |
| `/gut/forces/Fable_Forces_merged.html` | `/articles/Forces.html` (+ `.md`, `.pdf`) |
| `/gut/quantum/Fable_Quantum_merged.html` | `/articles/Quantum.html` (+ `.md`, `.pdf`) |
| `/gut/toe/TOE_FINAL_merged.html` | `/articles/TOE.html` (+ `.md`, `.pdf`) |
| `/gut/method/METHOD_CFCA.html` | `/supporting/METHOD_CFCA_June_14.md` |
| `/gut/gap04/UV_COMPLETION_CANDIDATE_MAP.html` | `/supporting/UV_COMPLETION_CANDIDATE_MAP.md` |
| `/gut/gap04/INDEX_UV_WALL_OBSTRUCTION_THEOREM.html` | `/supporting/INDEX_UV_WALL_OBSTRUCTION_THEOREM.md` |
| `/gut/gap04/GAP04_REVIEWER_DEFENSE_NOTE.html` | `/supporting/GAP04_REVIEWER_DEFENSE_NOTE.md` |
| `/gut/scripts/` and `/gut/scripts/reproduce_all.py` | `/scripts/` + `/scripts/reproduce_all.py` + `/scripts/MANIFEST.md` |
| `/gut/nasa/` | **kept** — `/gut/nasa/` (the one surviving external link, above) |

Result: uploading the staged root alone (plus keeping `/gut/nasa/`) leaves **no dead
links on the landing**. The old `/gut/` article/method/scripts tree may be archived to
`/old` freely.

---

## 5. Post-upload smoke checklist

- [ ] `GET /` returns the landing page (`index.html`).
- [ ] All six in-anchor jumps (`#articles`, `#concepts`, `#qc`, `#nasa`, `#reproduce`, `#falsifiers`) scroll on-page.
- [ ] Four article `Read (HTML)` links (`/articles/*.html`) render with MathJax (network on).
- [ ] Four `Markdown source` links (`/articles/*.md`) download/serve as text.
- [ ] Four `PDF` links (`/articles/*.pdf`) download (note `GUT.pdf` ~40 MB; confirm the host allows the large transfer).
- [ ] `/scripts/reproduce_all.py`, `/scripts/MANIFEST.md`, `/AUDIT.md`, `/NARRATIVE_FRAME.md`, `/DEPLOY_MANIFEST.md` serve.
- [ ] `/articles/`, `/scripts/`, `/scripts/outputs/`, `/supporting/` list (in-upload `index.html` present in each — no autoindex needed).
- [ ] All nine `/supporting/*.md` links serve (orphan closed).
- [ ] `/gut/nasa/` resolves (the one external link — owner-designated independent companion).
- [ ] Rollback rehearsed: `public_html/old/` holds the prior gated site intact.

---

## 6. Sign-off gates (honest, not deploy-blocking-by-this-agent)

- Author block pending entity formation (stated on the page, not hidden).
- Supporting docs are DRAFT pending Chris's countersign (per `supporting/INDEX.md`).
- Provisional-patent link is a dated placeholder ("Will be added July 16").
- `NARRATIVE_FRAME.md` stale "no HTML files" meta-note: **resolved** — corrected in-place
  to state the release ships HTML articles + landing + index pages with PDFs as downloads
  (front-matter self-description, not frozen science). No open item remains here.

---

## 7. What changed in this remediation pass (2026-06-15)

- **Self-contained links (B1/B2).** The four article cards in `index.html` now link the
  in-upload `/articles/{GUT,Forces,Quantum,TOE}.html` (primary), `.md` (source), and
  `.pdf` (canonical). The old `/gut/<article>` "canonical" links were **removed**. All
  nine `/supporting/*.md` docs are now directly linked from the landing (orphan closed).
  `/gut/nasa/` is **kept** as the one external link.
- **PDF downloads (honest).** Four canonical PDFs copied byte-for-byte (MD5-verified)
  into `articles/`: `TOE.pdf`, `Forces.pdf`, `Quantum.pdf`, `GUT.pdf`. The landing labels
  them "PDF = canonical typeset scientific artifact; the HTML version adds the reader
  on-ramp and minor reference fixes" and flags `GUT.pdf` as ~40 MB.
- **Reproducibility driver (B1).** New `scripts/reproduce_all.py` runs all 21 staged
  scripts and prints PASS / REFUSED-by-design / FAIL + summary; linked from the landing.
  Removed the dependence on `/gut/scripts/reproduce_all.py`. Verified run: 19 PASS, 2
  REFUSED-by-design, 0 FAIL, driver exit 0.
- **Narrative fix (D1).** `NARRATIVE_FRAME.md`'s false "no HTML files anywhere" line
  corrected to state the release ships HTML articles + landing.
- **Directory indexes (D2).** Added `articles/index.html`, `scripts/index.html`,
  `scripts/outputs/index.html`, and `supporting/index.html` so trailing-slash directory
  links resolve without server autoindex.
- **Frozen content untouched.** The four article bodies (`.html`/`.md`) and the canonical
  PDFs are byte-frozen; the §V truth table, decision-grade closures, economy headline,
  Gap-04 CLOSED-SCOPED / GLOBAL-UV-DELEGATED close-out, and T1/T2/T3/T1′ are unchanged.

### Link-resolution check (every `index.html` link)

Verified file-by-file: **37 unique `href` targets** in `index.html` — 6 in-page anchors,
30 in-upload files/directory-indexes (all resolve), and **1 external** (`/gut/nasa/`, by
design). **0 broken**, **0 dependence on the old `/gut/` article/method/scripts tree.**
The four new directory-index pages were also checked: every link inside them resolves to
an in-upload file. Payload: **77 files, 64.27 MB.**
