#!/usr/bin/env python3
"""Measure every figure the Patch Saver and memos quote, and print it.

Anything a report cites must appear here first. A figure that cannot be measured
by this script is not a figure the archive may state.
"""
from __future__ import annotations

import collections
import pathlib
import re
import sys

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
    r["TXT_WIDE_PROSE_LINES"] = sum(
        1
        for p in tx
        for line in read(p).split("\n")
        if len(line) > 118
        and not line.lstrip().startswith(("|", "+", "-", "*", "#", "=", "`", ">"))
    )
    r["MD_WIDE_PROSE_LINES"] = sum(
        1
        for p in md
        for line in read(p).split("\n")
        if len(line) > 118
        and not line.lstrip().startswith(("|", "+", "-", "*", "#", "=", "`", ">"))
    )

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

    for key, value in r.items():
        print(f"{key} {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
