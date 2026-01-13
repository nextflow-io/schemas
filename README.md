# schemas

This repository contains the schemas used by Nextflow.

The following schemas are currently defined:

- `pipeline`: Schema for pipeline specs
- `plugin`: Schema for plugin specs

Each folder contains the schema (`schema.json`) and a `tests` folder with test cases.

## Development

### Prettier formatting

We use [Prettier](https://prettier.io/) to format all files in this repository.
We use [prek](https://prek.j178.dev/) to run Prettier on all files before committing.

To install the pre-commit hooks, run the following command:

```bash
prek install
```

To run Prettier on all files, run the following command:

```bash
prek run --all-files
```

### Building Documentation

Serve documentation locally:

```bash
uv sync --dev
uv run zensical serve
```

Then open `http://127.0.0.1:8000` in your browser.

### Testing schemas

Schemas can be tested against their test cases using Docker and the `validate-docker.sh` script.

```bash
./validate-docker.sh
```

It is automatically tested in GitHub Actions via the `test.yml` workflow.
