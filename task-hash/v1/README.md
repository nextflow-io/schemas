# Task hash versions

A **task hash version** lists the keys that feed a task hash, and which fields of the
lineage `TaskRun` record carry each key. A lineage `TaskRun` record carries the id of the
version that produced its hash, in the `hashVersion` field.

A consumer that wants to explain why a task was not cached diffs two `TaskRun` records.
To do that honestly it needs to know which record fields feed the hash, and that set
changes over time. This directory is where it looks them up.

## Layout

| Path                     | What it holds                                                                     |
| ------------------------ | --------------------------------------------------------------------------------- |
| `schema.json`            | the shape of a spec file                                                          |
| `specs/<family>-vN.json` | one published version, keyed by its id                                            |
| `legacy-releases.json`   | Nextflow release to version, for `std` records written before the id was recorded |
| `tests/`                 | schema test cases                                                                 |

There is no index of available versions, because nothing needs one: a record names its
version, so a consumer fetches `specs/std-v2.json` by that name.

## Families

The part of an id before the slash is the **family**: the hasher that produced it. Two
families can hash the same task to different values, so a consumer must read the whole
id, never the number alone.

| Family   | Who writes it           | How it differs                                                                       |
| -------- | ----------------------- | ------------------------------------------------------------------------------------ |
| `std`    | Nextflow itself         | the baseline                                                                         |
| `global` | the Seqera global cache | drops `SESSION_ID` and `PROCESS_NAME`, so a hash is shared across runs and pipelines |

## Versions

A version is a set of keys and their lineage mapping, nothing more. Any change to either
is a new version, numbered with the next integer in its family. A published spec is never
edited.

| Version     | Releases                | Change                                        |
| ----------- | ----------------------- | --------------------------------------------- |
| `std/v1`    | 25.10.0 to 26.07.0-edge | the baseline                                  |
| `std/v2`    | 26.08.0-edge onwards    | adds `RESOURCES_BUNDLE` (#6914)               |
| `global/v1` | Seqera global cache     | `std/v2` without `SESSION_ID`, `PROCESS_NAME` |

## Reading a spec

```json
{
  "key": "SPACK",
  "lineage": ["spack", "architecture"]
}
```

`lineage` names the fields of the lineage `TaskRun` record that carry this key. An empty
list means the key is not recorded at all, and a consumer must report it as unseen rather
than as unchanged. A field that a record predates is missing from it, and must be treated
the same way.

## Comparing two records

For each key, compare the fields that carry it in each record:

- a field that differs explains the cache miss;
- a key that one record does not record is reported as unseen;
- a key that only one of the two versions has is reported as such.

Nextflow can change how it hashes a key's value without changing the key set, so two
hashes can differ while every recorded field is equal. This only happens across Nextflow
versions, and the version difference is then the explanation.

## Records with no version id

A `std` record written before Nextflow recorded the id is resolved from the Nextflow
version of its run, through `legacy-releases.json`. Four things about that lookup matter:

- It applies only where no id can exist. A record that names its version is always
  resolved from the record.
- The answer is **inferred**, not asserted. A patched or vendored build reports a version
  whose hasher may not be the one it used.
- Releases are listed exactly, never as ranges. A release that is not listed returns no
  answer rather than the answer of its neighbour.
- Anything before 25.10.0 cannot be identified and returns nothing.

The table covers `std` only. The global cache records its version from its first release.

The table is generated from the Nextflow repository: a release maps to the newest version
whose first commit it contains (`git tag --contains <commit>`), so a change backported into
an older maintenance line produces a correct table rather than one guessed from version
ordering. Releases are appended until Nextflow records `hashVersion`, after which the table
is frozen.

## Publishing a new version

A new version is due when Nextflow adds or removes a key from the task hash, or records a
key in a different lineage field. Add `specs/<family>-v<N+1>.json` with the full key list,
and add a row to the table above.
