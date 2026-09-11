# A.C.T FACILITY ARCHIVE FILE
## GOI RECOVERED DOCUMENT AND INTERCEPT FORMAT DOCTRINE

**Archive Status:** Active  
**Distribution:** Intelligence Division / Archiver Division / Civil Covert / GOI Desk  
**Authority:** Central Archive, Intelligence Division, and External Threat Review  

### Archive Note
This doctrine governs documents that originate from a Group of Interest, appear to originate from a Group of Interest, or imitate a Group of Interest well enough to affect A.C.T operations. It exists so a GOI may speak in its own voice inside the archive without being mistaken for A.C.T's institutional assessment.

A GOI dossier records what A.C.T believes about an organization. A recovered document records what an organization said, printed, hid, sold, sang, worshipped, ordered, forged, performed, or wanted A.C.T to believe. These are different records and must remain different even when they describe the same event.

---

# RECOVERED GOI DOCUMENT FOUNDATION

## 1. Purpose

Groups of Interest do not only act through weapons, markets, rituals, buildings, or anomalous subjects. They act through documents. A flyer can recruit. A price list can move an anomaly. A sermon can prepare a breach. A maintenance message can call a dead system home. A circus poster can hide a cage in plain sight. A corporate instruction can turn illness into product language. A government memo can make an impossible order look lawful.

The Facility therefore treats recovered GOI documents as operational artifacts. They may be harmless paper, dangerous information, social bait, evidence of a route, coded orders, memetic packaging, recruitment tools, legal masks, devotional texts, or fragments of an institution that no longer exists.

This doctrine gives those records a working form.

---

## 2. Separation of Voices

Every recovered GOI document must preserve three voices separately:

### Source Voice
The words, style, claims, formatting, slogans, threats, prayers, prices, jokes, commands, or technical language used by the GOI or suspected GOI.

### A.C.T Handling Voice
The archive note, recovery context, translation notice, hazard warning, redaction rule, containment limitation, and custody chain written by A.C.T personnel.

### Intelligence Assessment Voice
The interpretation of what the recovered document probably means, what remains uncertain, how it changes the GOI file, and what operational action follows.

A recovered document fails if the reader cannot tell whether a statement belongs to the GOI, A.C.T, or later analysis.

---

## 3. Recovered Document Designation

Recovered GOI documents use the following designation structure:

```text
GOI-RD-[GOI NUMBER]-[YEAR]-[SEQUENCE]
```

Examples:

```text
GOI-RD-027-2026-001
GOI-RD-049-2026-003
GOI-RD-051-2026-001
GOI-RD-052-2026-001
```

If the source GOI is unknown, use:

```text
GOI-RD-UNK-[YEAR]-[SEQUENCE]
```

The recovered document designation does not replace the GOI designation. It attaches evidence to the GOI record.

---

## 4. Required Header Fields

Every recovered GOI document record must include:

```text
RECOVERED DOCUMENT ID:
LINKED GOI:
SOURCE NAME OR CLAIMED SOURCE:
DOCUMENT TYPE:
RECOVERY DATE:
RECOVERY LOCATION:
RECOVERING UNIT:
CUSTODY STATUS:
ORIGINAL MEDIUM:
LANGUAGE / SYMBOL SYSTEM:
TRANSLATION STATUS:
INFORMATION HAZARD STATUS:
MEMETIC / COGNITIVE RISK:
PUBLIC EXPOSURE STATUS:
AUTHENTICITY STATUS:
A.C.T HANDLING AUTHORITY:
RELATED ANOMALY FILES:
RELATED GOI FILES:
ARCHIVE DISTRIBUTION:
```

The field **SOURCE NAME OR CLAIMED SOURCE** must remain cautious. A poster signed by a GOI is not proof that the GOI created it. A document may be planted, forged, stolen, translated badly, edited by an anomaly, or designed to make A.C.T classify the wrong enemy.

---

## 5. Document Type Classes

### RD-INT — Intercepted Communication
Messages captured during transmission: radio traffic, letters, encrypted message threads, dead-drop notes, maintenance signals, internal emails, command pings, and courier documents.

### RD-REC — Recovered Physical Document
Paper, books, tickets, posters, labels, prayer cards, catalogues, manuals, invoices, ledgers, surgical forms, or documents recovered from a scene.

### RD-DIG — Recovered Digital Archive
Databases, drives, tablets, corrupted files, executable records, wiki pages, internal indexes, machine logs, or recovered interfaces.

