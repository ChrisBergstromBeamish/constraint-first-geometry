---
name: Reproduction failure
about: A script behaves differently than documented (a genuine FAIL, not REFUSED-by-design).
title: "[REPRO] <script> FAILs / differs from documented output"
labels: reproduction
---

## Script
<!-- e.g. scripts/reproduce_all.py, or scripts/<name>.py -->

## Environment
<!-- OS, Python version, and whether you used the documented environment lock (see scripts/MANIFEST.md). Reproduction claims are environment-sensitive. -->

## Command run
```
python scripts/reproduce_all.py
```

## Output
<!-- Paste the relevant output, including the PASS / REFUSED-by-design / FAIL line and any traceback. -->

## Documented expectation
<!-- What scripts/MANIFEST.md / the script header says should happen. -->

## Is this REFUSED-by-design?
- [ ] No — this is a genuine FAIL
- [ ] Unsure — please advise

---
*Confirmed reproduction failures drop the affected gate from certificate to diagnostic and are logged in `ERRATA.md`.*
