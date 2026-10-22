# RESEARCH NOTE - INDIVIDUAL TECHNOLOGY RECORD STRUCTURE

**Date:** 18/09/2026
**Scope:** What a single technology record is supposed to contain, measured against the 204
records in `TECH_MD` and against published technical-documentation standards.
**Result:** The house shape is sound but incomplete. Five sections that every external
standard requires are absent from all 204 records. The best-structured existing record is
`TECH-ACT-006`.

---

## 1. INTERNAL BASELINE - MEASURED, NOT ASSUMED

All 204 records in `TECH_MD` were scored on hierarchy depth, tables, table cells, code
blocks, bullet lists, numbered steps and cross-references.

| Measure | Median across 204 | Best record |
|---|---|---|
| Words | 1288 | 2770 |
| H2 chapters | 10 | 11 |
| H3 sub-sections | 4 | 24 |
| H4 sub-sub-sections | 1 | 1 |
| Tables | 2 | 2 |
| Table cells | - | 40 |
| Code blocks | 1 | 6 |
| Numbered procedure steps | 0 | 0 |

**Structure score, top seven:**

| Score | Words | H3 | Code blocks | Record |
|---|---|---|---|---|
| 82.0 | 2279 | 22 | 6 | `TECH-ACT-006` Facility Converted Aircraft System |
| 81.0 | 2770 | 24 | 6 | `TECH-GOI-071-1` Mercy Lock Gentle Lock System |
| 80.0 | 2613 | 23 | 5 | `TECH-ACT-001` Reality Stabilization Anchor System |
| 79.5 | 2524 | 22 | 5 | `TECH-ACT-002` Anti-Reality Mesh System |
| 79.5 | 2316 | 22 | 5 | `TECH-ACT-005` Causal Static Generator System |
| 78.5 | 2433 | 22 | 5 | `TECH-ACT-004` 004-Series Amnestic Compound System |
| 77.5 | 2424 | 22 | 5 | `TECH-ACT-003` Quantum Narrative Buffer System |

The gap between the top tier and the field is almost entirely **H3 depth**.
The median
record carries 4 sub-sections; the gold standard carries 22 to 24. Chapter count is
identical across the corpus at 10 - the house vocabulary is already uniform. What
separates
a strong record is that every chapter is broken into named sub-sections rather than
written
as continuous prose.

For reference, `TECH-ACT` median score is 40.5 at 1323 words; `TECH-GOI` median is 11.0
at
505 words, because 54 of its 65 records are still on the obsolete four-section
shape.

**Device adoption across all 204 records:**

| Device | Records using it |
|---|---|
| Any H4 sub-section | 151 / 204 (74%) |
| Two or more tables | 152 / 204 (75%) |
| Any code block | 152 / 204 (75%) |
| Three or more cross-references | 14 / 204 (7%) |
| Any numbered procedure step | 1 / 204 (0.5%) |

---

## 2. THE GOLD STANDARD SKELETON, AS ACTUALLY BUILT

Taken from `TECH-ACT-006` and `TECH-GOI-071-1`, which agree almost line for line.

```text
[H1]  A.C.T FACILITY ARCHIVE FILE
[H3]  TECHNOLOGY RECORD - <NAME IN CAPS>

[ registry table, 13-16 fields ]
[ archive status table, 3-4 fields ]

[H4]  Archive Note        <- why this record exists; what the asset is NOT
always carries the Controlled label and core rule

[H2]  FUNCTION SUMMARY
[H3]  Practical Function            what it physically does
[H3]  Operational Role              where it sits in the containment chain
OR: Difference From Standard <X>

[H2]  ORIGIN AND CUSTODY
[H3]  Development History           era, programme, predecessor systems
[H3]  Custody                       who holds it, at which sites, under what lock
OR: Origin Assessment / Custody Status

[H2]  PHYSICAL AND SYSTEM DESCRIPTION
[H3]  Standard <Unit>               dimensions, materials, colours, finish
[H3]  Core Components               named bolded components, one per behaviour
[H3]  Variants                      transport, grid, field and site forms

[H2]  OPERATING PROCEDURE
[H3]  Authorized Use                who may request it and against what
[H3]  Operating States              STANDBY / ACTIVE / LOCKOUT style block
[H3]  Handling Rules                prohibitions and red lines

[H2]  KNOWN LIMITS
[H3]  What <X> Cannot Do            explicit non-capabilities
[H3]  Misuse Risk                   what happens when it is used wrongly

[H2]  FAILURE HISTORY
[H3]  <INCIDENT NAME> - <YEAR>      dated, per incident, cause and outcome

[H2]  DIVISION USE
[H3]  <Division>                    one H3 per division that touches it

[H2]  CROSS-REFERENCES
[H3]  Related A.C.T Records         path-linked
[H3]  Technology Relationship       how it couples to other assets

[H2]  OPEN QUESTIONS
[H3]  Intelligence Confidence       stated confidence level

[H2]  FILE METADATA                  created / updated / author / reviewer / status
```

