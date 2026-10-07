# Task hash versions

A **task hash version** describes how a task hash was computed: which keys were hashed,
in what order, how each value was encoded, and which hash function was applied. A lineage
`TaskRun` record carries the id of the version that produced its hash, in the
`hashVersion` field.

A consumer that wants to explain why a task was not cached diffs two `TaskRun` records.
To do that honestly it needs to know which record fields feed the hash, and that set
changes over time. This directory is where it looks them up.

## Layout

| Path                   | What it holds                                                               |
| ---------------------- | --------------------------------------------------------------------------- |
| `schema.json`           | the shape of a spec file                                                    |
| `specs/<family>-vN.M.json` | one published version, keyed by its id                                   |
| `legacy-releases.json`  | Nextflow release to version, for `std` records written before the id was recorded |
| `tests/`                | schema test cases                                                           |

There is no index of available versions, because nothing needs one: a record names its
version, so a consumer fetches `specs/std-v1.7.json` by that name.

## Families

The part of an id before the slash is the **family**: the hasher that produced it. Two
families can hash the same task to different values, so a consumer must read the whole
id, never the number alone.

| Family | Who writes it            | How it differs                                                                                      |
| ------ | ------------------------ | --------------------------------------------------------------------------------------------------- |
| `std`  | Nextflow itself          | the baseline                                                                                        |
| `glb`  | the Seqera global cache  | drops `SESSION_ID` and `PROCESS_NAME`, so a hash is shared across runs and pipelines; file inputs are hashed through the cache's file-identity strategy |

## Reading a spec

```json
{
  "key": "SPACK",
  "contributor": "spackEnvAndArch",
  "lineage": ["spack", "architecture"]
}
```

`lineage` names the fields of the lineage `TaskRun` record that carry this key. An empty
list means the key is not recorded at all, and a consumer must report it as unseen rather
than as unchanged.

Two versions can share a key set and still hash differently, because `encoding` decides
how a value is serialised before hashing. That is why a record carries a version id and
not just a list of fields.

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

The table covers `std` only. Other families do not need it, because they record their
version where it cannot be lost: a global cache stores it in the cache marker, and a
marker without one means the first version, `glb/v1.1`.

The table is generated from the Nextflow repository with `git tag --contains` on the
commit that ended each version, so a change backported into an older maintenance line
produces a correct table rather than one guessed from version ordering.

## Keeping these files true

A spec file is **frozen** once published, and is a byte-identical copy of the resource
shipped in the jar of whichever component owns the family. Editing one here changes the meaning of every task hash
already recorded under it, with no symptom a user could see.
