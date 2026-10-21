# A.C.T Corpus Bloat and Borrowed Vocabulary Cleanup Review

- **Prepared:** 2026-10-22
- **Scope:** all 968 documents in the repository, plus the SCP Wiki's own writing guides as an outside reference
- **Question asked:** which documents exist because automation produced them rather than because the archive needs them, and which carry vocabulary or content that is not A.C.T's own

---

## 1. Why this review exists

Automation was run at high volume across the technology records. Volume hides two failure modes that a per-file read does not catch: the same sentence being stamped into hundreds of files, and whole categories of document being created because a numbering rule said the slot should be filled. Both were found here.

The SCP Wiki was used as an outside yardstick because it runs the same kind of archive-fiction project at far larger scale and publishes its own editing standards. Nothing was copied from it. Its content is licensed CC BY-SA 3.0, which means anything lifted would have to be attributed and re-licensed under the same terms; the correct response is to read it and write differently, which is what was done.

## 2. What the SCP Wiki's own guides say, in paraphrase

Four rules from its writing guidance map directly onto defects in this corpus. They are restated here as principles, not quoted.

**An article should not be longer than it needs to be.** The guide's stated view is that length is free but not costless, and that the single simplest improvement available to a writer is cutting material that distracts from the piece. A record that fills a section because the house shape has a section is exactly the material it means.

**Procedures get a paragraph or two, not a chapter.** Containment procedures should be limited to what the object actually requires, and should stay grounded in technology that plausibly exists rather than reaching for invented machinery.

**Establish what the thing is before you introduce what is odd about it.** The guide's example is a bear: weight and height first, six paws second. A description that opens on the anomaly without first naming the ordinary object reads as chaotic.

**Every part of the format is a story beat.** Object class and procedures are the introduction, description and addenda are the development, the final addendum or log is the ending. The guide asks writers to check that each part contributes to the story rather than merely occupying its slot.

Its aesthetics guidance adds three small rules: avoid large blocks of text, do not use bold or italics to emphasise important sentences, and do not cross out large passages.

## 3. Findings, with counts

### 3.1 The stamp — one sentence in 308 files

The clearest automation signature in the corpus was a single sentence placed before the specification table of every technology record: *values the archive does not hold are marked NOT MEASURED and each is filed under OPEN QUESTIONS*. It appeared in **154 `.md` records and their 154 `.txt` twins**, spanning sets `001` through `136`. The sentence said nothing about any particular record. It was a note the builder wrote about itself.

**This is fixed.** See section 4.

### 3.2 Borrowed institutional vocabulary

| Term | Files | Occurrences | Assessment |
| --- | --- | --- | --- |
| `O5` in any form | 139 | 586 | SCP-derived governing body. Woven into 139 documents including the main history book. Canon decision, not a cleanup. |
| `amnestics` | 183 | 638 | Genre-shared term, strongest association is SCP. Heaviest in Technology Document at 247. |
| `memetic` | 223 | 707 | Genre-shared term. Heaviest in Technology Document at 208. |
| `Site-NN` shorthand | 68 | 159 | A.C.T's own full form `ACT-SITE-NN` appears 1357 times. The short form is internal shorthand, not leakage. |
| SCP object classes `Euclid` / `Keter` / `Thaumiel` / `Apollyon` | 8 | 24 | Only 2 are in in-world documents, and both are prohibitions against using the words. The other 22 are in research memos comparing the two wikis. |

**Nothing was rewritten here.** `O5` appears as 18 distinct forms — `O5 Council` 54 times, `O5-RESTRICTED` 58 times, `O5 Access`, `O5 Oversight`, `O5 Liaison`, `O5 Headquarters`, `O5-1`, `O5-level`. Replacing it across 139 files is a canon change to the governing body of the setting, not a formatting fix, and it belongs to whoever owns the setting. The count is recorded so the decision can be made with the scale in front of it.

`amnestics` and `memetic` are shared genre vocabulary rather than one wiki's property. Rewriting 1345 occurrences would be a larger intervention than the problem.

The SCP object classes are effectively absent from in-world documents. The one in-world memorandum that mentions `Keter` does so to forbid writing it in unofficial files, and the generation standard lists `Keter`/`Thaumiel` under nomenclature checks as banned terms. That is the corpus policing itself correctly.

### 3.3 Third-party crossover content

**18 files, roughly 78,000 words**, under `A.C.T_UNIVERSE_DOCUMENT/A.C.T Anomaly Document/Anomaly Legacy 01 .txt/STORY/`:

- `LobCorp_x_ACT_Crossover_Chapter_1` through `Chapter_8`, each as `.md` and `.txt` — 16 files
- `Lobotomy_Corporation_Lore_Research` as `.md` and `.txt` — 2 files

