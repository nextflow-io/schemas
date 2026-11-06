#!/bin/bash
#
# Compare the task hash specs of each producer with the ones published in specs/.
# Exit 1 when a published spec differs from the producer's. A producer spec that is not
# published yet is reported, not failed. A spec published here but not in the producer is fine.
# Any other exit code is an error of the check itself.
#
# Producers:
#   std  Nextflow master: a new version is published before it is released
#        (override: NEXTFLOW_REF=<git ref>)
#   glb  xpack-platform plugin, newest release: its source is private
#        (override: XPACK_ZIP=<local plugin zip>)
#
# With SYNC_OUT=<dir>, writes new/<spec>.json and drift/<spec>.json.diff, each with a
# <file>.origin naming the producer, for the workflow to open a PR or an issue. It writes
# <dir>/complete only when the check ran to the end.
#
# Needs curl, jq and unzip. Set GITHUB_TOKEN to avoid the GitHub API rate limit.

set -euo pipefail

SPECS="$(cd "$(dirname "$0")" && pwd)/specs"
WORK=$(mktemp -d)
trap 'rm -rf "$WORK"' EXIT
OUT=${SYNC_OUT:-}
[[ -z $OUT ]] || mkdir -p "$OUT/new" "$OUT/drift"
failed=0

gh_api() {
  curl -fsSL ${GITHUB_TOKEN:+-H "Authorization: Bearer $GITHUB_TOKEN"} "https://api.github.com/$1"
}

# HTTP status of a GitHub API path, body saved to $2
gh_status() {
  curl -sSL -o "$2" -w '%{http_code}' ${GITHUB_TOKEN:+-H "Authorization: Bearer $GITHUB_TOKEN"} "https://api.github.com/$1"
}

# compare <family> <dir with the producer spec files> <where they came from>
compare() {
  local family=$1 dir=$2 origin=$3 found=0
  for released in "$dir"/"$family"-v*.json; do
    [[ -e $released ]] || continue
    found=1
    local name=$(basename "$released")
    if [[ ! -f $SPECS/$name ]]; then
      echo "+ $name is in $origin but not published"
      if [[ -n $OUT ]]; then
        cp "$released" "$OUT/new/"
        echo "$origin" > "$OUT/new/$name.origin"
      fi
    elif ! cmp -s "$released" "$SPECS/$name"; then
      echo "✗ $name differs from $origin"
      diff -u --label "published $name" --label "producer $name" "$SPECS/$name" "$released" | tee ${OUT:+"$OUT/drift/$name.diff"} || true
      [[ -z $OUT ]] || echo "$origin" > "$OUT/drift/$name.origin"
      failed=1
    else
      echo "✓ $name"
    fi
  done
  # none yet is not an error: no build writes this family yet
  (( found )) || echo "- no $family specs in $origin yet"
}

# std: the spec resources in the Nextflow source, which is what the jar ships
check_std() {
  local ref=${NEXTFLOW_REF:-master} sha
  # resolved once, so every file comes from the same commit; a missing ref fails here
  # rather than reading as "no specs yet" below
  sha=$(gh_api "repos/nextflow-io/nextflow/commits/$ref" | jq -er .sha)
  local origin="Nextflow $ref (${sha:0:9})"
  local path=modules/nextflow/src/main/resources/nextflow/processor/hash
  local dir=$WORK/std
  mkdir -p "$dir"
  echo "std: $origin"
  local files=$WORK/std.json status
  status=$(gh_status "repos/nextflow-io/nextflow/contents/$path?ref=$sha" "$files")
  if [[ $status == 404 ]]; then
    echo "- no $path in $origin yet"
    return
  elif [[ $status != 200 ]]; then
    echo "GitHub API returned $status for $origin" >&2
    exit 2
  fi
  for url in $(jq -r '.[] | select(.name | test("^std-v.*\\.json$")) | .download_url' "$files"); do
    curl -fsSL -o "$dir/$(basename "$url")" "$url"
  done
  compare std "$dir" "$origin"
}

# glb: the spec resources inside the plugin zip published in the Nextflow plugin registry
check_glb() {
  local zip=${XPACK_ZIP:-}
  local origin="xpack-platform $zip"
  if [[ -z $zip ]]; then
    local release url scope token
    release=$(curl -fsSL https://registry.nextflow.io/api/v1/plugins/xpack-platform | jq -e '.plugin.releases[0]')
    url=$(jq -er .url <<<"$release")
    origin="xpack-platform $(jq -r .version <<<"$release")"
    # the registry serves plugins from an OCI registry, which wants an anonymous pull token
    scope=$(sed -E 's#https://[^/]+/v2/(.*)/blobs/.*#\1#' <<<"$url")
    token=$(curl -fsSL "https://auth.cr.seqera.io/auth/token?service=public.cr.seqera.io&scope=repository:$scope:pull" | jq -er '.token // .access_token')
    zip=$WORK/xpack-platform.zip
    curl -fsSL -H "Authorization: Bearer $token" -o "$zip" "$url"
  fi
  echo "glb: $origin"
  local dir=$WORK/glb
  mkdir -p "$dir"
  unzip -Z1 "$zip" | grep -E '(^|/)glb-v[^/]*\.json$' | while read -r entry; do
    unzip -p "$zip" "$entry" > "$dir/$(basename "$entry")"
  done || true
  compare glb "$dir" "$origin"
}

check_std
echo
check_glb

[[ -z $OUT ]] || touch "$OUT/complete"
exit $failed
