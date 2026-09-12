# A.C.T-FACILITY-UNIVERSE

**Anomaly Containment Transformation (A.C.T)** is an original containment-fiction universe about an institution that does not stop at locking the impossible away. The Facility studies anomalies, contains them, argues over them, transforms some of them into controlled uses, refuses others, and records the cost of every decision inside an archive that is never as clean as it pretends to be.

A.C.T. is built around the question: **what happens when containment becomes an engine for change instead of a permanent box?** The answer is not simple victory. Transformation creates tools, amnestics, infrastructure, cover stories, political debts, damaged personnel, false histories, and old lies that keep breathing underneath the official record.

---

## What the A.C.T. Universe Is

A.C.T. stands for **Anomaly Containment Transformation**. In-world, it is a global hidden institution built to respond to breaks in reality: objects that should not exist, subjects that should not survive, places that do not obey geography, memories that behave like infections, gods that sleep under foundations, and files that become dangerous when read too directly.

The Facility's public face is absence. Incidents become equipment failures, weather events, folklore, criminal cases, medical confusion, or records that no longer point where they used to point. Its internal face is documentation: classification manuals, floor dossiers, site registries, review boards, witness logs, amnestic histories, and contradictory archive copies that reveal as much through drift as through direct disclosure.

The universe's central tension is not simply **humanity versus anomaly**. It is **containment versus transformation**:

- containment asks how to keep the impossible from harming the world;
- research asks what the impossible means;
- transformation asks whether an anomaly can become useful without becoming an atrocity;
- the archive asks what had to be hidden so the institution could keep functioning.

A.C.T. uses other containment and facility-fiction traditions as historical research references, but the core universe is its own continuity with its own terminology, classes, sites, anomalies, ethics, and mysteries. Crossover material exists in the repository only where explicitly marked or folder-separated; it is not the default core canon.

---

## Tidbits / Core Identity Notes

- **The Facility transforms.** A.C.T.'s signature difference is that containment is not always the final state. Some anomalies become amnestics, systems, warnings, tools, doctrine, or permanent institutional scars.
- **The archive is a character.** Drift between records, missing context, redactions, legacy files, and archive copies are part of the setting's language.
- **ITHYOS / ENTITY-000 is foundational.** The First Vault material is not just another anomaly file; it is tied to the origin pressure beneath the Facility and the ABYSS.
- **NEMNOLIA matters because memory matters.** The 004-series amnestic archive is one of the clearest examples of A.C.T. converting an anomaly into an operational system while inheriting its cost.
- **Sites are not interchangeable.** Each SITE and SUB-SITE has regional purpose, floor logic, command function, containment profile, and local narrative pressure.
- **The ABYSS is below the floor system.** Floor designations run from **F-1** upward to surface level; below F-1 only the ABYSS access route continues.
- **`[ BLANK ]` and `[BLANK]` are different.** `[ BLANK ]` is a spaced redaction marker. `[BLANK]` is an unspaced containment class. Do not merge them.
- **GOIs are not only enemies.** Groups of Interest may be governments, markets, cults, companies, civil networks, rivals, witnesses, partial allies, or communities A.C.T. cannot cleanly classify.
- **The story layer is archive-adjacent.** Main story files dramatize the institution's contradictions, especially memory, origin, ABYSS history, and the cost of official truth.

---

## Repository Map

