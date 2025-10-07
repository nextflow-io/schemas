# Nextflow Schemas

Welcome to the Nextflow Schemas documentation. This repository contains JSON schemas used by Nextflow for validating pipeline inputs and plugin specifications.

## Overview

This repository provides two main schemas:

- **[Pipeline Input Schema](schemas/pipeline-input.md)**: Validates Nextflow pipeline input specifications, including parameter definitions, validation rules, and parameter grouping
- **[Plugin Schema](schemas/plugin.md)**: Validates Nextflow plugin specifications, including configuration scopes and function definitions

## Key Features

- ✅ **JSON Schema Draft 2020-12** compliant
- 🔍 **Comprehensive validation** for pipeline inputs and plugins
- 🧪 **Extensive test suite** with valid and invalid examples
- 🤖 **CI/CD integration** for automated validation
- 📚 **Well-documented** with examples and guides

## Quick Links

- [Getting Started](getting-started/overview.md)
- [Pipeline Input Schema Reference](schemas/pipeline-input.md)
- [Plugin Schema Reference](schemas/plugin.md)
- [Contributing Guidelines](development/contributing.md)
- [GitHub Repository](https://github.com/nextflow-io/schemas)

## Installation

Install the validation tools using uv:

```bash
uv sync --extra docs
```

Or install just the validation dependencies:

```bash
uv pip install check-jsonschema
```

## Quick Validation

Validate your schema files:

```bash
# Using the provided script
./validate.sh

# Or using Docker
./validate-docker.sh
```

## Community

- Report issues on [GitHub Issues](https://github.com/nextflow-io/schemas/issues)
- Join the [Nextflow Community](https://www.nextflow.io/community.html)
- Follow [@nextflow_io](https://twitter.com/nextflow_io) on Twitter
