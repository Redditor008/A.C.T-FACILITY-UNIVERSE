# A.C.T Technology Document

What the Facility builds once it has decided an anomaly can be useful. Every record here
covers one system, and every one carries its custody rules, operating limits, servicing
schedule, failure history and open questions.

## Start Here

Any record stands alone. A good first read is `TECH_MD/TECH-ACT-007-Static-Pulse-Crystal.md`
— a material record, which is the clearest shape in the set.

## What is in here

| Path | What it is |
|---|---|
| `TECH_MD/` | 242 technology records in Markdown |
| `TECH_TXT/` | Plain-text mirrors of the same records |
| `TECH_MD/00_Technology_Record_Template.md` | The blank template every record follows |

## Two designation families

| Prefix | What it covers |
|---|---|
| `TECH-ACT-000` | Technology A.C.T developed itself |
| `TECH-GOI-000-0` | Technology recovered from, or assessed against, a Group of Interest |

A `TECH-GOI` record exists to hazard-review a recovered device, set custody rules for a
physical object A.C.T holds, assess a rival capability, or support a counter-operation. A
GOI does not get a technology set simply for existing.

## What a record contains

Each record runs 14 chapters in a fixed order: function summary, origin and custody,
physical description, technical specification, interface, operating procedure, servicing,
fault isolation, known limits, failure history, division use, cross-references, open
questions, and file metadata. The open questions chapter is deliberate — the archive
records what it does not know rather than filling the gap.

## Markdown and plain-text twins

`TECH_MD/` and `TECH_TXT/` carry the same 242 records. The Markdown editions use pipe
tables; the plain-text editions draw the same tables as ASCII boxes. Neither is a summary
of the other.