Three habits make the top records work and are missing from weaker ones:

- Every chapter has two or three **named H3 sub-sections**, not one prose run.
- **Named components are bolded** in the physical description, each with its own sentence
of dimensions, material, colour and behaviour.
- Failure history entries are **titled and dated**, or marked `DATE WITHHELD`.

---

## 3. EXTERNAL STANDARDS - WHAT THEY REQUIRE

Four published frameworks were compared. They agree closely.

**ISO/IEC 26514** splits any instruction document into five sections: descriptive (product
characteristics), procedural (sequence of user actions), reference (technical data and
specifications), diagnostic (troubleshooting), and regulatory (safety requirements and
compliance) [1](https://processnavigation.com/insights/how-to-write-an-instruction-manual/).

**The technical-manual anatomy model** lists ten required parts: introduction and equipment
overview, safety instructions, technical specifications, equipment and component
description, installation requirements, operating procedures, control system or HMI
description, cleaning and maintenance, troubleshooting, spare parts and reference documents.
It also fixes the troubleshooting form as a three-column table of Problem, Possible Cause,
Recommended Action, and requires that instructions be written in the same sequence the user
performs the activity
[6](https://www.amergingtech.com/post/the-anatomy-of-an-effective-technical-manual).

**Construction O&M data requirements (Section 01730)** demand, for each unit of equipment:
description of unit and component parts including function, normal operating
characteristics, limiting conditions, performance curves and complete nomenclature of
replaceable parts; operating procedures covering start-up, break-in, routine and normal
operation, regulation, control, stopping, shutdown and emergency instructions; maintenance
procedures covering routine operations, a troubleshooting guide, disassembly and repair, and
alignment and adjustment; a servicing and lubrication schedule; and predicted life of parts
subject to wear [2](https://dalycity.org/DocumentCenter/View/1640/01730-Operating-and-Maintenance-Data-PDF).

**US Army O&M data packages** enumerate: safety precautions, operator prestart, startup /
shutdown / post-shutdown procedures, normal operations, emergency operations, operator
service requirements, environmental conditions, preventive maintenance plan and schedule,
cleaning recommendations, troubleshooting guides and diagnostic techniques, wiring and
control diagrams, maintenance and repair procedures, removal and replacement instructions,
spare parts and supply list, parts identification, testing equipment and special tool
information, and testing and performance data
[2](https://www.jblmdesignstandards.army.mil/Portals/109/doc_files/01%2078%2023.doc).

Two formatting rules recur across sources: keep heading nesting to three or four levels
[8](https://medium.com/word-garden/how-to-make-a-technical-document-in-2025-a999525eb093),
and keep the same component name, unit and tag consistent everywhere it appears
[6](https://www.amergingtech.com/post/the-anatomy-of-an-effective-technical-manual).
The house shape already satisfies the first - no record exceeds H4.

---

## 4. GAP ANALYSIS - HOUSE SHAPE VERSUS STANDARD

**What the house shape does better than a commercial manual.** Provenance and development
history; dated failure history, which is functionally an FMEA record; an open-questions
section with a stated intelligence confidence; custody, authority and clearance fields; and
per-division responsibility, which is the SOP "responsibilities" clause. No commercial
manual carries any of these. They should not be weakened.

**What the house shape is missing. All five are absent from all 204 records.**

| # | Missing section | Required by | Why it matters here |
|---|---|---|---|
| 1 | **Technical specification table** - dimensions, mass, power draw, materials, operating envelope, performance figures | ISO 26514 reference section; O&M 01730; Army data packages | The Visual Reference Guide already holds these figures in prose. They are never restated as a spec table in the record itself, so a reader cannot get numbers without opening a second document. |
| 2 | **Numbered operating sequence** - prestart, startup, normal, shutdown, emergency | All four sources | 1 of 204 records contains a single numbered step. "Authorized Use" and "Handling Rules" describe policy, not sequence. |
| 3 | **Fault isolation table** - Symptom / Probable Cause / Required Action | ISO 26514 diagnostic section; O&M 01730; industrial checklist | FAILURE HISTORY is narrative and backward-looking. Nothing tells a field team what to do when a readout goes wrong tonight. |
| 4 | **Servicing, calibration and consumables schedule** - interval, task, materials | O&M 01730; Army preventive maintenance plan | No record states an inspection interval, a calibration period, or a consumable. Assets described as needing maintenance have no schedule. |
| 5 | **Environmental and interface limits** - temperature, humidity, power, site class, control panel and readout inventory | Army environmental conditions; O&M 01730 limiting conditions | Operating envelope appears in prose in some records and nowhere in others. Readouts are described in the Visual Reference Guide but not indexed in the record. |

**One weakness of degree, not kind.** Only 14 of 204 records carry three or
more
cross-references, against a house rule that records couple to each other. This is a
completion gap rather than a structural one.

---

## 5. RECOMMENDED TARGET SKELETON

The existing ten chapters stay. Five sub-sections are added where the standards require
them. Nothing existing is removed.

```text
[H2]  FUNCTION SUMMARY                       (unchanged)
[H2]  ORIGIN AND CUSTODY                     (unchanged)
[H2]  TECHNICAL SPECIFICATION                NEW - table of measured figures
[H2]  PHYSICAL AND SYSTEM DESCRIPTION        (unchanged, bolded named components)
[H2]  INTERFACE AND OPERATING ENVELOPE       NEW - controls, readouts, limits
[H2]  OPERATING PROCEDURE                    ADD numbered prestart/startup/shutdown/emergency
[H2]  SERVICING AND CALIBRATION              NEW - interval, task, materials
[H2]  FAULT ISOLATION                        NEW - Symptom / Probable Cause / Required Action
[H2]  KNOWN LIMITS                           (unchanged)
[H2]  FAILURE HISTORY                        (unchanged, dated entries)
[H2]  DIVISION USE                           (unchanged)
[H2]  CROSS-REFERENCES                       raise to three or more links
[H2]  OPEN QUESTIONS                         (unchanged)
[H2]  FILE METADATA                          (unchanged)
```

Target metrics per record, taken from the measured top tier rather than from theory:

| Metric | Target |
|---|---|
| Words | 1800 to 2600 |
| H2 chapters | 13 to 14 |
| H3 sub-sections | 18 or more |
| Heading depth | H4 maximum |
| Tables | 4 or more |
| Code blocks | 4 to 6 |
| Numbered sequence steps | 8 or more |
| Cross-reference links | 3 or more |

Figures in the specification and envelope tables must come from the source dossier, the
Master Index, the Visual Reference Guide or the Evolution Timeline. Where no figure exists,
the cell reads `NOT MEASURED` and the gap is filed under OPEN QUESTIONS. Nothing
is
estimated to fill a table.

---

## 6. HONEST POSITION OF RECENT WORK

The `TECH-GOI-056` set delivered at `abe2ffa` scores **44.5**, against a top tier of 77
to
82. Its word counts (1338 to 1714) clear the 1300 floor but sit below
the 2279 to 2770 of
the best records, and it carries 3 to 5 H3 sub-sections against their 22
to 24. It is a
mid-pack record by this measurement, not a gold-standard one, and it lacks all five
missing
sections identified above.

---

## 7. NEXT ACTION

Adopt the target skeleton in section 5 and rebuild one record as the worked
exemplar before
applying it to the 58 obsolete records still outstanding. Recommended exemplar:
`TECH-GOI-048-1` (Children of the Deep, 5440-word dossier, richest available source
material). Retrofitting the five new sections into the existing 146 conforming records is a
separate, larger pass and should be scheduled after the obsolete-shape backlog is cleared.
