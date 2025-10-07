# Quick Start

Get started with Nextflow schemas in minutes.

## Creating a Pipeline Input Schema

Here's a minimal example of a pipeline input schema:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/my-pipeline/schema.json",
  "title": "My Pipeline Parameters",
  "description": "Input parameters for my Nextflow pipeline",
  "type": "object",
  "properties": {
    "input": {
      "type": "string",
      "format": "file-path",
      "description": "Path to input file",
      "help_text": "Provide the path to your input data file"
    },
    "outdir": {
      "type": "string",
      "format": "directory-path",
      "description": "Output directory",
      "default": "./results"
    }
  }
}
```

### With Parameter Groups

Organize parameters into logical groups using `$defs`:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/my-pipeline/schema.json",
  "title": "My Pipeline Parameters",
  "description": "Input parameters for my Nextflow pipeline",
  "type": "object",
  "$defs": {
    "input_options": {
      "title": "Input Options",
      "type": "object",
      "fa_icon": "fas fa-file-import",
      "description": "Parameters for input data",
      "properties": {
        "input": {
          "type": "string",
          "format": "file-path",
          "description": "Path to input file"
        }
      }
    },
    "output_options": {
      "title": "Output Options",
      "type": "object",
      "fa_icon": "fas fa-folder-open",
      "description": "Parameters for output",
      "properties": {
        "outdir": {
          "type": "string",
          "format": "directory-path",
          "description": "Output directory",
          "default": "./results"
        }
      }
    }
  },
  "allOf": [
    { "$ref": "#/$defs/input_options" },
    { "$ref": "#/$defs/output_options" }
  ]
}
```

## Creating a Plugin Schema

Here's a simple plugin schema example:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json",
  "definitions": [
    {
      "type": "ConfigScope",
      "spec": {
        "name": "myPlugin",
        "description": "Configuration for my plugin",
        "children": [
          {
            "type": "ConfigOption",
            "spec": {
              "name": "enabled",
              "description": "Enable the plugin",
              "type": "Boolean"
            }
          },
          {
            "type": "ConfigOption",
            "spec": {
              "name": "timeout",
              "description": "Timeout in seconds",
              "type": "Integer"
            }
          }
        ]
      }
    },
    {
      "type": "Function",
      "spec": {
        "name": "processData",
        "description": "Process input data",
        "returnType": "Map",
        "parameters": [
          {
            "name": "data",
            "type": "String"
          }
        ]
      }
    }
  ]
}
```

## Validating Your Schema

### Using the Validation Script

```bash
# Validate all schemas and tests
./validate.sh
```

### Validate a Specific File

```bash
# Validate against pipeline-input schema
check-jsonschema --schemafile pipeline-input/schema.json my-params.json

# Validate against plugin schema
check-jsonschema --schemafile plugin/schema.json my-plugin.json
```

### Expected Output

✅ **Success:**

```
ok -- validation done, no errors
```

❌ **Failure:**

```
ValidationError: 'type' is a required property
```

## Testing Your Schema

Add test cases to verify your schema works correctly:

### Valid Test Case

Create `tests/valid_example.json`:

```json
{
  "input": "/path/to/data.txt",
  "outdir": "./results"
}
```

### Invalid Test Case

Create `tests/invalid_missing_type.json`:

```json
{
  "input": 123
}
```

### Run Tests

```bash
./validate.sh
```

The script automatically:

- Validates files prefixed with `valid_` should pass
- Validates files prefixed with `invalid_` should fail

## Common Parameter Types

### File Paths

```json
{
  "input_file": {
    "type": "string",
    "format": "file-path",
    "description": "Input file",
    "exists": true
  }
}
```

### Numbers with Constraints

```json
{
  "threads": {
    "type": "integer",
    "description": "Number of threads",
    "minimum": 1,
    "maximum": 32,
    "default": 4
  }
}
```

### Enumerations

```json
{
  "output_format": {
    "type": "string",
    "description": "Output format",
    "enum": ["json", "csv", "tsv"],
    "default": "json"
  }
}
```

### Boolean Flags

```json
{
  "skip_qc": {
    "type": "boolean",
    "description": "Skip quality control steps",
    "default": false
  }
}
```

## Next Steps

- Learn more about the [Pipeline Input Schema](../schemas/pipeline-input.md)
- Explore the [Plugin Schema](../schemas/plugin.md)
- Check out [detailed examples](../examples/pipeline-input-examples.md)
- Read the [testing guide](../development/testing.md)
