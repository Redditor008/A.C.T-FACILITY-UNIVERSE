# A.C.T FACILITY ARCHIVE FILE
## Complete Designation and Class Reference

**Archive Status:** Active Reference Standard
**Distribution:** Internal / Archive / Classification Review / Training / All Divisions
**Authority:** Archive Administration and Classification Review, with Central Archive custody

### Archive Note
This file is the consolidated meaning reference for every designation, code, marker, and class used on A.C.T records. Until this file was opened, the same code could be read differently by an Archiver, a Field Operator, a Site Director, and a Transformation specialist, because its definition lived in a different supporting file each time. This reference ends that condition.

The file explains, in full, every entry that appears in an anomaly file, a GOI record, or a Site record:

- what each designation structure means, segment by segment;
- what every code stands for;
- what every class, category, state, and marker means;
- when each is assigned;
- how to read a real designation;
- and what each must not be confused with.

Meanings are recorded as the archive understands them. Where a source file lists a code without expanding its meaning, this reference records the standard archival interpretation so that no code is ever left as a bare label. Entries are written one code per section. Codes are explained, never merely listed.

### How Entries Are Read
Every code entry in this file follows the same shape:

- **The code** and the full words it abbreviates.
- **Meaning** — what the code actually records.
- **Assigned when** — the condition that earns the code.
- **Reading example** — a real or rule-built designation showing the code in use.
- **Do not confuse with** — the mistakes that have actually been made in the archive.

### Source Doctrine
This reference consolidates definitions preserved in the following source records, and where those records list a value without expansion, the working interpretation is stated openly in the entry itself:

- ACT_Anomaly_Classification_Manual_Archive (with Part Three)
- ACT_Internal_Structure_and_Reality_Doctrine_Archive (with Part Two)
- ACT_Anomaly_Standard_Format and ACT_Anomaly_RCT_Format
- ACT_Anomaly_Log_Categories_In_World_Explanation
- ACT_GOI_Registry_and_External_Threat_Doctrine_Archive (with Part Four)
- ACT_Site_Registry_File_Standard, ACT_Site_Doctrine_and_Installation_Structure, ACT_Global_Site_Registry

---

# PART I — ANOMALY FILE DESIGNATIONS AND CLASSES

This Part explains the designation and classification system that appears on every modern anomaly file. It is organized in the same order the fields appear on the Standard Format file: designation first, then registry band, field type, fracture logic, containment class, threat level, transformation viability, lifecycle state, clearance, hazard tags, and finally the operational fields (structure class, breach state, restrictions, redaction, and record state).

---

## I-1 Designation Anatomy — Reading an Anomaly Designation

An A.C.T anomaly designation is a compressed statement. Read from right to left, it tells the reader three things in order: **which registry entry this is** (the number), **what kind of anomaly it is** (the type code), and **how much of the record is settled** (the record prefix). The designation never describes danger by itself; danger is carried by the Containment Class and Threat Level fields beside it.

Three primary designation structures exist:

- `UFD-XX-###` — provisional record
- `AFD-XX-###` — verified record
- `ANM-XX-XX-####` — fracture-state record

In `UFD` and `AFD` forms:

- the first **XX** is the **field type code** (see I-2);
- the **###** is the **numerical registry code**, written with three digits.

In `ANM` form:

- the first **XX** is the **Fracture Containment Index** code (see I-3);
- the second **XX** is the **Fracture Sub-Threat Index** code;
- the **####** is the numerical registry code, written with four digits because fracture records share the registry with the older numbered series and require room for separate enumeration.

### UFD — Unknown Field Designation

**Meaning.** UFD is the provisional label. It records that something is **suspected** of being anomalous but has not yet been fully confirmed or stabilized in archive logic. The file exists because the object, subject, place, or phenomenon cannot be safely ignored; the file is provisional because A.C.T has not yet decided what it is dealing with.

**Assigned when.** Detection has occurred, anomalous status is suspected, and verification is still in progress. A UFD file may be opened on a civilian report, a sensor trace, an intelligence channel, an A.C.T patrol find, or an anomaly-triggered event before any stable description exists.

**Reading example.** `UFD-NB-004` — The Forgetting Bloom was first archived under this provisional designation while its biological and memetic behavior was still being separated. The same anomaly appears later in the register under its verified designation (see below), which is the normal life cycle of a record.

**Do not confuse with.** AFD. UFD is not a lower-value class; it is an earlier stage of the same record. Verification does not "promote" an anomaly, it settles the record. Nor is UFD a field type code: the type code follows the dash.

### AFD — Anomaly Field Designation

**Meaning.** AFD is the permanent label. It records that the anomaly has been **formally verified** and entered into the permanent A.C.T archive structure: detected, confirmed as anomalous, classified, and given a stable file identity.

**Assigned when.** Verification is complete and the anomaly is operationally logged. From this point the record carries the full Standard Format body — description, anomalous properties, containment procedures, research summary, transformation status, incident summary, and metadata.

**Reading example.** `AFD-NB-004` — the verified permanent record of The Forgetting Bloom after its UFD stage closed. `AFD-CH-000` — ITHYOS, The World-Sleeper, the first modern-era file written for the entity that was originally preserved as ENTITY-000. `AFD-SU-012` — Grumblesail, the Annoyingly Indestructible Lizard, a verified subject-type anomaly. `AFD-OB-502` — Ball of Knife, a verified object-type anomaly.

**Do not confuse with.** UFD (see above), ENTITY numbers (historical series, see below), or ANM. An AFD record describes an anomaly in settled archive terms; an ANM record exists because the anomaly broke those terms.

### ENTITY-### — Historical Vault Designation

**Meaning.** The oldest designation series in the archive, used **before** the formal anomaly system existed. In that era the impossible was recorded in survival documents as `ENTITY` files: no standardized field type, containment class, threat level, or transformation viability was attached. An ENTITY number means the file belongs to the first-vault era of A.C.T archive history.

**Assigned when.** The record predates the Anomaly Era transition. No new ENTITY files are opened; modern records use UFD/AFD/ANM. Existing ENTITY records may be re-filed under the modern system when their subject is re-documented (see the AFD-CH-000 example above), while the historical file is preserved.

**Reading example.** `ENTITY-000` — the first preserved vault record, the Slumbering Serpent God / ITHYOS, The World-Sleeper. **Naming note:** the historical designation is written `ENTITY-000`; sealed file titles use the underscore form `ENTITY_000_ITHYOS`.

**Do not confuse with.** Registry numbers. ENTITY numbers do not share the modern ### registry; they are a closed historical series.

### Reserved Registry Numbers — 000 and Foundational Significance

**Meaning.** Some numbers carry structural meaning. The number **000** is treated as a designation of **foundational or origin-level significance** and is never assigned casually. Its use marks the subject as load-bearing in A.C.T history.

**Reading example.** `ENTITY-000` (the first vault record) and `AFD-CH-000` (ITHYOS re-filed as the first modern sample entry) both carry 000 because the subject is origin-level, not because it is the "zeroth" anomaly found.

**Do not confuse with.** Anomalies whose registry number happens to contain zeros. Ordinary three- and four-digit registry codes are assigned in sequence; only 000 carries the reserved significance.

## I-1A Registry Band Doctrine

Registry Band Doctrine defines how A.C.T reads anomaly numbers across historical, provisional, verified, and fracture-state records. It exists because a number is not only an index; in some ranges it also records archive age, intake history, and protected significance.

### ENTITY Historical Band

**Range.** `ENTITY-###`, closed historical series.

**Meaning.** ENTITY numbers belong to the First Vault and pre-standard archive era. They are preserved as historical designations even when the same subject later receives a modern UFD, AFD, or ANM record.

**Rule.** No new ENTITY file is opened under ordinary modern doctrine. A modern file may cross-reference an ENTITY record, but it must not overwrite it.

### 000 Foundational Reserve

**Range.** `000` in modern UFD/AFD registry use, and `ENTITY-000` in the historical series.

**Meaning.** The number marks origin-level or foundation-level significance. It is not a normal first entry and is not assigned for sequence convenience.

**Rule.** Any new use of `000` requires O5-level or equivalent sealed archive authority. ITHYOS is the controlling example.

### LEGACY ACCEPTED Band

**Range.** `001–120` in UFD/AFD-style three-digit anomaly records.

**Meaning.** This band is accepted for legacy-era anomalies that predate, strain, or were later re-housed inside modern doctrine. Records in this band may preserve older tone, older intake history, and UFD-to-AFD traces without being treated as format errors.

**Rule.** A legacy anomaly may have both a UFD and an AFD record when the UFD preserves the provisional intake state and the AFD preserves the verified state. These are **distinct archive records, not duplicate copies**.

**Reading example.** `UFD-NB-004` and `AFD-NB-004` describe different archive states of The Forgetting Bloom rather than accidental duplicate numbering.

### Modern Registry Band

**Range.** `121–999` in standard UFD/AFD three-digit anomaly records.

**Meaning.** This is the ordinary modern registry range for verified and provisional anomalies after the legacy accepted range.

**Rule.** A modern UFD may become an AFD after verification, but the designation history must preserve the intake path. If the UFD file contains evidence that must remain historically readable, it should be archived rather than erased.

### ANM Fracture-State Band

**Range.** `ANM-XX-XX-0001` through `ANM-XX-XX-9999`, with `XXXX` reserved for unresolved or deliberately obscured numbering.

**Meaning.** ANM records use four digits because fracture-state files require their own enumeration and may describe anomalies that break ordinary registry assumptions.

**Rule.** ANM is not a stronger AFD. It is a different record logic used when standard archive categories fail, fracture, loop, rewrite, or become unsafe.

### Obscured, Reserved, and Closed Numbers

**Obscured numbers** may appear as `XXXX`, `[Question]`, or equivalent redacted forms when the number itself is not declassified or cannot be stabilized. **Reserved numbers** are held for structural, story, or archive-governance reasons. **Closed numbers** are numbers retired from new assignment because the previous record remains historically load-bearing.

No registry number should be reused merely because an anomaly is neutralized, lost, explained, transformed, or archived. The archive preserves the wound even when the wound stops moving.

