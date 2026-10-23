#!/usr/bin/env python3
"""Measure every figure the Patch Saver and memos quote, and print it.

Anything a report cites must appear here first. A figure that cannot be measured
by this script is not a figure the archive may state.
"""
from __future__ import annotations

import collections
import pathlib
import re
import subprocess
import sys

# A silent workspace reset takes local history back to this commit and wipes
# scratch folders. HISTORY_PARENT_IS_SESSION_BASE 1 means the working tree has
# been reset since the last push and must be recovered before any commit.
SESSION_BASE = "a17dfd048c8666ce55c1dc2363bc40a0cfa0bf80"

ROOT = pathlib.Path(__file__).resolve().parents[2]
DOC = ROOT / "A.C.T Universe Document"
TECH_MD = DOC / "A.C.T Technology Document" / "TECH_MD"
TECH_TXT = DOC / "A.C.T Technology Document" / "TECH_TXT"
GOI = DOC / "A.C.T GOI Document"
ANOM = DOC / "A.C.T Anomaly Document"
STORY = DOC / "ACT MAIN STORY"
DOCTRINE = DOC / "A.C.T .md Document"
PATCH = ROOT / "_ARCHIVE-OPS" / "PATCH SAVER" / "Technology_Phase_Patch_Saver.md"

SKIP_PARTS = (".git", ".arena", "_ARCHIVE-OPS")


def texts(include_ops: bool = False) -> list[pathlib.Path]:
    """Every Markdown and plain-text file in the archive.

    ``DOCUMENT_COUNT`` is the figure every report quotes and it counts the
    whole tree, backstage folders included. ``include_ops=False`` narrows to
    the reader-facing documents only, which is what the defect gates run over.
    """
    skip = (".git", ".arena") if include_ops else SKIP_PARTS
    out = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix not in (".md", ".txt"):
            continue
        if any(part in skip for part in p.parts):
            continue
        out.append(p)
    return out


