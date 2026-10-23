#!/bin/sh
# Batch bootstrap. Run this BEFORE the first edit of every batch.
#
# The workspace is re-cloned from scratch between turns, and the fresh clone
# creates the arena branch from local `main` rather than from
# `origin/<branch>`. Local history is therefore absent, not rewound. Editing
# before syncing produces a commit whose parent is the session base, which
# squashes the tree on push.
#
# STANDING RULE. Run this FIRST in every batch, before the first edit and
# before any commit. Never run it after a commit: it resets onto origin and
# would discard unpushed local work. The ahead-count guard below enforces
# that, but the rule is to not rely on the guard.
#
# Usage:  sh _ARCHIVE-OPS/tools/sync.sh
set -e

cd "$(dirname "$0")/../.."

BRANCH=$(git rev-parse --abbrev-ref HEAD)

# Owner ruling 2026-10-23: hard-refuse when HEAD sits on the session base.
# That is the exact state a re-clone leaves behind, and it was found mid-batch
# with 878 dirty entries showing every renamed top-level path as deleted. The
# pushed work was safe on origin the whole time, but any commit made in that
# state would have had the session base as its parent and squashed the tree on
# push. HISTORY_PARENT_IS_SESSION_BASE reports the condition after the fact;
# this stops before any edit is made.
SESSION_BASE="a17dfd048c8666ce55c1dc2363bc40a0cfa0bf80"
if [ "$(git rev-parse HEAD)" = "$SESSION_BASE" ]; then
    echo "REFUSED: HEAD is the session base $SESSION_BASE."
    echo "The workspace was re-cloned and local history is absent, not rewound."
    echo "Recover first, then re-run this script:"
    echo "  git fetch origin && git reset --hard origin/$BRANCH"
    exit 1
fi
BEFORE=$(git rev-parse HEAD)

git fetch -q origin

# Untracked files are allowed: a new tool must not block its own bootstrap.
# Modified or deleted tracked files are not, because reset --hard would eat them.
DIRTY=$(git status --porcelain --untracked-files=no)
if [ -n "$DIRTY" ]; then
    echo "REFUSED: tracked files are modified or deleted. Commit or stash first."
    echo "$DIRTY"
    exit 1
fi

# Never discard local commits. If local work has not been pushed, this script
# must stop rather than reset it away. This guard exists because the script
# destroyed an unpushed commit on its second run.
AHEAD=$(git rev-list --count "origin/$BRANCH..HEAD")
if [ "$AHEAD" != "0" ]; then
    echo "REFUSED: $AHEAD local commit(s) have not been pushed. Push them first."
    exit 1
fi

git reset --hard "origin/$BRANCH"
AFTER=$(git rev-parse HEAD)

echo "branch   $BRANCH"
echo "before   $BEFORE"
echo "after    $AFTER"
if [ "$BEFORE" != "$AFTER" ]; then
    echo "SYNCED: local history had drifted; it now matches origin."
else
    echo "in step with origin."
fi

python3 _ARCHIVE-OPS/tools/corpus_numbers.py

# Owner ruling 2026-10-23: re-prove the gates before any edit in the batch. A gate
# that reads 0 proves nothing on its own, and TXT_NARROW_BAR_LINES read 0 while
# 5,870 narrow bars sat in the corpus. gate_audit.py injects each defect into a
# scratch copy and exits with the count of gates that failed to fire, so a batch
# stops here rather than measuring with a blind instrument.
python3 _ARCHIVE-OPS/tools/gate_audit.py
AUDIT=$?
if [ "$AUDIT" -ne 0 ]; then
    echo "GATE AUDIT FAILED: $AUDIT gate(s) are blind. Fix corpus_numbers.py before editing."
    exit "$AUDIT"
fi
