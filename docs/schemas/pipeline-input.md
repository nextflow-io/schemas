# Pipeline Input Schema Reference

The pipeline input schema validates Nextflow pipeline parameter specifications. It follows JSON Schema Draft 2020-12 and includes both standard and custom keywords specific to Nextflow.

## Schema URI

```
https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json
```

## Top-Level Structure

### Required Properties

| Property      | Type   | Description                       |
| ------------- | ------ | --------------------------------- |
| `$schema`     | string | URI of the JSON Schema standard   |
| `$id`         | string | Unique identifier for your schema |
| `title`       | string | Human-readable title              |
| `description` | string | Schema description                |
| `type`        | string | Must be `"object"`                |

### Optional Properties

| Property            | Type   | Description                        |
| ------------------- | ------ | ---------------------------------- |
| `properties`        | object | Direct parameter definitions       |
| `$defs`             | object | Parameter group definitions        |
| `allOf`             | array  | References to parameter groups     |
| `dependentRequired` | object | Conditional parameter requirements |

## Parameter Definitions

Each parameter must include:

- `type` - The parameter data type
- `description` - Human-readable description

### Standard Keywords

#### Type Validation

```json
{
  "type": "string" | "integer" | "number" | "boolean" | "null"
}
```

Or multiple types:

```json
{
  "type": ["string", "null"]
}
```

#### Format Validation (String Types)

Validates string structure:

| Format              | Description              | Example                |
| ------------------- | ------------------------ | ---------------------- |
| `file-path`         | Path to a file           | `/data/input.txt`      |
| `directory-path`    | Path to a directory      | `/data/output/`        |
| `path`              | Generic file system path | `/data/`               |
| `file-path-pattern` | Glob pattern             | `*.fastq.gz`           |
| `date-time`         | ISO 8601 datetime        | `2024-01-01T12:00:00Z` |
| `date`              | ISO 8601 date            | `2024-01-01`           |
| `time`              | ISO 8601 time            | `12:00:00`             |
| `email`             | Email address            | `user@example.com`     |
| `uri`               | URI/URL                  | `https://example.com`  |
| `regex`             | Regular expression       | `^[A-Z]+$`             |

Example:

```json
{
  "input": {
    "type": "string",
    "format": "file-path",
    "description": "Input file path"
  }
}
```

#### Pattern Validation

Validate strings against regex:

```json
{
  "sample_id": {
    "type": "string",
    "pattern": "^[A-Za-z0-9_-]+$",
    "description": "Sample identifier"
  }
}
```

#### String Length Constraints

```json
{
  "name": {
    "type": "string",
    "minLength": 1,
    "maxLength": 100,
    "description": "Sample name"
  }
}
```

#### Numeric Constraints

```json
{
  "threads": {
    "type": "integer",
    "minimum": 1,
    "maximum": 128,
    "default": 4,
    "description": "Number of threads"
  },
  "quality_threshold": {
    "type": "number",
    "exclusiveMinimum": 0.0,
    "exclusiveMaximum": 1.0,
    "description": "Quality threshold"
  },
  "step_size": {
    "type": "number",
    "multipleOf": 0.5,
    "description": "Step size (multiples of 0.5)"
  }
}
```

#### Enumerations

Restrict to specific values:

```json
{
  "aligner": {
    "type": "string",
    "enum": ["bwa", "bowtie2", "star"],
    "default": "bwa",
    "description": "Read aligner to use"
  }
}
```

#### Constant Values

Parameter with fixed value:

```json
{
  "version": {
    "type": "string",
    "const": "1.0.0",
    "description": "Schema version"
  }
}
```

#### Default Values

```json
{
  "outdir": {
    "type": "string",
    "default": "./results",
    "description": "Output directory"
  }
}
```

#### Examples

Provide usage examples:

```json
{
  "input": {
    "type": "string",
    "description": "Input file",
    "examples": ["/data/sample1.fastq", "/data/sample2.fastq"]
  }
}
```

#### Deprecation

Mark parameters as deprecated:

```json
{
  "old_param": {
    "type": "string",
    "description": "Legacy parameter",
    "deprecated": true,
    "errorMessage": "This parameter is deprecated. Use 'new_param' instead."
  }
}
```

### Custom Nextflow Keywords

These are NON-STANDARD extensions specific to Nextflow:

#### `errorMessage`

Custom validation error message:

```json
{
  "threads": {
    "type": "integer",
    "minimum": 1,
    "maximum": 64,
    "description": "Thread count",
    "errorMessage": "Threads must be between 1 and 64"
  }
}
```

#### `exists`

Check if file/directory exists (requires appropriate `format`):

```json
{
  "reference": {
    "type": "string",
    "format": "file-path",
    "exists": true,
    "description": "Reference genome (must exist)"
  }
}
```