---

## I-2 Field Type Codes

The field type code is the first `XX` segment of a UFD or AFD designation. It answers one question: **in what category of existence does this anomaly live?** It is the first layer of operational understanding and is assigned before full study is complete. Modern files sometimes show a second, nuanced type line under the main field (for example a file whose main type is OB but whose behavior carries a ?.H note); the main field remains the filing category.

### OB — Object

**Meaning.** The anomaly is a **thing**: an item, device, artifact, sample, tool, or material object with anomalous properties. Object-type anomalies are the most common filings and are usually, but not always, the most containable.

**Assigned when.** The anomaly is a discrete non-living thing, or behaves as one for filing purposes, regardless of origin or apparent age.

**Reading example.** `AFD-OB-502` Ball of Knife — an object-type hazard. `AFD-OB-142` Book of Hero; `AFD-OB-312` AFS-312 Anti Force Shock.

**Do not confuse with.** Box Class (I-8), which describes the *structure* used to hold an object; and with Subject, when an object displays sentience or agency strong enough to reclassify it.

### SU — Subject

**Meaning.** The anomaly is a **living or sentient being**: a creature, entity, person, organism, or presence that acts, reacts, or is treated as an individual. Subject-type records place the anomaly's behavior and welfare at the center of the file.

**Assigned when.** The anomaly is alive, self-moving, self-aware, or entity-like enough that containment must account for its behavior, care, and responses.

**Reading example.** `AFD-SU-012` Grumblesail — a subject-type anomaly (the indestructible lizard). `AFD-SU-855` Argon Internal AI; `AFD-SU-572` Kazumi Mori profile filing; `AFD-SU-714` Mogi-At.

**Do not confuse with.** Field type is about the anomaly's category of existence; Containment Class is about its relationship to containment. A subject can be INERT; an object can be REACTIVE.

### PL — Place

**Meaning.** The anomaly is a **location**: a site, building, zone, room, territory, route, or area that is itself anomalous. Place-type anomalies may distort the space they occupy or exist only under certain conditions.

**Assigned when.** The anomalous condition is bound to a location rather than to a movable thing or being, and containment must therefore operate on the place.

**Reading example.** `AFD-PL-932` Dark World Door — a place-type anomaly with its own expedition and reactivity dossiers. `AFD-PL-384` Haunting Terror.

**Do not confuse with.** SP. Place is a location with a fixed identity; Space anomalies (below) attack spatial logic itself. A place-type file may still require Exploration & Survey dossiers (Part IV, Category V) when teams enter it.

### TI — Time

**Meaning.** The anomaly involves **time**: temporal distortion, loops, resets, acceleration, deceleration, aging effects, or interference with the order of events. Time-type records treat chronology itself as the hazardous medium.

**Assigned when.** The anomaly measurably alters, repeats, stops, reverses, or rewrites time, or produces effects that only make sense if time has moved incorrectly.

**Reading example.** `AFD-TI-003` THE CLOCK SAYS DAWN — a time-type anomaly with an Incident & Breach dossier. `AFD-TI-560` Stop-Watch.

**Do not confuse with.** The Cosmic Timer doctrine (the hidden cycle behind Minor Pauses) is reality theory, not a field type; TI is assigned to anomalies whose *own* effect is temporal.

### SP — Space

**Meaning.** The anomaly involves **space itself**: impossible interiors, non-Euclidean geometry, folding, wormhole behavior, infinite or contradictory dimensions, or places where distance and direction stop obeying the map.

**Assigned when.** Spatial law is locally broken in a way that is not simply "a strange place" but a condition where space cannot be trusted to behave as space.

**Reading example.** `AFD-SP-890` Infinity Train — a space-type anomaly with survey and E-Class recording dossiers attached.

**Do not confuse with.** PL. The cleanest distinction in the archive: PL means the place is the anomaly; SP means space is the anomaly. A door that is a wound in space may be filed PL with SP behavior noted, but the main field follows the dominant condition.

### ME — Memetic

**Meaning.** The anomaly is a **memetic hazard**: information, image, symbol, pattern, phrase, or idea that is itself dangerous to perceive, remember, or transmit. The threat is carried by the medium of meaning.

**Assigned when.** Exposure to the anomaly's form of information — sight, sound, text, pattern — produces the anomalous effect, and the effect can propagate through ordinary communication.

**Reading example.** `AFD-ME-018` Dread EYE — a memetic-type anomaly whose observation restrictions are the containment. Files of this type are among the most likely to carry redaction markers (I-12).

**Do not confuse with.** IH. Both live in information, and the boundary is strict: memetic hazard spreads through *meaning and perception* (see it, copy it, remember it); info hazard is dangerous in *information itself* (below).

### IH — Info Hazard

**Meaning.** The anomaly is an **information hazard**: a fact, datum, name, location, formula, or piece of knowledge that is dangerous to know regardless of the medium carrying it. The danger is in the content, not in the pattern of perception.

**Assigned when.** Knowing the information is itself the risk — the knowledge destabilizes, summons, empowers, or damages — independent of how it is delivered.

**Reading example.** `AFD-IH-721` DONT DENIED — an information-hazard type filing. Files of this type are held under the strictest document-suppression rules and frequently carry `[ INFO-HAZARD ]` or `[ Level 4-5 Lock ]` markers.

**Do not confuse with.** ME (see above) and with the redaction markers `[ MEMETIC ]` and `[ INFO-HAZARD ]`, which tell the reader which suppression regime a document sits under — the marker is not the field type.

### CH — Cosmic Hazard

**Meaning.** The anomaly operates on a **cosmic scale or origin**: it is connected to the structure of reality itself — the Minor Pause, the Cosmic Timer, Structural Reality, Void Collapse, Reality Reset — or it is simply too large, old, or fundamental to be treated as a local phenomenon.

**Assigned when.** The anomaly's origin or stakes are cosmological: it threatens or is part of the hidden machinery of existence, or its scale exceeds every other category.

**Reading example.** `AFD-CH-000` ITHYOS, The World-Sleeper — the first modern cosmic-hazard file. `AFD-CH-647` Jormungandr; `AFD-CH-703` Nyxara, Goddess of NIGHT (a TIAMAT-class cosmic filing at Threat Level 10); `AFD-CH-016` Apocalypses-NOT.

**Do not confuse with.** Threat Level. CH is an origin/scale category; a cosmic hazard can still be low-threat while contained, and a high threat is not automatically cosmic.

### NB — Non-Natural Bio Hazard

**Meaning.** The anomaly is **biological but not natural**: a life form, organism, pathogen, tissue, or biological process that violates natural biology. NB covers creatures that should not exist, biology that should not work, and contagions that do not follow ordinary rules of life.

**Assigned when.** The anomaly is organic, quasi-organic, or infectious and cannot be explained by natural biology.

**Reading example.** `AFD-NB-964` Death Angler; `AFD-NB-325` Crystal Butterfly; `AFD-NB-004` The Forgetting Bloom (its memetic-adjacent behavior notwithstanding, its filing category is biological). `AFD-NB-007` RED HOUND.

**Do not confuse with.** SU. A non-natural bio hazard that is also sentient is still filed NB when its biology is the dominant anomaly; sentience is then handled inside the file and in Behavioral & Observation dossiers (Part IV, Category VIII).

### ?.H — Shifting Hazard

**Meaning.** The reserved designation for anomalies that **resist stable categorization**. A shifting hazard may change between object and subject, place and space, memetic and cosmic, or otherwise alter its ontological status depending on observation, time, ritual state, or unknown triggers.

**Assigned when.** The anomaly has demonstrated that no single field type can be trusted to describe it, or that the act of categorizing it is itself inaccurate, incomplete, or dangerous.

**Handling principle.** A shifting hazard is treated with extreme caution because the act of categorization itself may be inaccurate, incomplete, or dangerous. Files on ?.H anomalies must note all observed form shifts, categorization failures, and any conditions under which the anomaly changed its ontological status.

**Reading example.** No live modern designation carries a primary `?.H` segment in the open register; the code appears as the reserved type in the Standard Format and RCT templates and as a secondary annotation on files whose behavior shifts (for example, object-type filings annotated with a `?.H` behavioral note).

**Do not confuse with.** ANM fracture designations (I-3). ANM describes anomalies whose *documentation* must use fracture logic; ?.H describes anomalies whose *category of existence* shifts. A ?.H anomaly may or may not require fracture filing.

---

## I-3 Fracture Designation and the Fracture Index Codes

### The ANM Format

**Meaning.** `ANM-XX-XX-####` is the designation used when **standard archive assumptions become structurally insufficient**. Not every anomaly threatens containment in a straightforward way; some distort the very logic used to describe, contain, or assess them. For those cases the record prefix is **ANM** and the two letter segments come from the Fracture Index rather than from the field type list.

**Assigned when.** An anomaly's documentation cannot honestly be kept in ordinary UFD/AFD terms — when describing it as "contained" or "a threat" or "an object" would require the file to lie about what is happening.

**Reading example.** `ANM-QU-AS-0003` At-the-end-of-the-day — QUESTIONED containment, ABSENT sub-threat, registry 0003. `ANM-UA-AS-0001` The Unwritten Return — UNAUTHORED containment, ABSENT sub-threat. A constructed example from the source doctrine: `ANM-AB-HM-0002` is read as **ABSURD** containment, **HARMLESS** sub-threat, registry number 0002.

**Do not confuse with.** AFD/UFD. ANM is not a "more dangerous" prefix; it is a *different filing logic*. An AFD record assumes archive terms hold; an ANM record exists because they do not.

### Fracture Index — Containment Codes
The first letter pair of an ANM designation abbreviates the **Fracture Containment Index**, which describes what containment has actually become for this anomaly.

### QU — QUESTIONED

**Meaning.** *Did we even put it in the box — it's so passive you wonder if containment ever happened.* The anomaly is so unresponsive that A.C.T cannot confirm its containment is doing anything; the question is whether containment exists or is theater.

**Reading example.** `ANM-QU-AS-0003`.

### AB — ABSURD

