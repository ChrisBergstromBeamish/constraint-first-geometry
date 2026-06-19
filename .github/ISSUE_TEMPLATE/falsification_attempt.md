---
name: Falsification attempt
about: You checked a specific claim against a specific locus and it failed (or you think it does).
title: "[FALSIFY] <claim> at <paper/section or script>"
labels: falsification
---

<!-- A finding needs a specific locus and a specific mismatch. "I don't believe it" is a prior, not a finding — convert it into the fields below. -->

## Locus
<!-- Exactly where the claim lives. e.g. "GUT §6.4", "TOE §V row 12", "scripts/reproduce_all.py line 40" -->

## Claim being challenged
<!-- State the claim you are attacking, in one sentence. -->

## Check performed
<!-- The arithmetic, derivation, or command you ran. Paste it. Make it reproducible. -->

## Expected vs. found
- **Claimed:**
- **Found:**

## Severity (your assessment)
- [ ] `fatal` — breaks the central over-determination claim (anomaly witness, counting claim, hidden input)
- [ ] `gate` — drops one gate/sector from certificate to diagnostic
- [ ] `claim` — downgrades one specific result
- [ ] `cosmetic`

## Reproduction
<!-- Steps / environment so a maintainer can reproduce. If it's a script, include the command and output. -->

---
*By filing, you accept that if confirmed this will be recorded — with your attribution — in `ERRATA.md`, and the affected claim will be fixed, downgraded, or withdrawn in public.*
