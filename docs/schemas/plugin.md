# Plugin Schema Reference

The plugin schema validates Nextflow plugin specifications, including configuration scopes, configuration options, and function definitions.

## Schema URI

```
https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json
```

## Top-Level Structure

The plugin schema has a single top-level property:

| Property      | Type  | Description                                               |
| ------------- | ----- | --------------------------------------------------------- |
| `definitions` | array | Array of definition objects (config scopes and functions) |

## Definition Types

Each item in the `definitions` array must be one of:

- **ConfigScope** - Configuration scope with nested children
- **ConfigOption** - Individual configuration option
- **Factory** - Factory function definition
- **Function** - Standard function definition
- **Operator** - Operator function definition

## Configuration Scopes

Configuration scopes define hierarchical configuration structures.

### Structure

```json
{
  "type": "ConfigScope",
  "spec": {
    "name": "string",
    "description": "string",
    "children": []
  }
}
```

### Properties

| Property           | Type   | Required | Description                     |
| ------------------ | ------ | -------- | ------------------------------- |
| `type`             | string | Yes      | Must be `"ConfigScope"`         |
| `spec.name`        | string | Yes      | Scope name                      |
| `spec.description` | string | Yes      | Scope description               |
| `spec.children`    | array  | Yes      | Nested config options or scopes |

### Example

```json
{
  "type": "ConfigScope",
  "spec": {
    "name": "aws",
    "description": "AWS plugin configuration",
    "children": [
      {
        "type": "ConfigScope",
        "spec": {
          "name": "batch",
          "description": "AWS Batch settings",
          "children": [
            {
              "type": "ConfigOption",
              "spec": {
                "name": "cliPath",
                "description": "Path to AWS CLI executable",
                "type": "String"
              }
            }
          ]
        }
      },
      {
        "type": "ConfigOption",
        "spec": {
          "name": "region",
          "description": "AWS region",
          "type": "String"
        }
      }
    ]
  }
}
```

This creates a configuration structure:

```groovy
aws {
    batch {
        cliPath = '/usr/bin/aws'
    }
    region = 'us-east-1'
}
```

## Configuration Options

Configuration options are individual settings within a scope.

### Structure

```json
{
  "type": "ConfigOption",
  "spec": {
    "name": "string",
    "description": "string",
    "type": "string"
  }
}
```

### Properties

| Property           | Type   | Required | Description                                |
| ------------------ | ------ | -------- | ------------------------------------------ |
| `type`             | string | Yes      | Must be `"ConfigOption"`                   |
| `spec.name`        | string | Yes      | Option name                                |
| `spec.description` | string | Yes      | Option description                         |
| `spec.type`        | string | Yes      | Data type (String, Integer, Boolean, etc.) |

### Common Data Types

- `String` - Text value
- `Integer` - Whole number
- `Boolean` - true/false
- `Duration` - Time duration (e.g., `10.s`, `5.m`)
- `MemoryUnit` - Memory size (e.g., `1.GB`, `512.MB`)
- `Map` - Key-value pairs
- `List` - Array of values

### Example

```json
{
  "type": "ConfigOption",
  "spec": {
    "name": "maxRetries",
    "description": "Maximum number of retry attempts",
    "type": "Integer"
  }
}
```

## Functions

Function definitions document callable functions provided by the plugin.

### Types of Functions

#### Function

Standard function:

```json
{
  "type": "Function",
  "spec": {
    "name": "string",
    "description": "string",
    "returnType": "string",
    "parameters": []
  }
}
```

#### Factory

Factory function that creates objects:

```json
{
  "type": "Factory",
  "spec": {
    "name": "string",
    "description": "string",
    "returnType": "string",
    "parameters": []
  }
}
```

#### Operator

Channel operator function:

```json
{
  "type": "Operator",
  "spec": {
    "name": "string",
    "description": "string",
    "returnType": "string",
    "parameters": []
  }
}
```

### Properties

| Property           | Type   | Required | Description                                |
| ------------------ | ------ | -------- | ------------------------------------------ |
| `type`             | string | Yes      | `"Function"`, `"Factory"`, or `"Operator"` |
| `spec.name`        | string | Yes      | Function name                              |
| `spec.description` | string | Yes      | Function description                       |
| `spec.returnType`  | string | Yes      | Return type                                |
| `spec.parameters`  | array  | No       | Function parameters                        |