**Meaning.** *How the hell is it in the box — it shouldn't fit, shouldn't stay, but somehow it does.* The anomaly violates every expectation about how it is being held, yet remains held; containment works while making no sense.

**Reading example.** Constructed: `ANM-AB-HM-0002`.

### MU — MUTATED

**Meaning.** *The box grew legs — containment itself became the anomaly.* The containment system has changed into something anomalous; the cage is now part of the problem.

### UA — UNAUTHORED

**Meaning.** *Who wrote this — the documentation is wrong, the procedure is wrong, something is rewriting the rules.* The file, procedure, or record chain cannot be trusted; something is altering the documentation of the anomaly.

**Reading example.** `ANM-UA-AS-0001` The Unwritten Return.

### SC — SCHRÖDINGER

**Meaning.** *It's in the box, but not in the box — simultaneously contained and not contained, and observation determines which.* The anomaly holds both states at once, and the act of looking fixes one of them.

### Fracture Index — Sub-Threat Codes
The second letter pair of an ANM designation abbreviates the **Fracture Sub-Threat Index**, which describes what the threat has actually done or failed to do.

### HM — HARMLESS

**Meaning.** *Did it even hurt anybody — no damage, no effect, no consequence to anyone.* The threat side of the file is empty; nothing has ever been harmed.

### BE — BENEFICIAL

**Meaning.** *It healed someone — the anomaly actively improves or repairs, not harms.* The anomaly's effect is restorative, which fractures every ordinary threat assumption in the file.

### RV — REVERTED

**Meaning.** *Somehow it reverted back — the damage undoes itself, as if the threat never happened.* Harm occurs and then reverses, so the file cannot record a stable consequence.

### AS — ABSENT

**Meaning.** *Where's the threat — the danger exists on paper but nowhere in reality.* The threat is documented but has never appeared; the danger is theoretical, historical, or fictional.

**Reading example.** `ANM-QU-AS-0003` and `ANM-UA-AS-0001`.

### NU — NULLIFIED

**Meaning.** *It stopped — whatever it was doing, it ceased entirely on its own.* The anomalous activity ended without A.C.T intervention, leaving a file without an active subject.

**Closing principle.** The Fracture Index exists so the Facility does not lie to itself when standard categories no longer describe the anomaly honestly.


---

## I-4 Containment Class

**What the field measures.** A.C.T's containment classes do not merely describe danger — they describe **the relationship between the anomaly and the act of containment itself**. Two anomalies of identical danger may carry different classes because one fights its box and one ignores it. The class tells the reader what containment is *up against*.

The recognized class list appears in full on the Standard Format template: **INERT / RESIDUAL / SPORADIC / UNDISCLOSED / ENTROPIC / REACTIVE / EXIGENT / INVERTED / UNENCLOSABLE / INTANGIBLE / TIAMAT / [BLANK]**. Each class below carries its defining line (the class in one sentence, as the archive says it) followed by its full meaning.

### INERT

**Defining line.** *Will not leave the box, even if it can.*

**Meaning.** The anomaly remains stable and passive under confinement and poses little active resistance. It may possess the capacity to act but does not act against its containment. INERT records the least demanding containment relationship.

**Reading example.** `AFD-OB-001` I-AM-A-Test (Threat 0); `AFD-OB-492` Infinite Water Jug (Threat 0) — inert objects that simply stay where they are placed.

**Do not confuse with.** Harmless or low threat. An INERT anomaly may still be profoundly dangerous if released or touched; INERT describes its behavior toward its box, not its power.

### RESIDUAL

**Defining line.** *Scratches the walls, nothing more.*

**Meaning.** The anomaly exerts minor interference with containment but rarely escalates beyond manageable disruption. It tests the box in small ways — noise, movement, low-level effect — without mounting a real escape attempt.

**Reading example.** `AFD-NB-004` The Forgetting Bloom (Threat 3), whose residual activity stays within manageable bounds under procedure.

### SPORADIC

**Defining line.** *Rarely breaks out, nothing unpredictable.*

**Meaning.** Containment failure is uncommon and follows recognizable patterns. When the anomaly does test or leave containment, the conditions are repeatable enough to schedule against; the file can predict when to watch.

**Reading example.** `AFD-SU-012` Grumblesail (Threat 1); `AFD-SU-011` Dream Eater / THEMESY (Threat 1).

### UNDISCLOSED

**Defining line.** *Leaves by unknown means, returns by known ones.*

**Meaning.** A deeply unsettling class in which exit conditions remain unexplained, even if recontainment patterns have been observed. The anomaly demonstrably leaves — and demonstrably comes back — but A.C.T cannot explain the leaving. Records of this class carry permanent uncertainty about the mechanism of departure.

**Reading example.** `AFD-SU-019` Helping Hand (Threat 1); `AFD-PL-384` Haunting Terror (Threat 3); `AFD-SU-015` Hunting Deer (Threat 4).

**Do not confuse with.** Undisclosed *information*. The class name records a known condition (undisclosed means of exit), not a decision to withhold data — though files of this class are often restricted for other reasons.

### ENTROPIC

**Defining line.** *Containment decays around it without maintenance.*

**Meaning.** The anomaly degrades systems, order, or structural consistency simply by existing. It does not attack its box; it corrodes the box, the building, the procedure, and the reality around it. ENTROPIC anomalies require constant maintenance because everything built to hold them quietly falls apart.

**Reading example.** No open modern file carries ENTROPIC in the public register at the time of this writing, but the class is canonical and named in the Site 01 and Site 02 holding doctrine, where ENTROPIC and EXIGENT object-class anomalies are routed to deep holding levels precisely because they consume structure.

**Do not confuse with.** Threat Level. An ENTROPIC anomaly may be slow; its danger is that it wins by waiting.

### REACTIVE

**Defining line.** *Containment fails the moment you look away.*

**Meaning.** The anomaly requires active monitoring and rapid procedural enforcement. Its compliance is conditional on continuous attention; the instant supervision lapses, containment begins to fail. REACTIVE is the most commonly assigned class in the open register.

**Reading example.** `AFD-SU-714` Mogi-At (Threat 1); `AFD-OB-021` The Ledger of the Thrones of Men (Threat 1); `AFD-SU-855` Argon Internal AI (Threat 2) — a spread of threat levels that shows REACTIVE describes monitoring demand, not danger.

**Do not confuse with.** EXIGENT. REACTIVE fails when you look away; EXIGENT demands full-time operation even while you watch (below).

### EXIGENT

**Defining line.** *Containment is a full-time 24/7 operation.*

**Meaning.** The anomaly demands constant labor, resources, surveillance, and intervention. Where a REACTIVE anomaly is stable under watch, an EXIGENT anomaly consumes the watch itself — staffing rotations, material upkeep, procedure enforcement, and intervention drills are never off.

**Reading example.** `AFD-OB-502` Ball of Knife (Threat 4); `AFD-PL-932` Dark World Door (Threat 4); `AFD-NB-007` RED HOUND (Threat 4).

**Do not confuse with.** REACTIVE (above). The distinction is workload: REACTIVE needs your eyes; EXIGENT needs your whole operation.

### INVERTED

**Defining line.** *It contains — does not merely need containing.*

**Meaning.** The anomaly itself is acting as a vessel, seal, barrier, or prison for something else. The relationship has flipped: instead of A.C.T containing the anomaly, the anomaly is doing containing work — and the file must account for what would be released if the anomaly failed or was removed.

**Reading example.** No open modern file carries INVERTED in the public register at the time of this writing; the class is canonical and its logic governs files whose subject holds something worse inside it.

**Do not confuse with.** INERT. INVERTED is not "passive"; it is *load-bearing*. An INVERTED anomaly may be highly active — as a seal.

### UNENCLOSABLE

**Defining line.** *Too vast to enclose.*

**Meaning.** The anomaly cannot be boxed, chambered, or physically bounded in a conventional sense. Containment must operate through jurisdiction, perimeter logic, monitoring, or relationship management rather than through walls.

**Reading example.** `AFD-SP-890` Infinity Train (Threat 3); `AFD-CH-647` Jormungandr (Threat 6).

**Do not confuse with.** Box Class "Unclose" (I-8). The class records the relationship (cannot be enclosed); the structure category records the practical answer (no structure, managed by procedure).

### INTANGIBLE

**Defining line.** *Cannot be touched, only witnessed.*

**Meaning.** Containment depends on perception control, information restriction, ritual procedure, or indirect interaction. The anomaly cannot be physically gripped, so the file's real work is controlling how it is seen, known, and approached.

**Reading example.** `AFD-ME-018` Dread EYE (Threat 3); `AFD-SU-010` Shadow Shark (Threat 3); `ANM-QU-AS-0003` At-the-end-of-the-day (Threat 5).

**Do not confuse with.** ME field type. INTANGIBLE is a containment relationship; ME is a category of existence. A memetic anomaly is *usually* intangible, but an intangible anomaly need not be memetic.

### TIAMAT

**Defining line.** *Beyond the frame of reference.*

**Meaning.** The anomaly exceeds conventional containment logic and may operate on scales outside ordinary ontology, space-time, or causal law. TIAMAT records that the anomaly does not fit the frame the Facility uses to contain anything else; the file is an honest admission that the frame has broken.

**Reading example.** `AFD-CH-703` Nyxara, Goddess of NIGHT (Threat 10); `AFD-NB-125` Proto-Thal (Threat 9).

**Do not confuse with.** Threat 9-10. TIAMAT is not a synonym for "world-ending"; it is the class for anomalies outside the containment frame. Most TIAMAT filings are also extreme threats, but the class and the threat are separate fields.

### [BLANK]

**Defining line.** *Engagement is itself the threat.*

**Meaning.** The most conceptually dangerous category, reserved for anomalies where observation, contact, naming, pursuit, or study may trigger escalation. The class token is written exactly as `[BLANK]` — unspaced — because even the act of filling in the class would be engagement. A `[BLANK]` file is a file that must not be completed.