These are crossover fiction using named characters and concepts from a commercial game series — Sephirah, Abnormality, Singularity, E.G.O, Ayin — appearing 381 and 204 times respectively. They are not A.C.T worldbuilding and no in-world document cites them.

**Flagged, not touched, and then removed by the owner.** `git log --diff-filter=A` showed all 18 were added in commit `a17dfd0` on 2026-09-17 by `Redditor008`, before this work began, so they were listed here rather than deleted — authored fiction is not an assistant's call to make. The owner then removed the whole directory in commit `d093b98` on 2026-10-22, deleting 11,170 lines. The `STORY` directory no longer exists in the tree.

Residual third-party proper nouns across the corpus after that deletion: **70**, all inside the comparative research memos (`Project-Moon-and-SCP-Wiki_Research.md` 43, `Cross-Wiki_Worldbuilding_Gap_Research.md` 17, `Wiki_Style_Research` 3) and two `TECH-GOI-058-1` twins. Those memos are the record of what was compared and why, and the two technology twins use one term in a passing simile, so nothing further was removed.

The same applies to `RESEARCH FOLDER/2026-09-06_Project-Moon-and-SCP-Wiki_Research.md` (11,096 words) and `RESEARCH FOLDER/2026-09-11_A.C.T._Cross-Wiki_Worldbuilding_Gap_Research.md` (9,404 words). Both are legitimate comparative research and both contain the bulk of the borrowed-class-name hits in section 3.2.

### 3.4 Redundant overview documents

Three near-duplicate pairs sit in `A.C.T .md Document` and `A.C.T .txt Document`. Similarity is by 8-word shingle Jaccard over the whole document.

| Pair | Words | Similarity |
| --- | --- | --- |
| `ACT_GOI_Registry_and_External_Threat_Doctrine_Archive` vs `Part/ACT_Universe_Part_4_GOI_Registry_Rival_Powers_and_External_Threat_Doctrine` | 2224 / 2196 | 0.959 |
| `ACT_Facility_Archive_Overview` vs `Part/ACT_Universe_Part_1_Overview` | 1211 / 1151 | 0.846 |
| `Part/ACT_Universe_Part_1_Overview` vs `Part/ACT_Universe_Part_1_Overview_Document` | 1151 / 1169 | 0.846 |

The same overview exists both standalone and inside a `Part/` series, and Part 1 exists twice under two filenames. **Not touched** — all pre-existing at `a17dfd0`, and which copy is canonical is an editorial call.

### 3.5 Process scaffolding

`PATCH SAVER/Technology_Phase_Patch_Saver.md` is **45,997 words in one file** with 40 log entries. It is the largest document in the repository and is not an in-world document at all — it is build scaffolding. It is useful, but at this size it belongs split into a live log and an archive rather than growing without bound.

`TECH_MD/README.md` is **10,021 words** across four sections, of which *Current Individual Technology Records* is 5,426 words and *Current Status* is 4,252. An index that runs to ten thousand words has become a second corpus.

### 3.6 A format defect found while measuring — now fixed

**137 of the 229 `.txt` technology twins carried the archive status as three plain `Label: value` lines while their `.md` twins carried it as a pipe table.** House policy is that `.txt` always uses the box, so those 137 twins broke the policy in one section each. One further twin, `TECH-GOI-071-5`, has no archive table in either format and is internally consistent. Four `TECH-GOI-071` twins carried the archive data twice — once as a correct box and again as plain lines.

**Correcting the first draft of this section.** An earlier version of this memo said the archive-status table was *absent* from 138 `.txt` twins. That was wrong. The data was present in every one of them, rendered as plain label lines instead of a box. Nothing was missing; the format was wrong. The count was also 137, not 138.

**This is fixed.** All 137 plain blocks were rendered as house boxes at the standard two-column widths of 28 and 87, with each value wrapped inside its own column. The four redundant plain blocks were removed, since those twins already carried the box. Every one of the 141 conversions was verified value-identical against `HEAD` — all three fields, word for word, in all 141 files.

The result is that **all 229 technology records now have `.md` table counts equal to `.txt` box counts**, where before 137 did not. The defect went unnoticed for as long as it did because the standing gate compared file counts, which were equal at 229/229, and never compared table counts.

## 4. What was cleaned in this pass

**The stamp was removed from all 308 files.** Each record now carries a sentence built from its own content: the parameters that are actually blank in that record's tables, named explicitly, or — where nothing is blank — that record's own first open question.

Examples of what replaced the shared sentence:

- `TECH-ACT-001` — 4 figures below are blank: Unit mass, Power draw, Field radius per unit, and 1 more.
- `TECH-ACT-022` — The archive holds no figure for Mixture bands, Viscosity range, Shelf life and storage band.
- `TECH-ACT-040` — 3 values below are not held by the archive: Model horizon, Concurrent asset count, Uplink latency limit.
- `TECH-GOI-048-2` — 2 values below are not held by the archive: Maps recovered, Confirmed mouth sites.

