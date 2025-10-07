# Overview

Nextflow Schemas is a collection of JSON Schema definitions used to validate Nextflow pipeline inputs and plugin specifications. These schemas ensure that your pipeline configurations and plugin definitions follow the correct structure and conventions.

## What Are JSON Schemas?

JSON Schema is a vocabulary that allows you to annotate and validate JSON documents. It provides a contract for your JSON data, describing:

- Required and optional properties
- Data types (string, number, boolean, etc.)
- Value constraints (min/max, patterns, enums)
- Property relationships and dependencies

## Why Use Nextflow Schemas?

### Pipeline Input Schema

The pipeline input schema helps you:

- **Define parameter specifications** for your Nextflow pipelines
- **Validate user inputs** before pipeline execution
- **Generate documentation** automatically from schema definitions
- **Group parameters** logically for better organization
- **Add custom validation rules** specific to Nextflow workflows

### Plugin Schema

The plugin schema enables you to:

- **Document plugin APIs** including functions and configuration options
- **Validate plugin specifications** during development
- **Generate reference documentation** for plugin users
- **Define configuration scopes** and their nested structure

## Schema Specifications

Both schemas follow the **JSON Schema Draft 2020-12** specification and include:

- Standard JSON Schema keywords (`type`, `enum`, `pattern`, etc.)
- Custom keywords specific to Nextflow requirements
- Comprehensive validation rules
- Support for nested definitions and references

## Use Cases

### For Pipeline Developers

- Validate pipeline parameter schemas during development
- Auto-generate parameter documentation
- Ensure consistent parameter naming and structure
- Validate user-provided input configurations

### For Plugin Developers

- Document plugin configuration options
- Define function signatures and return types
- Validate plugin specification files
- Generate API documentation

## Next Steps

- [Installation Guide](installation.md) - Set up validation tools
- [Quick Start](quick-start.md) - Create your first schema
- [Pipeline Input Schema Reference](../schemas/pipeline-input.md)
- [Plugin Schema Reference](../schemas/plugin.md)
