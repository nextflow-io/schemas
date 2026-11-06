#!/bin/bash
#
# Act on the output of check-sync.sh (SYNC_OUT dir, given as $1):
#   new/<spec>.json         -> open a PR publishing it, unless a PR for it ever existed
#   drift/<spec>.json.diff  -> open an issue, unless one is open for it
#
# Runs from a checkout of the default branch. Needs git and gh. DRY_RUN=1 prints instead.
# Refuses to act on the output of a check that did not finish.

set -euo pipefail
shopt -s nullglob

OUT=$1
[[ -f $OUT/complete ]] || { echo "The check did not finish: nothing to report" >&2; exit 1; }
BASE=$(git rev-parse --abbrev-ref HEAD)
SPECS=task-hash/v1/specs

run() {
  if [[ -n ${DRY_RUN:-} ]]; then
    echo "[dry-run] $*"
  else
    "$@"
  fi
}

for file in "$OUT"/new/*.json; do
  name=$(basename "$file")
  origin=$(cat "$file.origin")
  branch=task-hash-sync/${name%.json}
  # any PR, even a closed one: a closed PR means someone decided, so do not reopen it daily
  if [[ -n $(gh pr list --head "$branch" --state all --json number --jq '.[].number') ]]; then
    echo "PR for $name already exists"
    continue
  fi
  run git switch -c "$branch" "$BASE"
  run cp "$file" "$SPECS/$name"
  run git add "$SPECS/$name"
  run git commit -s -m "Publish task hash spec $name" -m "From $origin."
  run git push origin "$branch"
  run gh pr create --base "$BASE" --head "$branch" \
    --title "Publish task hash spec $name" \
    --body "$name is in $origin but not published here. Opened by the Task hash sync workflow."
  run git switch "$BASE"
done

for diff in "$OUT"/drift/*.json.diff; do
  name=$(basename "$diff" .diff)
  origin=$(cat "$OUT/drift/$name.origin")
  title="Published task hash spec $name differs from its producer"
  if [[ -n $(gh issue list --state open --search "\"$title\" in:title" --json number --jq '.[].number') ]]; then
    echo "Issue for $name already open"
    continue
  fi
  body=$(printf '%s\n\n```diff\n%s\n```\n\n%s\n' \
    "\`$SPECS/$name\` differs from the one in $origin." \
    "$(cat "$diff")" \
    "A published spec is frozen. Either the producer changed an existing version, which needs a new version id instead, or the file here was edited. Opened by the Task hash sync workflow.")
  run gh issue create --title "$title" --body "$body"
done