Ten sentence shapes are used, rotated by record index, so the fix does not become a new stamp. The replacement is wrapped to the same 20-word / 118-character rule as the rest of the paragraph, and the identical wrapped paragraph is written to both twins.

Net effect: **308 files changed, 872 lines removed, 640 inserted** — the corpus is 232 lines shorter and no longer repeats one sentence 308 times.

### Second pass — archive status rendered as boxes

A second pass converted the 137 plain `Archive Status:` / `Distribution:` / `Authority:` line blocks into house boxes at widths 28 and 87, with each value wrapped inside its own column, and removed the 4 redundant plain blocks in the `TECH-GOI-071` twins that already carried a box.

Every conversion was verified value-identical against `HEAD`: all three fields, word for word, in all 141 files. Four `TECH-GOI-071` twins were first given a duplicate box by the converter — they already had one — and were reverted before the redundant plain blocks were removed instead. That mistake was caught by a duplicate-row check, not by the parity check.

Net effect of the second pass: **141 files changed, 1344 lines added, 512 removed.** All 229 technology records now have `.md` table counts equal to `.txt` box counts, where 137 previously did not.

## 5. Verification

| Check | After pass 1 | After pass 2 |
| --- | --- | --- |
| Residual stamp occurrences | 0 | 0 |
| Records where `.md` tables ≠ `.txt` boxes | 137 | **0** |
| Twins with a duplicated archive box | 4 | **0** |
| Twins with plain archive label lines | 137 | **0** |
| Archive values changed by the conversion | — | **0 of 423 fields** |
| Box rules not exactly 118 characters | 0 | 0 |
| Widest box line in the repository | 118 | 118 |
| Lines over 118 in `.txt` | 6, all in `TECH_TXT/README.txt` | 6, same file, unchanged |
| DOCUMENT_COUNT | 968 | 969, then 951 after the owner deleted the 18 crossover files |
| `TECH_MD` / `TECH_TXT` file counts | 229 / 229 | 229 / 229 |
| multiH1 / odd-fence / bad-EOF / md-with-box | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| `git diff --check` | clean | clean |

Most-repeated sentence in the corpus after the pass, for comparison: 20 files. Before the pass: 308.

## 6. Not resolved, with reasons

- **`O5` across 139 files — RESOLVED as canon.** The owner confirmed `O5` stands for Overseer Five and is A.C.T's own governing authority. Nothing is rewritten. The reading is recorded in `ACT_Generation_Standard_2026_Update.md` under Canonical Term: O5 so it is not flagged again.
- **`amnestics` 638 and `memetic` 707 — RESOLVED as canon.** The owner ruled both stay. Their house forms are now defined in `ACT_Generation_Standard_2026_Update.md` under Canonical Term: Amnestics and Canonical Term: Memetic, alongside the O5 ruling, so no future pass flags them.
- **Redundant overview documents — RESOLVED.** Measuring the whole folder showed six archive records duplicating the six-part A.C.T Universe series at 0.863 to 0.975 line similarity, with Part One present a third time. Each archive record now carries a Series Position section, the Part folders are removed, and the five citations to them were rewritten.
- **Patch Saver and TECH README — RESOLVED.** A compact ledger of all 43 entries was written to `PATCH SAVER/Technology_Phase_Patch_Ledger_Compact.md` (2,128 words) and the full log left intact. `TECH_MD/README.md` went from 10,021 to 5,818 words and `TECH_TXT/README.txt` from 10,056 to 5,853, with the Current Status text moved to `PATCH SAVER/Technology_Phase_Current_Status.md` and `.txt`.
- **`docs/index.html` is 0 bytes.** Left alone at the owner's instruction; the document folder work is not finished yet.
- **Section-level uniformity across the technology records.** Removing one repeated sentence does not undo the fact that 229 records share one 14-section skeleton in the same order. That is a house shape decision, not a defect, and changing it is an editorial call.
- **The `^  \S` orphan-line metric reads 6629 across 453 files, and that number is not a defect count.** It matches ordinary indented prose. The true orphan count inside technology records is 209. The figure is recorded so it is not mistaken for a finding.

## 6.1 Resolved after this review was written

- **`O5` across 139 files** — ruled canon by the owner, standing for Overseer Five. Recorded in `ACT_Generation_Standard_2026_Update.md`.

- **18 crossover files, ~78,000 words** — removed by the owner at `d093b98`. See section 3.3.
- **137 `.txt` twins with archive status as plain lines** — rendered as boxes, see section 4.

## 7. Rule adopted going forward

A technology record earns its sections by what the archive actually holds about the object. Where it holds nothing, the record says so in one line and the section stays short. No sentence is written into a record unless it names something in that record.
