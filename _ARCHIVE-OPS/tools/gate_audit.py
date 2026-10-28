#!/usr/bin/env python3
"""Prove every defect gate in corpus_numbers.py actually fires.

A gate that reads 0 proves nothing on its own: it may be blind. On 2026-10-23
TXT_NARROW_BAR_LINES read 0 while 5,870 narrow bars sat in the corpus, because
its width test used set(x) > set("═ "), which tests proper superset rather than
"is not made only of bar characters". The 0 was an artefact of the bug, and a
figure quoted from it in a report had to be withdrawn.

This tool copies the corpus to a scratch directory, injects the exact defect
each gate claims to catch, and confirms the number moves. It never writes to the
real corpus. Run it after editing corpus_numbers.py.

    python3 _ARCHIVE-OPS/tools/gate_audit.py

Exit code is the number of blind gates, so a batch can fail on it.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
DOC = "A.C.T Universe Document"
MD = f"{DOC}/A.C.T .md Document/ACT_Facility_Archive_Overview.md"
TX = f"{DOC}/A.C.T .txt Document/ACT_Facility_Archive_Overview.txt"
TWIN = f"{DOC}/A.C.T Technology Document/TECH_TXT/TECH-ACT-047-Phase-Stable-Silicone.txt"
README = f"{DOC}/README.md"
WIDE = "word " * 40  # 200 characters, past the 118 limit


def resolve_target(repo: pathlib.Path, rel: str) -> pathlib.Path:
    """Locate an injection target, tolerating a folder reorganisation.

    Owner ruling 2026-10-25: the anomaly Log folders were divided into
    per-category subfolders and every injection target written as a flat Log
    path broke with FileNotFoundError, which aborts the whole suite instead of
    reporting one stale path. Targets stay written as full paths so the intent
    remains readable, but a missing path now falls back to a unique basename
    search inside the copied repo. An ambiguous or absent basename is a hard
    error, never a silent skip, because a suite that quietly tests nothing is
    the failure this file exists to prevent.
    """
    direct = repo / rel
    if direct.is_file():
        return direct
    hits = [p for p in repo.rglob(pathlib.Path(rel).name) if p.is_file()]
    if len(hits) != 1:
        raise SystemExit(
            f"injection target not resolvable: {rel} "
            f"({len(hits)} candidates for that basename)"
        )
    return hits[0]


def measure(work: pathlib.Path) -> dict[str, str]:
    out = subprocess.run(
        [sys.executable, "_ARCHIVE-OPS/tools/corpus_numbers.py"],
        capture_output=True, text=True, cwd=work,
    ).stdout
    return dict(l.split(" ", 1) for l in out.split("\n") if " " in l)


# (gate, target, kind, payload). kind: append text, strip the H1, double the
# trailing newline, or delete the file outright.
TEXT_TESTS = [
    ("RECORDS_NOT_ONE_H1", MD, "append", "\n\n# Second Heading\n"),
    ("RECORDS_ZERO_H1", MD, "strip_h1", None),
    ("BAD_EOF", MD, "dbl_nl", None),
    ("ODD_FENCE", MD, "append", "\n\n```text\nunclosed\n"),
    ("TXT_BOLD_FILES", TX, "append", "\n**bolded**\n"),
    ("TXT_LINK_FILES", TX, "append", "\nsee [x](http://example)\n"),
    ("TXT_BACKTICK_FILES", TX, "append", "\n`code`\n"),
    ("TXT_MD_HEADING_FILES", TX, "append", "\n## Heading\n"),
    ("TXT_MD_RULE_LINES", TX, "append", "\n---\n"),
    ("TXT_MD_ITALIC_SPANS", TX, "append", "\n*emphasised*\n"),
    # Any .txt line over 118, box rows included. The payload must exceed the limit
    # itself, which is the mistake an earlier wide-line injection made at 80 chars.
    ("TXT_LINES_OVER_118", TX, "append", "\n" + ("x" * 140) + "\n"),
    # A story twin that drifts from its .md. Target must be a twin whose .md
    # exists, or the gate has nothing to compare against.
    ("STORY_TWIN_WORD_DRIFT",
     f"{DOC}/ACT MAIN STORY/Chapters/Epilogue-00-The-Archive-Still-Breathes.txt",
     "append", "\n" + ("drift padding words " * 90) + "\n"),
    # Target must be a record the gate currently passes. Pointing this at a record
    # already counted made the audit call it blind: deleting a field from an
    # already-off-shape registry changes nothing.
    ("TECH_RECORDS_REGISTRY_OFF_SHAPE",
     "A.C.T Universe Document/A.C.T Technology Document/TECH_MD/"
     "TECH-GOI-072-1-Iron-Meridian-Suppression-Collar-and-Restraint-Harness.md",
     "drop_line", "TECHNOLOGY DESIGNATION"),
    # An entry heading that carries no date and no title still counts as an entry
    # but cannot be ordered or cited. Appended to the Patch Saver itself, which
    # lives under _ARCHIVE-OPS and so is skipped by the document-shape gates.
    ("PATCH_SAVER_ENTRIES_OFF_SHAPE",
     "_ARCHIVE-OPS/PATCH SAVER/Technology_Phase_Patch_Saver.md",
     "append", "\n## Prompt End Update, no date and no title\n"),
    ("BOXDRAW_CHARACTERS", TX, "append", "\n\u2550" * 3 + "\n"),
    # A narrow rule must sit alone to count: flanked by pipe rows it belongs to a
    # box and has to match those cells instead.
    ("TXT_NARROW_BAR_LINES", TX, "append", "\n+" + "-" * 48 + "+\n" + "x" * 100 + "\n"),
    ("DOUBLED_RULE_LINES", TX, "append", "\n+" + "=" * 48 + "+\n+" + "=" * 48 + "+\n"),
    ("THIN_READMES", "A.C.T Universe Document/ACT MAIN STORY/Outlines/README.md", "thin", None),
    ("TECH_RECORDS_UNDER_1800", "A.C.T Universe Document/A.C.T Technology Document/TECH_MD/TECH-ACT-001-Reality-Stabilization-Anchor-System.md", "truncate", None),
    ("MD_BOLD_IN_HEADING_LINES", MD, "append", "\n\n## **Bold Heading**\n"),
    ("TITLE_STACK_DOCUMENTS", MD, "stack", None),
    # Target must be a chapter the gate currently passes. Chapter 02 was
    # hand-verified clean with a highest shared word run of two, well under the
    # threshold of five, so an injected reworded duplicate has to be what fires it.
    # Target must be a chapter the gate currently passes. Chapter 12 was
    # hand-verified clean, so the injected line is what has to fire it.
    ("STORY_LOWERCASE_SENTENCE_STARTS",
     "A.C.T Universe Document/ACT MAIN STORY/Chapters/Chapter-12-The-Second-Self-Erasure.md",
     "append", "Filters changed. seal grids recalibrated. pressure lines held."),
    # A README the link gates currently pass. The payload points at a file that
    # does not exist, which is the exact defect a reader hits first.
    # An Experiment and Testing dossier that currently reads CATEGORY III, which
    # is correct. Flipping it to IV is the defect the gate exists to catch.
    # A house-form dossier that currently passes. Stripping the numbered section
    # headers is the flat shape the owner corrected, so this must fire.
    # A dossier whose category title currently matches the doctrine exactly.
    # Truncating it is the defect the substring clause used to miss, so it must fire.
    # A dossier carrying all four house-form markers. Stripping the purpose block
    # is the regression, so this must fire.
    ("LOG_MARKER_GAPS",
     "A.C.T Universe Document/A.C.T Anomaly Document/Anomaly Modern txt/Log/"
     "02-Interview-and-Testimony/Helping-Hand-Interview-Testimony-Dossier-AFD-SU-019.txt",
     "stripmarker", None),
    ("LOG_CATEGORY_MISMATCHES",
     "A.C.T Universe Document/A.C.T Anomaly Document/Anomaly Modern txt/Log/"
     "Circus-Monster-Recovered-Diary-Dossier-AFD-SU-507.txt",
     "trunclabel", None),
    ("LOG_HOUSE_FORM_DEFECTS",
     "A.C.T Universe Document/A.C.T Anomaly Document/Anomaly Legacy 01 .txt/Log/"
     "MACHINE-Heart-Transformation-Utilization-Dossier-AFD-OB-017.txt",
     "desect", None),
    ("LOG_CATEGORY_MISMATCHES",
     "A.C.T Universe Document/A.C.T Anomaly Document/Anomaly Legacy 01 .txt/Log/"
     "MACHINE-Heart-Experiment-Testing-Dossier-AFD-OB-017.txt",
     "recat", None),
    ("README_BROKEN_LINKS",
     "A.C.T Universe Document/Junior Handbook/README.md",
     "append", "[Missing](This-File-Does-Not-Exist.md)"),
    ("README_DEAD_ENDS",
     "A.C.T Universe Document/ACT MAIN STORY/Outlines/README.md",
     "strip_links", None),
    ("STORY_OPENING_REPEATS",
     "A.C.T Universe Document/ACT MAIN STORY/Chapters/Chapter-02-Wounds-in-the-Archive.md",
     "reword_dup", None),
    ("TXT_WIDE_PROSE_LINES", TX, "append", "\n" + WIDE + "\n"),
    ("MD_WIDE_PROSE_LINES", MD, "append", "\n" + WIDE + "\n"),
]
# A relocation rather than an edit. The Log folders are divided into
# per-category shelves, and the defect is a dossier standing in the wrong place,
# which no text injection can express.
MOVE_TESTS = [
    # A dossier correctly shelved under its category today. Lifting it back into
    # the flat Log root is the regression the shelf gate exists to catch.
    ("LOG_SHELF_MISMATCHES",
     "A.C.T Universe Document/A.C.T Anomaly Document/Anomaly Modern txt/Log/"
     "03-Experiment-and-Testing/Shadow-Shark-Experiment-Testing-Dossier-AFD-SU-010.txt",
     "up"),
]

DELETE_TESTS = [
    ("TECH_UNPAIRED_TWINS", TWIN),
    ("ROOT_FOLDERS_WITHOUT_README", README),
    ("FOLDERS_WITHOUT_README", "A.C.T Universe Document/ACT MAIN STORY/Characters/README.md"),
]


def main() -> int:
    work = pathlib.Path(tempfile.mkdtemp(prefix="gate_audit_"))
    try:
        shutil.copytree(ROOT, work / "repo", symlinks=True)
        repo = work / "repo"
        base = measure(repo)
        blind: list[str] = []
        print(f"{'GATE':34} {'BASE':>6} {'AFTER':>6}  VERDICT")
        print("-" * 62)
        for gate, rel, kind, payload in TEXT_TESTS:
            tgt = resolve_target(repo, rel)
            orig = tgt.read_text(encoding="utf-8")
            try:
                if kind == "truncate":
                    body = orig.split("\n")
                    tgt.write_text("\n".join(body[:40]), encoding="utf-8")
                elif kind == "thin":
                    tgt.write_text("# Outlines\n\nToo thin.\n", encoding="utf-8")
                elif kind == "repeat":
                    body = orig.split("\n\n")
                    tgt.write_text(
                        "\n\n".join(body[:2] + [body[1]] + body[2:]), encoding="utf-8"
                    )
                elif kind == "reword_dup":
                    # Insert a near-identical copy of the second paragraph with one
                    # word altered. An exact repeat would prove the gate fires; only
                    # a reworded copy proves it fires on paraphrase, which is the
                    # failure the previous exact-fragment version was blind to.
                    paras = orig.split("\n\n")
                    words = paras[1].split(" ")
                    words[len(words) // 2] = words[len(words) // 2] + "s"
                    tgt.write_text(
                        "\n\n".join(paras[:2] + [" ".join(words)] + paras[2:]),
                        encoding="utf-8",
                    )
                elif kind == "stripmarker":
                    # Remove a CATEGORY PURPOSE block. This is the regression the
                    # marker gate exists to catch: a dossier that has silently lost
                    # the statement of what it is for.
                    m = re.search(r"\n\nCATEGORY PURPOSE:\n(?:[^\n]+\n)+", orig)
                    tgt.write_text(orig.replace(m.group(0), "\n", 1), encoding="utf-8")
                elif kind == "trunclabel":
                    # Drop the trailing word Dossier from a DOCUMENT CATEGORY title.
                    # This is the exact defect 5 files carried by hand, which the
                    # substring comparison let through while reading 0.
                    tgt.write_text(
                        orig.replace(
                            "CATEGORY XII \u2014 Personal & Recovered Journal Dossier",
                            "CATEGORY XII \u2014 Personal & Recovered Journal",
                        ),
                        encoding="utf-8",
                    )
                elif kind == "desect":
                    # Remove the numbered SECTION headers, which is what turns a
                    # house-form dossier back into the flat generic shape the owner
                    # corrected. The body is left intact so only the structure goes.
                    tgt.write_text(
                        re.sub(r"SECTION\s+\d+\s*\u2014\s*", "SECTION \u2014 ", orig),
                        encoding="utf-8",
                    )
                elif kind == "recat":
                    # Swap the category number on the DOCUMENT CATEGORY line only.
                    # This is the exact defect the owner found by hand: an
                    # Experiment and Testing dossier claiming CATEGORY IV, which
                    # the doctrine reserves for Incident and Breach.
                    tgt.write_text(
                        re.sub(r"(DOCUMENT CATEGORY:\s*)CATEGORY\s+III",
                               r"\1CATEGORY IV", orig),
                        encoding="utf-8",
                    )
                elif kind == "strip_links":
                    # Remove every link and leave the words, which turns a README
                    # that points somewhere into one that describes and then stops.
                    tgt.write_text(
                        re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", orig), encoding="utf-8"
                    )
                elif kind == "stack":
                    body = orig.split("\n")
                    tgt.write_text(
                        body[0] + "\n\n## Stack A\n\n## Stack B\n\n" + "\n".join(body[1:]),
                        encoding="utf-8",
                    )
                elif kind == "append":
                    tgt.write_text(orig.rstrip("\n") + "\n" + payload, encoding="utf-8")
                elif kind == "drop_line":
                    # Remove every line containing the payload. Used to delete a
                    # registry field so the registry-shape gate has something to catch.
                    tgt.write_text(
                        "\n".join(l for l in orig.split("\n") if payload not in l),
                        encoding="utf-8",
                    )
                elif kind == "strip_h1":
                    tgt.write_text(
                        "\n".join(l for l in orig.split("\n") if not l.startswith("# ")),
                        encoding="utf-8",
                    )
                else:
                    tgt.write_text(orig.rstrip("\n") + "\n\n\n", encoding="utf-8")
                after = measure(repo).get(gate, "MISSING")
            finally:
                tgt.write_text(orig, encoding="utf-8")
            fired = after not in ("MISSING", base.get(gate))
            if not fired:
                blind.append(gate)
            print(f"{gate:34} {base.get(gate):>6} {after:>6}  {'FIRES' if fired else '*** BLIND ***'}")
        for gate, rel in DELETE_TESTS:
            tgt = resolve_target(repo, rel)
            bak = tgt.read_bytes()
            try:
                tgt.unlink()
                after = measure(repo).get(gate, "MISSING")
            finally:
                tgt.write_bytes(bak)
            fired = after not in ("MISSING", base.get(gate))
            if not fired:
                blind.append(gate)
            print(f"{gate:34} {base.get(gate):>6} {after:>6}  {'FIRES' if fired else '*** BLIND ***'}")
        for gate, rel, kind in MOVE_TESTS:
            tgt = resolve_target(repo, rel)
            dest = tgt.parent.parent / tgt.name
            tgt.rename(dest)
            try:
                after = measure(repo).get(gate, "MISSING")
            finally:
                dest.rename(tgt)
            fired = after not in ("MISSING", base.get(gate))
            if not fired:
                blind.append(gate)
            print(f"{gate:34} {base.get(gate):>6} {after:>6}  "
                  f"{'FIRES' if fired else '*** BLIND ***'}")
        total = len(TEXT_TESTS) + len(DELETE_TESTS) + len(MOVE_TESTS)
        print("-" * 62)
        print(f"gates tested {total} | fired {total - len(blind)} | blind {len(blind)}")
        if blind:
            print("blind gates: " + ", ".join(blind))
        return len(blind)
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
