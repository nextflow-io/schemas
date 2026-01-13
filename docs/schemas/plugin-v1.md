# Nextflow plugin schema

**Title:** Nextflow plugin schema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Schema for Nextflow plugin specs

**Schema:** https://json-schema.org/draft/2020-12/schema

**ID:** https://raw.githubusercontent.com/nextflow-io/schemas/main/plugin/v1/schema.json

| Property                                             | Type  | Deprecated | Definition | Title/Description |
| ---------------------------------------------------- | ----- | ---------- | ---------- | ----------------- |
| - [definitions](#Nextflow_plugin_schema_definitions) | array |            |            | -                 |

## <a name="Nextflow_plugin_schema_definitions"></a>`definitions`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Tuple validation** | See below          |

**Array Items:**

Each item must be of type: `combining`

## Definitions

The following definitions are used throughout the schema:

### config_scope

**Type:** `object`

| Property                          | Type             | Deprecated | Definition | Title/Description |
| --------------------------------- | ---------------- | ---------- | ---------- | ----------------- |
| - [type](#defs_config_scope_type) | enum (of string) |            |            | -                 |
| - [spec](#defs_config_scope_spec) | object           |            |            | -                 |

### config_option

**Type:** `object`

| Property                           | Type             | Deprecated | Definition | Title/Description |
| ---------------------------------- | ---------------- | ---------- | ---------- | ----------------- |
| - [type](#defs_config_option_type) | enum (of string) |            |            | -                 |
| - [spec](#defs_config_option_spec) | object           |            |            | -                 |

### function

**Type:** `object`

| Property                      | Type             | Deprecated | Definition | Title/Description |
| ----------------------------- | ---------------- | ---------- | ---------- | ----------------- |
| - [type](#defs_function_type) | enum (of string) |            |            | -                 |
| - [spec](#defs_function_spec) | object           |            |            | -                 |

---

Generated using a custom JSON Schema documentation generator.