#### `schema`

Validate a file against another schema:

```json
{
  "samplesheet": {
    "type": "string",
    "format": "file-path",
    "schema": "assets/samplesheet.json",
    "description": "Sample sheet (validated against schema)"
  }
}
```

#### `help_text`

Extended help documentation:

```json
{
  "input": {
    "type": "string",
    "description": "Input file",
    "help_text": "Provide a path to your input FASTQ file. The file should be gzip-compressed and follow the naming convention: sample_R1.fastq.gz"
  }
}
```

#### `fa_icon`

Font Awesome icon for documentation:

```json
{
  "input": {
    "type": "string",
    "fa_icon": "fas fa-file",
    "description": "Input file"
  }
}
```

#### `hidden`

Hide parameter from help and docs:

```json
{
  "internal_param": {
    "type": "string",
    "hidden": true,
    "description": "Internal parameter"
  }
}
```

#### `mimetype` (Deprecated)

⚠️ **Deprecated**: Use `format` or `pattern` instead.

```json
{
  "data": {
    "type": "string",
    "mimetype": "text/csv"
  }
}
```

## Parameter Groups

Organize parameters using `$defs` and `allOf`:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/schema.json",
  "title": "Pipeline Parameters",
  "description": "My pipeline parameters",
  "type": "object",
  "$defs": {
    "input_output_options": {
      "title": "Input/Output Options",
      "type": "object",
      "fa_icon": "fas fa-terminal",
      "description": "Define where the pipeline should find input data and save output data",
      "required": ["input", "outdir"],
      "properties": {
        "input": {
          "type": "string",
          "format": "file-path",
          "description": "Input samplesheet"
        },
        "outdir": {
          "type": "string",
          "format": "directory-path",
          "description": "Output directory",
          "default": "./results"
        }
      }
    },
    "reference_genome_options": {
      "title": "Reference Genome",
      "type": "object",
      "fa_icon": "fas fa-dna",
      "description": "Reference genome options",
      "properties": {
        "genome": {
          "type": "string",
          "description": "Genome name",
          "enum": ["GRCh38", "GRCh37"],
          "help_text": "Select the reference genome assembly"
        },
        "fasta": {
          "type": "string",
          "format": "file-path",
          "description": "Custom reference FASTA",
          "help_text": "Provide a custom reference genome FASTA file"
        }
      }
    }
  },
  "allOf": [
    { "$ref": "#/$defs/input_output_options" },
    { "$ref": "#/$defs/reference_genome_options" }
  ]
}
```

## Dependent Requirements

Make parameters conditionally required:

```json
{
  "properties": {
    "use_cache": {
      "type": "boolean",
      "description": "Enable caching"
    },
    "cache_dir": {
      "type": "string",
      "format": "directory-path",
      "description": "Cache directory"
    }
  },
  "dependentRequired": {
    "use_cache": ["cache_dir"]
  }
}
```

When `use_cache` is provided, `cache_dir` becomes required.

## Complete Example

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://raw.githubusercontent.com/my-org/my-pipeline/main/nextflow_schema.json",
  "title": "RNA-Seq Pipeline Parameters",
  "description": "Parameters for RNA-Seq analysis pipeline",
  "type": "object",
  "$defs": {
    "input_output_options": {
      "title": "Input/Output Options",
      "type": "object",
      "fa_icon": "fas fa-terminal",
      "description": "Input and output file paths",
      "required": ["input", "outdir"],
      "properties": {
        "input": {
          "type": "string",
          "format": "file-path",
          "exists": true,
          "description": "Input samplesheet",
          "help_text": "CSV file with sample information",
          "fa_icon": "fas fa-file-csv"
        },
        "outdir": {
          "type": "string",
          "format": "directory-path",
          "description": "Output directory",
          "default": "./results",
          "fa_icon": "fas fa-folder-open"
        }
      }
    },
    "alignment_options": {
      "title": "Alignment Options",
      "type": "object",
      "fa_icon": "fas fa-align-center",
      "description": "Parameters for read alignment",
      "properties": {
        "aligner": {
          "type": "string",
          "enum": ["star", "hisat2"],
          "default": "star",
          "description": "Read aligner"
        },
        "min_mapping_quality": {
          "type": "integer",
          "minimum": 0,
          "maximum": 60,
          "default": 10,
          "description": "Minimum mapping quality"
        }
      }
    }
  },
  "allOf": [
    { "$ref": "#/$defs/input_output_options" },
    { "$ref": "#/$defs/alignment_options" }
  ]
}
```

## See Also

- [Quick Start Guide](../getting-started/quick-start.md)
- [Pipeline Input Examples](../examples/pipeline-input-examples.md)
- [Testing Guide](../development/testing.md)
