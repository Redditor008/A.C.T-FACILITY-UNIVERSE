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

**Not touched.** `git log --diff-filter=A` shows all 18 were added in commit `a17dfd0` on 2026-09-17 by `Redditor008`, before this work began. They are pre-existing authored content, not automation output, and deleting someone's fiction is not a cleanup an assistant should make unilaterally. The list is here so the decision can be made with the file names in hand.

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

### 3.6 A defect found while measuring, not while cleaning

**138 of the 229 `.txt` technology twins contain no `ARCHIVE STATUS` and no `DISTRIBUTION` line at all.** Their `.md` twins carry five tables; the `.txt` carries four boxes. The archive-status table is simply absent from the `.txt` render of those records.

This is pre-existing and was not introduced by this cleanup — verified by running the same comparison against `HEAD` for all 229 records, where every record returned an identical result before and after the edit. It went unnoticed because the standing gate compares file counts, which are equal at 229/229, not table counts.

## 4. What was cleaned in this pass

**The stamp was removed from all 308 files.** Each record now carries a sentence built from its own content: the parameters that are actually blank in that record's tables, named explicitly, or — where nothing is blank — that record's own first open question.

Examples of what replaced the shared sentence:

- `TECH-ACT-001` — 4 figures below are blank: Unit mass, Power draw, Field radius per unit, and 1 more.
- `TECH-ACT-022` — The archive holds no figure for Mixture bands, Viscosity range, Shelf life and storage band.
- `TECH-ACT-040` — 3 values below are not held by the archive: Model horizon, Concurrent asset count, Uplink latency limit.
- `TECH-GOI-048-2` — 2 values below are not held by the archive: Maps recovered, Confirmed mouth sites.

Ten sentence shapes are used, rotated by record index, so the fix does not become a new stamp. The replacement is wrapped to the same 20-word / 118-character rule as the rest of the paragraph, and the identical wrapped paragraph is written to both twins.

Net effect: **308 files changed, 872 lines removed, 640 inserted** — the corpus is 232 lines shorter and no longer repeats one sentence 308 times.

## 5. Verification

| Check | Result |
| --- | --- |
| Residual stamp occurrences | 0 |
| Files changed | 308 (154 `.md` + 154 `.txt`) |
| Records where the twin check changed because of this edit | 0 of 229 |
| Box rules not exactly 118 characters | 0 |
| Widest box line in the repository | 118 |
| Lines over 118 characters in `.txt` | 6, all in `TECH_TXT/README.txt`, none in a changed file |
| DOCUMENT_COUNT | 968, unchanged |
| `TECH_MD` / `TECH_TXT` file counts | 229 / 229 |
| multiH1 / odd-fence / bad-EOF / md-with-box | 0 / 0 / 0 / 0 |
| `git diff --check` | clean |

Most-repeated sentence in the corpus after the pass, for comparison: 20 files. Before the pass: 308.

## 6. Not resolved, with reasons

- **`O5` across 139 files.** Canon decision, not formatting. Scale recorded in section 3.2.
- **`amnestics` 638 and `memetic` 707.** Shared genre vocabulary; rewriting exceeds the problem.
- **18 crossover files, ~78,000 words.** Pre-existing authored content by another author at `a17dfd0`. Flagged, not deleted.
- **3 redundant overview pairs.** Editorial call on which copy is canonical.
- **138 `.txt` twins missing the archive-status box.** Real defect, pre-existing, needs a separate render pass.
- **Patch Saver at 45,997 words and TECH README at 10,021 words.** Both should be split; neither was restructured here.
- **`docs/index.html` is 0 bytes.** Still empty.
- **The `^  \S` orphan-line metric reads 6629 across 453 files, and that number is not a defect count.** It matches ordinary indented prose. The true orphan count inside technology records is 209. The figure is recorded so it is not mistaken for a finding.

## 7. Rule adopted going forward

A technology record earns its sections by what the archive actually holds about the object. Where it holds nothing, the record says so in one line and the section stays short. No sentence is written into a record unless it names something in that record.
