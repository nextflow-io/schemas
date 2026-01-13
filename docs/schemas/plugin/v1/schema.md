# Nextflow plugin schema

**Title:** Nextflow plugin schema

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Schema for Nextflow plugin specs

| Property                      | Pattern | Type  | Deprecated | Definition | Title/Description |
| ----------------------------- | ------- | ----- | ---------- | ---------- | ----------------- |
| - [definitions](#definitions) | No      | array | No         | -          | -                 |

## <a name="definitions"></a>`definitions`

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

| Each item of this array must be         | Description |
| --------------------------------------- | ----------- |
| [definitions items](#definitions_items) | -           |

### definitions items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                              |
| ------------------------------------------- |
| [config_scope](#definitions_items_anyOf_i0) |
| [function](#definitions_items_anyOf_i1)     |

#### <a name="definitions_items_anyOf_i0"></a>`config_scope`

|                           |                      |
| ------------------------- | -------------------- |
| **Type**                  | `object`             |
| **Required**              | No                   |
| **Additional properties** | Any type allowed     |
| **Defined in**            | #/$defs/config_scope |

| Property                                   | Pattern | Type             | Deprecated | Definition | Title/Description |
| ------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [type](#definitions_items_anyOf_i0_type) | No      | enum (of string) | No         | -          | -                 |
| - [spec](#definitions_items_anyOf_i0_spec) | No      | object           | No         | -          | -                 |

##### <a name="definitions_items_anyOf_i0_type"></a>`type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:

- "ConfigScope"

##### <a name="definitions_items_anyOf_i0_spec"></a>`spec`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                      | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [name](#definitions_items_anyOf_i0_spec_name)               | No      | string | No         | -          | -                 |
| - [description](#definitions_items_anyOf_i0_spec_description) | No      | string | No         | -          | -                 |
| - [children](#definitions_items_anyOf_i0_spec_children)       | No      | array  | No         | -          | -                 |

###### <a name="definitions_items_anyOf_i0_spec_name"></a>`name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="definitions_items_anyOf_i0_spec_description"></a>`description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="definitions_items_anyOf_i0_spec_children"></a>`children`

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

| Each item of this array must be                                   | Description |
| ----------------------------------------------------------------- | ----------- |
| [children items](#definitions_items_anyOf_i0_spec_children_items) | -           |

###### children items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `combining`      |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Any of(Option)                                                            |
| ------------------------------------------------------------------------- |
| [config_scope](#definitions_items_anyOf_i0_spec_children_items_anyOf_i0)  |
| [config_option](#definitions_items_anyOf_i0_spec_children_items_anyOf_i1) |

###### <a name="definitions_items_anyOf_i0_spec_children_items_anyOf_i0"></a>`config_scope`

|                           |                                                           |
| ------------------------- | --------------------------------------------------------- |
| **Type**                  | `object`                                                  |
| **Required**              | No                                                        |
| **Additional properties** | Any type allowed                                          |
| **Same definition as**    | [definitions_items_anyOf_i0](#definitions_items_anyOf_i0) |

###### <a name="definitions_items_anyOf_i0_spec_children_items_anyOf_i1"></a>`config_option`

|                           |                       |
| ------------------------- | --------------------- |
| **Type**                  | `object`              |
| **Required**              | No                    |
| **Additional properties** | Any type allowed      |
| **Defined in**            | #/$defs/config_option |

| Property                                                                | Pattern | Type             | Deprecated | Definition | Title/Description |
| ----------------------------------------------------------------------- | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [type](#definitions_items_anyOf_i0_spec_children_items_anyOf_i1_type) | No      | enum (of string) | No         | -          | -                 |
| - [spec](#definitions_items_anyOf_i0_spec_children_items_anyOf_i1_spec) | No      | object           | No         | -          | -                 |

###### <a name="definitions_items_anyOf_i0_spec_children_items_anyOf_i1_type"></a>`type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:

- "ConfigOption"

###### <a name="definitions_items_anyOf_i0_spec_children_items_anyOf_i1_spec"></a>`spec`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                                                   | Pattern | Type   | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------------------------------------ | ------- | ------ | ---------- | ---------- | ----------------- |
| - [name](#definitions_items_anyOf_i0_spec_children_items_anyOf_i1_spec_name)               | No      | string | No         | -          | -                 |
| - [description](#definitions_items_anyOf_i0_spec_children_items_anyOf_i1_spec_description) | No      | string | No         | -          | -                 |
| - [type](#definitions_items_anyOf_i0_spec_children_items_anyOf_i1_spec_type)               | No      | string | No         | -          | -                 |

###### <a name="definitions_items_anyOf_i0_spec_children_items_anyOf_i1_spec_name"></a>`name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="definitions_items_anyOf_i0_spec_children_items_anyOf_i1_spec_description"></a>`description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="definitions_items_anyOf_i0_spec_children_items_anyOf_i1_spec_type"></a>`type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

#### <a name="definitions_items_anyOf_i1"></a>`function`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |
| **Defined in**            | #/$defs/function |

| Property                                   | Pattern | Type             | Deprecated | Definition | Title/Description |
| ------------------------------------------ | ------- | ---------------- | ---------- | ---------- | ----------------- |
| - [type](#definitions_items_anyOf_i1_type) | No      | enum (of string) | No         | -          | -                 |
| - [spec](#definitions_items_anyOf_i1_spec) | No      | object           | No         | -          | -                 |

##### <a name="definitions_items_anyOf_i1_type"></a>`type`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

Must be one of:

- "Factory"
- "Function"
- "Operator"

##### <a name="definitions_items_anyOf_i1_spec"></a>`spec`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                      | Pattern | Type            | Deprecated | Definition | Title/Description |
| ------------------------------------------------------------- | ------- | --------------- | ---------- | ---------- | ----------------- |
| - [name](#definitions_items_anyOf_i1_spec_name)               | No      | string          | No         | -          | -                 |
| - [description](#definitions_items_anyOf_i1_spec_description) | No      | string          | No         | -          | -                 |
| - [returnType](#definitions_items_anyOf_i1_spec_returnType)   | No      | string          | No         | -          | -                 |
| - [parameters](#definitions_items_anyOf_i1_spec_parameters)   | No      | array of object | No         | -          | -                 |

###### <a name="definitions_items_anyOf_i1_spec_name"></a>`name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="definitions_items_anyOf_i1_spec_description"></a>`description`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="definitions_items_anyOf_i1_spec_returnType"></a>`returnType`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="definitions_items_anyOf_i1_spec_parameters"></a>`parameters`

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

| Each item of this array must be                                       | Description |
| --------------------------------------------------------------------- | ----------- |
| [parameters items](#definitions_items_anyOf_i1_spec_parameters_items) | -           |

###### parameters items

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

| Property                                                         | Pattern | Type   | Deprecated | Definition | Title/Description |
| ---------------------------------------------------------------- | ------- | ------ | ---------- | ---------- | ----------------- |
| - [name](#definitions_items_anyOf_i1_spec_parameters_items_name) | No      | string | No         | -          | -                 |
| - [type](#definitions_items_anyOf_i1_spec_parameters_items_type) | No      | string | No         | -          | -                 |

###### <a name="definitions_items_anyOf_i1_spec_parameters_items_name"></a>`name`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

###### <a name="definitions_items_anyOf_i1_spec_parameters_items_type"></a>`type`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

---

Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans)
