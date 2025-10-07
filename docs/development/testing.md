# Testing Guide

This guide covers testing strategies for Nextflow schemas, including writing test cases, running validations, and interpreting results.

## Test Organization

Tests are organized by schema type:

```
pipeline-input/tests/
├── valid_minimal_schema.json
├── valid_full_featured_schema.json
├── invalid_missing_type.json
└── invalid_schema.json

plugin/tests/
├── valid_schema.json
└── invalid_schema.json
```

## Test Naming Convention

Test files must follow this naming pattern:

- **`valid_*.json`** - Files that should pass validation
- **`invalid_*.json`** - Files that should fail validation

The validation script (`validate.sh`) automatically:

- Expects `valid_*` files to pass
- Expects `invalid_*` files to fail
- Reports errors if expectations aren't met

## Running Tests

### Run All Tests

```bash
./validate.sh
```

This validates:

1. Schema files against JSON Schema Draft 2020-12
2. All test cases against their schemas
3. Naming convention compliance

### Run Tests with Docker

Use Docker for a clean, isolated environment:

```bash
./validate-docker.sh
```

### Validate a Single File

Test a specific schema or test file:

```bash
# Validate a schema file
check-jsonschema --schemafile https://json-schema.org/draft/2020-12/schema pipeline-input/schema.json

# Validate a test case
check-jsonschema --schemafile pipeline-input/schema.json pipeline-input/tests/valid_schema.json
```

### Validate Your Own Files

```bash
# Validate your pipeline schema
check-jsonschema --schemafile pipeline-input/schema.json /path/to/my-pipeline-schema.json

# Validate your plugin spec
check-jsonschema --schemafile plugin/schema.json /path/to/my-plugin-spec.json
```

## Writing Test Cases

### Valid Test Cases

Valid test cases should pass validation and cover:

#### Minimal Valid Case

Test the absolute minimum required properties:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/minimal-schema.json",
  "title": "Minimal Schema",
  "description": "Minimal valid schema",
  "type": "object"
}
```

#### Complete Feature Coverage

Test all schema features:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/full-schema.json",
  "title": "Full Featured Schema",
  "description": "Schema with all features",
  "type": "object",
  "properties": {
    "input": {
      "type": "string",
      "format": "file-path",
      "description": "Input file",
      "exists": true,
      "help_text": "Path to input file",
      "fa_icon": "fas fa-file"
    },
    "threads": {
      "type": "integer",
      "minimum": 1,
      "maximum": 64,
      "default": 4,
      "description": "Thread count"
    },
    "format": {
      "type": "string",
      "enum": ["json", "csv", "tsv"],
      "default": "json",
      "description": "Output format"
    }
  },
  "$defs": {
    "advanced_options": {
      "title": "Advanced Options",
      "type": "object",
      "properties": {
        "debug": {
          "type": "boolean",
          "description": "Enable debug mode",
          "default": false
        }
      }
    }
  },
  "allOf": [{ "$ref": "#/$defs/advanced_options" }]
}
```

#### Edge Cases

Test boundary conditions:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/edge-case.json",
  "title": "Edge Case Schema",
  "description": "Testing edge cases",
  "type": "object",
  "properties": {
    "nullable_string": {
      "type": ["string", "null"],
      "description": "Can be string or null"
    },
    "zero_value": {
      "type": "integer",
      "minimum": 0,
      "description": "Can be zero"
    },
    "empty_string": {
      "type": "string",
      "minLength": 0,
      "description": "Can be empty"
    }
  }
}
```

### Invalid Test Cases

Invalid test cases should fail validation and test specific error conditions:

#### Missing Required Properties

```json
{
  "title": "Invalid - Missing Required",
  "description": "Missing $schema, $id, and type"
}
```

#### Wrong Type

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/wrong-type.json",
  "title": "Invalid Type",
  "description": "Wrong type value",
  "type": "array"
}
```

#### Invalid Property Definition

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/invalid-prop.json",
  "title": "Invalid Property",
  "description": "Property missing required fields",
  "type": "object",
  "properties": {
    "bad_param": {
      "type": "string"
    }
  }
}
```

#### Constraint Violations

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/invalid-constraint.json",
  "title": "Invalid Constraint",
  "description": "Testing constraint violations",
  "type": "object",
  "properties": {
    "threads": {
      "type": "integer",
      "minimum": 10,
      "maximum": 5,
      "description": "Invalid: min > max"
    }
  }
}
```

