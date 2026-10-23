# GOI-BS-N-068 Velvet Provenance House — Technology Set Decision

- **Prepared:** 2026-10-22
- **Source dossier:** `GOI-BS-N-068-Velvet-Provenance-House.md`, 3,342 words
- **Question:** does this dossier warrant a `TECH-GOI` record set, and if so how many records
- **Recommendation:** **yes, but two records, not five.** Build the receipt instrument and the buyer-book page. Do not
build the cloth, the ledger, or the viewing room.

---

## 1. What the dossier actually commits to

**Capability class.** Handler. The dossier states the House handles and authenticates anomalous goods and is not
confirmed to create them, and it goes further: *claims that the House can make a dangerous object safe by writing a
better receipt are not supported. It can sometimes make danger legible.* That sentence rules out the most obvious
technology record — there is no receipt-writing machine that makes objects safe, because the dossier says the effect
is not supported.

**Dual Filing is conditional, not mandatory.** It is required *when* a receipt, seal, ledger page, velvet cloth,
return clause, or lot-status mark demonstrates active anomalous behaviour, and *when* a certified object changes
custody risk, inheritance behaviour, memory, physical location, or legal identity after sale. This is the only dossier
in the current build order whose dual filing is written as a trigger rather than a standing obligation.

**What A.C.T holds.** Six minor certificates, two forged Velvet-style receipts, one authentic return clause, one
damaged buyer-book page. The dossier states plainly that *the complete ledger system remains unrecovered*.

**What A.C.T does not hold.** Any velvet inspection cloth, any provenance ledger, any viewing room, any restoration
bench, any seal paper with a wax code.

## 2. Testing each candidate against the four purposes a technology record serves

| Candidate asset | A.C.T holds it | Hazard review | Custody rules | Rival capability | Counter-operation | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| Receipt and return-clause instrument | yes — 6 certificates, 2 forgeries, 1 clause | yes | yes | yes | yes | **Build** |
| Buyer-book mark page | yes — 1 damaged page | partial | yes | yes | yes | **Build** |
| Velvet inspection cloth | no | no | no | yes | no | **Do not build** |
| Provenance ledger system | no — stated unrecovered | no | no | yes | no | **Do not build** |
| Shielded private viewing room | no | no | no | no | partial | **Do not build** |

The two that pass are the two A.C.T physically holds. That is the test that decides it.

## 3. Why the receipt instrument earns a record

The recovered fragment is not a passive document. The dossier records that handwriting analysis indicates **two
writers**, that **ink dating produced three dates for one signature**, and that the fragment carries an explicit
handling instruction — *do not hang above sleeping children* — together with custody rules stating which parties the
object accepts custody from and which it rejects, and known harms of sleep reconstruction, childhood-room duplication,
and face misremembering.

That is a physical object with a documented effect on a person, a documented handling rule, and a documented custody
behaviour. All three are exactly what a technology record exists to carry, and none of it needs to be invented.

The forgery angle strengthens it: two Velvet-style forgeries are already in A.C.T custody, so a record that sets out
how the genuine instrument behaves is directly useful to the Legal Division, which the dossier names as the party that
must attach before any public filing or court-facing substitution.

## 4. Why the buyer-book page earns a record

One damaged page is held. The dossier states that buyer books record client reliability, payment, deaths, and
breaches, that barred-client cards are circulated to other hidden markets, and it asks directly *what buyer-book marks
are shared with Anstrall Market, Candle-Under Exchange, or other hidden markets*. A record covering the page can
describe the mark system from the surviving page, set handling rules for it, and file the cross-market question as
open. It cannot describe the whole book, and should not pretend to.

## 5. Why the other three must not be built

**The velvet inspection cloth** is listed by the dossier's own Persistent Questions as unresolved: *are velvet
inspection cloths anomalous tools, inherited ritual materials, or ordinary stabilizing convention?* Writing a
technology record for it would answer that question by assertion. A.C.T holds no cloth. The correct home for it is the
open questions of the receipt record.

**The provenance ledger system** is stated as unrecovered. A technology record for an unrecovered system would be
entirely inference, which is the failure mode the necessity review identified in sets `057` through `060` — records
whose specification tables filled with `NOT MEASURED` because there was nothing engineered to specify.

**The shielded viewing room** has no recovered component, no measured behaviour, and no stated anomalous effect beyond
being shielded from ordinary recording equipment. It is a location, and locations belong in site and dossier records,
not technology records.

## 6. Recommendation

Build **two** records:

1. `TECH-GOI-068-1` — Velvet receipt, seal paper, and return-clause instrument set. Covers the six certificates, the
two forgeries, the one authentic return clause, the custody acceptance and rejection behaviour, the handling
instruction, and the two-writer
three-date anomaly in the recovered fragment.
2. `TECH-GOI-068-2` — Velvet buyer-book page and barred-client mark system. Covers the one damaged page, the mark
categories visible on it, handling rules, and the open question of which marks are shared with other hidden markets.

Carry the cloth, the ledger, and the viewing room as **open questions inside those two records** rather than as
records of their own. Record the House's authentication capability — detecting forged origin papers through ink,
pressure, witness chain and responsive seal behaviour, and identifying ownership attachments that survive sale, theft,
inheritance, fire, or amnestic alteration — inside `TECH-GOI-068-1` as assessed rival capability, which is where it is
actually useful to a reader.

This keeps the set honest: two records where the archive holds the object, no records where it does not, and no
invented specification.

## 7. Effect on the build order

With `068` resolved as a two-record set, the remaining order from the necessity review stands unchanged: `073` Lantern
Accord, `074` Ninefold Ark, `069` Namewright Bazaar, `070` Saint Morrow Passage, then `068` at two records. Sets `061`
through `067` remain excluded.
