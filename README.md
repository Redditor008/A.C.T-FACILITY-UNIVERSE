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
- **GOIs are not only enemies.** Groups of Interest may be governments, markets, cults, companies, civil networks, rivals, witnesses, allied institutions, or communities outside A.C.T.; live relationship labels are POSITIVE, NEUTRAL, NEGATIVE, and WORK.
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
| Operational forms | `…/Operational Forms/` (both md & txt trees) | Reusable in-world working forms, including witness statement/testimony intake, access/egress ledgers, and amnestic memory-aftercare review |
| Site dossiers | `…/Site Dossier/` (both md & txt trees) | 5 `SITE` + 5 `SUB` comprehensive dossiers |
| Floor dossiers | `…/Site Dossier/Floor Dossier/` (both trees) | 46 individual floor dossiers (SUB-04 has no floors by canon) |
| Legacy anomalies | `…/A.C.T Anomaly Document/Anomaly Legacy 01 .txt/` (+ `Log/`, `STORY/`) and `Anomaly Legacy 01.md/` | Legacy-era files, observation logs, and the Lobotomy Corporation × A.C.T crossover story |
| Modern anomalies | `…/Anomaly Modern txt/` (+ `Log/`) | Modern-era anomaly files and dossiers, character/capability profiles |
| ITHYOS | `…/ITHYOS Document/` (`ITHYOS .md`, `ITHYOS .txt`, `ITHYOS Log`) | ENTITY-000 ITHYOS first-vault records, modern file standard, archive copies, tales |
| GOI | `…/A.C.T GOI Document/GOI_MD` ↔ `GOI_TXT` | Record template, recovered-document format, recovered-record holding folder, development roadmap, 30 dossiers (GAA, A-GA, Anstrall, CoTD, DREAM, L.F., Mysterious Guild, Amazoo Circus, Missing 404 Watch Tower, Lullaby Works, Cairn & Lintel, Saint-Vera Restoration Concern, Bureau of Unquiet Borders, Crown Office of Ash Keys, Grey Harbor Civil Rescue Directorate, Office for Witness Continuance, The Kindly Molt, Choir of the Unforgotten Name, Keepers of the Ninth Reliquary, Last Bell Congregation, Mercy of the Quiet Sun, Archivists of the Final Dawn, Candle-Under Exchange, Velvet Provenance House, Namewright Bazaar, Saint Morrow Passage, Mercy Lock Institute, Iron Meridian Authority, Lantern Accord, Ninefold Ark) |
| Technology records | `…/A.C.T Technology Document/TECH_MD` ↔ `TECH_TXT` | Per-technology controlled records for individual A.C.T, GOI, recovered, containment, medical, field, archival, infrastructure, and abnormal-material systems; currently includes the Technology Record Template, TECH-GOI-049-1 DREAM .INC Dream Nectar Extraction Apparatus, TECH-GOI-049-2 DREAM .INC Dream Nectar Sealed Batch System, TECH-GOI-049-3 DREAM .INC Wish Intake and Confidential Report System, TECH-GOI-049-4 DREAM .INC Twelve-Building Appointment Routing Network, TECH-GOI-049-5 DREAM .INC Quiet Machine Condition Indicator System, TECH-GOI-071-1 Mercy Lock Gentle Lock System, TECH-GOI-071-2 Mercy Lock Patient Bell Distress Signal System, TECH-GOI-071-3 Mercy Lock Consent Ledger and Custody Status System, TECH-GOI-071-4 Mercy Lock Quiet Room Low-Stimulation Care Architecture, TECH-GOI-071-5 Mercy Lock Shielded Ambulance Transfer System, TECH-ACT-001 Reality Stabilization Anchor System, TECH-ACT-002 Anti Reality Mesh System, TECH-ACT-003 Quantum Narrative Buffer System, TECH-ACT-004 004-Series Amnestic Compound System, TECH-ACT-005 Causal Static Generator System, TECH-ACT-006 Facility Converted Aircraft System, TECH-ACT-007 Static-Pulse Crystal, TECH-ACT-008 Causal Anchor Nails, TECH-ACT-009 Chrono-Stuttered Visors, TECH-ACT-010 Digital Resonance Sensors, TECH-ACT-011 Narrative Seal Varnish, TECH-ACT-012 Banalist White-Noise Broadcast, TECH-ACT-013 Magnetic Torsion Restraints, TECH-ACT-014 Tactical Feedbacker Arm, TECH-ACT-015 Static Pulse Biometric ID, TECH-ACT-016 Causal Tethering Cables, TECH-ACT-017 Vacuum Isolation Spheres, TECH-ACT-018 Non-Euclidean Compass, TECH-ACT-019 Cryo-Seismic Stabilizers, TECH-ACT-020 Regression-Resistant Ink, TECH-ACT-021 Spectral Vibration Sensors, TECH-ACT-022 Synthetic Sanguine-Fuel, TECH-ACT-023 Genetic Perfection Protocol, TECH-ACT-024 Pale Wood Scalpel, TECH-ACT-025 Thermal-Lure Beacon, TECH-ACT-026 Biometric Resonance Dampeners, TECH-ACT-027 Gold-Tipped Mining Drills, TECH-ACT-028 Neural Lacing Type 004-MOD, TECH-ACT-029 Cryogenic Biological Isolation Units, TECH-ACT-030 Soul-Stasis Harness, TECH-ACT-031 Adrenaline Micro-Surge Detectors, TECH-ACT-032 HPP Resonance Scanners, TECH-ACT-033 Abyssal Masonry, TECH-ACT-034 Abyssal Anchor Plating, TECH-ACT-035 Phase-Shifted Containment Glass, TECH-ACT-036 Ectothermic Regeneration Gel, TECH-ACT-037 Sub-Abyssal Sonar, TECH-ACT-038 Causal Static Earpieces, TECH-ACT-039 High-Density Liquid Lead, TECH-ACT-040 Vesper-Pattern Tactical AI, TECH-ACT-041 Harvested Pale Wood, TECH-ACT-042 Refined Steel-Dirt, TECH-ACT-043 Galaxy-Motive Textile, TECH-ACT-044 Causal-Reactive Mercury, TECH-ACT-045 Refined NEMNOLIA Sap, TECH-ACT-046 Sanguine-Conductive Alloy, TECH-ACT-047 Phase-Stable Silicone, TECH-ACT-048 Red-River Acid (Stabilized), TECH-ACT-049 Abyssal Basalt, TECH-ACT-050 Digital Resonance Mapping Suite, TECH-ACT-051 Steam-Drill Excavator, TECH-ACT-052 High-Density Lead Vaulting, TECH-ACT-053 Clockwork Causal Anchors, TECH-ACT-054 Reinforced Iron Caging, TECH-ACT-055 Silent Boundary System, TECH-ACT-056 Memetic Filtering Infrastructure, TECH-ACT-057 Anomalous Intake Screening Suites, TECH-ACT-058 F-1 Closure System, TECH-ACT-059 Document Quarantine Cells, TECH-ACT-060 Artifact-Influence Isolation Suites, TECH-ACT-061 Suspended Vault Mounting System, TECH-ACT-062 QNB-Hardened Archive Structure, TECH-ACT-063 Memetic Contamination Treatment Suites, TECH-ACT-064 Water-Capable Containment Chambers, TECH-ACT-065 Pressure-Rated Environmental Transition System, TECH-ACT-066 Maritime Platform Containment Infrastructure, TECH-ACT-067 Deep-Earth Sensor Arrays, TECH-ACT-068 Sensor Nexus Signal Processing Architecture, TECH-ACT-069 Abyss-Linked Observation Recording System, TECH-ACT-070 Deep Monitoring Processing Center, TECH-ACT-071 Seismic Records Vaults, TECH-ACT-072 Restricted Records Vaults, TECH-ACT-073 Marine Biology Laboratory Suites, TECH-ACT-074 Deep-Earth Sample Analysis Laboratories, TECH-ACT-075 Sonar Void Research Program Infrastructure, TECH-ACT-076 Command Communications Nexus, TECH-ACT-077 Internal Logistics Coordination Center, TECH-ACT-078 Seismic Preparedness Shelter and Response System, TECH-ACT-079 Surface Cover Research Campus, TECH-ACT-080 Concealed Transition Access Architecture, TECH-ACT-081 Maritime Separation Port Operations System, TECH-ACT-082 Emergency Intake and Secure Storage System, TECH-ACT-083 Coastal Watch Coordination Center, TECH-ACT-084 Volcanic-Seismic Monitoring Suites, TECH-ACT-085 Recovery Support Staging Area, TECH-ACT-086 Natural Cover Research Station System, TECH-ACT-087 Shared-Instrument Observation Network, TECH-ACT-088 Short-Term Holding Vault System, TECH-ACT-089 Witness Processing and Sanitation Suites, TECH-ACT-090 Archive Relay Buffering Area, TECH-ACT-091 Intake Staging and Routing System, TECH-ACT-092 Agricultural Biotech Cover Campus, TECH-ACT-093 Low-Visibility Processing Logistics System, TECH-ACT-094 Interim Cryogenic Holding System, TECH-ACT-095 Quarantine Assessment and Medical Staging Suites, TECH-ACT-096 Arctic Cold-Storage Cover and Silent Movement System, TECH-ACT-097 Minor Memetic Quarantine Vault System, TECH-ACT-098 Controlled Reading and Redaction Workroom System, TECH-ACT-099 Document Preservation Studio Cover System, TECH-ACT-100 Native Containment Field System, TECH-ACT-101 Concealed Perimeter Sector Network, TECH-ACT-102 Hollow Canopy Field Station and Remote Monitoring System, TECH-ACT-103 Interior Biological Habitat Chamber System, TECH-ACT-104 Biological Analysis and Sample Control Laboratories, TECH-ACT-105 Deep Cultivation Vault System, TECH-ACT-106 Reserve Command and Operations Coordination System, TECH-ACT-107 Personnel Processing and Reserve Clearance System, TECH-ACT-108 Surface Research Campus Cover Integration System, TECH-ACT-109 Maritime Holding Intake and Transfer System, TECH-ACT-110 Climate-Controlled Island Holding Unit System, TECH-ACT-111 Seismic Data Interpretation and Restriction Enforcement System, TECH-ACT-112 Island Personnel Habitation and Sustainment System, TECH-ACT-113 Relay Command Floor Status and Decision System, TECH-ACT-114 Surface Transition and Maritime Cover Gateway System, TECH-ACT-115 Archive Boundary Personnel Clearance System, TECH-ACT-116 Operational Archive Training and Doctrine Preparation System, TECH-ACT-117 Public Archive Absolute Separation and Immediate Transfer System, TECH-ACT-118 Symbol Behavior Controlled Observation Suites, TECH-ACT-119 Media Propagation Tracking Center System, TECH-ACT-120 Redaction Release Authorization and Filtering Record System, TECH-ACT-121 Unread Archive Anti-Reading Preservation Vault System, TECH-ACT-122 Blind Box and Eye Box Perception-Control Vault System, TECH-ACT-123 Signal-Isolated Anomalous Document Storage System, TECH-ACT-124 Standard Box Holding Chamber System, TECH-ACT-125 Ascending Authorization Transformation Staging Lock System, TECH-ACT-126 Controlled Study Environment and Research Sample-Custody System, TECH-ACT-127 Medical Isolation and Cognitive Recovery Ward System, TECH-ACT-128 QNB-Hardened Repository and Record Retrieval System, TECH-ACT-129 Vertical-Flow Personnel Processing and Clearance Verification System, TECH-ACT-130 Unmarked Wall Surface Boundary and Loading Transition System, TECH-ACT-131 Seasonal Arctic Research Cover and Transition Control System, TECH-ACT-132 Long-Rotation Habitation and Main Security Checkpoint System, TECH-ACT-133 Long-Term Biological Observation and Cold-Suppressed Study System, TECH-ACT-134 Biological Suppression Chamber and Climate-Controlled Deep-Isolation Holding System, TECH-ACT-135 Failure-Tolerant Entropic Holding and Self-Repairing Environment System, and TECH-ACT-136 Long Sleep Vault and F-1 Closure Containment System |
| Main story | `…/ACT MAIN STORY/` | Continuity Policy, Story Index, full manuscripts, chapters (1–12 + Epilogue, md+txt), Archives, Characters, Narrative, Outlines |
| Handbook | `…/Junior Handbook/` | `ACT_Orientation_Handbook` (md+txt) |
| BOOK | `…/'A History of Anomaly Containment Transformation' BOOK.md` | In-universe history, md-only |
| Reviews | `RESEARCH FOLDER/` | Dated consistency/style reviews + working/provenance notes — read before large edits |

---

## Development Rules

- **GOI development is gated**: create only approved GOIs; never batch-generate unapproved scaffold entries or scan results.
- **Dossier files are per-item documents**: individual, un-summarized, detailed, matching the ACT archive style. No compressed or abridged notes in the RESEARCH FOLDER either (extensive `.md` only).
- **Technology records are per-system documents**: the master technology index stays broad, while `A.C.T Technology Document` holds extended individual records with custody, function, limits, failure history, and cross-reference control.
- New content should reference the canonical role names, the ANM code table, and the containment-class list adopted by the 2026-09-07 consistency sweep so the chosen system stays load-bearing.
- Every completed change should be committed and pushed; keep `.md`/`.txt` twins in lockstep.
