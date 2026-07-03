# Release v1.6.1 — Frozen Public Record

This page is the **priority stamp**: it asserts that this exact set of files, with these hashes, existed publicly on the date below. Priority was first established **2026-06-15** with v1.0.x (versioned DOI 10.5281/zenodo.20709154); this record now reflects the current **v1.6.1** set.

> **v1.6.1 is a metadata-only patch over v1.6.0** — the frozen content (137 files, manifest digest below) is byte-identical. It corrects the `.zenodo.json` deposit metadata (which had gone stale at 1.4.0) so the versioned Zenodo DOI mints correctly. All physics/site content is exactly as in v1.6.0.

| Field | Value |
|---|---|
| **Version** | 1.6.1 |
| **Date released** | 2026-07-03 (priority first established 2026-06-15) |
| **Author** | Chris Bergstrom |
| **Canonical site** | https://physics.magflowmeters.com/ |
| **Community / narrative** | https://chrisbergstrom42.substack.com/ |
| **License** | CC-BY-4.0 |
| **DOI** | versioned DOI for v1.6.1 is auto-minted when this GitHub release is published (see the Zenodo record) · concept (all versions, cite this): [10.5281/zenodo.20709153](https://doi.org/10.5281/zenodo.20709153) |
| **Git tag** | `v1.6.1` |
| **`HASHES.sha256` manifest digest (SHA-256)** | `115b20bd0f7b1fa8800c1713358eddb65483e6e06b4d53091a8c211847c64604` |
| **Files frozen** | 137 (top-level summaries + narrative + AI test kit, papers, examples, scripts, supporting, audit, and the public site sections under `site/` including the early-universe granularity test suite and the "what the geometry forces" insight page) |
| **Status** | NOT peer-reviewed — in submission to *Physical Review D* and *Foundations of Physics* |

## What changed in v1.6.0

- **Gap-08 (inflation σ-slope) — CLOSED-NEGATIVE.** The headline λ²=1/6 is **retired** as a forced geometric prediction. The frozen 13D internal-curvature term is a valid *target-blind* lever, but its canonical slopes are 8/3, 4, 22/9 — none is 1/6, which came only from the separate convention λ²:=4/K_σσ. Verified three independent ways (specialist theorem + independent recomputation + first-principles radion). The branch-independent falsifier r ∈ [3.5, 36]×10⁻³ is unaffected. `supporting/GAP08_INFLATION_CLOSED_NEGATIVE.md`.
- **Early-Universe Granularity Test Suite** (`site/early-universe/tests/`) — 44 epoch-by-epoch consistency checks of "cosmic history = increasing recordable distinction," each honestly tagged SHARED-WITH-ΛCDM vs framework-specific. A CLOSED verdict means *consistent with standard cosmology*, not a unique prediction.
- **"What the geometry forces, and what it measures"** (`site/process/what-geometry-forces.html`) — the geometry forces the DISCRETE/topological quantities (N_ν=3=χ, the gauge group, the dimensions, Born p=2) but not the CONTINUOUS magnitudes, which stay measured. The top-Yukawa RG infrared quasi-fixed-point — the one continuous candidate with a real mechanism — was tested (1- and 2-loop) and does **not** reduce y_t. Full triage: `supporting/JUST_IS_LEDGER.md`.
- **Anchor status:** M_Pl and the finest-ℤ₆ shape sub-choice are each CERTIFIED-IRREDUCIBLE (proven-no-lever + named observation). No anchor-count reduction — the five honest measured anchors stand.
- Gate count corrected to 33 site-wide.

## What is frozen here

- `papers/` — five manuscripts: **TOE** (capstone), **GUT**, **Forces**, **Quantum**, **Particles** (PDF + Markdown).
- `site/` — the public sections as deployed to the canonical site: **The Process**, **The Tests**, **Early & Distant Universe** (now with the 44-test granularity suite and the honestly-blocked blind cosmology prediction), the new **"What the geometry forces"** insight page, **Emergent Separability / Theory of Differentiated Unity** (the ontology, explicitly subordinate in rigor), and **Consciousness** (a clearly-labeled speculative framework). Rendered HTML with site-absolute links, archived as-deployed.
- `In_Search_of_Natures_Elegance.{md,pdf}` — the plain-language summary.
- `The_Last_Wall.{md,pdf}` — narrative companion, first-person account by the AI orchestrator.
- `FABLE_FOUNDATIONS_TESTFILE.md`, `DOWNLOAD_PROMPT.md`, `HUMAN_SUMMARY.md` — the AI test kit.
- `scripts/` — the reproducibility bundle (`reproduce_all.py` + the script suite).
- `supporting/` — method (CFCA), the Gap-04 close-out, the **Gap-08 CLOSED-NEGATIVE** record, the **Just-Is ledger**, and referee-aid reader guides.
- `audit/` — completeness & exact-path audit, narrative frame, deploy manifest.

Honest posture is unchanged: **PROMOTIONS = 0**, nothing physics-CLOSED, every claim carries an honest status label, and open questions are named as open — never rounded up.

## How the priority record works

1. **GitHub** — this tagged release (`v1.6.0`) fixes the commit and the file tree at a timestamp.
2. **`HASHES.sha256`** — the SHA-256 of every frozen file; the digest above covers the manifest itself.
3. **Zenodo** — archiving the release mints a citable, versioned **DOI** that resolves permanently, independent of GitHub.

Together: *"this version existed on this date, with this DOI, this manifest hash, these files, and this public record."*