**Reading example.** The template-class demonstration file held under `ANM-BL-BL-XXXX` carries Containment Class `[BLANK]`, Fracture Containment `UNAUTHORED`, and Threat 5, with `[ Level 4-5 Lock ]` and `[ ABYSS ACCESS ONLY ]` markers: the class is present on the file as the reason the file cannot be opened.

**Do not confuse with.** The redaction marker `[ BLANK ]` (spaced). The distinction is fixed and load-bearing across the whole archive:
- `[BLANK]` — **unspaced** — is the containment class above;
- `[ BLANK ]` — **spaced** — is the redaction marker used to cover text that must not be read (see I-12).
A file that mixes the two spellings has already corrupted its own classification.

---

## I-5 Threat Level

**What the field measures.** Threat Level measures the scale of harm an anomaly may inflict **if uncontained, mismanaged, or triggered**. It is not a description of current behavior inside containment; it is a statement of what the anomaly is capable of doing to the world.

The recognized scale runs **0 to 10**:

- **0** — *no threat — harmless to all forms of life and environment*
- **1** — *minor threat — slight risk to an unprotected individual*
- **2** — *moderate threat — can injure or endanger a single person*
- **3** — *elevated threat — lethal to an individual, manageable with preparation*
- **4** — *severe threat — lethal to multiple individuals, team-level response required*
- **5** — *critical threat — city-wide danger, mass casualties if uncontained*
- **6** — *regional threat — devastation spans across multiple cities or a province*
- **7** — *national threat — an entire country is at risk of collapse or destruction*
- **8** — *continental threat — the scale swallows whole regions and crosses borders effortlessly*
- **9** — *global threat — the entire planet and everything on it is at stake*
- **10** — *existential threat — reality, existence, and the very framework that holds it together — undone*

**What the number drives.** Threat Level is not simply a warning scale. In A.C.T procedure it dictates the size of the response, the degree of secrecy enforcement, evacuation priority, transformation prohibition, and the level of command required for intervention. Two anomalies of the same field type and containment class may still demand entirely different operational responses because their threat levels differ.

**Reading examples.** Threat 0: `AFD-OB-492` Infinite Water Jug. Threat 3: `AFD-OB-312` AFS-312. Threat 4: `AFD-OB-502` Ball of Knife, `AFD-PL-932` Dark World Door. Threat 6: `AFD-CH-647` Jormungandr. Threat 9: `AFD-NB-125` Proto-Thal. Threat 10: `AFD-CH-703` Nyxara.

**Do not confuse with.** GOI Threat Level. Anomaly threat runs 0–10 on the scale above; **GOI threat runs 0–5** and measures an organization's threat to A.C.T and the masquerade, not an anomaly's destructive capacity (see Part II, II-7). The two scales share the word "threat" and share no numbers.

---

## I-6 Transformation Viability

**What the field measures.** Transformation is what distinguishes A.C.T from organizations that only imprison the unknown. A.C.T believes that some anomalies, once understood, may be altered in status. Transformation Viability records **whether this anomaly can be changed — and how far the change may go**.

The recognized values are **INVIOLABLE / NEUTRAL / CONTAINED-STUDY / STABILIZED / NEUTRALIZED / REPURPOSED / INTEGRATED**.

### INVIOLABLE

**Meaning.** *Transformation is not an option.* The anomaly cannot be altered, influenced, or repurposed without catastrophic consequence. The file's transformation line is a standing prohibition, not a deferral.

**Reading example.** `AFD-OB-502` Ball of Knife carries INVIOLABLE: attempting to change it is assessed to trigger the harm that containment exists to prevent.

### NEUTRAL

**Meaning.** *Transformation is inadvisable.* The anomaly is stable enough in containment, and the risk of experimentation outweighs the benefit. The file declines transformation for now, on risk grounds rather than absolute grounds.

### CONTAINED-STUDY

**Meaning.** *Not ready for transformation.* Research is active, but no operational transformation is authorized yet. The anomaly is being studied under containment with transformation as a possible future, not a present program.

**Reading example.** The source doctrine's suggested file format block shows the combination: `AFD-OB-042` — REACTIVE / Threat 4 / **CONTAINED-STUDY**.

### STABILIZED

**Meaning.** *The anomaly has crossed the first threshold.* Its behavior is predictable enough for controlled use beyond strict isolation. STABILIZED is the safer, more predictable, lower-threat state that transformation aims at first.

### NEUTRALIZED

**Meaning.** *Its harmful effect has been suppressed or nullified.* The anomaly no longer poses its original danger, though it may no longer be useful. NEUTRALIZED records that the threat was removed even at the cost of the anomalous property.

### REPURPOSED

**Meaning.** *Its function has been redirected.* The anomaly now serves a defined Facility purpose, such as logistics, surveillance, defense, medicine, or energy support. REPURPOSED is transformation with a mission.

### INTEGRATED

**Meaning.** *The anomaly has become part of A.C.T itself.* At this stage it is no longer treated as an external object of study, but as a permanent system component embedded within infrastructure, doctrine, or operational capacity.

**Reading example of the full ladder.** The scale runs from refusal (INVIOLABLE, NEUTRAL) through study (CONTAINED-STUDY) to achieved states (STABILIZED, NEUTRALIZED, REPURPOSED, INTEGRATED). The RCT template renders the range as `INVIOLABLE → INTEGRATED`.

**Do not confuse with.** Containment Class. Class describes the relationship between the anomaly and the act of containment; viability describes whether and how the anomaly may be *changed*. A REACTIVE anomaly may be INVIOLABLE; an INERT one may be INTEGRATED.

### Supporting Transformation Statuses

Beyond the seven viability values, transformation doctrine carries four status conditions that appear in files and Transformation & Utilization dossiers:

- **Stabilized** — the anomaly has become safer, more predictable, and lower-threat (distinct from the viability value above only in context: viability is the ceiling, status is the achieved state).
- **Repurposed** — the anomaly has been turned into a Facility asset.
- **Unstable Asset** — the anomaly is considered an unstable asset if it has failed transformation before, if transformation changes its threat level, if transformation changes its containment class, if it remains unstable after conversion, or if it carries a heavy ethical burden.
- **Inviolable** — attempting to change the anomaly's structure or nature may itself trigger catastrophic harm.

### Transformation Authorization and Prohibition

- Transformation may only proceed through ascending authority: **Field Operating Chief > High Researcher > Site Director > Head Transformation > High Threat Administrator > O5**.
- Transformation is **not allowed** when the anomaly is marked **Content**, **Unstable**, **Don't Touch**, **Don't See**, or **Don't Fix**.
- Before transformation, the file must demonstrate: **compatibility, application, use, lower projected danger or improved control, and high-need operational justification**.

## I-6A Anomaly Lifecycle State

**What the field measures.** Lifecycle State records the anomaly's present archive and operational condition. It is not the same as Containment Class and not the same as Transformation Viability. Containment Class asks how containment relates to the anomaly. Transformation Viability asks whether the anomaly can be changed. Lifecycle State asks where the anomaly currently stands in A.C.T custody, knowledge, or loss.

Recognized lifecycle states are **PROVISIONAL / ACTIVE-CONTAINED / ACTIVE-UNCONTAINED / UNDER REVIEW / TRANSFORMATION-CANDIDATE / INTEGRATED / RETIRED / ARCHIVED / NEUTRALIZED / EXPLAINED / LOST / MEMORIALIZED / PROHIBITED-FROM-TRANSFORMATION**.

### PROVISIONAL

**Meaning.** The anomaly is suspected, detected, or partially documented, but verification remains incomplete. Most UFD records begin here.

### ACTIVE-CONTAINED

**Meaning.** The anomaly remains active and is presently held, bounded, monitored, or managed by A.C.T procedure.

### ACTIVE-UNCONTAINED

**Meaning.** The anomaly remains active and is not presently under reliable A.C.T control. This state may apply to mobile subjects, open places, spreading effects, escaped objects, public phenomena, or anomalies whose containment is theoretical only.

### UNDER REVIEW

**Meaning.** The anomaly's classification, containment procedure, transformation status, or record integrity is under formal review. This state is used when the archive knows that the current file may no longer be safe to trust.

### TRANSFORMATION-CANDIDATE

**Meaning.** The anomaly is being considered for controlled transformation, repurposing, stabilization, neutralization, or integration. No operational transformation is implied unless separately authorized.

### INTEGRATED

**Meaning.** The anomaly or a derivative of it has become part of A.C.T infrastructure, procedure, equipment, medicine, archive function, or operational capacity. The source anomaly may still require containment.

### RETIRED

**Meaning.** The anomaly no longer requires active operational handling, but its file remains open as a controlled historical and procedural record.

### ARCHIVED

**Meaning.** The active case has closed and the file is preserved for reference, history, training, law, or future reactivation.

### NEUTRALIZED

**Meaning.** The anomalous effect has ceased, been suppressed, been exhausted, or been rendered nonfunctional. The file remains because the cause, method, or consequence may still matter.

### EXPLAINED

**Meaning.** The anomaly was resolved into non-anomalous cause, misclassification, hoax, ordinary science, or a known non-A.C.T phenomenon. The file is retained so the mistake cannot repeat unexamined.

### LOST

**Meaning.** The anomaly, source, file body, route, or confirming evidence has been lost. LOST does not mean safe; it means A.C.T no longer knows enough to claim control.

### MEMORIALIZED

**Meaning.** The anomaly record is retained primarily because personnel, civilians, sites, or historical events attached to it require formal remembrance. Memorialized files may still contain hazardous information.

### PROHIBITED-FROM-TRANSFORMATION

**Meaning.** Transformation is formally forbidden by doctrine, review, ethical determination, or risk. This lifecycle state can coexist with active containment.

**Do not confuse with.** Transformation Viability. An anomaly may be INVIOLABLE as a viability value and ACTIVE-CONTAINED as a lifecycle state. A different anomaly may be REPURPOSED as a viability value and INTEGRATED as a lifecycle state.

---

## I-7 Clearance Levels

**What the field measures.** Clearance in A.C.T is not simply a matter of authority — it is a matter of **survivable knowledge**. Not all truths can be safely known, and not all personnel can be trusted with the same version of reality. The clearance field on an anomaly file states who may lawfully hold the file's knowledge.

