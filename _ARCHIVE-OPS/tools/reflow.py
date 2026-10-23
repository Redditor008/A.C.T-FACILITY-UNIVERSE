#!/usr/bin/env python3
"""Balanced re-wrap of wrapped prose paragraphs only.

The house limit is 118 characters. Greedy wrapping strands the last few words of a
paragraph on a line of their own, and across a long document that reads as a crooked
edge with words jumping down. A single stranded character is the extreme case.

This tool touches ONLY runs that are already a wrapped paragraph: consecutive lines
that are full, ending in one short line. Everything else keeps its own line, because
line breaks in this corpus carry meaning — a registry field, a list item, a box row
and a rule are each one line and must stay one line.

An earlier version of this tool joined every run of consecutive non-blank lines and
destroyed the metadata registry in the plain-text twins. The narrow rule below exists
because of that.
"""
from __future__ import annotations

import pathlib
import re
import sys

MAXC = 118
# A line at or above this many characters is "full": it was filled by the wrapper
# rather than written short on purpose.
FULL_AT = 88
# A trailing line at or below this many characters is what the eye reads as a jump.
ORPHAN_AT = 30

BOX_START = ("|", "+")
SKIP_START = ("#", ">", "`")
LIST_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")


def is_rule(line: str) -> bool:
    s = line.strip()
    return bool(s) and set(s) <= set("-=─━═╌╍┅")


def is_own_line(line: str) -> bool:
    """True when this line must never be joined to its neighbours."""
    s = line.strip()
    if not s:
        return True
    if s.startswith(BOX_START) or s.startswith(SKIP_START):
        return True
    if is_rule(s) or set(s) <= set("|-: "):
        return True
    if LIST_RE.match(line):
        return True
    # A registry field such as "Designation: TECH-GOI-070-2".
    if re.match(r"^[A-Za-z][A-Za-z /&'()\-]{2,32}:\s", s):
        return True
    return False


# NOTE ON SPAN TOKENISATION. An earlier version treated a bold span, a code span
# and a markdown link as unbreakable units. Splitting around them and rejoining
# with spaces corrupted the text: "[ BLANK ]" became "[]", which is a canonical
# term the owner ruled must never be rewritten, and "(\u0060QU\u0060)" became
# "( \u0060QU\u0060)". Balancing alone removes most orphans without touching a
# single character of content, so the units are plain words again.
def _greedy(units: list[str], width: int) -> list[str]:
    out: list[str] = []
    cur = ""
    for w in units:
        if cur and len(cur) + 1 + len(w) > width:
            out.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        out.append(cur)
    return out


def balance(units: list[str], width: int) -> list[str]:
    """Wrap to at most ``width``, evening the lines out."""
    if not units:
        return []
    base = _greedy(units, width)
    if len(base) <= 1 or any(len(w) > width for w in units):
        return base
    lo, hi = 1, width
    while lo < hi:
        mid = (lo + hi) // 2
        if len(_greedy(units, mid)) <= len(base):
            hi = mid
        else:
            lo = mid + 1
    return _greedy(units, lo)


def reflow(text: str) -> tuple[str, int]:
    lines = text.split("\n")
    out: list[str] = []
    fixed = 0
    i = 0
    in_fence = False
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if in_fence or is_own_line(line) or len(line) < FULL_AT:
            out.append(line)
            i += 1
            continue
        # Start of a candidate: a full line. Collect full lines, then one short tail.
        start = i
        while i < len(lines) and not is_own_line(lines[i]) and len(lines[i]) >= FULL_AT:
            i += 1
        tail = None
        if i < len(lines):
            cand = lines[i]
            if (
                not is_own_line(cand)
                and cand.strip()
                and len(cand.strip()) <= ORPHAN_AT
            ):
                tail = cand
                i += 1
        block = lines[start:i - 1] if tail is not None else lines[start:i]
        if tail is None or len(block) < 1:
            out.extend(lines[start:i])
            continue
        indent_m = re.match(r"^(\s+)", block[0])
        indent = indent_m.group(1) if indent_m else ""
        units = " ".join(x.strip() for x in block + [tail]).split()
        new = balance(units, MAXC - len(indent))
        if len(new) < len(block) + 1:
            fixed += 1
        out.extend(indent + s for s in new)
    return "\n".join(out), fixed


def main(paths: list[str] | None = None) -> int:
    if paths:
        files = [pathlib.Path(p) for p in paths]
    else:
        files = [
            p
            for p in pathlib.Path(".").rglob("*")
            if p.is_file()
            and p.suffix in (".md", ".txt")
            and ".git" not in p.parts
            and ".arena" not in p.parts
        ]
    n_files = 0
    n_fixed = 0
    for p in files:
        old = p.read_text(encoding="utf-8", errors="replace")
        new, fixed = reflow(old)
        if new != old:
            p.write_text(new.rstrip("\n") + "\n", encoding="utf-8")
            n_files += 1
            n_fixed += fixed
    print(f"rebalanced {n_files} files, {n_fixed} orphan paragraphs fixed")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or None))
