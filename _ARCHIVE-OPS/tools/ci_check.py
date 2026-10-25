#!/usr/bin/env python3
"""Fail the build when any tracked corpus defect figure is non-zero.

Runs corpus_numbers.py and reads its `KEY value` output, one pair per line. Only the keys in
DEFECTS are enforced. Scale figures such as DOCUMENT_COUNT are reported but never
fail the build, and the three figures accepted by owner ruling are excluded here
rather than being quietly deleted from the audit: MD_WIDE_LINK_LINES counts
atomic link targets, WIDEST_LINE_ANY_FILE tracks with those, and
DOCTRINE_WITH_CONTENTS reads 24 of 29 because five documents are forms and
fragments where a contents block would be wrong.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent

DEFECTS = [
    "BAD_EOF", "BOXDRAW_CHARACTERS",
    "DOUBLED_RULE_LINES", "FOLDERS_WITHOUT_README", "HISTORY_PARENT_IS_SESSION_BASE", "LOG_CATEGORY_MISMATCHES", "LOG_HOUSE_FORM_DEFECTS",
    "MD_BOLD_IN_HEADING_LINES", "MD_WIDE_PROSE_LINES", "ODD_FENCE",
    "PATCH_SAVER_ENTRIES_OFF_SHAPE", "README_BROKEN_LINKS", "README_DEAD_ENDS",
    "READMES_WITHOUT_SECTIONS", "RECORDS_NOT_ONE_H1", "RECORDS_ZERO_H1",
    "ROOT_FOLDERS_WITHOUT_README", "STORY_LOWERCASE_SENTENCE_STARTS",
    "STORY_MANUSCRIPT_LOCKSTEP_FAILURES", "STORY_OPENING_REPEATS",
    "STORY_PARTS_UNDER_1500", "STORY_TWIN_WORD_DRIFT", "TECH_RECORDS_OFF_SHAPE",
    "TECH_RECORDS_REGISTRY_OFF_SHAPE", "TECH_RECORDS_UNDER_1800",
    "TECH_UNPAIRED_TWINS", "THIN_READMES", "TITLE_STACK_DOCUMENTS",
    "TXT_BACKTICK_FILES", "TXT_BOLD_FILES", "TXT_LINK_FILES",
    "TXT_LINES_OVER_118", "TXT_MD_HEADING_FILES", "TXT_MD_ITALIC_SPANS",
    "TXT_MD_RULE_LINES", "TXT_NARROW_BAR_LINES", "TXT_WIDE_PROSE_LINES",
]


def main() -> int:
    out = subprocess.run(
        [sys.executable, str(HERE / "corpus_numbers.py")],
        capture_output=True, text=True,
    ).stdout
    vals = {
        m.group(1): int(m.group(2))
        for m in re.finditer(r"^(\w+)\s+(-?\d+)$", out, re.M)
    }
    missing = [k for k in DEFECTS if k not in vals]
    if missing:
        print("CI CHECK INCOMPLETE: corpus_numbers.py did not report these keys:")
        for k in missing:
            print("   ", k)
        return 1
    bad = {k: vals[k] for k in DEFECTS if vals[k] != 0}
    for k in sorted(DEFECTS):
        flag = "OK  " if vals[k] == 0 else "FAIL"
        print(f"  {flag} {k} {vals[k]}")
    print(f"\ndefect keys checked: {len(DEFECTS)}")
    if bad:
        print(f"FAILING: {len(bad)} -> {sorted(bad)}")
        return 1
    print("all defect keys read 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