### Non-Access

**Meaning.** Civilians. No awareness of A.C.T is permitted. The public is not merely uninformed; it is intentionally protected from knowledge that could destabilize minds, societies, or reality itself.

### Level E — E-Class / Excommunicated Class

**Meaning.** A highly restricted category assigned to condemned, disposable, censured, or operationally isolated individuals. E-Class personnel may be used in dangerous testing, exposure trials, punitive assignments, or sacrificial procedures where standard personnel cannot be risked.

### Level 0

**Meaning.** Assigned to Janitors and Recruiters. These individuals are acknowledged as operationally necessary but receive only the most minimal controlled awareness.

### Level 1

**Meaning.** Assigned to Junior Employees. They possess limited institutional knowledge and access only to low-risk support areas.

### Level 2

**Meaning.** Assigned to Guards, Archivers, and Junior Archivers. These personnel require controlled access to security zones, archived records, and restricted internal workflows.

### Level 3

**Meaning.** Assigned to Field Operators and Senior Researchers. This level allows active engagement with operational anomalies, field response data, and site-level classified incidents.

### Level 4

**Meaning.** Assigned to Field Operating Chiefs, Task Force Command, Head Transformation, High Researchers, and Site Directors. These individuals oversee dangerous operations and possess broad knowledge of live anomaly programs.

### Level 5

**Meaning.** Assigned to the Facility Administrator and High Threat Administrators. This level grants near-total site authority, full administrative oversight, and access to highly restricted truth sets.

### O5 Access Card

**Meaning.** Reserved exclusively for O5 Council members. This clearance does not simply exceed Level 5; it bypasses ordinary compartmentalization entirely. O5 access permits entry into truths that may be hidden even from Administrators and Site Directors.

**Reading example.** An anomaly file's clearance field is written in template form as `[Non-Access / Level E / Level 0 / Level 1 / Level 2 / Level 3 / Level 4 / Level 5 / O5 Access]`. Files carrying `[ Level 4-5 Lock ]` or `[ O5 - ONLY ]` markers (I-12) are the practical enforcement of this scale.

**Do not confuse with.** Redaction markers that cite levels. The clearance field is the file's standing access rule; a level marker on a redaction tells the reader that a *specific passage* is locked to that tier or higher.

---

## I-8 Box Class — Containment Structure Category

**What the field measures.** Box Class (the Containment Structure Category) answers a different question from Containment Class: **what kind of structure will reality tolerate around this anomaly?** In A.C.T, containment is not only about difficulty — it is also about what kind of enclosure the anomaly and reality permit. Every anomaly file states its structure category so the physical plant, not just the procedure, is on record.

The recognized categories are: **Small Box / Medium Box / Large Box / Massive Box / Enclosure Box / Box-cass / Monitoring Field / Blind Box / Eye Box / Non-Box / Unclose**.

### Small Box

**Meaning.** Used for compact anomalous objects, devices, samples, or low-volume materials requiring minimal secure enclosed storage. A Small Box filing means the anomaly fits ordinary vault scale and its containment is dominated by the object's own stability rather than by the room around it.

### Medium Box

**Meaning.** Used for larger objects or manageable contained anomalies needing modest chamber space. Medium Box is the default scale for the majority of object-type holdings that do not fit small storage but do not require a full chamber regime.

### Large Box

**Meaning.** Used for significant objects, active subjects, or anomalies requiring broad enclosure room. A Large Box filing usually implies live occupancy: the enclosure must hold not only the anomaly but its movement, caretaker access, and monitoring equipment.

### Massive Box

**Meaning.** Used for oversized entities, large-scale hazards, or high-volume enclosures requiring heavy structural containment. Massive Box structures are industrial-grade enclosures built around the anomaly rather than rooms prepared for it.

### Enclosure Box

**Meaning.** Used when the anomaly requires a perimeter or territory-style enclosure rather than a simple chamber. Enclosure Box is the structure answer for place-type and territory-bound anomalies: the "box" is a bounded region with controlled access, not a room with walls.

### Box-cass

**Meaning.** Used when the anomaly is already effectively a box, shell, vessel, or self-contained container-state object. Box-cass filings note that the anomaly arrives with its own containment built in, and the Facility's task is to hold the container rather than to build one.

### Monitoring Field

**Meaning.** Used when the anomaly is best controlled through a monitored field, exclusion area, perimeter, or indirect watch-zone instead of a hard chamber. Monitoring Field is the structure answer for anomalies that cannot or must not be walled, and it pairs naturally with UNENCLOSABLE and INTANGIBLE containment classes.

### Blind Box

**Meaning.** Used when direct observation is dangerous and the anomaly must be enclosed under visual-denial or sensory-restricted conditions. Blind Box structures are built so that the anomaly is held *without being seen* — observation denial is part of the physical design.

### Eye Box

**Meaning.** Used when active or continuous observation is itself part of containment and the anomaly must remain visible under controlled conditions. Eye Box is the inverse of Blind Box: the structure exists to keep the anomaly in view because looking is the containment.

### Non-Box

**Meaning.** Used when the anomaly cannot be described by ordinary enclosure logic but may still be managed through procedure. Non-Box is not "no containment"; it is the record that containment will be procedural rather than architectural.

### Unclose

**Meaning.** Used when the anomaly is too vast, too distributed, too abstract, or too structurally broad to enclose meaningfully at all. Unclose is the end of the Box Class scale: the file records that no enclosure exists or could exist, and containment is jurisdictional, observational, or doctrinal.

**Do not confuse with.** Containment Class (I-4). A common filing error: writing "REACTIVE" where the question asked for a box, or "Medium Box" where the question asked for a class. The class records the anomaly's relationship to containment; the Box Class records the structure reality tolerates. The two must be filled separately and consistently — for example, an INTANGIBLE anomaly held under a Monitoring Field, or a small INERT object in a Small Box.

---

## I-9 Containment Location, Condition, Exposure, and Transport Fields

Four short fields govern how containment is conducted rather than what it is. Each is explained here because each is a source of abbreviation errors in the archive.

### Containment Location Behavior Category

Every anomaly is assigned one of four location-behavior statements, describing the required relationship between the anomaly and its monitoring:

- **LEFT ALONE** — the anomaly is safer when undisturbed; the correct posture is non-intervention.
- **CAN'T BE LEFT ALONE** — the anomaly requires continuous presence or attention; leaving it unattended invites failure.
- **MUST MONITOR** — the anomaly requires active observation on a schedule or in real time; monitoring is a containment requirement, not a precaution.
- **DON'T MONITOR** — monitoring the anomaly is itself dangerous; observation must be withheld or indirect. (DON'T MONITOR pairs with Blind Box structures and with the observation restrictions in I-11.)

### Containment Condition Category

Every anomaly is categorized by the kind of thing containment is dealing with:

- **Humanoid** — the anomaly has human form or near-human form; containment must account for person-shaped behavior, communication, and care.
- **Non-Humanoid** — the anomaly is a living or acting thing without human form.
- **Object** — the anomaly is a thing (see OB field type, I-2).
- **Phenomenon** — the anomaly is an event, process, or condition rather than a thing or being; containment addresses the phenomenon's recurrence.

### Exposure Authorization

Direct exposure to an anomaly is restricted to three categories of personnel:

- **E-Class Test Subject** — personnel assigned to exposure trials under the E-Class clearance condition (I-7).
- **Current Researcher** — the researcher or research team currently holding the file.
- **Designated Field Personnel** — operators formally designated for the anomaly's field handling.

Anyone outside these categories is unauthorized for direct exposure regardless of general clearance.

### Transport Rule

Movable anomalies must be transported using **REALITY STABILIZATION ANCHOR / RSA** support:

- **standard anomalies** — RSA transport support;
- **oversized anomalies** — Facility Converted Aircraft;
- **unmovable anomalies** — a Facility-built perimeter, enclosure, and support system is constructed around the anomaly itself.

---

## I-10 Breach States

Every anomaly file includes a current breach-state condition describing not only whether the anomaly is in its assigned place, but **whether containment reality itself remains coherent around it**. The recognized states:

- **Stable** — containment holds; the anomaly is in place; reality around it is coherent.
- **Content** — the anomaly is settled and non-resistant; the file may record it as satisfied with its condition.
- **Contain** — containment is actively holding; the state is nominal but effortful.
- **Unstable** — containment holds but is degrading or unreliable; the anomaly or its environment is shifting.
- **Agitated** — the anomaly is actively distressed or provoked; behavioral escalation is likely.
- **Leaking** — the anomaly's effect is escaping containment even though the anomaly itself remains held.
- **Compromised** — a containment component, procedure, or record has failed or been corrupted.
- **Breached** — containment has failed and the anomaly is out of its assigned place.
- **Escalating** — the situation is worsening in real time toward or beyond breach.
- **Critical** — the anomaly or its environment has reached a point where catastrophic failure is imminent or underway.
- **Structural Failure State** — containment reality itself has failed around the anomaly; ordinary containment terms no longer describe the condition.

**Transformation link.** A file marked **Content**, **Unstable**, or under a **Don't Touch / Don't See / Don't Fix** standing mark is barred from transformation (see I-6).

---

## I-11 Observation and Handling Restrictions

Anomalies may carry one or more direct interaction restrictions. These are **part of containment, not optional notes**. The recognized restrictions and their meanings:

- **no direct eye contact** — visual engagement with the anomaly's eyes (or eye-equivalent) triggers or escalates its effect; handlers must avert or shield sight.
- **no verbal naming** — speaking the anomaly's name or designation aloud invokes or strengthens it.
- **no mirrored reflection exposure** — the anomaly must not be seen or allowed to see itself through reflective surfaces.
- **no digital replication** — the anomaly must not be photographed, filmed, scanned, or otherwise copied by electronic means.
- **no written duplication** — the anomaly must not be described in writing that can be duplicated outside controlled records.
- **no solo observation** — the anomaly may only be observed by paired or team personnel; a lone observer is an unacceptable risk.
- **no biological contact** — personnel must not physically touch the anomaly or its biological products without full barrier procedure.
- **no serpent-class organism proximity** — serpent-form or serpent-class organisms must not be brought near the anomaly (a restriction class with direct historical weight in the ITHYOS lineage).
- **no descent below assigned floor without clearance** — the anomaly's holding level is a clearance boundary; deeper access is prohibited without authorization.
- **no destabilizing** — the anomaly must not be shocked, provoked, altered, or placed under stress conditions.
- **no weak psychic** — personnel with known psychic susceptibility (or unverified resistance) must not interact with the anomaly.

