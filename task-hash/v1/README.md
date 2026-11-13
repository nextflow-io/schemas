# Task hash versions

A **task hash version** lists the keys that feed a task hash, and which fields of the
lineage `TaskRun` record carry each key. A lineage `TaskRun` record carries the id of the
version that produced its hash, in the `hashVersion` field.

A consumer that wants to explain why a task was not cached diffs two `TaskRun` records.
To do that honestly it needs to know which record fields feed the hash, and that set
changes over time. This directory is where it looks them up.

## Layout

| Path                     | What it holds                          |
| ------------------------ | -------------------------------------- |
| `schema.json`            | the shape of a spec file               |
| `specs/<family>-vN.json` | one published version, keyed by its id |
| `tests/`                 | schema test cases                      |

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

A record written before Nextflow recorded `hashVersion` is read with the `std/v2` mapping.
`std/v2` differs from `std/v1` only by `RESOURCES_BUNDLE`, which is not recorded, so every
recorded field maps the same way under both. For an older run, the only inaccuracy is that
`RESOURCES_BUNDLE` is reported as unseen when it was not hashed at all.

The global cache records its version from its first release, so this applies to `std` only.

## Publishing a new version

A new version is due when Nextflow adds or removes a key from the task hash, or records a
key in a different lineage field. Add `specs/<family>-v<N+1>.json` with the full key list,
and add a row to the table above. If it changes the mapping of a recorded field, records
with no version id can no longer all be read with one mapping, and need resolving from
the Nextflow version of their run.
