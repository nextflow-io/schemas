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
version, so a consumer fetches `specs/std-v1.json` by that name.

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

| Version     | Written by                                    | Keys                                          |
| ----------- | --------------------------------------------- | --------------------------------------------- |
| `std/v1`    | the first Nextflow release with `hashVersion` | the current task hash key set                 |
| `global/v1` | the Seqera global cache                       | `std/v1` without `SESSION_ID`, `PROCESS_NAME` |

Only versions that a record can name are published. The task hash changed before
`hashVersion` existed, and that history is kept below for reference rather than as specs.

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

A `std` record written before Nextflow recorded `hashVersion`, from 25.04.0 (the first
release with lineage) onwards, is read with the `std/v1` mapping. Some keys of `std/v1`
were not hashed by older releases, but the fields that carry them are also missing from
those records, so they are reported as unseen, never as changed.

| Releases                     | Task hash keys compared with `std/v1` | Lineage fields compared with `std/v1` |
| ---------------------------- | ------------------------------------- | ------------------------------------- |
| 25.04.0 to 25.06.0-edge      | no `EVAL_OUTPUTS`, `RESOURCES_BUNDLE` | no `eval`                             |
| 25.07.0-edge to 26.04.x      | no `RESOURCES_BUNDLE`                 | no `eval`                             |
| 26.05.0-edge to 26.07.0-edge | no `RESOURCES_BUNDLE`                 | same                                  |
| 26.08.0-edge onwards         | same                                  | same                                  |

`EVAL_OUTPUTS` entered the task hash in 25.07.0-edge, `eval` entered lineage in
26.05.0-edge (nextflow-io/nextflow#7211), and `RESOURCES_BUNDLE` entered the task hash in
26.08.0-edge (nextflow-io/nextflow#6914).

Two caveats about older records:

- 25.04.0 wrote lineage records without the `v1beta1` envelope, which arrived in 25.04.1.
  The `TaskRun` fields are the same, but the record does not match `lineage/v1beta1`.
- In a stub run before 26.05.0-edge, `codeChecksum` may not reflect the stub source
  (nextflow-io/nextflow#7211 fixed how it is read), so a change to the stub may not show
  in lineage.

The global cache records its version from its first release, so this applies to `std` only.

## Publishing a new version

A new version is due when Nextflow adds or removes a key from the task hash, or records a
key in a different lineage field. Add `specs/<family>-v<N+1>.json` with the full key list,
and add a row to the table above. Keys are listed in the order Nextflow adds them to the
task hash (`TaskHasher.compute()` for `std`), so a spec can be checked line by line against
the code. A consumer must not depend on the order. If it changes the mapping of a recorded field, records
with no version id can no longer all be read with one mapping, and need resolving from
the Nextflow version of their run.