---

## I-12 Redaction and Suppression Markers

Information suppression is part of containment. Authorized markers tell the reader **why a passage is missing and what regime governs it**:

- `[ BLANK ]` — **spaced** — the standard redaction marker: text has been removed. It carries no reason and asserts nothing; it is the archive's way of saying the words exist but will not be written here.
- `[ MEMETIC ]` — the passage is suppressed because the information itself carries a memetic hazard (see ME, I-2).
- `[ INFO-HAZARD ]` — the passage is suppressed because knowing the information is dangerous (see IH, I-2).
- `[MEMETIC FILTER APPLIED]` — a memetic filter has been applied to the text; what remains has been processed for safe reading.
- `[STRUCTURAL DATA OMITTED]` — the passage concerned Structural Reality data whose omission is itself a containment measure.
- `[ABYSS ACCESS ONLY]` — the passage is readable only through ABYSS access protocols.
- `[ O5 - ONLY ]` — the passage is restricted to O5 Council access.
- `[O5-RESTRICTED]` — the passage falls under O5 restriction authority (same tier as above; spelling varies by file era).
- `[ Level 4-5 Lock ]` — the passage is locked to Level 4 and Level 5 clearance holders.
- `[ Specialize Only ]` — the passage is readable only by personnel of the relevant specialization, regardless of general clearance.

**The fixed spelling rule.** `[ BLANK ]` with spaces is always a redaction marker; `[BLANK]` without spaces is always the containment class (I-4). The distinction is load-bearing: a file that mixes the spellings has corrupted its own classification, and a reader who treats a class as a redaction (or a redaction as a class) has misread the file.

---

## I-13 RCT Format and Its Axes

**What the RCT format is.** The RCT Format is a specialized anomaly record focused on three operational axes, written for anomalies under continuing containment strain, live research pressure, and transformation review. It answers the question: **how are we holding it, what are we learning from it, and can it be changed into something useful without destroying ourselves?**

The three axes, which also give the format its name:

- **CO — Containment.** The current holding state: containment summary, specifications, site, history, and the live condition of the box.
- **RE — Research.** The active learning state: research summary, lead researcher and team, current research phase, anomalous-properties research profile, key log entries, and research restrictions.
- **TR — Transformation.** The conversion state: transformation summary, target end state, and the current viability position on the INVIOLABLE → INTEGRATED scale.

**Relationship to Standard Format.** The two formats are not competing systems; they are parallel tools. **Standard Format = full archival identity; RCT Format = live operational handling body.** A single anomaly may possess both a Standard file and an RCT file if its archival and operational importance justify dual-record status.

**Range shorthand.** In RCT files the classification block is written as a range: `CONTAINMENT CLASS: [INERT → [BLANK]]`, `THREAT LEVEL: [0 → 10]`, `TRANSFORMATION VIABILITY: [INVIOLABLE → INTEGRATED]`. The left value is the least demanding end of the scale and the right value the most; the live value sits somewhere on that span. The span is a filing convenience, not a promise that classes escalate in a strict order.

---

## I-14 Record and File State Vocabulary

Anomaly files and their supporting records carry state fields whose vocabulary is consistent across the archive:

- **Archive Status** (on the file header): **Active** — the file is in current operational use; **Active Restricted Record** — active but distribution-limited; **Archived** — retired from active use; **Sealed** — closed by authority and not to be opened without higher clearance.
- **FILE STATUS** (in metadata): **Active / Restricted / Sealed** follow the same meaning as above; other file-status values appear in context (Under Review, Dormant).
- **RECORD CONDITION**: describes the record's own completeness — **Draft / Operational / Archived** are the standard metadata values on controlled forms, with operational meaning: Draft = not yet authoritative, Operational = authoritative in current use, Archived = preserved for history.
- **CURRENT STATUS** (on anomaly and registry files): Active / Dormant / Fragmented / Contained / Sealed / Unknown / Under Expansion / Compromised / Archived — the value states the live condition of the subject (anomaly, site, or organization) at the file's last update.
- **DESIGNATION HISTORY**: records every designation the subject has carried, in order — for example a file noting it was opened as UFD and verified as AFD, or a GOI record noting a retained registry designation. When a designation changes, the history line is how the archive keeps the subject identifiable across its own name changes.

## I-15 Anomaly Hazard Tag Index

Hazard Tags are controlled search and routing markers attached to an anomaly file. They do not replace Field Type, Containment Class, Threat Level, or Transformation Viability. A tag only names a documented hazard behavior so the archive can find similar risks across different files.

**Rule of evidence.** A Hazard Tag may appear on a file only when the description, anomalous properties, containment procedure, incident history, log dossier, or research summary demonstrates the hazard. Tags are not mood labels and not guesses.

**Rule of restraint.** A file should carry the smallest useful set of tags. If every danger is tagged, the tags stop helping containment.

### PHYS — Physical Hazard Tags

Used for direct material harm, kinetic danger, cutting, crushing, impact, weaponization, pressure, heat, cold, radiation-like output, or other body/world damage not better described by a more specific family.

Example tags: `PHYS-IMPACT`, `PHYS-CUTTING`, `PHYS-THERMAL`, `PHYS-PRESSURE`, `PHYS-WEAPONIZED`.

### BIO — Biological Hazard Tags

Used for anomalous life, infection, growth, mutation, parasitism, ecological disruption, bodily transformation, or non-natural biological systems.

Example tags: `BIO-INFECTION`, `BIO-MUTAGENIC`, `BIO-GROWTH`, `BIO-PARASITIC`, `BIO-ECOLOGICAL`.

### COG — Cognitive and Identity Hazard Tags

Used for memory alteration, compulsion, perception failure, personality drift, identity replacement, false recognition, dream intrusion, or cognition damage.

Example tags: `COG-MEMORY`, `COG-COMPULSION`, `COG-IDENTITY-DRIFT`, `COG-PERCEPTION`, `COG-DREAM`.

### MEM — Memetic and Information Hazard Tags

Used when information, symbols, language, sound, images, documents, naming, or knowledge transmission carries the hazard.

Example tags: `MEM-SYMBOL`, `MEM-LANGUAGE`, `MEM-AUDIO`, `MEM-VISUAL`, `INFO-READING-HAZARD`, `INFO-NAMING-HAZARD`.

### TEMP — Temporal Hazard Tags

Used for loops, pre-echoes, time loss, acceleration, delay, chronology damage, predictive contamination, or events remembered before they occur.

Example tags: `TEMP-LOOP`, `TEMP-LOSS`, `TEMP-PRE-ECHO`, `TEMP-DELAY`, `TEMP-CHRONOLOGY`.

### SPAT — Spatial Hazard Tags

Used for impossible geometry, nonlocal interiors, false distance, extradimensional routing, transit anomalies, unstable thresholds, or space behaving as the active hazard.

Example tags: `SPAT-NONLOCAL`, `SPAT-THRESHOLD`, `SPAT-TRANSIT`, `SPAT-INTERIOR`, `SPAT-DISTANCE`.

### STR — Structural-Reality Hazard Tags

Used when the anomaly affects the rules that allow reality, containment, documentation, causality, classification, or observation to remain stable.

Example tags: `STR-REALITY-FRACTURE`, `STR-CLASSIFICATION-FAILURE`, `STR-CONTAINMENT-LOGIC`, `STR-OBSERVATION`, `STR-ARCHIVE-DRIFT`.

### COS — Cosmic / Abyssal Hazard Tags

Used for origin-level, abyssal, divine, cosmic, foundational, world-scale, or structure-bearing hazards whose scope exceeds ordinary local anomaly behavior.

Example tags: `COS-ABYSSAL`, `COS-FOUNDATIONAL`, `COS-DIVINE`, `COS-WORLD-SCALE`, `COS-SLEEPING-SYSTEM`.

### SOC — Social / Operational Exposure Tags

Used for hazards that spread through institutions, groups, secrecy failures, recruitment, markets, public narratives, or operational handling rather than only through physical contact.

Example tags: `SOC-RECRUITMENT`, `SOC-MARKET`, `SOC-COVER-RISK`, `SOC-GOI-INTERFERENCE`, `OPR-HANDLING-RISK`, `OPR-ASSET-DEPENDENCY`.

**Reading principle.** The first tag family should match the most operationally urgent hazard, not the most dramatic one. A beautiful object that primarily rewrites memory is filed with a cognitive or memetic hazard tag before a physical one.

---

# PART II — GOI DESIGNATION AND CLASSIFICATION STACK

Groups of Interest are filed under their own registry logic, separate from anomaly records. The GOI designation and its seven classification fields tell the reader, at a glance, what kind of organization the GOI is, how it relates to A.C.T, how large it reaches, what it can do with anomalies, how dangerous it is to A.C.T, how it affects the masquerade, and what A.C.T intends to do about it.

## II-1 GOI Designation Anatomy

The designation structure is **GOI-XX-X-XXX**:

- **GOI** — Group of Interest;
- the first **XX** — the **Nature Class code** (what kind of group it is);
- the second **X** — the **Alignment Class marker** (its broad relationship to A.C.T);
- the **XXX** — the **numerical registry code**.

**Reading example.** `GOI-ML-X-050` — Militant nature, Negative alignment, registry 050 (Liberty Freedoms). `GOI-GV-P-001` — Government nature, Positive alignment, registry 001 (GAA).

**Do not confuse with.** Anomaly designations. GOI records use their own numbering and their own code tables; an anomaly designation never begins with GOI and a GOI designation never carries a field type or fracture code.

## II-2 Nature Class Codes