#### Invalid Format Usage

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/invalid-format.json",
  "title": "Invalid Format",
  "description": "Wrong format usage",
  "type": "object",
  "properties": {
    "input": {
      "type": "string",
      "format": "file-path",
      "exists": true,
      "description": "Input file"
    },
    "bad_exists": {
      "type": "integer",
      "exists": true,
      "description": "Invalid: exists on non-string type"
    }
  }
}
```

## Test Coverage Guidelines

Ensure comprehensive test coverage:

### Required Coverage

- ✅ Minimal valid case
- ✅ All required properties
- ✅ Missing each required property
- ✅ Wrong types for key properties

### Recommended Coverage

- ✅ All schema features (if applicable)
- ✅ Parameter groups and `allOf` references
- ✅ Custom keywords (`exists`, `schema`, etc.)
- ✅ Constraint boundaries (min/max values)
- ✅ Format validation
- ✅ Enum validation
- ✅ Pattern matching
- ✅ Dependent requirements

### Plugin Schema Coverage

- ✅ Each definition type (ConfigScope, ConfigOption, Function, Operator, Factory)
- ✅ Nested configuration scopes
- ✅ Functions with and without parameters
- ✅ Various parameter types

## Interpreting Test Results

### Successful Test Run

```bash
$ ./validate.sh
Validating pipeline-input/schema.json ...
ok -- validation done, no errors

Validating test cases...
Testing pipeline-input/tests/valid_schema.json:
ok -- validation done, no errors
✓ Valid

Testing pipeline-input/tests/invalid_schema.json:
ValidationError: 'type' is a required property
✓ Invalid

Validating plugin/schema.json ...
ok -- validation done, no errors
...
```

All tests passed ✅

### Failed Test Run

```bash
$ ./validate.sh
Validating pipeline-input/schema.json ...
ValidationError: Additional properties are not allowed ('bad_property' was unexpected)
```

Schema itself is invalid ❌

```bash
Testing pipeline-input/tests/valid_schema.json:
ValidationError: 'description' is a required property
```

A supposedly valid test case failed validation ❌

```bash
Testing pipeline-input/tests/invalid_schema.json:
ok -- validation done, no errors
```

A supposedly invalid test case passed validation ❌

## Continuous Integration

### GitHub Actions

Tests run automatically on:

- Push to any branch
- Pull requests
- Changes to `*.json` files
- Changes to `validate.sh`

### CI Workflow

The CI workflow:

1. Checks out the repository
2. Installs Python and `check-jsonschema`
3. Runs `./validate.sh`
4. Reports results

## Debugging Failed Tests

### Check Schema Validity

First, ensure the schema itself is valid:

```bash
check-jsonschema --schemafile https://json-schema.org/draft/2020-12/schema pipeline-input/schema.json
```

### Verbose Validation

Get detailed error messages:

```bash
check-jsonschema --schemafile pipeline-input/schema.json --verbose pipeline-input/tests/invalid_test.json
```

### Test Individual Properties

Isolate the problem by testing minimal cases:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json",
  "$id": "https://example.com/test.json",
  "title": "Test",
  "description": "Isolate problematic property",
  "type": "object",
  "properties": {
    "problematic_param": {
      "type": "string",
      "description": "Testing this specific parameter"
    }
  }
}
```

### Check JSON Syntax

Ensure JSON is well-formed:

```bash
python -m json.tool test.json
```

## Best Practices

1. **Test one thing at a time** - Each invalid test should fail for one specific reason
2. **Use descriptive names** - Make it clear what each test validates
3. **Cover edge cases** - Test boundary conditions and unusual inputs
4. **Keep tests simple** - Avoid unnecessary complexity
5. **Document expectations** - Add comments if the test case isn't obvious
6. **Run tests frequently** - Validate after each change

## See Also

- [Contributing Guidelines](contributing.md)
- [CI/CD Documentation](ci-cd.md)
- [Pipeline Input Schema Reference](../schemas/pipeline-input.md)
- [Plugin Schema Reference](../schemas/plugin.md)
