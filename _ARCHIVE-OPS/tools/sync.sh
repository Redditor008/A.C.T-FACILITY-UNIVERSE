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
