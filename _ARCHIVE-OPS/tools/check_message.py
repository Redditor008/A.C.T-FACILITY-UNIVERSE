#!/usr/bin/env python3
"""Refuse a commit message that carries a number the verification block never produced.

Two commits in one session shipped figures drafted from expectation rather than from measurement:
one stated 1,177 words against a measured 1,153, another stated a drop to four against a measured
one. Both verification blocks printed the correct figures in the same command, above the push. A
rule in a markdown file did not prevent the second failure, because it was broken in the turn it
was written. This script is the mechanical version.

Usage:
    python3 _ARCHIVE-OPS/tools/check_message.py <verification-output-file> <message-file>

Exit status is 0 when every number in the message also appears in the verification output, and 1
when any does not. The failing numbers are printed so the message can be corrected rather than
guessed at.

Numbers are compared as bare digits, ignoring thousands separators and any surrounding units, so
"1,116 words" and "1116" match. Years, dates and designations are excluded by the same rule that
excludes them from being claims: a number attached to a slash or hyphen date, or part of a
designation pattern, is not a measured quantity.

Known limitation. The check cannot distinguish a claim about this change from a citation of a past
failure, because both are bare numbers. A message that quotes historical figures in order to
explain what this tool catches will be refused even when it is accurate. Where that happens the
figures belong in the working log, which is not checked, and the commit message stays to measured
claims only. This was found by running the tool against the message written to commit it.
"""

import re
import sys

# A measured quantity is a run of digits, optionally with thousands separators.
NUMBER = re.compile(r"(?<![\w./-])(\d{1,3}(?:,\d{3})+|\d+)(?![\w/])")

# Numbers that are not claims about the change and must not be checked.
IGNORE = re.compile(
    r"""
    \d{4}-\d{2}-\d{2}          # ISO dates
    | \d{2}/\d{2}/\d{4}        # archive dates
    | TECH-(?:ACT|GOI)-\d{3}   # designations
    | GOI-[A-Z]{2}-[A-Z]-\d{3}
    | AFD-[A-Z]{2}-\d{3}
    | SITE-\d{2}
    | \d+(?:\.\d+)?%           # percentages, which are derived rather than counted
    """,
    re.VERBOSE,
)


def numbers(text: str) -> set:
    """Every bare integer in the text, with thousands separators stripped."""
    masked = IGNORE.sub(" ", text)
    return {n.replace(",", "") for n in NUMBER.findall(masked)}


def check(verification: str, message: str):
    produced = numbers(verification)
    claimed = numbers(message)
    missing = sorted(claimed - produced, key=lambda n: (len(n), n))
    return produced, claimed, missing


# Labels the verification block is expected to carry, and that the message must therefore be able
# to quote. A message that omits every figure passes the original check trivially, which is how a
# commit was pushed with no numbers in it at all and nothing enforced.
REQUIRED_LABELS = ("md words", "DOCUMENT_COUNT")


def check_required(verification: str, message: str):
    """Report any expected label whose figure the message does not carry."""
    missing = []
    for label in REQUIRED_LABELS:
        m = re.search(re.escape(label) + r":\s*(\d+)", verification)
        if not m:
            continue
        if m.group(1) not in numbers(message):
            missing.append((label, m.group(1)))
    return missing


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    verification = open(argv[1], encoding="utf-8").read()
    message = open(argv[2], encoding="utf-8").read()
    produced, claimed, missing = check(verification, message)
    absent = check_required(verification, message)
    if absent and not missing:
        print("REFUSED: the message omits figures the verification block measured:")
        for label, value in absent:
            print("    %s = %s" % (label, value))
        print("\na message that quotes no figures passes the number check trivially and enforces")
        print("nothing. State the measured figures so they can be checked.")
        return 1
    if not missing:
        print("ok: %d number(s) in the message, all appear in the verification output" % len(claimed))
        return 0
    print("REFUSED: the message carries %d number(s) the verification output never produced:"
          % len(missing))
    for n in missing:
        print("    %s" % n)
    print("\nthe verification output produced these %d number(s):" % len(produced))
    print("    " + " ".join(sorted(produced, key=lambda n: (len(n), n))))
    print("\ncorrect the message from the verification output, or re-run the verification.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
