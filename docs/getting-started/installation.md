# Installation

This guide will help you set up the tools needed to work with Nextflow schemas.

## Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)
- Docker (optional, for containerized validation)

## Installing uv

If you don't have uv installed, install it using:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Installation Methods

### Option 1: Using uv (Recommended)

Clone the repository and install dependencies:

```bash
git clone https://github.com/nextflow-io/schemas.git
cd schemas
uv sync
```

This will install all development dependencies including `check-jsonschema` for validation.

### Option 2: Install Validation Tool Only

If you only need the validation tool:

```bash
uv pip install check-jsonschema
```

Or using pip:

```bash
pip install check-jsonschema
```

### Option 3: Using Docker

No local installation required. Just use the provided Docker validation script:

```bash
./validate-docker.sh
```

## Installing Pre-commit Hooks

To automatically format JSON files on commit:

```bash
# Install pre-commit
uv pip install pre-commit

# Set up git hooks
pre-commit install
```

Now Prettier will automatically format your JSON files when you commit.

## Building Documentation

To build and serve this documentation locally:

```bash
# Install docs dependencies
uv sync --extra docs

# Serve documentation locally
uv run mkdocs serve
```

Then open your browser to `http://127.0.0.1:8000`

## Verifying Installation

Test that everything is working:

```bash
# Validate schemas
./validate.sh

# Should output:
# ✅ All schemas are valid
# ✅ All test cases passed
```

## Editor Integration

### VS Code

Install the [JSON Schema Store](https://marketplace.visualstudio.com/items?itemName=remcohaszing.schemastore) extension for automatic schema validation and autocomplete.

Add to your workspace settings (`.vscode/settings.json`):

```json
{
  "json.schemas": [
    {
      "fileMatch": ["**/pipeline-input/**/*.json"],
      "url": "./pipeline-input/schema.json"
    },
    {
      "fileMatch": ["**/plugin/**/*.json"],
      "url": "./plugin/schema.json"
    }
  ]
}
```

### JetBrains IDEs (IntelliJ, PyCharm, etc.)

JetBrains IDEs have built-in JSON Schema support. Configure schemas via:

1. Go to **Settings** → **Languages & Frameworks** → **Schemas and DTDs** → **JSON Schema Mappings**
2. Add mappings for each schema file

## Troubleshooting

### Permission Denied on Scripts

Make validation scripts executable:

```bash
chmod +x validate.sh validate-docker.sh
```

### Python Version Issues

Ensure you're using Python 3.8+:

```bash
python --version
```

### Docker Issues

If Docker validation fails, ensure Docker is running:

```bash
docker ps
```

## Next Steps

- [Quick Start Guide](quick-start.md)
- [Pipeline Input Schema Reference](../schemas/pipeline-input.md)
- [Contributing Guidelines](../development/contributing.md)
