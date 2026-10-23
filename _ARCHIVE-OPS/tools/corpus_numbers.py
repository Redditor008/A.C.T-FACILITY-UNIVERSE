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
    # A house bar narrower than the widest line in its own file reads as a broken
    # rule, so the bar must span the text it separates.
    r["TXT_NARROW_BAR_LINES"] = 0
    for p in tx:
        ls = read(p).split("\n")
        widest = max(
            (len(x) for x in ls if x.strip() and set(x.strip()) > set("═ ")),
            default=0,
        )
        r["TXT_NARROW_BAR_LINES"] += sum(
            1
            for x in ls
            if x.strip() and set(x.strip()) <= set("═") and len(x.strip()) < min(widest, 118)
        )
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
        if f.is_file()
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
