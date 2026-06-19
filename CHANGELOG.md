# Changelog

## v1.3.0 — 2026-06-19

- **Worked examples added** (`examples/`). Eight short "does it get the right numbers?" notes, each shrinking the geometry to four dimensions and checking it against known physics: Einstein's 1.75″ light-bending (*The Sun as a Lens*), the hydrogen spectrum, Newton's law from single-graviton exchange, the muon-decay law, all four forces from one shape, the three-family count (LEP N_ν = 2.984 ± 0.008), the three-qubit bit-flip QEC rate, and one clearly-labeled speculative toy-metric note (*The Road in Front of the Ship* — a screening story, **not** a drive or FTL). Each is a reproduce-known consistency check, not a proof. See `examples/README.md`.
- Regenerated `HASHES.sha256` (59 files; manifest digest `20bd91bcf9607e4438f8957fcbd411d16aec9809478201a13075cf09eeec0852`).

## v1.2.0 — 2026-06-19

- **Companion refreshed.** *In Search of Nature's Elegance* updated to the expanded edition (120 pp, up from 107): adds "The Case in Sixty Seconds," a Technical Abstract, "The Gauntlet," "Predictions," "The Four Numbers and the One Law," and a Falsification Challenge. Cross-references point to the rendered site papers; author/contact footer retained.
- **Public-review layer.** Added `CONTRIBUTING.md` (How to Break This), `FALSIFIERS.md` (open claims + named falsifiers), `ERRATA.md` (public delta ledger), `CODE_OF_CONDUCT.md`, and `.github/ISSUE_TEMPLATE/` (falsification / reproduction / hidden-input); spliced a "How this is reviewed" section into the README. Issues + Discussions enabled and the first four falsifiers seeded as issues.
- **Citation metadata.** Added a README Zenodo DOI badge; synced `CITATION.cff` + `.zenodo.json` to the concept DOI and current version, with author affiliation and a GitHub-repo related identifier.
- Regenerated `HASHES.sha256` (manifest digest `854df0303c95a7f3ef63fa41b5f48d94f5f9389651bf19a8f70ab3543bf119e9`).
- **Zenodo:** this release auto-minted versioned DOI `10.5281/zenodo.20763694`; cite the **concept DOI** `10.5281/zenodo.20709153` (always resolves to the latest version).

## v1.1.1 — 2026-06-19

- **Quantum:** restored the §12.1 note *"The overhead is a floor at scale — the two-stage design"* (the two-stage scale-invariant QC memory-floor record) into the External Engineering Bridge Pointer; re-rendered `Quantum.pdf`. Regenerated `HASHES.sha256`.
- **Zenodo:** this release auto-minted versioned DOI `10.5281/zenodo.20763136`; cite the **concept DOI** `10.5281/zenodo.20709153` (always resolves to the latest version).

## v1.1.0 — 2026-06-19

Documentation refresh and companions added.

- Updated **GUT / Forces / Quantum / TOE** to the current reformatted manuscripts (the post-passes reader versions).
- Added **Particles** — *Observed Particle Spectrum Closure* companion (PDF + Markdown).
- Added **In Search of Nature's Elegance** — a plain-language summary of the whole series (PDF + Markdown).
- Added an author/contact footer (Chris Bergstrom · cbergstr@gmail.com · physics.magflowmeters.com) to every document.
- Regenerated `HASHES.sha256` over the 50 files in this release.
- The v1.0.0 Zenodo DOI (10.5281/zenodo.20709154) continues to identify the frozen 1.0.0 release; a new DOI would be minted separately for 1.1.0.

## v1.0.0 — 2026-06-15

Initial public, frozen release.

- Four manuscripts: **TOE** (capstone & tie-breaker), **GUT** (the certificate paper), **Forces**, **Quantum** — each as PDF and Markdown.
- The reproducibility bundle (`scripts/`): `reproduce_all.py` plus the 21-script suite and outputs.
- Supporting documents (`supporting/`): the CFCA method, the Gap-04 close-out (CLOSED-SCOPED / GLOBAL-UV-DELEGATED, with T1/T2/T3/T1'), and the referee-aid reader guides.
- Completeness & exact-path audit (`audit/`).
- `HASHES.sha256` — SHA-256 over all 46 frozen files.
- **Status:** not peer-reviewed; in submission to *Physical Review D* and *Foundations of Physics*.
