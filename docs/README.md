# Documentation

This directory contains the MkDocs documentation for Nextflow Schemas.

## Building Documentation

### Install Dependencies

Using uv:

```bash
uv sync --extra docs
```

### Serve Locally

Start the development server:

```bash
uv run mkdocs serve
```

Then open your browser to `http://127.0.0.1:8000`

### Build Static Site

Generate static HTML:

```bash
uv run mkdocs build
```

Output will be in the `site/` directory.

## Deploy to GitHub Pages

```bash
uv run mkdocs gh-deploy
```

## Documentation Structure

```
docs/
├── index.md                          # Home page
├── getting-started/
│   ├── overview.md                   # Overview of the project
│   ├── installation.md               # Installation instructions
│   └── quick-start.md                # Quick start guide
├── schemas/
│   ├── pipeline-input.md             # Pipeline input schema reference
│   └── plugin.md                     # Plugin schema reference
├── development/
│   ├── contributing.md               # Contributing guidelines
│   ├── testing.md                    # Testing guide
│   └── ci-cd.md                      # CI/CD documentation
└── examples/
    ├── pipeline-input-examples.md    # Pipeline examples
    └── plugin-examples.md            # Plugin examples
```

## Writing Documentation

- Use GitHub-flavored Markdown
- Code blocks should specify language for syntax highlighting
- Use admonitions for notes, warnings, tips:

  ```markdown
  !!! note
  This is a note

  !!! warning
  This is a warning
  ```

- Cross-reference other pages with relative links
- Include practical examples where possible
