# A.C.T-FACILITY-UNIVERSE

**Anomaly Containment Transformation (A.C.T)** — a worldbuilding project about a facility that does not merely contain anomalies: it transforms them. Built from the author's original idea layered over other publicly known projects.

---

## Repository Map

```
A.C.T-FACILITY-UNIVERSE/
├── README.md                     ← this canonical index (authoritative map of the repo)
├── A.C.T_UNIVERSE_DOCUMENT/      ← the universe itself (all canon text lives here)
│   ├── A.C.T .md Document/       ← core doctrine — Markdown editions
│   │   ├── Part/                 ← Part series (Part One → …), Markdown
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
│   ├── ACT MAIN STORY/           ← story root (Index, Archives, Chapters, Characters, Narrative, Outlines)
│   ├── Junior Handbook/          ← ACT Orientation Handbook (junior/Level 1–2 edition)
│   └── 'A History of Anomaly Containment Transformation' BOOK.md  ← in-universe history book
├── RESEARCH FOLDER/              ← dated maintenance reviews (2026-09-06 → 2026-09-08)
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
- **Anomaly Modern txt / Anomaly Legacy 01** hold the actual anomaly files (`AFD-…`, `UFD-…`, `ANM-…` codes). Anomaly code families: `AFD` (anomaly), `UFD` (unfiled), `ANM` (anomaly, modern), with type codes such as OB / SU / CH / NB / ME / IH / PL / TI / ?.H.
- **GOI designation** is `GOI-XX-X-XXX` (doctrine matches the GOI folder files).
- **Floor canon**: floor designations run **F-1** (deepest numbered floor) upward to **F-N** at surface level; below F-1 only the **ABYSS** access route continues. `F-xxxx` is in-draft shorthand where the precise floor is not declassified.
- **Site designation**: `ACT-SITE-01-US-W` / `ACT-SUB-01-US-W` style (regional codes defined by the Global Site Registry).

---

## Document Families (what lives where)

| Family | Path | Contents |
|---|---|---|
| Core doctrine (md) | `A.C.T_UNIVERSE_DOCUMENT/A.C.T .md Document/` | 19 top-level texts: Site Doctrine, Site Map & Jurisdiction, Global Site Registry, Classification Manual, Standard/RCT/Log-Categories formats, Reality Doctrine, Divisions & Personnel, Technology Timeline, Master Index 50, Visual Reference Guide, NEMNOLIA archive, and the Archive-series copies |
| Core doctrine (txt) | `…/A.C.T .txt Document/` | Twin mirrors of all of the above (+ the 2 legacy-only records) |
| Part series | `…/A.C.T .md Document/Part/` ↔ `…/A.C.T .txt Document/PART/` | The numbered Part One → … universe texts |
| Site dossiers | `…/Site Dossier/` (both md & txt trees) | 5 `SITE` + 5 `SUB` comprehensive dossiers |
| Floor dossiers | `…/Site Dossier/Floor Dossier/` (both trees) | 46 individual floor dossiers (SUB-04 has no floors by canon) |
| Legacy anomalies | `…/A.C.T Anomaly Document/Anomaly Legacy 01 .txt/` (+ `Log/`, `STORY/`) and `Anomaly Legacy 01.md/` | Legacy-era files, observation logs, and the Lobotomy Corporation × A.C.T crossover story |
| Modern anomalies | `…/Anomaly Modern txt/` (+ `Log/`) | Modern-era anomaly files and dossiers, character/capability profiles |
| ITHYOS | `…/ITHYOS Document/` (`ITHYOS .md`, `ITHYOS .txt`, `ITHYOS Log`) | ENTITY-000 ITHYOS first-vault records, modern file standard, archive copies, tales |
| GOI | `…/A.C.T GOI Document/GOI_MD` ↔ `GOI_TXT` | Record template, development roadmap, GOI dossiers |
| Main story | `…/ACT MAIN STORY/` | Story Index, full manuscripts, chapters (1–12 + Epilogue, md+txt), Archives, Characters, Narrative, Outlines |
| Handbook | `…/Junior Handbook/` | `ACT_Orientation_Handbook` (md+txt) |
| BOOK | `…/'A History of Anomaly Containment Transformation' BOOK.md` | In-universe history, md-only |
| Reviews | `RESEARCH FOLDER/` | Dated consistency/style reviews + working/provenance notes — read before large edits |

---

## Development Rules

- **GOI development is gated**: one new GOI per owner prompt — never batch-generate GOIs.
- **Dossier files are per-item documents**: individual, un-summarized, detailed, matching the ACT archive style. No compressed or abridged notes in the RESEARCH FOLDER either (extensive `.md` only).
- New content should reference the canonical role names, the ANM code table, and the containment-class list adopted by the 2026-09-07 consistency sweep so the chosen system stays load-bearing.
- Every completed change should be committed and pushed; keep `.md`/`.txt` twins in lockstep.
