# Plugin Examples

This page provides practical examples of plugin schemas for various use cases.

## Basic Examples

### Minimal Plugin

Simplest valid plugin schema:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json",
  "definitions": []
}
```

### Simple Configuration

Plugin with basic configuration options:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json",
  "definitions": [
    {
      "type": "ConfigScope",
      "spec": {
        "name": "myPlugin",
        "description": "My plugin configuration",
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
              "name": "debug",
              "description": "Enable debug mode",
              "type": "Boolean"
            }
          }
        ]
      }
    }
  ]
}
```

**Usage**:

```groovy
myPlugin {
    enabled = true
    debug = false
}
```

### Simple Function

Plugin with a single function:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json",
  "definitions": [
    {
      "type": "Function",
      "spec": {
        "name": "greet",
        "description": "Generate a greeting message",
        "returnType": "String",
        "parameters": [
          {
            "name": "name",
            "type": "String"
          }
        ]
      }
    }
  ]
}
```

**Usage**:

```groovy
def message = greet('World')
println message  // "Hello, World!"
```

## AWS Plugin Example

Comprehensive AWS integration plugin:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json",
  "definitions": [
    {
      "type": "ConfigScope",
      "spec": {
        "name": "aws",
        "description": "AWS plugin configuration",
        "children": [
          {
            "type": "ConfigOption",
            "spec": {
              "name": "region",
              "description": "AWS region",
              "type": "String"
            }
          },
          {
            "type": "ConfigOption",
            "spec": {
              "name": "profile",
              "description": "AWS credentials profile name",
              "type": "String"
            }
          },
          {
            "type": "ConfigScope",
            "spec": {
              "name": "batch",
              "description": "AWS Batch configuration",
              "children": [
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "cliPath",
                    "description": "Path to AWS CLI executable",
                    "type": "String"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "jobQueue",
                    "description": "Default job queue name",
                    "type": "String"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "maxParallelTransfers",
                    "description": "Maximum parallel file transfers",
                    "type": "Integer"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "retryMode",
                    "description": "Retry strategy mode",
                    "type": "String"
                  }
                }
              ]
            }
          },
          {
            "type": "ConfigScope",
            "spec": {
              "name": "client",
              "description": "AWS client configuration",
              "children": [
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "maxConnections",
                    "description": "Maximum HTTP connections",
                    "type": "Integer"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "connectionTimeout",
                    "description": "Connection timeout",
                    "type": "Duration"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "uploadMaxThreads",
                    "description": "Maximum upload threads",
                    "type": "Integer"
                  }
                }
              ]
            }
          }
        ]
      }
    },
    {
      "type": "Function",
      "spec": {
        "name": "uploadToS3",
        "description": "Upload a file to S3 bucket",
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
    },
    {
      "type": "Function",
      "spec": {
        "name": "downloadFromS3",
        "description": "Download a file from S3 bucket",
        "returnType": "Path",
        "parameters": [
          {
            "name": "bucket",
            "type": "String"
          },
          {
            "name": "key",
            "type": "String"
          },
          {
            "name": "localPath",
            "type": "String"
          }
        ]
      }
    }
  ]
}
```

**Usage**:

```groovy
aws {
    region = 'us-east-1'
    profile = 'my-profile'

    batch {
        cliPath = '/usr/local/bin/aws'
        jobQueue = 'my-queue'
        maxParallelTransfers = 4
        retryMode = 'standard'
    }

    client {
        maxConnections = 20
        connectionTimeout = '30.s'
        uploadMaxThreads = 4
    }
}

// Upload file
uploadToS3('/data/results.txt', 'my-bucket', 'outputs/results.txt')

// Download file
downloadFromS3('my-bucket', 'inputs/data.txt', '/tmp/data.txt')
```

## Database Plugin Example

