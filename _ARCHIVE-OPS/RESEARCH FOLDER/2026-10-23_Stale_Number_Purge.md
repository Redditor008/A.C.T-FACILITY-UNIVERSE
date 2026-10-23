# Stale Number Purge

**Date:** 2026-10-23
**Scope:** Every figure the Patch Saver and the research memos carried forward without re-measuring
**Method:** `_ARCHIVE-OPS/tools/corpus_numbers.py`, run against the whole tree
**Status:** Complete. Six figures corrected, one withdrawn, one gate added.

---

## Why this record exists

Two figures quoted in nearly every report for many batches turned out to be false. `TECH_MD` was
reported at 231 files and 229 records; it measures 244 and 242. The GOI alignment letters were
reported as an open discrepancy against the root README; the README already lists all seven and
there was never a conflict.

Neither error came from a bad measurement. Both came from a good measurement that was carried
forward through later batches and never re-run while the corpus changed underneath it. The purge
below re-measures every figure the archive states and corrects or strikes each one.

## The measuring instrument

`_ARCHIVE-OPS/tools/corpus_numbers.py` is now the only source for corpus figures. It prints a
labelled line per figure, and no report may quote a number this script does not produce. Two
counts are deliberately separate:

| LABEL | MEANS |
|---|---|
| `DOCUMENT_COUNT` | Every `.md` and `.txt` in the tree, backstage folders included. This is the figure reports quote. |
| `DOCUMENT_COUNT_EX_OPS` | The reader-facing documents only. This is the population the defect gates run over. |

Conflating the two is how the earlier counts drifted.

## Corrected

| FIGURE | WAS REPORTED AS | MEASURES | NOTE |
|---|---|---|---|
| Technology records | 229 | **242** | `TECH_MD` 244 files less README and template. 244 twins, 0 unpaired. |
| `TECH_MD` files | 231 | **244** | Never re-counted after sets 069, 070, 073 and 074 shipped. |
| GOI alignment letters | 7 in corpus vs 4 claimed | **7, and the README lists all 7** | `B2 N8 P16 T2 U2 W12 X18`. Root README line 174 already carries all seven. |
| `.md` prose lines over 118 | 18 | **80** | The old filter dropped indented continuation lines, which is where they all lived. |
| Anomaly index claim | 176 files | **174** indexed files | The folder holds 178 files overall; 175 are Markdown or plain text; 174 exclude this index; 173 exclude the README too. The index's own claim was corrected in place. |
| GOI dossiers | 30 | **30** — the README was right | The 36 figure was a whole-folder `.md` count, not a dossier count. `GOI_DOSSIERS` and `GOI_MD_FILES` are now separate labels. |

## Withdrawn

**The GOI designation-letter discrepancy.** Recorded for several batches as an unresolved backlog
item. It is not a discrepancy. The corpus carries seven alignment letters and the root README
documents seven: `P` positive, `N` neutral, `X` negative, `W` work, `B` business, `T` trade,
`U` unknown. The finding was stale on arrival and is struck from the queue.

## Defect found while purging, and fixed

Six doctrine records each carried a single prose line between 308 and 353 characters. These are the
`This record is Part ... of the A.C.T Universe reading order` opening paragraphs, written as one
unwrapped block. All six were re-wrapped at 118.

| FILE | LINE | WAS | NOW |
|---|---|---|---|
| `ACT_Facility_Archive_Overview.md` | 182 | 308 | 3 lines, widest 116 |
| `ACT_Divisions_Personnel_and_Operational_Life_Archive.md` | 516 | 353 | 4 lines, widest 115 |
| `ACT_GOI_Registry_and_External_Threat_Doctrine_Archive.md` | 484 | 352 | 4 lines, widest 116 |
| `ACT_Historical_Origin_and_Abyss_Archive.md` | 380 | 328 | 3 lines, widest 117 |
| `ACT_Anomaly_Classification_Manual_Archive.md` | 638 | 324 | 3 lines, widest 116 |
| `ACT_Internal_Structure_and_Reality_Doctrine_Archive.md` | 644 | 314 | 3 lines, widest 117 |

The plain-text twins did not change. They were already wrapped at 118 and the `.txt` wide-prose
count is unaffected, which confirms the long lines were an `.md`-only defect.

## What the 80 remaining wide `.md` lines are

Not prose. Seventy-nine sit in `TECH_MD/README.md` and one in `GOI_MD/README.md`. Every one is a
markdown link to a technology record whose filename is long enough that the link target alone
exceeds the limit. A link target is an atomic token and cannot be broken across lines without
breaking the link. These stay as they are and are recorded here so they are not re-found as a
defect.

## Standing rule from this purge

Quote a figure only in the same turn it was measured. Where a figure must be carried forward, carry
the label from `corpus_numbers.py` and not the number, and re-run the script before the report.

## Full-suite state after the purge

| GATE | RESULT |
|---|---|
| `DOCUMENT_COUNT` | 1000 |
| `DOCUMENT_COUNT_EX_OPS` | 979 |
| `RECORDS_NOT_ONE_H1` | 0 |
| `BAD_EOF` | 0 |
| `ODD_FENCE` | 0 |
| `TXT_BOLD_FILES` / `TXT_BACKTICK_FILES` / `TXT_MD_HEADING_FILES` | 0 / 0 / 0 |
| `TXT_LINK_FILES` | 1 — `TECH_TXT/README.txt` |
| `TXT_WIDE_PROSE_LINES` | 10 — all `TECH_TXT/README.txt` |
| `MD_WIDE_PROSE_LINES` | 80 — all link continuations, see above |
| `TECH_MD` / `TECH_TXT` | 244 / 244, 242 records, 0 unpaired |
| `GOI_DOSSIERS` / `GOI_MD_FILES` | 30 / 36 |
| `GOI_ALIGNMENT_LETTERS` | 7 |
| `PATCH_SAVER_ENTRIES` | 80 |
| `STORY_CHAPTER_MD_FILES` | 13 |