### RD-PUB — Public-Facing Mask
Advertisements, press releases, product labels, fake legal notices, fairground posters, public charity material, corporate brochures, or official-looking public cover documents.

### RD-RIT — Ritual / Devotional Text
Chants, hymns, prayers, vows, liturgy, initiations, curse texts, offering records, dream instructions, or sacramental instructions.

### RD-COM — Commercial / Transaction Record
Price lists, auction sheets, market catalogues, shipping manifests, receipts, ownership transfers, client notes, broker records, and product instructions.

### RD-OPS — Operational Order
Orders, mission briefs, purge instructions, recruitment instructions, route sheets, equipment deployment notes, target lists, or training material.

### RD-PER — Personal GOI-Affiliated Record
Diary, confession, performer writing, employee complaint, field notebook, survivor note, handler journal, or other personal text linked to GOI activity.

### RD-FRG — Fragment / Unstable Record
Partial, damaged, looping, redacted, burned, corrupted, anomalously incomplete, or self-altering records.

---

## 6. Authenticity Status

### AUTHENTIC
Confirmed as produced by the linked GOI or its authorized apparatus.

### PROBABLE
Strong evidence supports GOI origin, but full proof is absent.

### CLAIMED
The document names a GOI, but the origin is not verified.

### FORGED
The document imitates a GOI and is confirmed false.

### CONTESTED
Evidence supports more than one origin or intent.

### ANOMALOUSLY UNSETTLED
The record's origin changes, cannot be fixed, or is affected by anomalous conditions.

### ARCHIVE-ONLY
The document survives only as an A.C.T transcription, witness copy, recovered photograph, or partial reconstruction.

---

## 7. Information Hazard Status

Recovered GOI documents use the same caution as anomaly files. A document may be dangerous because of what it is, what it says, what it makes the reader remember, what it makes the reader want, what system it tries to contact, or what public story it can break.

Status values:

- **CLEAR** - no known information hazard;
- **SENSITIVE** - operationally restricted but not anomalously hazardous;
- **COGNITIVE REVIEW** - may affect thought, attention, dream, memory, identity, or compulsion;
- **MEMETIC RESTRICTED** - may replicate, compel, recruit, or infect through perception or repetition;
- **TECHNICAL QUARANTINE** - digital or machine-readable components may execute, call outward, rewrite, or sync;
- **RITUAL QUARANTINE** - reading, recitation, performance, or copying may complete a ritual effect;
- **SEALED** - no general reproduction authorized.

---

## 8. Recovery Context Block

Every recovered GOI document must include a recovery context before the source text.

Required recovery context:

- who recovered it;
- where it was found;
- whether civilians saw it;
- whether it was intact;
- whether A.C.T moved, copied, photographed, translated, or destroyed the original;
- whether a GOI may know A.C.T has it;
- whether the document affected personnel during handling;
- whether the document is evidence, bait, warning, or unresolved.

This block is written in A.C.T voice.

---

## 9. Source Text Handling

The source text section must preserve the GOI's voice without cleaning it into A.C.T tone. It may include slang, slogans, threats, devotional language, corporate euphemism, market formatting, circus patter, broken translation, machine syntax, field shorthand, or deliberate ugliness.

Rules:

- do not paraphrase when exact wording matters;
- preserve line breaks when they appear meaningful;
- mark illegible portions as `[ ILLEGIBLE ]`;
- mark removed hazardous content as `[ SEALED CONTENT OMITTED ]`;
- mark uncertain translations as `[ APPROXIMATE TRANSLATION ]`;
- do not repair grammar if the broken grammar is evidence;
- do not make a hostile GOI sound like A.C.T unless the document itself is impersonating A.C.T.

---

## 10. A.C.T Commentary Block

After the source text, A.C.T commentary must identify:

- confirmed facts;
- claims made by the document;
- claims unsupported by evidence;
- operational implications;
- GOI behavior shown by the text;
- anomaly connections;
- normalcy risk;
- required follow-up.

Commentary is not allowed to solve every mystery. A good recovered document may create more questions than answers.

---

## 11. GOI-Specific Voice Examples

### Government Anti Anomaly / GAA
Recovered GAA material may resemble lawful memoranda, emergency powers, infrastructure exceptions, classified liaison notes, or jurisdictional language. It usually tries to make impossible events look administratively survivable.