Database integration with connection pooling:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json",
  "definitions": [
    {
      "type": "ConfigScope",
      "spec": {
        "name": "database",
        "description": "Database plugin configuration",
        "children": [
          {
            "type": "ConfigOption",
            "spec": {
              "name": "url",
              "description": "Database connection URL",
              "type": "String"
            }
          },
          {
            "type": "ConfigOption",
            "spec": {
              "name": "username",
              "description": "Database username",
              "type": "String"
            }
          },
          {
            "type": "ConfigOption",
            "spec": {
              "name": "password",
              "description": "Database password",
              "type": "String"
            }
          },
          {
            "type": "ConfigScope",
            "spec": {
              "name": "pool",
              "description": "Connection pool settings",
              "children": [
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "minConnections",
                    "description": "Minimum pool connections",
                    "type": "Integer"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "maxConnections",
                    "description": "Maximum pool connections",
                    "type": "Integer"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "timeout",
                    "description": "Connection timeout",
                    "type": "Duration"
                  }
                }
              ]
            }
          }
        ]
      }
    },
    {
      "type": "Factory",
      "spec": {
        "name": "createConnection",
        "description": "Create a database connection",
        "returnType": "Connection",
        "parameters": []
      }
    },
    {
      "type": "Function",
      "spec": {
        "name": "executeQuery",
        "description": "Execute a SQL query",
        "returnType": "List",
        "parameters": [
          {
            "name": "query",
            "type": "String"
          },
          {
            "name": "params",
            "type": "Map"
          }
        ]
      }
    },
    {
      "type": "Function",
      "spec": {
        "name": "executeUpdate",
        "description": "Execute a SQL update statement",
        "returnType": "Integer",
        "parameters": [
          {
            "name": "statement",
            "type": "String"
          },
          {
            "name": "params",
            "type": "Map"
          }
        ]
      }
    }
  ]
}
```

**Usage**:

```groovy
database {
    url = 'jdbc:postgresql://localhost:5432/mydb'
    username = 'user'
    password = 'pass'

    pool {
        minConnections = 2
        maxConnections = 10
        timeout = '30.s'
    }
}

// Create connection
def conn = createConnection()

// Query data
def results = executeQuery(
    'SELECT * FROM samples WHERE status = :status',
    [status: 'active']
)

// Update data
def affected = executeUpdate(
    'UPDATE samples SET processed = true WHERE id = :id',
    [id: 123]
)
```

## Channel Operator Plugin

Custom channel operators:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json",
  "definitions": [
    {
      "type": "Operator",
      "spec": {
        "name": "customFilter",
        "description": "Filter channel items with custom predicate",
        "returnType": "DataflowChannel",
        "parameters": [
          {
            "name": "predicate",
            "type": "Closure"
          }
        ]
      }
    },
    {
      "type": "Operator",
      "spec": {
        "name": "batchBy",
        "description": "Group items into batches by a key function",
        "returnType": "DataflowChannel",
        "parameters": [
          {
            "name": "size",
            "type": "Integer"
          },
          {
            "name": "keyFunc",
            "type": "Closure"
          }
        ]
      }
    },
    {
      "type": "Operator",
      "spec": {
        "name": "retryOn",
        "description": "Retry failed items based on exception type",
        "returnType": "DataflowChannel",
        "parameters": [
          {
            "name": "exceptionClass",
            "type": "Class"
          },
          {
            "name": "maxRetries",
            "type": "Integer"
          }
        ]
      }
    },
    {
      "type": "Operator",
      "spec": {
        "name": "transformParallel",
        "description": "Transform items in parallel with specified concurrency",
        "returnType": "DataflowChannel",
        "parameters": [
          {
            "name": "concurrency",
            "type": "Integer"
          },
          {
            "name": "transformer",
            "type": "Closure"
          }
        ]
      }
    }
  ]
}
```

**Usage**:

```groovy
// Custom filter
Channel
    .from(1, 2, 3, 4, 5)
    .customFilter { it % 2 == 0 }
    .view()  // 2, 4

// Batch by key
Channel
    .from('apple', 'apricot', 'banana', 'blueberry')
    .batchBy(2) { it[0] }  // Group by first letter
    .view()  // ['apple', 'apricot'], ['banana', 'blueberry']

// Retry on failure
Channel
    .from(urls)
    .retryOn(IOException, 3)
    .view()

// Parallel transformation
Channel
    .from(files)
    .transformParallel(4) { file ->
        processFile(file)
    }
    .view()
```

## API Client Plugin