Nature Class describes what kind of group the GOI is at its core. Recognized codes:

### GV — Government
**Meaning.** The group is a state or governmental body — an agency, ministry, secretariat, or official apparatus — operating within or across national authority.

### CP — Corporate
**Meaning.** The group is a company or commercial enterprise whose structure, profit motive, or corporate form is the operative reality.

### CU — Cultic
**Meaning.** The group is organized around belief, ritual, worship, or doctrinal commitment, whether harmful, useful, or mixed.

### SC — Scientific
**Meaning.** The group is organized around research, knowledge, or method — an epistemic actor rather than a commercial or political one.

### CV — Civil
**Meaning.** The group is a civilian or community organization: mutual aid, survivor networks, associations, or ordinary people organized around shared circumstance.

### ML — Militant
**Meaning.** The group is armed or force-capable and uses organized violence, coercion, or military-style action as a core method.

### AN — Anomalous
**Meaning.** The group is itself anomalous — its existence, membership, or operation cannot be explained without anomalous conditions. Anomalous-nature GOIs require dual filing consideration (see II-10).

### IH — In-Human
**Meaning.** The group is non-human in origin, nature, or membership — an intelligent collective, entity, or structure that is not a human organization.

### BS — Business
**Meaning.** The group is a commercial operation — trade, logistics, or commerce — where the *transactional network* rather than corporate form is the defining feature (distinct from CP in that the group may have no single corporate body).

### HY — Hybrid
**Meaning.** The group's structure crosses human, technological, and anomalous boundaries — part institution, part system, part anomaly.

## II-3 Alignment Class Markers

Alignment Class records the GOI's broad relationship to A.C.T. Recognized markers:

- **N — Neutral** — neither aligned against nor with A.C.T; its purposes simply do not center on the Facility.
- **P — Positive** — aligned with A.C.T or actively cooperative in intent.
- **X — Negative** — hostile or opposed to A.C.T.
- **U — Unknown** — the relationship cannot yet be assessed.
- **T — Trade** — the relationship is transactional; the group trades with the anomalous world or with A.C.T.
- **B — Business** — the relationship is commercial; the group's dealings are the point of contact.
- **G — Guild** — the relationship is that of a craft or protective body with its own rules, neither purely hostile nor purely aligned.

**Reading examples.** `GOI-CU-X-048` Children of the Deep — Cultic, Negative. `GOI-BS-T-027` Anstrall Market — Business, Trade. `GOI-ML-G-039` (roadmap provisional) — Militant, Guild.

## II-4 Registry Numbering and the Live Register

The registry number is sequential and unique within the GOI series. Existing live records at the time of this writing:

- `GOI-GV-P-001` — Government Anti Anomaly / GAA
- `GOI-ML-X-014` — Anti-Global Anomaly / A-GA
- `GOI-BS-T-027` — Anstrall Market
- `GOI-CU-X-048` — Children of the Deep / CoTD
- `GOI-CP-B-049` — DREAM .INC / DREAM
- `GOI-ML-X-050` — Liberty Freedoms / L.F.

## II-5 Reach Class

Reach Class records how large the GOI's influence is. Recognized values:

- **CELLULAR** — the group operates as small, disconnected units.
- **LOCAL** — influence is confined to a single locality.
- **REGIONAL** — influence spans a defined region.
- **NATIONAL** — influence spans one country.
- **TRANSNATIONAL** — influence crosses borders without being global.
- **GLOBAL** — influence is worldwide.
- **STRUCTURAL** — the group's reach is not geographic but structural: it operates inside systems, doctrine, reality, or infrastructure themselves.

## II-6 Anomalous Capability Class

This class records how capable the GOI is when dealing with anomalies directly. Recognized values:

- **NULL** — no anomalous capability; the group has no meaningful means of engaging anomalies.
- **EXPOSED** — the group is affected by or exposed to anomalies but does not command them.
- **HANDLER** — the group can seize, secure, transport, or tend anomalies — it handles them — without necessarily understanding them.
- **PRACTITIONER** — the group works with anomalies through practice, ritual, or trained method.
- **ENGINEERING** — the group can build, adapt, or deploy technical systems for direct interaction with anomalies.
- **REALITY-ACTIVE** — the group operates on reality itself, not merely on anomalies within it.
- **STRUCTURAL** — the group's capability is bound into the structure of a system, site, or doctrine rather than into its members.

**Reading example.** A-GA is ENGINEERING (builds anti-anomalous tools); Liberty Freedoms is HANDLER (carries and tends what it seizes, using defector knowledge rather than new engineering).

## II-7 GOI Threat Level (0–5)

GOI threat is measured from **0 to 5** — a different scale from the anomaly threat ladder (I-5):

- **0** = no meaningful threat
- **1** = low threat
- **2** = moderate threat
- **3** = high threat
- **4** = severe threat
- **5** = critical threat

**Do not confuse with.** Anomaly Threat Level (0–10). The GOI scale measures the organization's threat to A.C.T, its operations, and the masquerade; the anomaly scale measures an anomaly's destructive capacity if uncontained.

## II-8 Secrecy Risk

Secrecy Risk measures how dangerous the GOI is to the masquerade of normal life:

- **VEILED** — the group operates beneath the veil and does not threaten it.
- **LEAKING** — the group's activity creates recurring leaks of concealed information even when exposure is not its goal.
- **EXPOSURE-ACTIVE** — exposure is a method: the group deliberately produces public evidence of the concealed world.
- **NORMALCY-BREACHING** — the group's existence or success would break the masquerade at scale.

## II-9 A.C.T Posture

Posture records what A.C.T intends to do with the GOI:

- **MONITOR** — observe and assess without intervention.
- **INFILTRATE** — place or maintain sources inside the group.
- **MISDIRECT** — feed the group false or managed information.
- **CONTAIN** — restrict the group's capacity to act.
- **DISMANTLE** — remove the group's ability to regenerate or operate.
- **APPROPRIATE** — take the group's assets, methods, or capacity for Facility use.
- **ERASE** — remove the group from existence and record.
- **COOPERATED** — A.C.T is formally cooperating with the group.
- **HELP** — A.C.T's posture is assistance rather than control.

Postures are written in combination where multiple actions apply — for example `CONTAIN / DISMANTLE / INFILTRATE` (Liberty Freedoms) or `MONITOR / INFILTRATE` (Anstrall Market) — with the primary action first.

## II-10 Dual Filing for Anomalous-Nature GOIs

A GOI whose nature is AN (Anomalous), or any GOI later shown to be itself an anomalous condition, requires **dual filing**: a GOI record for the organizational behavior and a separate AFD (or ANM) record for the anomalous condition. The two records must remain distinct — organizational responsibility is not dissolved by anomalous origin, and anomalous condition is not reduced to organizational misconduct. Each dossier's Cross-Reference Status section states the ruling: dual filing required, not required, or under review.


---

# PART III — SITE, SUB-SITE, AND FLOOR DESIGNATIONS

## III-1 Site Designation Anatomy

Permanent A.C.T installations are designated under **ACT-SITE-XX-##-#** (primary sites) or **ACT-SUB-XX-##-#** (sub-sites):

- **ACT** — A.C.T Facility registration;
- **SITE** / **SUB** — the installation class (primary site vs sub-site);
- **XX** — the site number;
- **##** — the country abbreviation;
- **#** — the regional area code.

**Reading example.** `ACT-SITE-01-US-W`: Site 01, United States, Western region. `ACT-SUB-05-ID-C`: Sub-Site 05, Indonesia, Central region.

**Do not confuse with.** Anomaly designations and GOI designations. The `ACT-` prefix is reserved for Facility installations; an anomaly file may *reference* a site (`CONTAINMENT SITE: ACT-SITE-01-US-W`) but the site designation never replaces the anomaly's own UFD/AFD/ANM identity.

## III-2 Regional Area Codes

The final regional code marks broad placement within the country:

- **N** = North
- **S** = South
- **W** = West
- **E** = East
- **C** = Central

**Reading example.** `ACT-SITE-03-JP-E` — Site 03, Japan, East (the Kurokawa Archive Node). `ACT-SITE-02-RU-N` — Site 02, Russia, North (White Grave Station). `ACT-SITE-04-BR-C` — Site 04, Brazil, Central (Verde Null Bio-Reserve).

## III-3 The Registered Site and Sub-Site Network

The Global Site Registry records ten major recognized installations:

| Designation | Codename | Class |
|---|---|---|
| ACT-SITE-01-US-W | Redwood Veil Complex | Regional Site |
| ACT-SITE-02-RU-N | White Grave Station | Regional Site |
| ACT-SITE-03-JP-E | Kurokawa Archive Node | Regional Site |
| ACT-SITE-04-BR-C | Verde Null Bio-Reserve | Regional Site |
| ACT-SITE-05-ID-C | Nusantara Deep Relay | Regional Site |
| ACT-SUB-01-US-W | Glass Orchard Relay | Sub-Site (reports to SITE-01) |
| ACT-SUB-02-RU-N | Frost Hollow Depot | Sub-Site (reports to SITE-02) |
| ACT-SUB-03-JP-E | Silent Reed Annex | Sub-Site (reports to SITE-03) |
| ACT-SUB-04-BR-C | Hollow Canopy Enclosure | Sub-Site (reports to SITE-04) |
| ACT-SUB-05-ID-C | Ash Tide Watchpoint | Sub-Site (reports to SITE-05) |

The registry is not exhaustive: relay sites, black sites, temporary enclosures, and hidden support points exist outside the numbered series and are not given registry numbers unless formally recognized.

## III-4 Site Type Classes

A site's own file states its type:

- **Primary Site** — a major high-authority installation of broad strategic importance (the Central Facility itself).
- **Regional Site** — a major official installation assigned to one large region or operational zone (the five SITE-01 through SITE-05 installations).
- **Sub-Site** — a smaller or more specialized installation attached to a parent SITE or regional command.
- **Relay Site** — a support node used for transfer, archive routing, witness handling, or covert logistical continuity.
- **Black Site** — an unacknowledged installation whose existence is itself classified.

