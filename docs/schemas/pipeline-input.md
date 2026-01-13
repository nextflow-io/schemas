# Nextflow pipeline input schema

**Title:** Nextflow pipeline input schema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Schema to validate Nextflow pipeline input specs

**Schema:** https://json-schema.org/draft/2020-12/schema

**ID:** https://raw.githubusercontent.com/nextflow-io/schemas/main/pipeline-input/schema.json

| Property                                                                 | Type            | Deprecated | Definition                  | Title/Description         |
| ------------------------------------------------------------------------ | --------------- | ---------- | --------------------------- | ------------------------- |
| + [\$schema](#Nextflow_pipeline_input_schema_schema)                     | string          |            |                             | schema                    |
| + [\$id](#Nextflow_pipeline_input_schema_id)                             | string          |            |                             | ID URI                    |
| + [title](#Nextflow_pipeline_input_schema_title)                         | string          |            |                             | Title                     |
| + [description](#Nextflow_pipeline_input_schema_description)             | string          |            |                             | Description               |
| + [type](#Nextflow_pipeline_input_schema_type)                           | const           |            |                             | Top level type            |
| - [\$defs](#Nextflow_pipeline_input_schema_defs)                         | object          |            |                             | Parameter groups          |
| - [properties](#Nextflow_pipeline_input_schema_properties)               | object          |            | In #/$defs/parameterOptions | -                         |
| - [dependentRequired](#Nextflow_pipeline_input_schema_dependentRequired) | object          |            |                             | -                         |
| - [allOf](#Nextflow_pipeline_input_schema_allOf)                         | array of object |            |                             | Combine definition groups |

## <a name="Nextflow_pipeline_input_schema_schema"></a>`$schema`

**Title:** schema

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

## <a name="Nextflow_pipeline_input_schema_id"></a>`$id`

**Title:** ID URI

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

## <a name="Nextflow_pipeline_input_schema_title"></a>`title`

**Title:** Title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

## <a name="Nextflow_pipeline_input_schema_description"></a>`description`

**Title:** Description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

## <a name="Nextflow_pipeline_input_schema_type"></a>`type`

**Title:** Top level type

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"object"`

## <a name="Nextflow_pipeline_input_schema_defs"></a>`$defs`

**Title:** Parameter groups

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

**Pattern Properties:**

Properties matching pattern `^.*$` must conform to:

### <a name="Nextflow_pipeline_input_schema_defs_pattern:_."></a>`pattern: ^.*$`

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

**Properties:**

| Property                                                                                 | Type   | Deprecated | Definition                  | Title/Description |
| ---------------------------------------------------------------------------------------- | ------ | ---------- | --------------------------- | ----------------- |
| + [title](#Nextflow_pipeline_input_schema_defs_pattern:_._title)                         | string |            |                             | -                 |
| + [type](#Nextflow_pipeline_input_schema_defs_pattern:_._type)                           | const  |            |                             | -                 |
| - [fa_icon](#Nextflow_pipeline_input_schema_defs_pattern:_._fa_icon)                     | string |            |                             | -                 |
| - [description](#Nextflow_pipeline_input_schema_defs_pattern:_._description)             | string |            |                             | -                 |
| - [required](#Nextflow_pipeline_input_schema_defs_pattern:_._required)                   | array  |            |                             | -                 |
| + [properties](#Nextflow_pipeline_input_schema_defs_pattern:_._properties)               | object |            | In #/$defs/parameterOptions | -                 |
| - [dependentRequired](#Nextflow_pipeline_input_schema_defs_pattern:_._dependentRequired) | object |            |                             | -                 |

#### <a name="Nextflow_pipeline_input_schema_defs_pattern:_._title"></a>`title`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

#### <a name="Nextflow_pipeline_input_schema_defs_pattern:_._type"></a>`type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"object"`

#### <a name="Nextflow_pipeline_input_schema_defs_pattern:_._fa_icon"></a>`fa_icon`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                 |
| --------------------------------- | ----------------------------------------------- |
| **Must match regular expression** | `^fa` [Test](https://regex101.com/?regex=%5Efa) |

#### <a name="Nextflow_pipeline_input_schema_defs_pattern:_._description"></a>`description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="Nextflow_pipeline_input_schema_defs_pattern:_._required"></a>`required`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

#### <a name="Nextflow_pipeline_input_schema_defs_pattern:_._properties"></a>`properties`

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | Yes      |

#### <a name="Nextflow_pipeline_input_schema_defs_pattern:_._dependentRequired"></a>`dependentRequired`

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

## <a name="Nextflow_pipeline_input_schema_properties"></a>`properties`

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

## <a name="Nextflow_pipeline_input_schema_dependentRequired"></a>`dependentRequired`

|              |          |
| ------------ | -------- |
| **Type**     | `object` |
| **Required** | No       |

## <a name="Nextflow_pipeline_input_schema_allOf"></a>`allOf`

**Title:** Combine definition groups

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Tuple validation** | See below          |

**Array Items:**

Each item must be of type: `object`

## Definitions

The following definitions are used throughout the schema:

### typeAnnotation

**Type:** `enum (of string)`

### allTypes

**Type:** `boolean or integer or null or number or string`

### nonNegativeInteger

**Type:** `integer`

### parameterOptions

**Type:** `object`

### standardKeywords

**Description:** Allowed standard JSON Schema properties.

**Type:** `object`

| Property                                                      | Type             | Deprecated | Definition                    | Title/Description                                                                                                             |
| ------------------------------------------------------------- | ---------------- | ---------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| - [type](#defs_standardKeywords_type)                         | combining        |            |                               | The type of the parameter value. Can be one or more of these: `['integer', 'boolean', 'number', 'string', 'null']`            |
| - [format](#defs_standardKeywords_format)                     | enum (of string) |            |                               | The format of a parameter value with the 'string' type. This is used for additional validation on the structure of the value. |
| - [pattern](#defs_standardKeywords_pattern)                   | string           |            |                               | Check a parameter value of 'string' type against a regex pattern                                                              |
| - [description](#defs_standardKeywords_description)           | string           |            |                               | The description of the current parameter                                                                                      |
| - [default](#defs_standardKeywords_default)                   | object           |            | In #/$defs/allTypes           | Specifies a default value to use for this parameter                                                                           |
| - [examples](#defs_standardKeywords_examples)                 | array            |            |                               | A list of examples for the current parameter                                                                                  |
| - [deprecated](#defs_standardKeywords_deprecated)             | boolean          |            |                               | States that the parameter is deprecated. Please provide a nice deprecation message using 'errorMessage'                       |
| - [minLength](#defs_standardKeywords_minLength)               | object           |            | In #/$defs/nonNegativeInteger | The minimum length a 'string' parameter value should be                                                                       |
| - [maxLength](#defs_standardKeywords_maxLength)               | object           |            | In #/$defs/nonNegativeInteger | The maximum length a 'string' parameter value should be                                                                       |
| - [minimum](#defs_standardKeywords_minimum)                   | number           |            |                               | The mimimum value an 'integer' or 'number' parameter value should be                                                          |
| - [exclusiveMinimum](#defs_standardKeywords_exclusiveMinimum) | number           |            |                               | The exclusive mimimum value an 'integer' or 'number' parameter value should be                                                |
| - [maximum](#defs_standardKeywords_maximum)                   | number           |            |                               | The maximum value an 'integer' or 'number' parameter value should be                                                          |
| - [exclusiveMaximum](#defs_standardKeywords_exclusiveMaximum) | number           |            |                               | The exclusive maximum value an 'integer' or 'number' parameter value should be                                                |
| - [multipleOf](#defs_standardKeywords_multipleOf)             | number           |            |                               | The 'integer' or 'number' parameter value should be a multiple of this value                                                  |
| - [enum](#defs_standardKeywords_enum)                         | array            |            |                               | The parameter value should be one of the values specified in this enum array                                                  |
| - [const](#defs_standardKeywords_const)                       | object           |            | In #/$defs/allTypes           | The parameter value should be equal to this value                                                                             |

### customKeywords

**Description:** Additional custom JSON Schema properties.

**Type:** `object`

| Property                                            | Type    | Deprecated | Definition | Title/Description                                                                                                                                                                       |
| --------------------------------------------------- | ------- | ---------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [errorMessage](#defs_customKeywords_errorMessage) | string  |            |            | NON STANDARD OPTION: The custom error message to display in case validation against this parameter fails. Can also be used as a deprecation message if 'deprecated' is true             |
| - [exists](#defs_customKeywords_exists)             | boolean |            |            | NON STANDARD OPTION: Check if a file exists. This parameter value needs to be a `string` type with one of these formats: `['path', 'file-path', 'directory-path', 'file-path-pattern']` |
| - [schema](#defs_customKeywords_schema)             | string  |            |            | NON STANDARD OPTION: Check the given file against a schema passed to this keyword. Will only work when type is `string` and format is `path` or `file-path`                             |
| - [help_text](#defs_customKeywords_help_text)       | string  |            |            | NON STANDARD OPTION: A more detailed help text                                                                                                                                          |
| - [fa_icon](#defs_customKeywords_fa_icon)           | string  |            |            | NON STANDARD OPTION: A font awesome icon to use in the nf-core parameter documentation                                                                                                  |
| - [hidden](#defs_customKeywords_hidden)             | boolean |            |            | NON STANDARD OPTION: Hide this parameter from the help message and documentation                                                                                                        |
| - [mimetype](#defs_customKeywords_mimetype)         | string  | Yes        |            | NON STANDARD OPTION: The MIME type of the parameter value                                                                                                                               |

---

Generated using a custom JSON Schema documentation generator.