REST API integration:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json",
  "definitions": [
    {
      "type": "ConfigScope",
      "spec": {
        "name": "apiClient",
        "description": "API client configuration",
        "children": [
          {
            "type": "ConfigOption",
            "spec": {
              "name": "baseUrl",
              "description": "API base URL",
              "type": "String"
            }
          },
          {
            "type": "ConfigOption",
            "spec": {
              "name": "apiKey",
              "description": "API authentication key",
              "type": "String"
            }
          },
          {
            "type": "ConfigOption",
            "spec": {
              "name": "timeout",
              "description": "Request timeout",
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
      "type": "Factory",
      "spec": {
        "name": "createClient",
        "description": "Create an API client instance",
        "returnType": "ApiClient",
        "parameters": [
          {
            "name": "config",
            "type": "Map"
          }
        ]
      }
    },
    {
      "type": "Function",
      "spec": {
        "name": "get",
        "description": "Perform GET request",
        "returnType": "Map",
        "parameters": [
          {
            "name": "endpoint",
            "type": "String"
          },
          {
            "name": "params",
            "type": "Map"
          }
        ]
      }
    },
    {
      "type": "Function",
      "spec": {
        "name": "post",
        "description": "Perform POST request",
        "returnType": "Map",
        "parameters": [
          {
            "name": "endpoint",
            "type": "String"
          },
          {
            "name": "body",
            "type": "Map"
          }
        ]
      }
    },
    {
      "type": "Function",
      "spec": {
        "name": "uploadFile",
        "description": "Upload a file via multipart POST",
        "returnType": "Map",
        "parameters": [
          {
            "name": "endpoint",
            "type": "String"
          },
          {
            "name": "filePath",
            "type": "String"
          },
          {
            "name": "metadata",
            "type": "Map"
          }
        ]
      }
    }
  ]
}
```

**Usage**:

```groovy
apiClient {
    baseUrl = 'https://api.example.com/v1'
    apiKey = secrets.API_KEY
    timeout = '60.s'
    retries = 3
}

// Create client
def client = createClient([
    baseUrl: 'https://custom-api.com',
    apiKey: 'custom-key'
])

// GET request
def data = get('/samples', [status: 'active', limit: 100])

// POST request
def result = post('/samples', [
    name: 'Sample1',
    type: 'RNA-seq',
    metadata: [organism: 'human']
])

// Upload file
def response = uploadFile(
    '/uploads',
    '/data/results.csv',
    [description: 'Analysis results']
)
```

## Notification Plugin

Multi-channel notifications:

```json
{
  "$schema": "https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/schema.json",
  "definitions": [
    {
      "type": "ConfigScope",
      "spec": {
        "name": "notifications",
        "description": "Notification plugin configuration",
        "children": [
          {
            "type": "ConfigScope",
            "spec": {
              "name": "email",
              "description": "Email notification settings",
              "children": [
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "enabled",
                    "description": "Enable email notifications",
                    "type": "Boolean"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "to",
                    "description": "Recipient email address",
                    "type": "String"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "from",
                    "description": "Sender email address",
                    "type": "String"
                  }
                }
              ]
            }
          },
          {
            "type": "ConfigScope",
            "spec": {
              "name": "slack",
              "description": "Slack notification settings",
              "children": [
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "enabled",
                    "description": "Enable Slack notifications",
                    "type": "Boolean"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "webhook",
                    "description": "Slack webhook URL",
                    "type": "String"
                  }
                },
                {
                  "type": "ConfigOption",
                  "spec": {
                    "name": "channel",
                    "description": "Slack channel name",
                    "type": "String"
                  }
                }
              ]
            }
          }
        ]
      }
    },
    {
      "type": "Function",
      "spec": {
        "name": "sendNotification",
        "description": "Send notification via all enabled channels",
        "returnType": "Boolean",
        "parameters": [
          {
            "name": "message",
            "type": "String"
          },
          {
            "name": "level",
            "type": "String"
          }
        ]
      }
    },
    {
      "type": "Function",
      "spec": {
        "name": "notifyOnComplete",
        "description": "Send notification when pipeline completes",
        "returnType": "void",
        "parameters": []
      }
    }
  ]
}
```

**Usage**:

```groovy
notifications {
    email {
        enabled = true
        to = 'user@example.com'
        from = 'pipeline@example.com'
    }

    slack {
        enabled = true
        webhook = 'https://hooks.slack.com/...'
        channel = '#pipeline-notifications'
    }
}

// Send notification
sendNotification('Pipeline started', 'info')
sendNotification('Critical error occurred', 'error')

// Notify on completion
workflow.onComplete {
    notifyOnComplete()
}
```

## See Also

- [Plugin Schema Reference](../schemas/plugin.md)
- [Quick Start Guide](../getting-started/quick-start.md)
- [Testing Guide](../development/testing.md)
