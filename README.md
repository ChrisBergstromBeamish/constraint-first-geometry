# Constraint-First Geometry — a GUT / Theory-of-Everything candidate series

> One small thirteen-dimensional shape. Four measured numbers in. Twenty-two-plus quantities out — and every place it breaks, named first.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20709153.svg)](https://doi.org/10.5281/zenodo.20709153)

This repository is the **frozen, citable record** for a constraint-first derivation program in fundamental physics. A single frozen internal geometry, fed four measured anchors, is used to read the gauge sector and nineteen-plus flavor observables off the geometry — including the most arbitrary-looking fact in physics, *why there are exactly three families of matter*, which comes out as an integer the shape counts, with no dial to turn it to two or four.

- **Canonical reading site:** https://physics.magflowmeters.com/
- **Community & narrative (Substack):** https://chrisbergstrom42.substack.com/
- **Author:** Chris Bergstrom
- **Version:** 1.1.1 · **Released:** 2026-06-19 (priority first established 2026-06-15)

## Status — read this first

This work is **NOT peer-reviewed.** It is currently **in submission to *Physical Review D* and *Foundations of Physics***. It is a *front door for external review*, not a settled result. It is offered honestly: maybe right, maybe wrong, maybe partly each — with every open question carrying a named way it could be proven wrong.

## How this is reviewed — and how to break it

This repository is both a **frozen, citable record** and a **living public review**. Those are not in conflict:

- The **tagged releases**, the **Zenodo DOI**, and `HASHES.sha256` are the *frozen* snapshots — cite those.
- The **`main` branch** is the *living*, reviewed version, which changes as flaws are found and fixed.
- **[`ERRATA.md`](ERRATA.md)** is the public ledger of every delta between them: each confirmed flaw, dated, attributed, with its resolution (`fixed` / `downgraded` / `refuted`). Each accepted fix bumps a release.

The request is not that you believe this — it is that you **try to break it**.

- **[`FALSIFIERS.md`](FALSIFIERS.md)** — every open claim with a named way to kill it. Each entry is a ready-to-open issue. Two checks take the spine and are the best place to start: the **anomaly witness** (30 seconds, by hand) and the **counting claim** (does the over-determination survive an audit of output independence and freeze-before-compare?).
- **[`CONTRIBUTING.md`](CONTRIBUTING.md)** — *How to Break This*: where to push, the four-grade vocabulary, and how to file a finding so it can be acted on. A finding needs a **specific locus** (paper + section, or script + line) and a **specific mismatch** — "I don't believe it" is a prior, not a bug report.
- **Issues** are for checkable claims; **Discussions** are for "I smell a problem but can't yet name the locus."

Every confirmed flaw is recorded in public, with the finder credited, and the affected claim is fixed, downgraded, or withdrawn. **Finding flaws is the success condition of this repository, not the failure condition.**

## What this claims, and what it does not

**Claims.** One frozen 13-dimensional shape + four measured numbers reproduces a large amount of the Standard Model's structure; more independent answers come out than numbers go in (the "four in → twenty-two-plus out" economy); the family count (three) is a topological integer, not a fitted dial.

**Does not claim.** It is not peer-reviewed, not finished, and not certainly correct. Of eighteen open questions tracked in the capstone, fourteen are deliberately open with kill-conditions. The hardest number in physics — the cosmological constant — was tested against the theory's deepest idea, **failed, and the failure was published.** The "reproduce-known" checks are consistency demonstrations, not proofs, and do not replace general relativity or Maxwell.

## Contents

| Path | What it is |
|---|---|
| `papers/` | The five manuscripts (PDF + Markdown): **TOE** (capstone & tie-breaker), **GUT** (the certificate paper), **Forces**, **Quantum**, **Particles** (observed-spectrum closure). |
| `In_Search_of_Natures_Elegance.{md,pdf}` | Plain-language summary — the non-technical on-ramp to the whole program. |
| `examples/` | Eight worked-example notes — *"does the geometry give the right numbers?"* Each reduces the geometry to 4D and reproduces a known result (light-bending, hydrogen, the muon law, …). See [`examples/README.md`](examples/README.md). |
| `scripts/` | The reproducibility bundle. Run `python scripts/reproduce_all.py` — it runs the suite and prints PASS / REFUSED-by-design / FAIL per script. |
| `supporting/` | Method (CFCA — Constraint-First Consilient Abduction), the Gap-04 close-out documentation, and the referee-aid reader guides. |
| `audit/` | Completeness & exact-path audit, the narrative frame, and the deploy manifest. |
| `HASHES.sha256` | SHA-256 of every frozen file — the integrity and priority record. |
| `RELEASE.md` | Version, date, canonical URL, DOI, and the manifest digest. |
| `CITATION.cff` | Citation metadata (GitHub "Cite this repository"). |

## How to cite

See [`CITATION.cff`](CITATION.cff). **Cite the concept DOI (always resolves to the latest version):** [10.5281/zenodo.20709153](https://doi.org/10.5281/zenodo.20709153) (Zenodo).

## Integrity / priority

`HASHES.sha256` lists the SHA-256 of every frozen file. Together with the dated, tagged GitHub release and the Zenodo DOI, this establishes that *this exact set of files existed publicly on this date*.

## License

Released under **CC-BY-4.0** (see `LICENSE`) — free to share and adapt with attribution. Change it before publishing if you prefer a different license.

## The honest deal

This is a front door for review, not a settled result. Wherever it breaks, it is named first. **Check it at every gate.**
