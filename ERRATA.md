# Errata — the public log of flaws found and how each was resolved

This is the most important file in the repository.

A construction that survives a public list of its own corrections has earned more trust than one that was never tested. Every confirmed flaw — whether caught internally during the build or reported by a reviewer — is recorded here, dated, attributed, with a severity and a resolution. **Nothing confirmed is ever quietly dropped.**

**Resolutions** are one of: `fixed` (construction corrected), `downgraded` (claim moved to its true grade), `refuted` (claim withdrawn), or `open` (confirmed real, fix pending).

**Severity:** `fatal` (breaks the central claim) · `gate` (drops one gate/sector) · `claim` (downgrades one result) · `cosmetic`.

---

## Found and resolved (seeded from the internal build record)

These were caught during construction and are listed here in the same spirit we ask reviewers to use — so the log starts honest rather than empty.

| ID | Date | Found by | Severity | What | Resolution |
|----|------|----------|----------|------|------------|
| E-001 | 2026-06 | internal | `refuted` | Candidate structural cancellation of the cosmological constant (Λ). Computed at full strength; the supertrace does **not** cancel (ratio 0.58 at k=0); the sharper claim is a refuted theorem. | `refuted` — Λ carried as a published failure; left Weinberg-open; **no** comparison to observed Λ claimed. |
| E-002 | 2026-06 | internal | `claim` | A boundary-coefficient **sign** was initially mis-attributed (the `c_bdry` leading share). | `fixed` — full arithmetic reversed the attributed sign; superseded entry kept on the record with its superseding event (self-caught #5). |
| E-003 | 2026-06 | internal | `gate` | Gap-04 was at risk of being read as certificate-grade. | `downgraded` — explicitly recorded as **CLOSED at decision grade, not certificate grade**; global-UV question delegated. |
| E-004 | 2026-06 | internal | `claim` | A determinant-identity line required correction (ERRATUM-K1). | `fixed` — corrected and countersigned; recorded in the handbook packet. |
| E-005 | (standing) | internal | `open` | Up-quark mass sits at **~4.4σ** against its tight experimental band — the largest single tension in the fermion sector. | `open` — disclosed, not hidden; carried in [`FALSIFIERS.md`](FALSIFIERS.md) #9. |
| E-006 | (standing) | internal | `open` | Atmospheric mixing **octant** ambiguity. | `open` — graded diagnostic; DUNE/JUNO named as resolving experiments ([`FALSIFIERS.md`](FALSIFIERS.md) #16). |

---

## Reported by reviewers

*(empty — be the first. Open an issue per [`CONTRIBUTING.md`](CONTRIBUTING.md); confirmed findings are entered here with your attribution.)*

| ID | Date | Found by | Severity | What | Resolution |
|----|------|----------|----------|------|------------|
| — | — | — | — | — | — |

---

### How an entry gets here

1. A finding is filed as an issue with a specific locus.
2. A maintainer reproduces it.
3. If confirmed, it is added above — **with the reporter's name** — and the construction is `fixed`, the claim is `downgraded`, or the claim is `refuted`. The linked issue is closed with a reference to the errata ID.

If you reported something and it is not here within a reasonable time, that is itself a bug — open an issue about the missing errata entry.
