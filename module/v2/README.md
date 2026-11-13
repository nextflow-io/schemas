# Module spec schema v2

Schema for the `meta.yml` of modules written as [typed processes](https://docs.seqera.io/nextflow/process-typed) or typed workflows. Modules written with legacy (DSL2) processes use [`v1`](../v1/schema.json), which is frozen.

## Changes from v1

- Types are Nextflow types (`Path?`, `List<Path>`, `Channel<Sample>`) instead of a fixed vocabulary (`file`, `channel`).
- Nullability is part of the type (`Path?`). There is no `optional` flag.
- Records and tuples are objects with `fields` / `components` instead of nested lists.
- Topic entries have the same shape as outputs, with `topic` instead of `name`.
- Record and enum types used by the interface are declared in `types`.
- Objects reject unknown keys, except extension keys prefixed with `x-`.

## Entries

Inputs, outputs, record fields, tuple components and topic values are all described by an entry:

| Key           | Description                                                                                                 |
| ------------- | ----------------------------------------------------------------------------------------------------------- |
| `name`        | Name of the input, output, field or component. Omitted for destructured inputs and a single unnamed output. |
| `topic`       | Name of the topic channel (topic entries only, instead of `name`).                                          |
| `type`        | Nextflow type. A trailing `?` marks the type as nullable.                                                   |
| `description` | Human-readable description (required).                                                                      |
| `pattern`     | Glob pattern of the file name(s), for `Path`-like types.                                                    |
| `ontologies`  | Ontology terms, e.g. EDAM formats.                                                                          |
| `fields`      | Fields of a record. Requires `type: Record`.                                                                |
| `components`  | Components of a tuple, in order. Requires `type: Tuple`.                                                    |

A record can be described inline (`type: Record` with `fields`) or by referencing a type declared in `types` (`type: Sample`).

## Example

```nextflow
nextflow.enable.types = true

record Sample {
    id: String
    fastq_1: Path
    fastq_2: Path?
}

process FASTQC {
    input:
    sample: Sample

    output:
    record(id: sample.id, html: file('*.html'))

    topic:
    tuple('fastqc', eval('fastqc --version')) >> 'versions'

    script:
    // ...
}
```

```yaml
$schema: https://raw.githubusercontent.com/nextflow-io/schemas/main/module/v2/schema.json
name: nf-core/fastqc
version: 1.0.0
description: Run FastQC on sequenced reads
license: MIT
input:
  - name: sample
    type: Sample
    description: Sample to check
output:
  - type: Record
    description: FastQC report
    fields:
      - name: id
        type: String
        description: Sample identifier
      - name: html
        type: Path
        description: FastQC HTML report
        pattern: "*.html"
topics:
  - topic: versions
    type: Tuple
    description: FastQC version
    components:
      - type: String
        description: Tool name
      - type: String
        description: Tool version
types:
  - name: Sample
    kind: record
    description: A sequenced sample
    fields:
      - name: id
        type: String
        description: Sample identifier
      - name: fastq_1
        type: Path
        description: Read 1
      - name: fastq_2
        type: Path?
        description: Read 2, for paired-end samples
```

## Checks outside the schema

JSON Schema can't express these, so tools such as `nextflow module validate` are expected to check them:

- every type name is a standard type or declared in `types`
- field names are unique within a record
- inputs and outputs are named, except destructured inputs and a single unnamed output
- names and types match the module script
