# A.C.T FACILITY ARCHIVE FILE
### TECHNOLOGY RECORD - INTAKE STAGING AND ROUTING SYSTEM

| REGISTRY FIELD | CURRENT VALUE |
|---|---|
| TECHNOLOGY DESIGNATION | TECH-ACT-091 |
| TECHNOLOGY NAME | Intake Staging and Routing System |
| SHORT NAME | ISRS |
| TECHNOLOGY FAMILY | INTAKE STAGING / LIMIT ASSESSMENT / ROUTE CONTROL |
| ORIGIN | GLASS ORCHARD RELAY F-2 INTAKE STAGING AREA |
| PRIMARY CONTROLLER | Processing Officer / Recovery Support Lead |
| ATTACHED DIVISIONS | Recovery Support, Security, Medical, Limited Archive |
| OPERATIONAL STATUS | ACTIVE / TRANSIENT ROUTING USE |
| RISK STATUS | MISROUTING / LIMIT FAILURE / UNDOCUMENTED MOVEMENT RISK |
| CLEARANCE REQUIRED | Level 3 for intake staging; Level 4 for high-threat refusal, emergency transit, or parent-site<br>routing override |

| REGISTRY FIELD | CURRENT VALUE |
|---|---|
| ARCHIVE STATUS | Active Intake Routing Technology Record |
| DISTRIBUTION | Glass Orchard Relay / Redwood Veil Complex / Recovery Support / Security / Medical<br>/ Limited Archive |
| AUTHORITY | Processing Officer, Recovery Support Lead, Sub-Site Chief, Redwood Veil Site Command, and Central Archive |

#### Archive Note
Intake Staging and Routing System is the ninety-first main A.C.T technology expanded into an
individual record. The
Glass Orchard Relay sub-site dossier defines the relay as an overflow hand for Redwood
Veil and identifies overflow
intake as one of its modern roles. The F-2 Processing and Staging Level dossier
identifies the intake staging area as
the floor space where recovered material from field operations is logged, assessed against relay
holding limits, and
routed to temporary holding cells, the vault below, or direct transfer preparation.

ISRS exists because the relay's first decision after receipt is not how to keep
an arrival. It is where the arrival is
allowed to go next.

Controlled label: **ISRS ROUTE-BEFORE-HOLD**.

Core operating rule:

```text
LOG FIRST, TEST LIMITS, ROUTE UNDER AUTHORITY.
```

---

## FUNCTION SUMMARY

The Intake Staging and Routing System is the F-2 procedural and physical technology that
receives recovered material,
exposed persons, field packets, and low-threat anomaly arrivals entering Glass Orchard Relay from recovery
operations.
It creates the first relay custody record, checks the arrival against the relay's limits,
assigns the next location,
and prevents material from moving through the floor without a record.

ISRS is separate from the Short-Term Holding Vault System. The vault holds. ISRS decides
whether holding is allowed,
where it occurs, and whether the item or person must instead move directly to
transfer preparation or parent-site
escalation. The system sits between the surface cover, witness processing, temporary holding cells, archive
buffering,
and the F-1 vault.

Approved roles include field arrival receipt, intake logging, threat-limit assessment, witness/object/person
separation, temporary cell routing, F-1 vault routing, direct transfer preparation, high-threat refusal, parent-site
notice, and chain-of-custody initiation.

---

## ORIGIN AND DEVELOPMENT

Glass Orchard Relay grew from witness routing into overflow intake because Redwood Veil's regional
operations created
too much traffic for every arrival to go straight to the parent core. That
growth required a disciplined intake
decision point. Without ISRS, the relay would have a dangerous gap between arrival and
custody: a few minutes where
something could be placed in the wrong room, assigned the wrong file, or normalized
before anyone had decided whether
the relay was permitted to hold it.

The F-2 dossier's staging discipline became the system's foundation: every item is logged, assessed
against relay
limits, and routed under documentation. ISRS is therefore not only a room but a
control method for refusing improper
custody.

---

## TECHNICAL SPECIFICATION