### Parameters

Each parameter object:

| Property | Type   | Required | Description    |
| -------- | ------ | -------- | -------------- |
| `name`   | string | Yes      | Parameter name |
| `type`   | string | Yes      | Parameter type |

### Example: Function

```json
{
  "type": "Function",
  "spec": {
    "name": "uploadFile",
    "description": "Upload a file to S3",
    "returnType": "String",
    "parameters": [
      {
        "name": "localPath",
        "type": "String"
      },
      {
        "name": "bucket",
        "type": "String"
      },
      {
        "name": "key",
        "type": "String"
      }
    ]
  }
}
```

Usage in Nextflow:

```groovy
def result = uploadFile('/data/file.txt', 'my-bucket', 'output/file.txt')
```

### Example: Operator

```json
{
  "type": "Operator",
  "spec": {
    "name": "customFilter",
    "description": "Filter channel items with custom logic",
    "returnType": "DataflowChannel",
    "parameters": [
      {
        "name": "closure",
        "type": "Closure"
      }
    ]
  }
}
```

Usage in Nextflow:

```groovy
Channel
    .from(1, 2, 3, 4, 5)
    .customFilter { it > 2 }
```

### Example: Factory

```json
{
  "type": "Factory",
  "spec": {
    "name": "createClient",
    "description": "Create an API client",
    "returnType": "ApiClient",
    "parameters": [
      {
        "name": "config",
        "type": "Map"
      }
    ]
  }
}
```

Usage in Nextflow:

```groovy
def client = createClient([
    endpoint: 'https://api.example.com',
    apiKey: 'secret'
])
```

## Complete Example

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json",
  "definitions": [
    {
      "type": "ConfigScope",
      "spec": {
        "name": "myPlugin",
        "description": "My custom plugin configuration",
        "children": [
          {
            "type": "ConfigScope",
            "spec": {
              "name": "server",
              "description": "Server connection settings",
              "children": [
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "endpoint",
                    "description": "API endpoint URL",
                    "type": "String"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "timeout",
                    "description": "Connection timeout",
                    "type": "Duration"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "retries",
                    "description": "Maximum retry attempts",
                    "type": "Integer"
                  }
                }
              ]
            }
          },
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
              "name": "debug",
              "description": "Enable debug logging",
              "type": "Boolean"
            }
          }
        ]
      }
    },
    {
      "type": "Function",
      "spec": {
        "name": "processData",
        "description": "Process input data and return results",
        "returnType": "Map",
        "parameters": [
          {
            "name": "input",
            "type": "String"
          },
          {
            "name": "options",
            "type": "Map"
          }
        ]
      }
    },
    {
      "type": "Operator",
      "spec": {
        "name": "transform",
        "description": "Transform channel data",
        "returnType": "DataflowChannel",
        "parameters": [
          {
            "name": "mapper",
            "type": "Closure"
          }
        ]
      }
    },
    {
      "type": "Factory",
      "spec": {
        "name": "createProcessor",
        "description": "Create a data processor instance",
        "returnType": "DataProcessor",
        "parameters": [
          {
            "name": "config",
            "type": "Map"
          }
        ]
      }
    }
  ]
}
```

### Resulting Configuration

The above schema allows this configuration:

```groovy
myPlugin {
    enabled = true
    debug = false

    server {
        endpoint = 'https://api.example.com'
        timeout = '30.s'
        retries = 3
    }
}
```

### Resulting Functions

And these function calls:

```groovy
// Function
def result = processData('/path/to/input', [format: 'json'])

// Operator
Channel
    .from('data1', 'data2')
    .transform { it.toUpperCase() }

// Factory
def processor = createProcessor([threads: 4, memory: '8.GB'])
```

## Validation

Validate your plugin schema:

```bash
check-jsonschema --schemafile plugin/schema.json my-plugin-spec.json
```

## Best Practices

1. **Use descriptive names** - Make config options and function names self-explanatory
2. **Provide clear descriptions** - Help users understand what each option does
3. **Group related options** - Use nested ConfigScopes for logical grouping
4. **Document parameters** - Specify parameter types and purposes
5. **Be consistent** - Follow naming conventions (camelCase for options, snake_case for parameters)

## See Also

- [Quick Start Guide](../getting-started/quick-start.md)
- [Plugin Examples](../examples/plugin-examples.md)
- [Testing Guide](../development/testing.md)
