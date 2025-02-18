# schema-spec

This repository contains the specification of the Nextflow schema.

## Schema

The `parameters_meta_schema.json` file describes the structure of the `nextflow_schema.json` file.

## Development

### Prettier formatting

We use [Prettier](https://prettier.io/) to format all files in this repository.
We use [pre-commit](https://pre-commit.com/) to run Prettier on all files before committing.

To install the pre-commit hooks, run the following command:

```bash
pre-commit install
```

To run Prettier on all files, run the following command:

```bash
pre-commit run --all-files
```

This is done automatically when committing.

### Testing the meta-schema

The meta-schema can be tested against a set of test schemas located in the `test_schemas` directory using docker and the `validate.sh` script.

```bash
./validate.sh
```

It is automatically tested in GitHub Actions via the `test-meta-schema.yml` workflow.
