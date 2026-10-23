# Audit Corrections — Two False Findings Retracted

- **Prepared:** 2026-10-22
- **Corrects:** the corpus audit run on the same date over the technology, anomaly, and GOI folders
- **Summary:** two of the three findings reported from the anomaly and GOI folders were false positives produced by
the checker, not defects in the corpus. Both are retracted here. The technology-folder finding is real but was
mischaracterised, and is restated correctly below.

---

## 1. Retracted — "220 GOI `.md` cells over 118 characters"

**What was reported.** 220 lines over 118 characters across 28 files in the GOI folder, described as box lines
breaching the wrap rule.

**What is actually true.** Every one of the 220 is a **`.md` pipe-table source row**, not a `.txt` box rule. Measured
separately:

| Folder | `.md` pipe cells over 118 | `.txt` box lines over 118 | `.txt` prose over 118 |
| --- | --- | --- | --- |
| GOI Document | 220 | **0** | **0** |
| Technology Document | 196 | **0** | 6 |

The technology folder, which has been passing the width gate for many batches, carries 196 of the same `.md` pipe
cells. A Markdown pipe table renders with wrapped cells, so a long source row does not force horizontal scrolling. The
118-character rule exists because monospaced `.txt` box lines do scroll, and against that rule the GOI folder is clean
at zero.

**Why the checker was wrong.** It tested `line.startswith(("|", "+"))` without separating `.md` pipe rows from `.txt`
box rules, so it counted ordinary table source as box overflow.

**Why the attempted fix could never have worked.** The wrapper inserted `<br>` into long cells. Inserting `<br>` makes
the source line *longer*, not shorter — it changes how the cell renders, never the character count of the line it sits
on. The tool reported 220 cells wrapped and the recount still returned 220, which was the wrapper reporting its own
impossibility. It was reverted in full and nothing was committed.

## 2. Retracted — "4 GOI dossiers without a capability statement"

**What was reported.** `GOI-BS-T-027`, `GOI-CU-X-048`, `GOI-GV-P-001`, and `GOI-ML-X-014` listed as missing a
capability classification.

**What is actually true.** All four carry one, as a registry row rather than a prose sentence. The checker looked for
`assigned **X**`, `capability class`, and `Anomalous Capability Assessment`, and these four use a different house
form:

| Dossier | Row present |
| --- | --- |
| `GOI-BS-T-027` Anstrall Market | `| ANOMALOUS CAPABILITY | HANDLER |` |
| `GOI-CU-X-048` Children of the Deep | `| ANOMALOUS CAPABILITY | PRACTITIONER |` |
| `GOI-GV-P-001` Government Anti-Anomaly | `| ANOMALOUS CAPABILITY | HANDLER |` |
| `GOI-ML-X-014` Anti-Global Anomaly | `| ANOMALOUS CAPABILITY | ENGINEERING |` |

All 30 GOI dossiers carry a capability classification. There is no gap.

## 3. Corrected — the 144 technology records "off the house chapter order"

**What was reported.** 144 of 229 records do not match the 14-chapter house order.

**What is actually true, and it is less severe than reported.** Every one of the 144 has **14 chapters**. None is
missing a section. What differs is naming and the position of two sections:

| Variant | Records |
| --- | --- |
| `ORIGIN AND DEVELOPMENT` in place of `ORIGIN AND CUSTODY` | 90 |
| `TECHNICAL SPECIFICATION` and `PHYSICAL OR SYSTEM DESCRIPTION` in the opposite order | 136 |
| `FUNCTION OUTLINE` in place of `FUNCTION SUMMARY` | 16 |
| `ORIGIN AND DEPLOYMENT` in place of `ORIGIN AND CUSTODY` | 8 |
| `PHYSICAL AND SYSTEM DESCRIPTION` and `OPEN ENGINEERING AND INTELLIGENCE QUESTIONS` | 4 |

All 144 are `TECH-ACT` records (137) plus 7 `TECH-GOI` records. The 85 records on the exact house order are the
`TECH-GOI` sets.

**Why this was not fixed in the same pass.** Renaming `ORIGIN AND DEVELOPMENT` to `ORIGIN AND CUSTODY` is only correct
where the section actually covers custody. Several of those sections cover development history instead, and a blind
rename would put a custody heading over development content. Each of the 90 needs a read before the heading changes.
The section reordering is safe and mechanical; the renaming is not.

## 4. Fixed in this pass

`TECH-GOI-071-5-Mercy-Lock-Shielded-Ambulance-Transfer-System` was the one technology record genuinely missing a `FILE METADATA` section. It now carries one in both twins, in the set-071 seven-field form used by its four siblings, with dates inside the 1598 to 2026 archive cycle. The only files still without that section are `00_Technology_Record_Template.md` and `README.md`, neither of which is a record.

## 5. What the corrected audit leaves standing

| Finding | Status |
| --- | --- |
| 136 records with two sections in the opposite order | Real, safe to fix mechanically |
| 90 records whose origin heading may not match its content | Real, needs a per-record read |
| 16 records using `FUNCTION OUTLINE` | Real, safe to rename |
| 4 records using two legacy heading names | Real, safe to rename |
| 17 records with 26 to 27 H3 subsections against a house 8 | Real |
| 7 records with 9 numbered steps against a house 8 | Real |
| GOI `.md` cells over 118 | **Retracted** |
| GOI dossiers without a capability statement | **Retracted** |
| Anomaly folder, 173 files | Clean, unchanged |

## 6. Rule taken from this

A checker that counts lines must know which format it is reading. `.md` pipe rows and `.txt` box rules both begin with
`|` and mean different things, and conflating them produced two false findings and one impossible fix in a single
pass. Any width gate from here on separates the two by file suffix before counting.

## Correction to This Memo's Own Swap Count

This memo reported **122** records holding `TECHNICAL SPECIFICATION` ahead of the physical or
system description. The correct figure is **136**. The first count matched the heading
`PHYSICAL OR SYSTEM DESCRIPTION` exactly and therefore missed the older records headed
`PHYSICAL AND SYSTEM DESCRIPTION`. Matching on the heading prefix instead returns 136, and
all 136 were reordered in commits `21e3383` and `d6719a1`.