```
A.C.T-FACILITY-UNIVERSE/
├── README.md                     ← this canonical index (authoritative map of the repo)
├── A.C.T_UNIVERSE_DOCUMENT/      ← the universe itself (all canon text lives here)
│   ├── A.C.T .md Document/       ← core doctrine — Markdown editions
│   │   ├── Part/                 ← Part series (Part One → …), Markdown
│   │   ├── Operational Forms/    ← reusable in-world working forms
│   │   ├── Site Dossier/         ← 10 site/sub-site dossiers (5 SITE + 5 SUB)
│   │   └── Site Dossier/Floor Dossier/ ← 46 individual floor dossiers
│   ├── A.C.T .txt Document/      ← core doctrine — plain-text twin editions
│   │   └── (PART/ + Site Dossier mirror tree with the same dossiers)
│   ├── A.C.T Anomaly Document/   ← the anomalies themselves
│   │   ├── Anomaly Legacy 01 .txt/  ← legacy-era files (+ Log/, + STORY/ crossover)
│   │   ├── Anomaly Legacy 01.md/    ← legacy-era Markdown (a few files)
│   │   ├── Anomaly Modern txt/      ← modern-era files (+ Log/)
│   │   └── ITHYOS Document/         ← ITHYOS / ENTITY-000 (ITHYOS .md, ITHYOS .txt, ITHYOS Log)
│   ├── A.C.T GOI Document/       ← Groups of Interest (GOI_MD + GOI_TXT)
│   ├── ACT MAIN STORY/           ← story root (Continuity Policy, Index, Archives, Chapters, Characters, Narrative, Outlines)
│   ├── Junior Handbook/          ← ACT Orientation Handbook (junior/Level 1–2 edition)
│   └── 'A History of Anomaly Containment Transformation' BOOK.md  ← in-universe history book
├── RESEARCH FOLDER/              ← dated maintenance reviews, research records, and provenance notes
├── LOGO/                         ← project logo assets (png / svg / seal)
└── docs/                         ← future wiki/site scaffold (empty landing page)
```

---

## The Twin Convention (read before editing)

The repository runs a strong **`.md` / `.txt` twin** discipline:

- Most documents exist as a **Markdown edition** (headings, bold, tables) and a **plain-text mirror** in the matching twin folder (headings/bold/backticks stripped; content otherwise lossless).
- `A.C.T .md Document/` ↔ `A.C.T .txt Document/`, `GOI_MD/` ↔ `GOI_TXT/`, `ITHYOS .md/` ↔ `ITHYOS .txt/`, `Anomaly Legacy 01.md/` ↔ `Anomaly Legacy 01 .txt/`, and every floor/site dossier has both twins.
- **Edits must be mirrored to both twins** so they don't drift (regenerate the twin from the `.md` and diff).
- Documented exceptions:
  - The **BOOK** is `.md`-only (single authoritative file).
  - `A.C.T .txt Document/` holds two **legacy records that are intentionally `.txt`-only**: `The-Infant-State-Scientific-Frustration-Log-LEGACY.txt` and `The-Unfiled-Registry-The-Black-Ledger-of-the-Five-LEGACY.txt`.
  - `GOI_TXT/` copies are deliberately plain-text/ASCII-styled reading copies (documented convention, not drift).
- Spelling rules that must stay distinct: **`[ BLANK ]`** (spaced) = redaction marker; **`[BLANK]`** (unspaced) = containment class.

---

## Canon / Authority Guidance

Per the **2026-09-07 Core Worldbuilding Consistency Review** (`RESEARCH FOLDER/`):

- **Part series** — `Part/ACT_Universe_Part_1_Overview.md` is the **canonical** universe-compilation edition. `ACT_Universe_Part_1_Overview_Document.md` is its companion ("Introduction / Closing Note" framing) edition; the Archive folder holds the in-universe archive copy. All three number identically.
- **Archive series** (…`_Archive.md`/`.txt` under `.md Document` / `.txt Document`) are the in-universe institutional copies of the same doctrine. Do not let them drift from the Part series.
- **BOOK** is the in-universe *history* of A.C.T — a readable synthesis, not the doctrine source of record.
- **Junior Handbook** is deliberately simplified for junior orientation (Level 1–2); do not force the full mid-level role ladder into it.
- **Anomaly Modern txt / Anomaly Legacy 01** hold the actual anomaly files (`AFD-…`, `UFD-…`, `ANM-…` codes). Anomaly code families: `AFD` (anomaly), `UFD` (unfiled), `ANM` (anomaly, modern), with type codes such as OB / SU / CH / NB / ME / IH / PL / SP / TI / ?.H.
- **GOI designation** is `GOI-XX-X-XXX` (doctrine matches the GOI folder files).
- **Floor canon**: floor designations run **F-1** (deepest numbered floor) upward to **F-N** at surface level; below F-1 only the **ABYSS** access route continues. `F-xxxx` is in-draft shorthand where the precise floor is not declassified.
- **Site designation**: `ACT-SITE-01-US-W` / `ACT-SUB-01-US-W` style (regional codes defined by the Global Site Registry).