def read(p: pathlib.Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    files = texts()
    md = [p for p in files if p.suffix == ".md"]
    tx = [p for p in files if p.suffix == ".txt"]
    r: "collections.OrderedDict[str, object]" = collections.OrderedDict()

    r["DOCUMENT_COUNT"] = len(texts(include_ops=True))
    r["DOCUMENT_COUNT_EX_OPS"] = len(files)
    r["MD_FILES"] = len(md)
    r["TXT_FILES"] = len(tx)
    r["RECORDS_NOT_ONE_H1"] = sum(
        1 for p in md if len(re.findall(r"^# ", read(p), re.M)) != 1
    )
    r["RECORDS_ZERO_H1"] = sum(
        1 for p in md if len(re.findall(r"^# ", read(p), re.M)) == 0
    )
    r["BAD_EOF"] = sum(
        1 for p in files if not read(p).endswith("\n") or read(p).endswith("\n\n")
    )
    r["ODD_FENCE"] = sum(1 for p in files if read(p).count("\n```") % 2)
    r["TXT_BOLD_FILES"] = sum(1 for p in tx if "**" in read(p))
    r["TXT_LINK_FILES"] = sum(1 for p in tx if "](" in read(p))
    r["TXT_BACKTICK_FILES"] = sum(1 for p in tx if "`" in read(p))
    r["TXT_MD_HEADING_FILES"] = sum(
        1 for p in tx if re.search(r"^#{1,6} ", read(p), re.M)
    )
    # The four gates above never caught the markdown that was actually leaking.
    # TXT_BOLD/LINK/BACKTICK/HEADING all read 0 on 2026-10-23 while 3,584 markdown
    # horizontal rules and 93 markdown italics spans sat in the corpus. A gate is
    # only as good as the pattern it checks, so these two close that hole:
    # a bare --- line is a markdown rule (the house bar is 71 box characters), and
    # a single-asterisk pair is markdown italics. In-world notation is exempt:
    # ^_* is a stage direction in the MAGICAL MEW lyric scripts and a lone * is a
    # scene break, so only paired spans on one line count.
    # Owner ruling 2026-10-23: the corpus carries no box-drawing characters at all.
    # Every rule and box is ASCII, so a stray ═ or ╔ is a regression.
    boxdraw = "\u2550\u2551\u2554\u2557\u255a\u255d"
    r["BOXDRAW_CHARACTERS"] = sum(
        read(p).count(c) for p in files for c in boxdraw
    )
    r["TXT_MD_RULE_LINES"] = sum(
        1
        for p in tx
        for line in read(p).split("\n")
        if re.match(r"^[ \t]*(---+|\*\*\*+|___+)[ \t]*$", line)
    )
    r["TXT_MD_ITALIC_SPANS"] = sum(
        1
        for p in tx
        for m in re.finditer(r"(?<!\*)\*(?!\s)([^*\n]{1,120}?)(?<!\s)\*(?!\*)", read(p))
    )
    # A rule narrower than the widest line in its own file reads as a broken rule,
    # so it must span the text it separates. Owner ruling 2026-10-23: measure the
    # file's own max character count per row first, then size every rule to it.
    # Covers both the box-bar form and the ASCII +---+ form.
    #
    # This gate shipped blind on its first draft. It used set(x) > set("═ "),
    # which tests proper superset, not "is not made only of bar characters", so
    # widest collapsed to its 0 default and the comparison could never fire. The
    # injection audit caught it: the gate read 0 against a file holding a
    # 9-character bar over 100 characters of text.
    # Owner ruling 2026-10-23: two box separators in a row is a defect. 25 of them
    # sat unnoticed in 4 GOI records until they were counted by hand, which is the
    # whole argument for a gate: a defect nobody counts stays a defect.
    # Owner ruling 2026-10-24: a markdown heading is already emphasised, so bold
    # markup inside one is redundant and renders literally in some viewers. 131 of
    # them sat across 13 files, found only because a newcomer read turned up one.
    # Owner ruling 2026-10-24: an H1 immediately followed by 2 or more sibling H2s
    # with no prose between makes one document appear in a table of contents as
    # several separate entries. A newcomer read found one instance by hand; scanning
    # the shape found 60. The shape is the defect, so the gate tests the shape.
    # Owner ruling 2026-10-24: a chapter whose opening tells the same beat twice.
    # Seven chapters carried a leftover paragraph from the RULE 3.1 opening rewrite,
    # where the new opening was prepended and the old one never removed. The
    # manuscript lockstep gate could not see it: the manuscript carried the same
    # duplication, so the two still agreed.
    r["STORY_OPENING_REPEATS"] = 0
    for p in sorted(STORY.glob("Chapters/*.md")):
        body = re.sub(r"^#.*$", "", read(p), flags=re.M).strip()
        sents = [
            re.sub(r"\s+", " ", s).strip()
            for s in re.split(r"(?<=[.!?])\s+", body)
            if len(s.strip()) > 40
        ][:6]
        found = False
        for i in range(len(sents)):
            for j in range(i + 1, len(sents)):
                for k in range(min(30, len(sents[i]) - 24)):
                    frag = sents[i][k : k + 24]
                    if (frag in sents[j][:60]
                            and not frag.startswith(("the ", "and ", "of the"))):
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if found:
            r["STORY_OPENING_REPEATS"] += 1
    r["TITLE_STACK_DOCUMENTS"] = 0
    for p in md:
        ls = read(p).split("\n")
        if not ls or not ls[0].startswith("# "):
            continue
        i = 1
        stack = 0
        while i < len(ls):
            s = ls[i].strip()
            if not s:
                i += 1
                continue
            if s.startswith("## ") and not s.startswith("### "):
                stack += 1
                i += 1
                continue
            break
        if stack >= 2:
            r["TITLE_STACK_DOCUMENTS"] += 1
    r["MD_BOLD_IN_HEADING_LINES"] = sum(
        1
        for p in md
        for line in read(p).split("\n")
        if re.match(r"^#{1,6} ", line) and "**" in line
    )
    # Owner ruling 2026-10-24: GitHub renders a folder's README as its landing page,
    # so every folder needs one. ROOT_FOLDERS_WITHOUT_README only ever tested the
    # top level and read 0 while 24 nested folders had nothing.
    _skip = {".git", ".arena", "Logo", "docs", "node_modules"}
    # Owner ruling 2026-10-24: a README that renders is not the same as a README
    # worth reading. The first 24 were generated with a correct shape and nothing to
    # say, and no gate complained because none tested quality.
    r["THIN_READMES"] = 0
    r["READMES_WITHOUT_SECTIONS"] = 0
    for p in ROOT.rglob("README.md"):
        if any(part in {".git", ".arena"} for part in p.parts):
            continue
        body = read(p)
        if len(body.split()) < 40:
            r["THIN_READMES"] += 1
        if not re.search(r"^## ", body, re.M):
            r["READMES_WITHOUT_SECTIONS"] += 1
    r["FOLDERS_WITHOUT_README"] = 0
    for d in ROOT.rglob("*"):
        if not d.is_dir() or any(part in _skip for part in d.parts):
            continue
        if not any((d / n).exists() for n in ("README.md", "readme.md", "README.txt", "README")):
            r["FOLDERS_WITHOUT_README"] += 1
    r["DOUBLED_RULE_LINES"] = 0
    for p in files:
        ls = read(p).split("\n")
        for a, b in zip(ls, ls[1:]):
            if (a.strip() and set(a.strip()) <= set("+= ") and "=" in a
                    and b.strip() and set(b.strip()) <= set("+= ") and "=" in b):
                r["DOUBLED_RULE_LINES"] += 1
    r["TXT_NARROW_BAR_LINES"] = 0
    rule_chars = set("═+- ")
    for p in tx:
        ls = read(p).split("\n")
        widest = max(
            (len(x) for x in ls if x.strip() and not set(x.strip()) <= rule_chars),
            default=0,
        )
        for i, x in enumerate(ls):
            if not (x.strip() and set(x.strip()) <= rule_chars and {"═", "-"} & set(x.strip())):
                continue
            # A rule flanked by pipe cell rows belongs to a box and must match the
            # width of those cells, not the width of the file. Only a standalone
            # separator is required to span the text it divides.
            above = ls[i - 1].strip() if i else ""
            below = ls[i + 1].strip() if i + 1 < len(ls) else ""
            if above.startswith("|") or below.startswith("|"):
                continue
            # Below 40 characters a rule is a small label frame, not a separator.
            if len(x.strip()) >= 40 and len(x.strip()) < min(widest, 118):
                r["TXT_NARROW_BAR_LINES"] += 1
    r["TXT_WIDE_PROSE_LINES"] = sum(
        1
        for p in tx
        for line in read(p).split("\n")
        if len(line) > 118
        and not line.lstrip().startswith(("|", "+", "-", "*", "#", "=", "`", ">"))
    )
    # A wide line carrying a link target is atomic and cannot be wrapped without
    # breaking the link, so it is counted apart from wide prose. Owner ruling:
    # links are written as [Short Name](GitHub blob URL) and the URL length is
    # accepted. Prose over the limit is still a defect.
    wide_link = 0
    wide_prose = 0
    for p in md:
        for line in read(p).split("\n"):
            if len(line) <= 118 or line.lstrip().startswith(
                ("|", "+", "-", "*", "#", "=", "`", ">")
            ):
                continue
            if "](" in line:
                wide_link += 1
            else:
                wide_prose += 1
    r["MD_WIDE_LINK_LINES"] = wide_link
    r["MD_WIDE_PROSE_LINES"] = wide_prose

    tmd = sorted(p for p in TECH_MD.iterdir() if p.is_file() and p.suffix == ".md")
    ttx = sorted(p for p in TECH_TXT.iterdir() if p.is_file() and p.suffix == ".txt")
    r["TECH_MD_FILES"] = len(tmd)
    r["TECH_TXT_FILES"] = len(ttx)
    r["TECH_RECORDS"] = len(tmd) - 2
    # Owner ruling 2026-10-24: the house record shape is 14 named H2s in a fixed
    # order and 1,800 to 2,600 words. Nine records sat below the floor and one was
    # off-shape, and both were found by hand-listing rather than by a gate.
    HOUSE_H2 = [
        "FUNCTION SUMMARY", "ORIGIN AND CUSTODY", "PHYSICAL OR SYSTEM DESCRIPTION",
        "TECHNICAL SPECIFICATION", "INTERFACE AND OPERATING ENVELOPE", "OPERATING PROCEDURE",
        "SERVICING AND CALIBRATION", "FAULT ISOLATION", "KNOWN LIMITS", "FAILURE HISTORY",
        "DIVISION USE", "CROSS-REFERENCES", "OPEN QUESTIONS", "FILE METADATA",
    ]
    r["TECH_RECORDS_UNDER_1800"] = 0
    r["TECH_RECORDS_OFF_SHAPE"] = 0
    for f in tmd:
        # The record template is a scaffold, not a record: it is short by design and
        # names every section without filling it in. Counting it made both gates
        # report a defect that is not one.
        if f.name == "README.md" or f.name.startswith("00_"):
            continue
        body = read(f)
        if len(body.split()) < 1800:
            r["TECH_RECORDS_UNDER_1800"] += 1
        heads = [h.strip() for h in re.findall(r"^## (.+)$", body, re.M)]
        # Match on the leading phrase, not the exact string. 123 records carry the
        # origin section as ORIGIN AND DEPLOYMENT, ORIGIN AND DOCTRINE or ORIGIN AND
        # DEVELOPMENT, and an exact-name test reported all of them as missing a
        # section they plainly have. The first reading of this gate gave 131
        # off-shape records when the real count is far lower.
        # Key on the FIRST WORD only. The previous fix keyed on the phrase before
        # " AND ", which handled ORIGIN AND DEPLOYMENT but still missed FUNCTION
        # OUTLINE against FUNCTION SUMMARY, leaving 33 records falsely flagged.
        # A section is present when a heading opens with the same first word.
        def present(want):
            key = want.split()[0]
            return any(h.split()[0] == key for h in heads if h.split())
        if any(not present(h) for h in HOUSE_H2):
            r["TECH_RECORDS_OFF_SHAPE"] += 1

    r["TECH_UNPAIRED_TWINS"] = len({p.stem for p in tmd} ^ {p.stem for p in ttx})

    goi_md = [p for p in GOI.rglob("*") if p.is_file() and p.suffix == ".md"]
    r["GOI_MD_FILES"] = len(goi_md)
    # GOI_MD_FILES counts every Markdown file under the GOI folder, READMEs,
    # templates and format notes included. GOI_DOSSIERS counts the dossiers
    # themselves, which is the figure the root README quotes.
    r["GOI_DOSSIERS"] = len(
        [
            p
            for p in goi_md
            if re.match(r"GOI-[A-Z]{2}-[A-Z]-\d{3}", p.stem)
        ]
    )
    letters: "collections.Counter[str]" = collections.Counter()
    for p in GOI.rglob("*"):
        if p.is_file() and p.suffix in (".md", ".txt"):
            for m in re.finditer(r"GOI-([A-Z]{2})-([A-Z])-\d{3}", p.name):
                letters[m.group(2)] += 1
    r["GOI_ALIGNMENT_LETTERS"] = len(letters)
    r["GOI_LETTER_TALLY"] = " ".join(f"{k}{letters[k]}" for k in sorted(letters))

    anom = [
        p
        for p in ANOM.rglob("*")
        if p.is_file()
        and p.suffix in (".md", ".txt")
        and p.name != "ANOMALY_RECORD_INDEX.md"
    ]
    r["ANOMALY_FILES"] = len(anom)

    doc_md = [
        p
        for p in DOCTRINE.rglob("*.md")
        if p.is_file() and p.name != "README.md" and "Dossier" not in str(p.parent)
    ]
    r["DOCTRINE_MD_FILES"] = len(doc_md)
    r["DOCTRINE_WITH_CONTENTS"] = sum(1 for p in doc_md if "## Contents" in read(p))

    r["PATCH_SAVER_ENTRIES"] = len(
        re.findall(r"^## Prompt (?:Start|End) Update", read(PATCH), re.M)
    )
    r["PATCH_SAVER_WORDS"] = len(read(PATCH).split())

    # Story gates. The house rules live in
    # _ARCHIVE-OPS/STORY WRITING RULE/Unified-Narrative-Writing-Rules-for-AI-updated.md.
    # RULE 0.10 sets a 1,500-word floor per part. RULE 3.1 requires a chapter to open
    # on action or dialogue. The lockstep gate keeps the manuscript and the chapters
    # agreeing, because editing one without the other is how the drift happened.
    chap_files = sorted(
        f
        for f in (STORY / "Chapters").glob("*.md")
        # A folder README is navigation, not a chapter. Adding Chapters/README.md
        # for GitHub made the lockstep gate count it as a thirteenth chapter and
        # report a failure that was not there.
        if f.is_file() and f.name != "README.md"
    ) if (STORY / "Chapters").is_dir() else []
    r["STORY_PARTS_UNDER_1500"] = sum(
        1 for f in chap_files if len(read(f).split()) < 1500
    )
    action_open = 0
    for f in chap_files:
        if not f.stem.startswith("Chapter-"):
            continue
        body = [line for line in read(f).split("\n") if line.strip()]
        if len(body) < 2:
            continue
        first = body[1].strip()
        # Dialogue, or a named subject doing something. Irregular past tenses are
        # listed because a regex on \w+ed alone missed "wrote" and "read" and
        # reported two compliant chapters as violations.
        if first.startswith(('"', "“")) or re.match(
            r"^(She|He|Sera|Someone|The order|The clerk|The reviewer)\s+"
            r"(?:\w+ed|wrote|read|said|went|sat|stood|took|put|ran|held|kept|found|left)\b",
            first,
        ):
            action_open += 1
    r["STORY_CHAPTERS_TOTAL"] = sum(
        1 for f in chap_files if f.stem.startswith("Chapter-")
    )
    r["STORY_CHAPTERS_ACTION_OPEN"] = action_open

    ms = sorted(STORY.glob("01-*.md"))
    lockstep = -1
    if ms and chap_files:
        mstext = read(ms[0])
        agree = 0
        for f in chap_files:
            body = [line for line in read(f).split("\n") if line.strip()]
            if len(body) < 2:
                continue
            opener = " ".join(body[1].split())[:60]
            if opener in " ".join(mstext.split()):
                agree += 1
        lockstep = len(chap_files) - agree
    r["STORY_MANUSCRIPT_LOCKSTEP_FAILURES"] = lockstep

    chap_dir = STORY / "Chapters"
    chapters = (
        [p for p in chap_dir.rglob("*.md") if p.is_file()]
        if chap_dir.is_dir()
        else []
    )
    r["STORY_CHAPTER_MD_FILES"] = len(chapters)

    width = 0
    for p in files:
        for line in read(p).split("\n"):
            width = max(width, len(line))
    r["WIDEST_LINE_ANY_FILE"] = width

    # A root folder holding documents with no README gives a newcomer a bare file
    # listing and no orientation. Reported as a count, not a failure, because some
    # folders are legitimately backstage.
    r["ROOT_FOLDERS_WITHOUT_README"] = sum(
        1
        for d in sorted(ROOT.iterdir())
        if d.is_dir()
        and not d.name.startswith((".", "_"))
        and not (d / "README.md").is_file()
        and any(
            f.is_file() and f.suffix in (".md", ".txt") for f in d.rglob("*")
        )
    )

    r["HISTORY_PARENT_IS_SESSION_BASE"] = history_reset()

    for key, value in r.items():
        print(f"{key} {value}")
    bad = r["HISTORY_PARENT_IS_SESSION_BASE"]
    if bad:
        print("REFUSED: local HEAD sits on the session base. Recover before committing.")
        return 1
    return 0


def _git(*args: str) -> str:
    try:
        return subprocess.run(
            ["git", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        ).stdout.strip()
    except OSError:
        return ""


def history_reset() -> int:
    """1 when a reset has taken local history back to the session base."""
    parent = _git("rev-parse", "HEAD~1")
    if parent != SESSION_BASE:
        return 0
    branch = _git("rev-parse", "--abbrev-ref", "HEAD")
    remote = _git("rev-parse", f"origin/{branch}") if branch else ""
    return 1 if remote and remote != SESSION_BASE else 0


if __name__ == "__main__":
    sys.exit(main())
