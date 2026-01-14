# Nextflow pipeline input schema

**Title:** Nextflow pipeline input schema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

**Description:** Schema to validate Nextflow pipeline input specs

| Property                                  | Type            |
| ----------------------------------------- | --------------- |
| + [$schema](#schema)                      | string          |
| + [$id](#id)                              | string          |
| + [title](#title)                         | string          |
| + [description](#description)             | string          |
| + [type](#type)                           | const           |
| - [$defs](#defs)                          | object          |
| - [properties](#properties)               | object          |
| - [dependentRequired](#dependentRequired) | object          |
| - [allOf](#allOf)                         | array of object |

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
| **Additional properties** | Any type allowed |

**Description:** A slightly strange use of a JSON schema standard that we use for Nextflow schema is `$defs`.

JSON schema can group variables together in an `object`, but then the validation expects this structure to exist in the data that it is validating.
In reality, we have a very long "flat" list of parameters, all at the top level of `params.foo`.

In order to give some structure to log outputs, documentation and so on, we group parameters into `$defs`.
Each `def` is an object with a title, description and so on.
However, as they are under `$defs` scope they are effectively ignored by the validation and so their nested nature is not a problem.
We then bring the contents of each definition object back to the "flat" top level for validation using a series of `allOf` statements at the end of the schema,
which reference the specific definition keys.

| Property                  | Type   |
| ------------------------- | ------ |
| - [^.\*$](#defs_pattern1) | object |

### <a name="defs_pattern1"></a>`^.*$`

> All properties whose name matches the regular expression
> `^.*$` ([Test](https://regex101.com/?regex=%5E.%2A%24))
> must respect the following conditions

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                                                | Type   |
| ------------------------------------------------------- | ------ |
| + [title](#defs_pattern1_title)                         | string |
| + [type](#defs_pattern1_type)                           | const  |
| - [fa_icon](#defs_pattern1_fa_icon)                     | string |
| - [description](#defs_pattern1_description)             | string |
| - [required](#defs_pattern1_required)                   | array  |
| + [properties](#defs_pattern1_properties)               | object |
| - [dependentRequired](#defs_pattern1_dependentRequired) | object |

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

|                                   |                                                     |
| --------------------------------- | --------------------------------------------------- |
| **Type**                          | `string`                                            |
| Restrictions                      |                                                     |
| --------------------------------- | --------------------------------------------------- |
| **Must match regular expression** | `^fa` [Test](https://regex101.com/?regex=%5Efa)     |

#### <a name="defs_pattern1_description"></a>`description`

|          |          |
| -------- | -------- |
| **Type** | `string` |

#### <a name="defs_pattern1_required"></a>`required`

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** Any parameters that _must_ be specified should be set as `required` in the schema.

!!! tip

    Make sure you do set `null` as a default value for the parameter, otherwise it will have a value even if not supplied by the pipeline user and the required property will have no effect.

This is not done with a property key like other things described below, but rather by naming
the parameter in the `required` array in the definition object / top-level object.

For more information, see the [JSON schema documentation](https://json-schema.org/understanding-json-schema/reference/object.html#required-properties).

#### <a name="defs_pattern1_properties"></a>`properties`

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `object`                 |
| **Required**              | Yes                      |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/$defs/parameterOptions |

| Property                                      | Type        |
| --------------------------------------------- | ----------- |
| - [^.\*$](#defs_pattern1_properties_pattern1) | Combination |

##### <a name="defs_pattern1_properties_pattern1"></a>`^.*$`

> All properties whose name matches the regular expression
> `^.*$` ([Test](https://regex101.com/?regex=%5E.%2A%24))
> must respect the following conditions

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

| All of(Requirement)                                                |
| ------------------------------------------------------------------ |
| [standardKeywords](#defs_pattern1_properties_pattern1_pattern2_i0) |
| [customKeywords](#defs_pattern1_properties_pattern1_pattern2_i1)   |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0"></a>`standardKeywords`

|                           |                          |
| ------------------------- | ------------------------ |
| **Type**                  | `object`                 |
| **Additional properties** | Any type allowed         |
| **Defined in**            | #/$defs/standardKeywords |

**Description:** Allowed standard JSON Schema properties.

| Property                                                                              | Type                                     |
| ------------------------------------------------------------------------------------- | ---------------------------------------- |
| - [type](#defs_pattern1_properties_pattern1_pattern2_i0_type)                         | Combination                              |
| - [format](#defs_pattern1_properties_pattern1_pattern2_i0_format)                     | enum (of string)                         |
| - [pattern](#defs_pattern1_properties_pattern1_pattern2_i0_pattern)                   | string                                   |
| - [description](#defs_pattern1_properties_pattern1_pattern2_i0_description)           | string                                   |
| - [default](#defs_pattern1_properties_pattern1_pattern2_i0_default)                   | integer, boolean, string, number or null |
| - [examples](#defs_pattern1_properties_pattern1_pattern2_i0_examples)                 | array                                    |
| - [deprecated](#defs_pattern1_properties_pattern1_pattern2_i0_deprecated)             | boolean                                  |
| - [minLength](#defs_pattern1_properties_pattern1_pattern2_i0_minLength)               | integer                                  |
| - [maxLength](#defs_pattern1_properties_pattern1_pattern2_i0_maxLength)               | integer                                  |
| - [minimum](#defs_pattern1_properties_pattern1_pattern2_i0_minimum)                   | number                                   |
| - [exclusiveMinimum](#defs_pattern1_properties_pattern1_pattern2_i0_exclusiveMinimum) | number                                   |
| - [maximum](#defs_pattern1_properties_pattern1_pattern2_i0_maximum)                   | number                                   |
| - [exclusiveMaximum](#defs_pattern1_properties_pattern1_pattern2_i0_exclusiveMaximum) | number                                   |
| - [multipleOf](#defs_pattern1_properties_pattern1_pattern2_i0_multipleOf)             | number                                   |
| - [enum](#defs_pattern1_properties_pattern1_pattern2_i0_enum)                         | array                                    |
| - [const](#defs_pattern1_properties_pattern1_pattern2_i0_const)                       | integer, boolean, string, number or null |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_type"></a>`type`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Additional properties** | Any type allowed |

**Description:** Variable type, taken from the [JSON schema keyword vocabulary](https://json-schema.org/understanding-json-schema/reference/type.html):

- `string`
- `number` (float)
- `integer`
- `boolean` (true / false)
- `object` (currently only supported for file validation, see Nested parameters)
- `array` (currently only supported for file validation, see Nested parameters)

Validation checks that the supplied parameter matches the expected type, and will fail with an error if not.

This JSON schema type is _not_ supported:

- `null`

| Any of(Option)                                                                 |
| ------------------------------------------------------------------------------ |
| [typeAnnotation](#defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i0) |
| [item 1](#defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i1)         |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i0"></a>`typeAnnotation`

|                |                        |
| -------------- | ---------------------- |
| **Type**       | `enum (of string)`     |
| **Defined in** | #/$defs/typeAnnotation |

Must be one of:

- "string"
- "boolean"
- "integer"
- "number"
- "null"

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i1"></a>`item 1`

|                                                                                      |             |
| ------------------------------------------------------------------------------------ | ----------- |
| **Type**                                                                             | `array`     |
| Each item of this array must be                                                      | Description |
| ------------------------------------------------------------------------------------ | ----------- |
| [typeAnnotation](#defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i1_items) | -           |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i1_items"></a>typeAnnotation

|                        |                                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Type**               | `enum (of string)`                                                                                                          |
| **Same definition as** | [defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i0](#defs_pattern1_properties_pattern1_pattern2_i0_type_anyOf_i0) |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_format"></a>`format`

|          |                    |
| -------- | ------------------ |
| **Type** | `enum (of string)` |

**Description:** Formats can be used to give additional validation checks against `string` values for certain properties.

!!! example "Non-standard key (values)"

    The `format` key is a [standard JSON schema key](https://json-schema.org/understanding-json-schema/reference/string.html#format),
    however we primarily use it for validating file / directory path operations with non-standard schema values.

Example usage is as follows:

```json
{
  "type": "string",
  "format": "file-path"
}
```

The available `format` types are below:

`file-path`
: States that the provided value is a file. Does not check its existence, but it does check if the path is not a directory.

`directory-path`
: States that the provided value is a directory. Does not check its existence, but if it exists, it does check that the path is not a file.

`path`
: States that the provided value is a path (file or directory). Does not check its existence.

`file-path-pattern`
: States that the provided value is a glob pattern that will be used to fetch files. Checks that the pattern is valid and that at least one file is found.

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

|            |          |
| ---------- | -------- |
| **Type**   | `string` |
| **Format** | `regex`  |

**Description:** Regular expression which the string must match in order to pass validation.

- See the [JSON schema docs](https://json-schema.org/understanding-json-schema/reference/string.html#regular-expressions)
  for details.
- Use <https://regex101.com/> for help with writing regular expressions.

For example, this pattern only validates if the supplied string ends in `.fastq`, `.fq`, `.fastq.gz` or `.fq.gz`:

```json
{
  "type": "string",
  "pattern": ".*.f(ast)?q(.gz)?$"
}
```

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_description"></a>`description`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** A short description of what the parameter does, written in markdown.
Printed in docs and terminal help text.
Should be maximum one short sentence.

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_default"></a>`default`

|                |                                            |
| -------------- | ------------------------------------------ |
| **Type**       | `integer, boolean, string, number or null` |
| **Defined in** | #/$defs/allTypes                           |

**Description:** Default value for the parameter.

Should match the `type` and validation patterns set for the parameter in other fields.

!!! tip

    If no default should be set, completely omit this key from the schema.
    Do not set it as an empty string, or `null`.

    However, parameters with no defaults _should_ be set to `null` within your Nextflow config file.

!!! note

    When creating a schema using `nf-core schema build`, this field will be automatically created based
    on the default value defined in the pipeline config files.

    Generally speaking, the two should always be kept in sync to avoid unexpected problems and usage errors.
    In some rare cases, this may not be possible (for example, a dynamic groovy expression cannot be encoded in JSON),
    in which case try to specify as "sensible" a default within the schema as possible.

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_examples"></a>`examples`

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** A list of examples for the current parameter

| Each item of this array must be                                           | Description |
| ------------------------------------------------------------------------- | ----------- |
| [allTypes](#defs_pattern1_properties_pattern1_pattern2_i0_examples_items) | -           |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_examples_items"></a>allTypes

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| **Type**               | `integer, boolean, string, number or null`                        |
| **Same definition as** | [default](#defs_pattern1_properties_pattern1_pattern2_i0_default) |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_deprecated"></a>`deprecated`

|          |           |
| -------- | --------- |
| **Type** | `boolean` |

**Description:** !!! example "Extended key"

A boolean JSON flag that instructs anything using the schema that this parameter/field is deprecated and should not be used. This can be useful to generate messages telling the user that a parameter has changed between versions.

JSON schema states that this is an informative key only, but in `nf-schema` this will cause a validation error if the parameter/field is used.

!!! tip

    Using the [`errorMessage`](#errormessage) keyword can be useful to provide more information about the deprecation and what to use instead.

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_minLength"></a>`minLength`

|                |                            |
| -------------- | -------------------------- |
| **Type**       | `integer`                  |
| **Defined in** | #/$defs/nonNegativeInteger |

**Description:** Specify a minimum / maximum string length with `minLength` and `maxLength`.

- See the [JSON schema docs](https://json-schema.org/understanding-json-schema/reference/string.html#length)
  for details.

```json
{
  "type": "string",
  "minLength": 2,
  "maxLength": 3
}
```

| Restrictions |        |
| ------------ | ------ |
| **Minimum**  | &ge; 0 |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_maxLength"></a>`maxLength`

|                        |                                                                       |
| ---------------------- | --------------------------------------------------------------------- |
| **Type**               | `integer`                                                             |
| **Same definition as** | [minLength](#defs_pattern1_properties_pattern1_pattern2_i0_minLength) |

**Description:** Specify a minimum / maximum string length with `minLength` and `maxLength`.

- See the [JSON schema docs](https://json-schema.org/understanding-json-schema/reference/string.html#length)
  for details.

```json
{
  "type": "string",
  "minLength": 2,
  "maxLength": 3
}
```

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_minimum"></a>`minimum`

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** Specify a minimum / maximum value for an integer or float number length with `minimum` and `maximum`.

- See the [JSON schema docs](https://json-schema.org/understanding-json-schema/reference/numeric.html#range)
  for details.

> If x is the value being validated, the following must hold true:
>
> - `x` ≥ `minimum`
> - `x` ≤ `maximum`

```json
{
  "type": "number",
  "minimum": 0,
  "maximum": 100
}
```

!!! note

    The JSON schema doc also mention `exclusiveMinimum`, `exclusiveMaximum` and `multipleOf` keys.
    Because nf-schema uses stock JSON schema validation libraries, these _should_ work for validating keys.
    However, they are not officially supported within the Nextflow schema ecosystem and so some interfaces may not recognise them.

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_exclusiveMinimum"></a>`exclusiveMinimum`

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** Specify a minimum / maximum value for an integer or float number length with `minimum` and `maximum`.

- See the [JSON schema docs](https://json-schema.org/understanding-json-schema/reference/numeric.html#range)
  for details.

> If x is the value being validated, the following must hold true:
>
> - `x` ≥ `minimum`
> - `x` ≤ `maximum`

```json
{
  "type": "number",
  "minimum": 0,
  "maximum": 100
}
```

!!! note

    The JSON schema doc also mention `exclusiveMinimum`, `exclusiveMaximum` and `multipleOf` keys.
    Because nf-schema uses stock JSON schema validation libraries, these _should_ work for validating keys.
    However, they are not officially supported within the Nextflow schema ecosystem and so some interfaces may not recognise them.

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_maximum"></a>`maximum`

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** Specify a minimum / maximum value for an integer or float number length with `minimum` and `maximum`.

- See the [JSON schema docs](https://json-schema.org/understanding-json-schema/reference/numeric.html#range)
  for details.

> If x is the value being validated, the following must hold true:
>
> - `x` ≥ `minimum`
> - `x` ≤ `maximum`

```json
{
  "type": "number",
  "minimum": 0,
  "maximum": 100
}
```

!!! note

    The JSON schema doc also mention `exclusiveMinimum`, `exclusiveMaximum` and `multipleOf` keys.
    Because nf-schema uses stock JSON schema validation libraries, these _should_ work for validating keys.
    However, they are not officially supported within the Nextflow schema ecosystem and so some interfaces may not recognise them.

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_exclusiveMaximum"></a>`exclusiveMaximum`

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** Specify a minimum / maximum value for an integer or float number length with `minimum` and `maximum`.

- See the [JSON schema docs](https://json-schema.org/understanding-json-schema/reference/numeric.html#range)
  for details.

> If x is the value being validated, the following must hold true:
>
> - `x` ≥ `minimum`
> - `x` ≤ `maximum`

```json
{
  "type": "number",
  "minimum": 0,
  "maximum": 100
}
```

!!! note

    The JSON schema doc also mention `exclusiveMinimum`, `exclusiveMaximum` and `multipleOf` keys.
    Because nf-schema uses stock JSON schema validation libraries, these _should_ work for validating keys.
    However, they are not officially supported within the Nextflow schema ecosystem and so some interfaces may not recognise them.

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_multipleOf"></a>`multipleOf`

|          |          |
| -------- | -------- |
| **Type** | `number` |

**Description:** The 'integer' or 'number' parameter value should be a multiple of this value

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_enum"></a>`enum`

|          |         |
| -------- | ------- |
| **Type** | `array` |

**Description:** An array of enumerated values: the parameter must match one of these values exactly to pass validation.

- See the [JSON schema docs](https://json-schema.org/understanding-json-schema/reference/generic.html#enumerated-values)
  for details.
- Available for strings, numbers and integers.

```json
{
  "enum": ["red", "amber", "green"]
}
```

| Each item of this array must be                                       | Description |
| --------------------------------------------------------------------- | ----------- |
| [allTypes](#defs_pattern1_properties_pattern1_pattern2_i0_enum_items) | -           |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_enum_items"></a>allTypes

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| **Type**               | `integer, boolean, string, number or null`                        |
| **Same definition as** | [default](#defs_pattern1_properties_pattern1_pattern2_i0_default) |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i0_const"></a>`const`

|                        |                                                                   |
| ---------------------- | ----------------------------------------------------------------- |
| **Type**               | `integer, boolean, string, number or null`                        |
| **Same definition as** | [default](#defs_pattern1_properties_pattern1_pattern2_i0_default) |

**Description:** The parameter value should be equal to this value

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1"></a>`customKeywords`

|                           |                        |
| ------------------------- | ---------------------- |
| **Type**                  | `object`               |
| **Additional properties** | Any type allowed       |
| **Defined in**            | #/$defs/customKeywords |

**Description:** Additional custom JSON Schema properties.

| Property                                                                      | Type    |
| ----------------------------------------------------------------------------- | ------- |
| - [errorMessage](#defs_pattern1_properties_pattern1_pattern2_i1_errorMessage) | string  |
| - [exists](#defs_pattern1_properties_pattern1_pattern2_i1_exists)             | boolean |
| - [schema](#defs_pattern1_properties_pattern1_pattern2_i1_schema)             | string  |
| - [help_text](#defs_pattern1_properties_pattern1_pattern2_i1_help_text)       | string  |
| - [fa_icon](#defs_pattern1_properties_pattern1_pattern2_i1_fa_icon)           | string  |
| - [hidden](#defs_pattern1_properties_pattern1_pattern2_i1_hidden)             | boolean |
| - [mimetype](#defs_pattern1_properties_pattern1_pattern2_i1_mimetype)         | string  |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_errorMessage"></a>`errorMessage`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:**
!!! example "Non-standard key"

If validation fails, an error message is printed to the terminal, so that the end user knows what to fix.
However, these messages are not always very clear - especially to newcomers.

To improve this experience, pipeline developers can set a custom `errorMessage` for a given parameter in a the schema.
If validation fails, this `errorMessage` is printed after the original error message to guide the pipeline users to an easier solution.

For example, instead of printing:

```
* --input (samples.yml): "samples.yml" does not match regular expression [^\S+\.csv$]
```

We can set

```json
"input": {
  "type": "string",
  "pattern": "^\S+\.csv$",
  "errorMessage": "File name must end in '.csv' cannot contain spaces"
}
```

and get:

```
* --input (samples.yml): "samples.yml" does not match regular expression [^\S+\.csv$] (File name must end in '.csv' cannot contain spaces)
```

| Restrictions   |     |
| -------------- | --- |
| **Min length** | 1   |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_exists"></a>`exists`

|          |           |
| -------- | --------- |
| **Type** | `boolean` |

**Description:** When a format is specified for a value, you can provide the key `exists` set to true in order to validate that the provided path exists. Set this to `false` to validate that the path does not exist.

Example usage is as follows:

```json
{
  "type": "string",
  "format": "file-path",
  "exists": true
}
```

!!! note

    If the parameter is an S3, Azure or Google Cloud URI path, this validation is ignored.

!!! warning

    Make sure to only use the `exists` keyword in combination with any file path format. Using `exists` on a normal string will assume that it's a file and will probably fail unexpectedly.

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_schema"></a>`schema`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** Path to a JSON schema file used to validate _the supplied file_.

Should only be set when `format` is `file-path`.

!!! tip

    Setting this field is key to working with sample sheet validation and channel generation, as described in the next section of the nf-schema docs.

These schema files are typically stored in the pipeline `assets` directory, but can be anywhere.

```json
{
  "type": "string",
  "format": "file-path",
  "schema": "assets/foo_schema.json"
}
```

!!! note

    If the parameter is set to `null`, `false` or an empty string, this validation is ignored. The file won't be validated.

| Restrictions                      |                                                           |
| --------------------------------- | --------------------------------------------------------- |
| **Min length**                    | 1                                                         |
| **Must match regular expression** | `\.json$` [Test](https://regex101.com/?regex=%5C.json%24) |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_help_text"></a>`help_text`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:**
!!! example "Non-standard key"

A longer text with usage help for the parameter, written in markdown.
Can include newlines with multiple paragraphs and more complex markdown structures.

Typically hidden by default in documentation and interfaces, unless explicitly clicked / requested.

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_fa_icon"></a>`fa_icon`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:**
!!! example "Non-standard key"

A text identifier corresponding to an icon from [Font Awesome](https://fontawesome.com/).
Used for easier visual navigation of documentation and pipeline interfaces.

Should be the font-awesome class names, for example:

```json
"fa_icon": "fas fa-file-csv"
```

| Restrictions                      |                                                 |
| --------------------------------- | ----------------------------------------------- |
| **Must match regular expression** | `^fa` [Test](https://regex101.com/?regex=%5Efa) |

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_hidden"></a>`hidden`

|          |           |
| -------- | --------- |
| **Type** | `boolean` |

**Description:**
!!! example "Non-standard key"

A boolean JSON flag that instructs anything using the schema that this is an unimportant parameter.

Typically used to keep the pipeline docs / UIs uncluttered with common parameters which are not used by the majority of users.
For example, `--plaintext_email` and `--monochrome_logs`.

```json
"hidden": true
```

###### <a name="defs_pattern1_properties_pattern1_pattern2_i1_mimetype"></a>`mimetype`

|          |          |
| -------- | -------- |
| **Type** | `string` |

**Description:** MIME type for a file path. Setting this value informs downstream tools about what _kind_ of file is expected.

Should only be set when `format` is `file-path`.

- See a [list of common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)

```json
{
  "type": "string",
  "format": "file-path",
  "mimetype": "text/csv"
}
```

###### <a name="autogenerated_heading_2"></a>The following properties are required

- type
- description

#### <a name="defs_pattern1_dependentRequired"></a>`dependentRequired`

|                           |                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Type**                  | `object`                                                                                                     |
| **Additional properties** | [Each additional property must conform to the schema](#defs_pattern1_dependentRequired_additionalProperties) |

| Property                                                    | Type            |
| ----------------------------------------------------------- | --------------- |
| - [](#defs_pattern1_dependentRequired_additionalProperties) | array of string |

##### <a name="defs_pattern1_dependentRequired_additionalProperties"></a>`additionalProperties`

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `[]`              |

| Each item of this array must be                                                           | Description |
| ----------------------------------------------------------------------------------------- | ----------- |
| [additionalProperties items](#defs_pattern1_dependentRequired_additionalProperties_items) | -           |

###### <a name="defs_pattern1_dependentRequired_additionalProperties_items"></a>additionalProperties items

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="properties"></a>`properties`

|                           |                                         |
| ------------------------- | --------------------------------------- |
| **Type**                  | `object`                                |
| **Additional properties** | Any type allowed                        |
| **Same definition as**    | [properties](#defs_pattern1_properties) |

## <a name="dependentRequired"></a>`dependentRequired`

|                           |                                                                                                |
| ------------------------- | ---------------------------------------------------------------------------------------------- |
| **Type**                  | `object`                                                                                       |
| **Additional properties** | [Each additional property must conform to the schema](#dependentRequired_additionalProperties) |

| Property                                      | Type            |
| --------------------------------------------- | --------------- |
| - [](#dependentRequired_additionalProperties) | array of string |

### <a name="dependentRequired_additionalProperties"></a>`additionalProperties`

|             |                   |
| ----------- | ----------------- |
| **Type**    | `array of string` |
| **Default** | `[]`              |

| Each item of this array must be                                             | Description |
| --------------------------------------------------------------------------- | ----------- |
| [additionalProperties items](#dependentRequired_additionalProperties_items) | -           |

#### <a name="dependentRequired_additionalProperties_items"></a>additionalProperties items

|          |          |
| -------- | -------- |
| **Type** | `string` |

## <a name="allOf"></a>`allOf`

**Title:** Combine definition groups

|                                 |                   |
| ------------------------------- | ----------------- |
| **Type**                        | `array of object` |
| Each item of this array must be | Description       |
| ------------------------------- | -----------       |
| [allOf items](#allOf_items)     | -                 |

### <a name="allOf_items"></a>allOf items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Additional properties** | Any type allowed |

| Property                   | Type   |
| -------------------------- | ------ |
| + [$ref](#allOf_items_ref) | string |

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