Figures below are restated from this record's component list and routing doctrine. Values the
archive does
not hold are marked NOT MEASURED and each is filed under OPEN QUESTIONS.

| ROUTING PARAMETER | VALUE |
|---|---|
| Receiving | field arrival receiving lane |
| Log | intake identity and object log |
| Checklist | relay limit checklist |
| Board | routing status board |
| Assignment | temporary holding cell assignment panel |
| Vault request | F-1 vault request terminal |
| Transfer | direct transfer preparation marker |
| Diversion | witness processing diversion card |
| Archive | archive packet attachment tray |
| Escalation | parent-site escalation line |
| Routes | local holding, direct transfer, witness route, refusal |
| Decision authority | processing officer within relay limits |
| Lane count | NOT MEASURED |
| Median routing time | NOT MEASURED |
| Misrouting events | NOT MEASURED |

Routing is the only point in a relay where a mistake is still cheap.
Once an item is inside a unit or on a
vehicle the relay has committed resources, staff, and reputation to the earlier judgement. The
limit
checklist therefore exists to be read before movement rather than consulted after arrival.

## PHYSICAL OR SYSTEM DESCRIPTION

An ISRS installation includes a receiving lane, intake desk, threat-limit checklist, routing board, transfer
preparation marker, temporary cell assignment controls, F-1 vault request line, witness diversion indicator, archive
packet tray, Security observation, and parent-site escalation terminal. The layout keeps arrival movement visible
without exposing the buried relay to the surface cover.

Known components include:

- field arrival receiving lane;
- intake identity and object log;
- relay limit checklist;
- routing status board;
- temporary holding cell assignment panel;
- F-1 vault request terminal;
- direct transfer preparation marker;
- witness processing diversion card;
- archive packet attachment tray;
- parent-site escalation line.

The system treats uncertainty as a routing condition, not permission to improvise.

---

## INTERFACE AND OPERATING ENVELOPE

### Routing Controls

- field arrival receiving lane
- routing status board
- F-1 vault request terminal
- parent-site escalation line

### Routing Readouts

- intake identity and object log entries
- relay limit checklist results
- temporary holding cell assignments
- direct transfer preparation markers

### Routing And Personnel Limits

- Do not route before the limit checklist is complete.
- Do not move an item on an undocumented decision.
- Do not accept a high-threat item the relay cannot hold.
- Do not divert a witness without the diversion card raised.
- Weakest against arrivals with incomplete field paperwork.
- Weakest against simultaneous arrivals at one lane.

Lane count, routing time, and misrouting rate are NOT MEASURED.

## OPERATING PROCEDURE

### Numbered Operating Sequence

The sequence closes only when the item has physically moved, not when the decision
was taken. The relay has
repeatedly found that intentions and movements diverge most often under intake load.

1. Receive the arrival in the lane and log identity and object.
2. Read the relay limit checklist against the field report.
3. Post the provisional route on the routing status board.
4. Raise the diversion card if a witness is present.
5. Request a vault unit or mark direct transfer preparation.
6. Attach the archive packet at the attachment tray.
7. Escalate to the parent site if any limit fails.
8. Close the routing record once the item has physically moved.

Step 8 is deliberately last. A routing record closed at decision time records an
intention, and an intention
cannot be reconciled against a floor position when somebody later asks where the item
actually went.

On receipt, ISRS staff record source team, arrival time, field condition, provisional threat category,
required
environment, witness relation, medical need, archive attachments, and parent-site instruction. Security confirms
containment posture and access boundary. Medical reviews living arrivals. Limited Archive opens or attaches
the
temporary file.

The Processing Officer assigns a route: witness processing, temporary holding cell, F-1 vault, direct
transfer
preparation, archive buffering, or immediate parent-site escalation. If the arrival exceeds relay limits, ISRS
must
refuse local holding and request transfer under maximum procedural restriction. No item or person
leaves intake
staging without a route entry.

---

## SERVICING AND CALIBRATION