**Do not confuse with.** Site Type is about command class; Site Type is not the same field as a site's codename, containment profile, or jurisdiction.

## III-5 Floor Designations (F-1 to F-N)

Floors are designated by the **F-series**, with a fixed reading rule: floor designations run **F-1** (deepest) upward to **F-N** at the surface level.

**Reading rule.** F-1 is always the deepest numbered floor of an installation, not the first floor a visitor meets. The numbering is depth-first: F-2 sits above F-1, and F-N is the topmost (surface or transition) level. Below F-1 only the ABYSS access route continues.

**Reading example.** `ACT-SITE-01-US-W-F-1` is The Hanging Vault, the deepest numbered floor of Redwood Veil; `ACT-SITE-01-US-W-F-9` is its Surface Transition Level. A site with six floors runs F-1 (deepest) to F-6 (surface), which is why the breach rule's "closing of F-1 to the outside" seals the deepest access route during a response.

**Floor reference in canon.** In Part Three's breach response rule, "Closing of F-1 To the Outside" seals the deepest access route; the floor naming note in that doctrine states the F-1-to-F-N rule above. The shorthand `F-xxxx` seen in some draft files is the in-draft form where the precise floor is not declassified.

## III-6 Floor Dossier Series

Each numbered floor has its own dossier file following the ACT Floor Record Standard. Floor dossier files carry a **Dossier Number** in the **FLOOR-DOSSIER** series and are named with the floor's full designation — for example `ACT-SITE-01-US-W-F-2-The-Deep-Object-and-Memetic-Component-Vaults`.

**Coverage rule.** Floor dossiers are written for all five primary SITES and for the four SUB-SITES with numbered buried components (Glass Orchard Relay, Frost Hollow Depot, Silent Reed Annex, Ash Tide Watchpoint). **ACT-SUB-04-BR-C, the Hollow Canopy Enclosure, is a concealed-perimeter installation rather than a building-dominant facility: it carries no numbered floor register**, and its operational architecture is documented through concealed perimeter sectors and field stations rather than floor dossiers.

**Do not confuse with.** The ABYSS. The F-series numbers only the main floors of an installation; the ABYSS is a deeper access route, not a numbered floor, and ABYSS records carry their own access restrictions.

---

# PART IV — SUPPORTING RECORD AND LOG CATEGORIES

## IV-1 What Log Categories Are

Beyond the main anomaly file, A.C.T maintains categorized supporting dossiers for anomalies that generate too much evidence, transcript material, testing history, or review complexity to live safely in one file. Each category preserves **how A.C.T learned what it learned** without overloading the active containment file. Category dossiers are named by their kind — Recovery, Testimony, Testing, Incident, Exploration, Research, Recovered Document, Behavioral, Transformation, Correspondence, Sensor, or Personal — and attach to an anomaly by its designation.

## CATEGORY I — Recovery & Discovery Dossier

**Function.** Records how A.C.T first detected, verified, approached, recovered, transported, or stabilized an anomaly. Preserves the first chain of custody.

**Used when.** The anomaly was found in public; civilian witnesses were involved; the recovery operation was complex; the anomaly was unstable during intake; or future review may need to know exactly how A.C.T first encountered it.

**Common contents.** Discovery Log, Recovery Log, Retrieval Log, Initial Contact Log, Field Intake Log, Civilian Exposure Log, Witness Intake Log, Evidence Collection Log, Transport Log, After-Action Report.

## CATEGORY II — Interview & Testimony Dossier

**Function.** Records statements from sentient anomalies, affected subjects, personnel, civilian witnesses, survivors, or related parties. Preserves how individuals describe an anomaly from inside the event.

**Used when.** The anomaly speaks; witness memory changes over time; subjective experience is important; the anomaly appears as a familiar figure; personnel interpretation affects containment.

**Common contents.** Interview Log, Interview Transcript, Eyewitness Interview, Subject Testimony, Survivor Statement, Personnel Debrief, Civilian Statement, Memetic Screening Note.

## CATEGORY III — Experiment & Testing Dossier

**Function.** Records controlled interaction with an anomaly to determine triggers, limits, safe handling rules, exposure thresholds, and containment weaknesses.

**Used when.** The anomaly has measurable activation conditions; personnel need safe exposure limits; containment theory requires confirmation; the anomaly is being studied for transformation viability; A.C.T must know what not to do.

**Common contents.** Test Log, Experiment Log, Exposure Log, Trigger Test, Material Test, Behavioral Test, Containment Test, Simulation Log, Stress Test, Interaction Trial, Cross-Anomaly Test, Failure Log.

## CATEGORY IV — Incident & Breach Dossier

**Function.** Records containment failures, unexpected activations, operational mistakes, exposure events, and emergency responses. Used to prevent repeat failures.

**Used when.** Containment fails; personnel are exposed; the anomaly behaves outside prediction; procedure is changed because of an event; the anomaly enters a dangerous state.

**Common contents.** Incident Log, Incident Report, Breach Log, Containment Failure Report, Emergency Response Log, Security Transcript, Audio/Video Transcript, After-Action Report, Exposure Summary, Procedure Change Note.

## CATEGORY V — Exploration & Survey Dossier

**Function.** Records movement through anomalous spaces, structures, zones, routes, or environments. Used when the anomaly is a place, creates a place, changes routes, or affects navigation.

**Used when.** The anomaly is spatial; terrain changes; maps cannot be trusted; a field team enters an unknown area; drones or personnel survey a location.

**Common contents.** Exploration Log, Survey Log, Mapping Log, Drone Log, Field Team Transcript, Route Record, Environmental Reading Log, Spatial Contradiction Log, Landmark Log.

## CATEGORY VI — Research & Analysis Dossier

**Function.** Records scientific review, classification debate, theory development, and long-term study. Used when the anomaly's meaning or mechanics remain uncertain.

**Used when.** Classification is uncertain; recovered evidence requires interpretation; the anomaly has multiple possible explanations; A.C.T divisions disagree; the anomaly connects to larger doctrine.

**Common contents.** Research Log, Analysis Report, Classification Review, Theory Log, Laboratory Report, Material Analysis, Biological Review, Memetic Review, Temporal Review, Database Review, Archive Comparison.

## CATEGORY VII — Recovered Document & Archive Dossier

**Function.** Preserves documents, files, notes, images, recordings, manuals, or data recovered with or because of an anomaly. Used when the evidence itself matters.

**Used when.** The anomaly includes a document; a recovered file contains important context; a database may be anomalous; old records contradict current history; the archive object must be separated from interpretation.

**Common contents.** Recovered Document, Archive Copy, Document Transcript, Audio Transcript, Video Transcript, Image Description, Database Extract, Recovered Note, Personal Letter, Manual Fragment.

## CATEGORY VIII — Behavioral & Observation Dossier

**Function.** Records repeated behavior, care notes, habits, routines, responses, and long-term monitoring. Used for subjects whose containment depends on understanding behavior rather than simply locking them away.

**Used when.** The anomaly is alive or behaves like it is alive; emotional state affects containment; routine reduces breach chance; care procedures matter; the anomaly learns or changes over time.

**Common contents.** Observation Log, Behavioral Log, Care Log, Routine Log, Feeding Log, Sleep Log, Social Interaction Log, Preference Record, Stimulus Response Log, Deterioration Note.

## CATEGORY IX — Transformation & Utilization Dossier

**Function.** Records A.C.T attempts to stabilize, neutralize, repurpose, integrate, or reject use of an anomaly. Used when the question is not only how to contain it but whether it can become useful or safer.

**Used when.** A.C.T wants to use the anomaly; the anomaly may become a tool, medicine, asset, or infrastructure component; an ethical dispute exists; transformation failed; use is prohibited but repeatedly proposed.

**Common contents.** Transformation Log, Repurposing Trial, Stabilization Log, Neutralization Log, Integration Report, Utilization Proposal, Ethical Review, Failure Record, Authorization Chain.

## CATEGORY X — Communication & Internal Correspondence Dossier

**Function.** Records internal messages, command decisions, interdepartmental disputes, authorization requests, and administrative reactions. Used when bureaucracy is part of the containment story.

**Used when.** Departments disagree; command decisions matter; an action requires authorization; ethics review affects containment; archive politics hide or reveal important information.

**Common contents.** Email Log, Internal Memo, Command Notice, Clearance Request, Authorization Chain, Ethics Committee Note, Archive Dispute, Site Directive, Denial Record.

## CATEGORY XI — Audio / Video / Sensor Dossier

**Function.** Preserves recorded evidence where timing, image, sound, or instrument readings are central. Used when the record is more important than a written summary.

**Used when.** The anomaly is visible only on footage; timestamps contradict reality; audio contains important phrases; sensor readings reveal hidden behavior; personnel perception cannot be trusted.

**Common contents.** Audio Log, Video Log, CCTV Transcript, Bodycam Transcript, Drone Feed, Sensor Log, Black Box Log, Radio Transcript, Transmission Record, Timecode Transcript, Visual Analysis Note.

## CATEGORY XII — Personal & Recovered Journal Dossier

**Function.** Preserves subjective writing, personal logs, diaries, field notebooks, and anomaly-authored or affected journal entries.

**Used when.** Memory changes; dreams matter; personnel experience gradual effects; the anomaly writes or causes writing; official summaries cannot capture subjective progression.

**Common contents.** Personal Log, Recovered Journal, Researcher Diary, Field Notebook, Subject-Written Entry, Dream Journal, Confession Note, Survivor Diary, Automatic Writing Sample, Private Audio Note, Fragmented Memory Log.

**Reliability note.** Personal dossiers are not automatically less reliable than formal reports. In some anomalies, subjective records are the only records that survive contact with the event.

---

# CLOSING NOTE

This reference exists to end the archive's oldest documentation failure: codes written down as though their meaning were obvious. Every designation, class, category, state, and marker in this file is explained above. Where a source record listed a value without expansion, the working interpretation is recorded here so the archive can be read, taught, and audited without guesswork.

Maintainers' rule: when any code's meaning is revised, this file and its companion working record are updated together, so the reference never silently drifts from the archive's decision.
