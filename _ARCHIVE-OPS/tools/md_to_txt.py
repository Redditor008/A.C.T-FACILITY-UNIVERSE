#!/usr/bin/env python3
"""Render the .txt twin of a technology record from its .md source.

House rules enforced here:
  * .txt twins carry NO markup at all - no backticks, no bold, no link syntax,
    no heading markers. Every line, INCLUDING TABLE CELLS, is passed through
    clean(). An earlier version of this converter cleaned prose and headings
    but sent cells straight to the box renderer, and backticks leaked.
  * Ordinary data renders as an ASCII box at house widths: two columns use
    [28, 87], three columns use [28, 43, 43]. Both total 118.
  * One H1 per document; the title stack collapses to plain lines.

Usage:  python3 md_to_txt.py <path-to-record.md> [more.md ...]
Writes <same-stem>.txt into the sibling TECH_TXT folder and reports the word
count, the line count, the widest line, and how many lines still carry markup.
A non-zero markup count is a failure and exits 1.
"""
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from engine import box  # noqa: E402

W2 = [28, 87]
W3 = [28, 43, 43]


def clean(s):
    """Strip every markdown construct the twin is not allowed to carry."""
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)          # bold
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", s)  # italics
    s = re.sub(r"`([^`]*)`", r"\1", s)              # code span
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)  # link -> short name only
    return s.rstrip()


def convert(md_path):
    src = md_path.read_text(encoding="utf-8").split("\n")
    out = []
    i = 0
    while i < len(src):
        ln = src[i]
        if ln.strip() == "---":                      # horizontal rule: drop
            i += 1
            continue
        if ln.startswith("|"):                       # pipe table -> ASCII box
            rows = []
            while i < len(src) and src[i].startswith("|"):
                cells = [clean(c) for c in src[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            n = len(rows[0])
            if n == 2:
                w = W2
            elif n == 3:
                w = W3
            else:
                raise SystemExit(
                    "unhandled column count %d in %s: %r" % (n, md_path.name, rows[0])
                )
            out.extend(box(rows[0], rows[1:], w))
            out.append("")
            continue
        if ln.startswith("```"):                     # code fence -> plain block
            i += 1
            while i < len(src) and not src[i].startswith("```"):
                out.append(clean(src[i]))
                i += 1
            i += 1
            out.append("")
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            lvl, txt = m.groups()
            if lvl == "##":
                out.append("")
            out.append(clean(txt))
            out.append("")
            i += 1
            continue
        out.append(clean(ln))
        i += 1
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def main(argv):
    if not argv:
        raise SystemExit(__doc__)
    failed = False
    for arg in argv:
        md = pathlib.Path(arg)
        txt = md.parent.parent / "TECH_TXT" / (md.stem + ".txt")
        txt.parent.mkdir(parents=True, exist_ok=True)
        body = convert(md)
        txt.write_text(body, encoding="utf-8")
        lines = body.splitlines()
        bad = [
            l for l in lines
            if "`" in l or "**" in l or "](" in l or l.lstrip().startswith("#")
        ]
        widest = max((len(l) for l in lines), default=0)
        print(
            "%s -> %s | %d words | %d lines | widest %d | markup lines %d"
            % (md.name, txt.name, len(body.split()), len(lines), widest, len(bad))
        )
        for l in bad[:5]:
            print("    MARKUP LEFT: %s" % l[:90])
        if bad or widest > 118:
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