| INTERVAL | TASK |
|---|---|
| Each arrival | complete the checklist before any movement |
| Daily | reconcile the status board with physical locations |
| Weekly | compare diversion cards with processing records |
| Monthly | audit routing records for undocumented moves |
| Quarterly | rehearse a high-threat refusal at the lane |

Board-to-floor reconciliation is the meaningful check here. The board is a claim about where
things are, and
the relay's routing errors have almost always been visible on that comparison before they
became visible
anywhere else.

## FAULT ISOLATION

| SYMPTOM | PROBABLE CAUSE | REQUIRED ACTION |
|---|---|---|
| Item moved without a record | Board updated after the movement | Stop the lane, reconstruct the routing record |
| Checklist incomplete at routing | Field report missing a limit field | Return to the lane, escalate if needed |
| Vault request refused | No unit available at F-1 | Escalate before holding the item locally |
| Witness not diverted | Diversion card not raised | Stop processing, notify the medical lead |
| Two routes posted at once | Simultaneous arrivals at one lane | Split the lane and sequence the decisions |

## KNOWN LIMITS

ISRS depends on early information that may be incomplete. Field reports may be wrong,
calm objects may become active,
witnesses may hide exposure, and low-threat categories may fail under relay conditions. The system
also depends on
staff remembering that fast routing is not safe routing unless the record moves with
the arrival.

Known failure modes include wrong route assignment, missing archive attachment, witness/object confusion, temporary
cell overuse, F-1 vault request delay, unmarked medical risk, high-threat material accepted as low-threat,
direct
transfer without custody record, and parent-site escalation after movement has already occurred.

---

## FAILURE HISTORY

### ISRS-Overflow Intake Formation
The Glass Orchard dossier records overflow intake as a modern role of the relay.
ISRS was formalized when simple
recovery handoff proved insufficient for the number of distinct paths through F-2.

### ISRS-Route Mismatch Drill
A drill sent a recovered object toward temporary holding before its file showed a
direct transfer order. Current
procedure requires the route board and archive packet to match before movement.

### ISRS-High-Threat Refusal Review
A simulated low-threat arrival escalated during intake. Current doctrine requires rejection criteria to be
checked
before any local holding assignment is accepted.

---

## DIVISION USE

Recovery Support delivers field arrivals and receives routing orders. Security controls the receiving lane
and
movement boundary. Medical evaluates living arrivals and witness injuries. Limited Archive attaches records and
opens
custody files. The Processing Officer owns the route decision until Redwood Veil overrides it.

ISRS doctrine holds that the relay is safest when the first answer is a
route, not a room.

---

## CROSS-REFERENCES

- ACT-SUB-01-US-W Glass Orchard Relay Sub-Site Dossier;
- ACT-SUB-01-US-W-F-2 Processing and Staging Level Floor Dossier;
- ACT-SUB-01-US-W-F-1 Short-Term Holding Vault Floor Dossier;
- TECH-ACT-088 — Short-Term Holding Vault System;
- TECH-ACT-089 — Witness Processing and Sanitation Suites;
- TECH-ACT-090 — Archive Relay Buffering Area;
- Glass Orchard intake routing boards [restricted].

---

## OPEN QUESTIONS

- Which field signs should force direct parent-site escalation before local intake completes?
- Can an object exploit routing delay better than holding delay?
- Should witness-related objects always follow the witness processing route first?
- How much uncertainty is acceptable before temporary holding becomes forbidden?
- Can repeated direct-transfer events expose the relay's low-visibility logistics?
- When does a routing error become a containment failure rather than paperwork failure?

- Which field signs should force escalation before intake finishes?
- How long may an item wait in the lane before a route is
  forced?
- Should every routing error be treated as a containment failure?

---

## FILE METADATA

- **Created:** 2002-12-15
- **Author Desk:** Processing Officer / Recovery Support Lead / Central Archive
- **Review Status:** Active intake routing record; live route boards, rejection criteria, and
  parent-site escalation contacts censored
- **Next Review:** After any misrouting, undocumented movement, high-threat refusal, intake overload,
  file mismatch, or parent-site routing dispute