### Anti-Global Anomaly / A-GA
Recovered A-GA material often reads as militant certainty: eradication orders, target lists, anti-containment manifestos, martyr statements, or instructions for destroying anomalies without understanding what they stabilize.

### Anstrall Market
Recovered Anstrall material may be catalogues, broker notes, price tiers, provenance masks, route phrases, and ownership chains. It usually hides danger under value.

### Children of the Deep
Recovered CoTD material may be hymns, tide calendars, initiation fragments, inland-route maps, devotional warnings, or body-of-water metaphors. It should sound patient rather than loud.

### DREAM .INC
Recovered DREAM material may be company emails, medicine instructions, client forms, extraction logs, building memos, or product language. It should hide extraction under wellness and service.

### Liberty Freedoms
Recovered L.F. material may be leaks, recruitment letters, defector testimony, rescue claims, propaganda, or transport instructions. It may contain enough truth to be more dangerous than a lie.

### Mysterious Guild
Recovered Guild material may appear as technical database pages, registry maintenance instructions, surgical logs, weapon specifications, OMEGA platform files, Ghost File markers, or machine-readable leash warnings. It must preserve uncertainty over whether the Guild is a living group, a future archive, or a system calling through evidence.

### Amazoo Circus
Recovered Amazoo material may be posters, tickets, stage directions, performer ledgers, cage labels, chant sheets, diary fragments, route notes, animal-handler records, or ringmaster commands. It must not convert survivor writing into spectacle.

---

## 12. Sample Blank Form

```text
A.C.T FACILITY ARCHIVE FILE
GOI RECOVERED DOCUMENT RECORD

RECOVERED DOCUMENT ID:
LINKED GOI:
SOURCE NAME OR CLAIMED SOURCE:
DOCUMENT TYPE:
RECOVERY DATE:
RECOVERY LOCATION:
RECOVERING UNIT:
CUSTODY STATUS:
ORIGINAL MEDIUM:
LANGUAGE / SYMBOL SYSTEM:
TRANSLATION STATUS:
INFORMATION HAZARD STATUS:
MEMETIC / COGNITIVE RISK:
PUBLIC EXPOSURE STATUS:
AUTHENTICITY STATUS:
A.C.T HANDLING AUTHORITY:
RELATED ANOMALY FILES:
RELATED GOI FILES:
ARCHIVE DISTRIBUTION:

RECOVERY CONTEXT:
[Write A.C.T handling context here.]

SOURCE TEXT / TRANSCRIPTION:
[Preserve GOI voice here.]

A.C.T COMMENTARY:
[Separate confirmed fact, claim, uncertainty, and operational action.]

FOLLOW-UP ORDERS:
[Record actions without resolving unproven conditions.]

FILE METADATA:
FILE CREATED:
FILE LAST UPDATED:
FILE AUTHOR:
REVIEWED BY:
FILE STATUS:
RECORD CONDITION:
```

---

## 13. Storage Rule

Recovered GOI document records may be stored beside the relevant GOI dossier or inside a dedicated recovered-record subfolder when volume grows. The storage decision must preserve three things:

1. the linked GOI designation;
2. the recovered document ID;
3. separation between A.C.T assessment and source voice.

If a recovered document is itself anomalous, the document requires anomaly filing in addition to GOI evidence filing.

---

## 14. Red Lines

A.C.T will not:

- treat a GOI's claim as fact without corroboration;
- erase source voice until only A.C.T language remains;
- publish recruitment material without hazard review;
- connect recovered digital archives to live systems;
- recite ritual documents for completeness;
- force survivors to authenticate abusive material casually;
- use a market catalogue as permission to trade;
- use a government memo as permission to surrender containment authority;
- use a Guild maintenance instruction as permission to contact the Guild;
- use a circus poster as permission to make pain into performance again.

---

## 15. Related Records

- `00_GOI_Record_Template.md`
- `ACT_GOI_Registry_and_External_Threat_Doctrine_Archive.md`
- `ACT_Anomaly_Log_Categories_In_World_Explanation.md`
- `ACT_Complete_Designation_and_Class_Reference.md`
- GOI dossiers in `GOI_MD/`
- Plain-text reading copies in `GOI_TXT/`

---

## File Metadata

```text
FILE CREATED:        12/09/2026
FILE LAST UPDATED:   12/09/2026
FILE AUTHOR:         Intelligence Division / Archiver Division
REVIEWED BY:         External Threat Review / Central Archive
FILE STATUS:         ACTIVE
DOCTRINE STATUS:     ACTIVE
```