---

## Document Families (what lives where)

| Family | Path | Contents |
|---|---|---|
| Core doctrine (md) | `A.C.T_UNIVERSE_DOCUMENT/A.C.T .md Document/` | 24 top-level texts: Site Doctrine, Site Map & Jurisdiction, Global Site Registry, Classification Manual, Standard/RCT/Log-Categories formats, Reality Doctrine, Divisions & Personnel, Personnel Exposure/Excommunicated Class/Resilience Doctrine, Normalcy Management Doctrine, Transformation Review Board/Field Asset Doctrine, Standing Field Units/Cross-Containment Doctrine, Technology Timeline, Master Index 50, Visual Reference Guide, NEMNOLIA archive, and the Archive-series copies |
| Core doctrine (txt) | `…/A.C.T .txt Document/` | Twin mirrors of all of the above (+ the 2 legacy-only records) |
| Part series | `…/A.C.T .md Document/Part/` ↔ `…/A.C.T .txt Document/PART/` | The numbered Part One → … universe texts |
| Operational forms | `…/Operational Forms/` (both md & txt trees) | Reusable in-world working forms, including witness statement/testimony intake and access/egress ledgers |
| Site dossiers | `…/Site Dossier/` (both md & txt trees) | 5 `SITE` + 5 `SUB` comprehensive dossiers |
| Floor dossiers | `…/Site Dossier/Floor Dossier/` (both trees) | 46 individual floor dossiers (SUB-04 has no floors by canon) |
| Legacy anomalies | `…/A.C.T Anomaly Document/Anomaly Legacy 01 .txt/` (+ `Log/`, `STORY/`) and `Anomaly Legacy 01.md/` | Legacy-era files, observation logs, and the Lobotomy Corporation × A.C.T crossover story |
| Modern anomalies | `…/Anomaly Modern txt/` (+ `Log/`) | Modern-era anomaly files and dossiers, character/capability profiles |
| ITHYOS | `…/ITHYOS Document/` (`ITHYOS .md`, `ITHYOS .txt`, `ITHYOS Log`) | ENTITY-000 ITHYOS first-vault records, modern file standard, archive copies, tales |
| GOI | `…/A.C.T GOI Document/GOI_MD` ↔ `GOI_TXT` | Record template, recovered-document format, recovered-record holding folder, development roadmap, 8 dossiers (GAA, A-GA, Anstrall, CoTD, DREAM, L.F., Mysterious Guild, Amazoo Circus) |
| Main story | `…/ACT MAIN STORY/` | Continuity Policy, Story Index, full manuscripts, chapters (1–12 + Epilogue, md+txt), Archives, Characters, Narrative, Outlines |
| Handbook | `…/Junior Handbook/` | `ACT_Orientation_Handbook` (md+txt) |
| BOOK | `…/'A History of Anomaly Containment Transformation' BOOK.md` | In-universe history, md-only |
| Reviews | `RESEARCH FOLDER/` | Dated consistency/style reviews + working/provenance notes — read before large edits |

---

## Development Rules

- **GOI development is gated**: create only approved GOIs; never batch-generate unapproved scaffold entries or scan results.
- **Dossier files are per-item documents**: individual, un-summarized, detailed, matching the ACT archive style. No compressed or abridged notes in the RESEARCH FOLDER either (extensive `.md` only).
- New content should reference the canonical role names, the ANM code table, and the containment-class list adopted by the 2026-09-07 consistency sweep so the chosen system stays load-bearing.
- Every completed change should be committed and pushed; keep `.md`/`.txt` twins in lockstep.
