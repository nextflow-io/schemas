# Nextflow pipeline input schema

**Title:** Nextflow pipeline input schema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Schema to validate Nextflow pipeline input specs

| Property                                  | Pattern | Type            | Deprecated | Definition                                      | Title/Description         |
| ----------------------------------------- | ------- | --------------- | ---------- | ----------------------------------------------- | ------------------------- |
| + [$schema](#schema)                      | No      | string          | No         | -                                               | schema                    |
| + [$id](#id)                              | No      | string          | No         | -                                               | ID URI                    |
| + [title](#title)                         | No      | string          | No         | -                                               | Title                     |
| + [description](#description)             | No      | string          | No         | -                                               | Description               |
| + [type](#type)                           | No      | const           | No         | -                                               | Top level type            |
| - [$defs](#defs)                          | No      | object          | No         | -                                               | Parameter groups          |
| - [properties](#properties)               | No      | object          | No         | Same as [properties](#defs_pattern1_properties) | -                         |
| - [dependentRequired](#dependentRequired) | No      | object          | No         | -                                               | -                         |
| - [allOf](#allOf)                         | No      | array of object | No         | -                                               | Combine definition groups |

## <a name="schema"></a>`$schema`

**Title:** schema

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

## <a name="id"></a>`$id`

**Title:** ID URI

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

## <a name="title"></a>`title`

**Title:** Title

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

## <a name="description"></a>`description`

**Title:** Description

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

## <a name="type"></a>`type`

**Title:** Top level type

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"object"`

## <a name="defs"></a>`$defs`

**Title:** Parameter groups

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                  | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [^.\*$](#defs_pattern1) | Yes     | object | No         | -          | -                 |

### <a name="defs_pattern1"></a>`^.*$`

> All properties whose name matches the regular expression
> `^.*$` ([Test](https://regex101.com/?regex=%5E.%2A%24))
> must respect the following conditions

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                | Pattern | Type   | Deprecated | Definition                  | Title/Description |
| ------------------------------------------------------- | ------- | ------ | ---------- | --------------------------- | ----------------- |
| + [title](#defs_pattern1_title)                         | No      | string | No         | -                           | -                 |
| + [type](#defs_pattern1_type)                           | No      | const  | No         | -                           | -                 |
| - [fa_icon](#defs_pattern1_fa_icon)                     | No      | string | No         | -                           | -                 |
| - [description](#defs_pattern1_description)             | No      | string | No         | -                           | -                 |
| - [required](#defs_pattern1_required)                   | No      | array  | No         | -                           | -                 |
| + [properties](#defs_pattern1_properties)               | No      | object | No         | In #/$defs/parameterOptions | -                 |
| - [dependentRequired](#defs_pattern1_dependentRequired) | No      | object | No         | -                           | -                 |

#### <a name="defs_pattern1_title"></a>`title`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

#### <a name="defs_pattern1_type"></a>`type`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"object"`

#### <a name="defs_pattern1_fa_icon"></a>`fa_icon`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

| Restrictions                      |                                                 |
| --------------------------------- | ----------------------------------------------- |
| **Must match regular expression** | `^fa` [Test](https://regex101.com/?regex=%5Efa) |

#### <a name="defs_pattern1_description"></a>`description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="defs_pattern1_required"></a>`required`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | N/A                |

#### <a name="defs_pattern1_properties"></a>`properties`

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `object`                 |
| **Required**              | Yes                      |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/$defs/parameterOptions |

| Property                                      | Pattern | Type        | Deprecated | Definition | Title/Description |
| --------------------------------------------- | ------- | ----------- | ---------- | ---------- | ----------------- |
| - [^.\*$](#defs_pattern1_properties_pattern1) | Yes     | Combination | No         | -          | -                 |

##### <a name="defs_pattern1_properties_pattern1"></a>`^.*$`

> All properties whose name matches the regular expression
> `^.*$` ([Test](https://regex101.com/?regex=%5E.%2A%24))
> must respect the following conditions

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| All of(Requirement)                                                |
| ------------------------------------------------------------------ |
| [standardKeywords](#defs_pattern1_properties_pattern1_pattern2_i0) |
| [customKeywords](#defs_pattern1_properties_pattern1_pattern2_i1)   |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0"></a>`standardKeywords`

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `object`                 |
| **Required**              | No                       |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/$defs/standardKeywords |

**Description:** Allowed standard JSON Schema properties.

| Property                                                                              | Pattern | Type                                     | Deprecated | Definition                                                                    | Title/Description                                                                                                             |
| ------------------------------------------------------------------------------------- | ------- | ---------------------------------------- | ---------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| - [type](#defs_pattern1_properties_pattern1_pattern2_i0_type)                         | No      | Combination                              | No         | -                                                                             | The type of the parameter value. Can be one or more of these: \`['integer', 'boolean', 'number', 'string', 'null']\`          |
| - [format](#defs_pattern1_properties_pattern1_pattern2_i0_format)                     | No      | enum (of string)                         | No         | -                                                                             | The format of a parameter value with the 'string' type. This is used for additional validation on the structure of the value. |
| - [pattern](#defs_pattern1_properties_pattern1_pattern2_i0_pattern)                   | No      | string                                   | No         | -                                                                             | Check a parameter value of 'string' type against a regex pattern                                                              |
| - [description](#defs_pattern1_properties_pattern1_pattern2_i0_description)           | No      | string                                   | No         | -                                                                             | The description of the current parameter                                                                                      |
| - [default](#defs_pattern1_properties_pattern1_pattern2_i0_default)                   | No      | integer, boolean, string, number or null | No         | In #/$defs/allTypes                                                           | Specifies a default value to use for this parameter                                                                           |
| - [examples](#defs_pattern1_properties_pattern1_pattern2_i0_examples)                 | No      | array                                    | No         | -                                                                             | A list of examples for the current parameter                                                                                  |
| - [deprecated](#defs_pattern1_properties_pattern1_pattern2_i0_deprecated)             | No      | boolean                                  | No         | -                                                                             | States that the parameter is deprecated. Please provide a nice deprecation message using 'errorMessage'                       |
| - [minLength](#defs_pattern1_properties_pattern1_pattern2_i0_minLength)               | No      | integer                                  | No         | In #/$defs/nonNegativeInteger                                                 | The minimum length a 'string' parameter value should be                                                                       |
| - [maxLength](#defs_pattern1_properties_pattern1_pattern2_i0_maxLength)               | No      | integer                                  | No         | Same as [minLength](#defs_pattern1_properties_pattern1_pattern2_i0_minLength) | The maximum length a 'string' parameter value should be                                                                       |
| - [minimum](#defs_pattern1_properties_pattern1_pattern2_i0_minimum)                   | No      | number                                   | No         | -                                                                             | The mimimum value an 'integer' or 'number' parameter value should be                                                          |
| - [exclusiveMinimum](#defs_pattern1_properties_pattern1_pattern2_i0_exclusiveMinimum) | No      | number                                   | No         | -                                                                             | The exclusive mimimum value an 'integer' or 'number' parameter value should be                                                |
| - [maximum](#defs_pattern1_properties_pattern1_pattern2_i0_maximum)                   | No      | number                                   | No         | -                                                                             | The maximum value an 'integer' or 'number' parameter value should be                                                          |
| - [exclusiveMaximum](#defs_pattern1_properties_pattern1_pattern2_i0_exclusiveMaximum) | No      | number                                   | No         | -                                                                             | The exclusive maximum value an 'integer' or 'number' parameter value should be                                                |
| - [multipleOf](#defs_pattern1_properties_pattern1_pattern2_i0_multipleOf)             | No      | number                                   | No         | -                                                                             | The 'integer' or 'number' parameter value should be a multiple of this value                                                  |
| - [enum](#defs_pattern1_properties_pattern1_pattern2_i0_enum)                         | No      | array                                    | No         | -                                                                             | The parameter value should be one of the values specified in this enum array                                                  |
| - [const](#defs_pattern1_properties_pattern1_pattern2_i0_const)                       | No      | integer, boolean, string, number or null | No         | Same as [default](#defs_pattern1_properties_pattern1_pattern2_i0_default)     | The parameter value should be equal to this value                                                                             |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_type"></a>`type`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** The type of the parameter value. Can be one or more of these: `['integer', 'boolean', 'number', 'string', 'null']`

| Any of(Option)                                                                 |
| ------------------------------------------------------------------------------ |
| [typeAnnotation](#defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i0) |
| [item 1](#defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i1)         |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i0"></a>`typeAnnotation`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `enum (of string)`     |
| **Required**   | No                     |
| **Defined in** | #/$defs/typeAnnotation |

Must be one of:

- "string"
- "boolean"
- "integer"
- "number"
- "null"

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i1"></a>`item 1`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                      | Description |
| ------------------------------------------------------------------------------------ | ----------- |
| [typeAnnotation](#defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i1_items) | -           |

###### typeAnnotation

|                        |                                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Type**               | `enum (of string)`                                                                                                          |
| **Required**           | No                                                                                                                          |
| **Same definition as** | [defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i0](#defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i0) |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_format"></a>`format`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** The format of a parameter value with the 'string' type. This is used for additional validation on the structure of the value.

Must be one of:

- "file-path"
- "directory-path"
- "path"
- "file-path-pattern"
- "date-time"
- "date"
- "time"
- "email"
- "uri"
- "regex"

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_pattern"></a>`pattern`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `regex`  |

**Description:** Check a parameter value of 'string' type against a regex pattern

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_description"></a>`description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** The description of the current parameter

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_default"></a>`default`

|                |                                            |
| -------------- | ------------------------------------------ |
| **Type**       | `integer, boolean, string, number or null` |
| **Required**   | No                                         |
| **Defined in** | #/$defs/allTypes                           |

**Description:** Specifies a default value to use for this parameter

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_examples"></a>`examples`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** A list of examples for the current parameter

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                           | Description |
| ------------------------------------------------------------------------- | ----------- |
| [allTypes](#defs_pattern1_properties_pattern1_pattern2_i0_examples_items) | -           |

###### allTypes

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| **Type**               | `integer, boolean, string, number or null`                        |
| **Required**           | No                                                                |
| **Same definition as** | [default](#defs_pattern1_properties_pattern1_pattern2_i0_default) |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_deprecated"></a>`deprecated`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** States that the parameter is deprecated. Please provide a nice deprecation message using 'errorMessage'

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_minLength"></a>`minLength`

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `integer`                  |
| **Required**   | No                         |
| **Defined in** | #/$defs/nonNegativeInteger |

**Description:** The minimum length a 'string' parameter value should be

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_maxLength"></a>`maxLength`

|                        |                                                                       |
| ---------------------- | --------------------------------------------------------------------- |
| **Type**               | `integer`                                                             |
| **Required**           | No                                                                    |
| **Same definition as** | [minLength](#defs_pattern1_properties_pattern1_pattern2_i0_minLength) |

**Description:** The maximum length a 'string' parameter value should be

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_minimum"></a>`minimum`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** The mimimum value an 'integer' or 'number' parameter value should be

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_exclusiveMinimum"></a>`exclusiveMinimum`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** The exclusive mimimum value an 'integer' or 'number' parameter value should be

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_maximum"></a>`maximum`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** The maximum value an 'integer' or 'number' parameter value should be

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_exclusiveMaximum"></a>`exclusiveMaximum`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** The exclusive maximum value an 'integer' or 'number' parameter value should be

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_multipleOf"></a>`multipleOf`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** The 'integer' or 'number' parameter value should be a multiple of this value

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_enum"></a>`enum`

|              |         |
| ------------ | ------- |
| **Type**     | `array` |
| **Required** | No      |

**Description:** The parameter value should be one of the values specified in this enum array

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                       | Description |
| --------------------------------------------------------------------- | ----------- |
| [allTypes](#defs_pattern1_properties_pattern1_pattern2_i0_enum_items) | -           |

###### allTypes

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| **Type**               | `integer, boolean, string, number or null`                        |
| **Required**           | No                                                                |
| **Same definition as** | [default](#defs_pattern1_properties_pattern1_pattern2_i0_default) |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_const"></a>`const`

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| **Type**               | `integer, boolean, string, number or null`                        |
| **Required**           | No                                                                |
| **Same definition as** | [default](#defs_pattern1_properties_pattern1_pattern2_i0_default) |

**Description:** The parameter value should be equal to this value

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1"></a>`customKeywords`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Required**              | No                     |
| **Additional properties** | Any type allowed       |
| **Defined in**            | #/$defs/customKeywords |

**Description:** Additional custom JSON Schema properties.

| Property                                                                      | Pattern | Type    | Deprecated | Definition | Title/Description                                                                                                                                                                           |
| ----------------------------------------------------------------------------- | ------- | ------- | ---------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - [errorMessage](#defs_pattern1_properties_pattern1_pattern2_i1_errorMessage) | No      | string  | No         | -          | NON STANDARD OPTION: The custom error message to display in case validation against this parameter fails. Can also be used as a deprecation message if 'deprecated' is true                 |
| - [exists](#defs_pattern1_properties_pattern1_pattern2_i1_exists)             | No      | boolean | No         | -          | NON STANDARD OPTION: Check if a file exists. This parameter value needs to be a \`string\` type with one of these formats: \`['path', 'file-path', 'directory-path', 'file-path-pattern']\` |
| - [schema](#defs_pattern1_properties_pattern1_pattern2_i1_schema)             | No      | string  | No         | -          | NON STANDARD OPTION: Check the given file against a schema passed to this keyword. Will only work when type is \`string\` and format is \`path\` or \`file-path\`                           |
| - [help_text](#defs_pattern1_properties_pattern1_pattern2_i1_help_text)       | No      | string  | No         | -          | NON STANDARD OPTION: A more detailed help text                                                                                                                                              |
| - [fa_icon](#defs_pattern1_properties_pattern1_pattern2_i1_fa_icon)           | No      | string  | No         | -          | NON STANDARD OPTION: A font awesome icon to use in the nf-core parameter documentation                                                                                                      |
| - [hidden](#defs_pattern1_properties_pattern1_pattern2_i1_hidden)             | No      | boolean | No         | -          | NON STANDARD OPTION: Hide this parameter from the help message and documentation                                                                                                            |
| - [mimetype](#defs_pattern1_properties_pattern1_pattern2_i1_mimetype)         | No      | string  | No         | -          | NON STANDARD OPTION: The MIME type of the parameter value                                                                                                                                   |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_errorMessage"></a>`errorMessage`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** NON STANDARD OPTION: The custom error message to display in case validation against this parameter fails. Can also be used as a deprecation message if 'deprecated' is true

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_exists"></a>`exists`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** NON STANDARD OPTION: Check if a file exists. This parameter value needs to be a `string` type with one of these formats: `['path', 'file-path', 'directory-path', 'file-path-pattern']`

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_schema"></a>`schema`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** NON STANDARD OPTION: Check the given file against a schema passed to this keyword. Will only work when type is `string` and format is `path` or `file-path`

| Restrictions                      |                                                           |
| --------------------------------- | --------------------------------------------------------- |
| **Min length**                    | 1                                                         |
| **Must match regular expression** | `\.json$` [Test](https://regex101.com/?regex=%5C.json%24) |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_help_text"></a>`help_text`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** NON STANDARD OPTION: A more detailed help text

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_fa_icon"></a>`fa_icon`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** NON STANDARD OPTION: A font awesome icon to use in the nf-core parameter documentation

| Restrictions                      |                                                 |
| --------------------------------- | ----------------------------------------------- |
| **Must match regular expression** | `^fa` [Test](https://regex101.com/?regex=%5Efa) |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_hidden"></a>`hidden`

|              |           |
| ------------ | --------- |
| **Type**     | `boolean` |
| **Required** | No        |

**Description:** NON STANDARD OPTION: Hide this parameter from the help message and documentation

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_mimetype"></a>`mimetype`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** NON STANDARD OPTION: The MIME type of the parameter value

###### The following properties are required

- type
- description

#### <a name="defs_pattern1_dependentRequired"></a>`dependentRequired`

|                           |                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                     |
| **Required**              | No                                                                                                           |
| **Additional properties** | [Each additional property must conform to the schema](#defs_pattern1_dependentRequired_additionalProperties) |

| Property                                                    | Pattern | Type            | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| - [](#defs_pattern1_dependentRequired_additionalProperties) | No      | array of string | No         | -          | -                 |

##### <a name="defs_pattern1_dependentRequired_additionalProperties"></a>`additionalProperties`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |
| **Default**  | `[]`              |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                                           | Description |
| ----------------------------------------------------------------------------------------- | ----------- |
| [additionalProperties items](#defs_pattern1_dependentRequired_additionalProperties_items) | -           |

###### additionalProperties items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="properties"></a>`properties`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Required**              | No                                      |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [properties](#defs_pattern1_properties) |

## <a name="dependentRequired"></a>`dependentRequired`

|                           |                                                                                                |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                       |
| **Required**              | No                                                                                             |
| **Additional properties** | [Each additional property must conform to the schema](#dependentRequired_additionalProperties) |

| Property                                      | Pattern | Type            | Deprecated | Definition | Title/Description |
| --------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| - [](#dependentRequired_additionalProperties) | No      | array of string | No         | -          | -                 |

### <a name="dependentRequired_additionalProperties"></a>`additionalProperties`

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of string` |
| **Required** | No                |
| **Default**  | `[]`              |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | True               |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be                                             | Description |
| --------------------------------------------------------------------------- | ----------- |
| [additionalProperties items](#dependentRequired_additionalProperties_items) | -           |

#### additionalProperties items

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

## <a name="allOf"></a>`allOf`

**Title:** Combine definition groups

|              |                   |
| ------------ | ----------------- |
| **Type**     | `array of object` |
| **Required** | No                |

|                      | Array restrictions |
| -------------------- | ------------------ |
| **Min items**        | N/A                |
| **Max items**        | N/A                |
| **Items unicity**    | False              |
| **Additional items** | False              |
| **Tuple validation** | See below          |

| Each item of this array must be | Description |
| ------------------------------- | ----------- |
| [allOf items](#allOf_items)     | -           |

### allOf items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| -------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| + [$ref](#allOf_items_ref) | No      | string | No         | -          | -                 |

#### <a name="allOf_items_ref"></a>`$ref`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

| Restrictions                      |                                                                                                 |
| --------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Must match regular expression** | `^#/\$defs/[^/]+$` [Test](https://regex101.com/?regex=%5E%23%2F%5C%24defs%2F%5B%5E%2F%5D%2B%24) |

---

Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
