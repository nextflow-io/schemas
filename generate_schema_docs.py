#!/usr/bin/env python3
"""
Generate markdown documentation from JSON schemas.
Similar to json-schema-for-humans output format.
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import quote


class SchemaDocGenerator:
    """Generate markdown documentation from JSON Schema."""

    # Characters to remove/replace in anchor IDs
    ANCHOR_CLEANUP = str.maketrans({
        " ": "_", ">": "", "$": "", "#": "", "/": "_",
        "[": "", "]": "", "(": "", ")": "", "{": "",
        "}": "", "^": "", "*": ""
    })

    def __init__(self, schema: Dict[str, Any]):
        self.schema = schema
        self.defs = schema.get("$defs", {})

    def generate_id(self, *parts: str) -> str:
        """Generate a unique ID for anchors."""
        id_str = "_".join(str(p) for p in parts if p)
        id_str = id_str.translate(self.ANCHOR_CLEANUP)
        id_str = re.sub(r'_+', '_', id_str)
        return id_str.strip("_")

    def type_str(self, prop: Dict[str, Any]) -> str:
        """Get human-readable type string."""
        if "const" in prop:
            return "const"
        if "enum" in prop:
            return "enum (of string)"

        type_val = prop.get("type")
        if isinstance(type_val, list):
            return " or ".join(sorted(type_val))

        if type_val:
            if type_val == "array" and "items" in prop:
                items_type = prop["items"].get("type")
                if items_type:
                    return f"array of {items_type}s"
            return type_val

        # Check for combining keywords
        if any(key in prop for key in ("anyOf", "allOf", "oneOf")):
            return "combining"

        return "object"

    @staticmethod
    def format_table_cell(text: str) -> str:
        """Format text for use in markdown table cells."""
        return str(text).replace("|", "\\|").replace("\n", " ")

    def generate_property_table(
        self, properties: Dict[str, Any], required: List[str], path: str = ""
    ) -> str:
        """Generate a table of properties."""
        if not properties:
            return ""

        rows = [
            "| Property | Type | Deprecated | Definition | Title/Description |",
            "| " + " | ".join(["-" * 10] * 5) + " |"
        ]

        for prop_name, prop_def in properties.items():
            prefix = "+ " if prop_name in required else "- "
            prop_type = self.type_str(prop_def)

            # Only show deprecated if it's actually deprecated
            deprecated = "Yes" if prop_def.get("deprecated") else ""

            # Check for $ref
            definition = f"In {prop_def['$ref']}" if "$ref" in prop_def and prop_def["$ref"].startswith("#/") else ""

            title_desc = prop_def.get("title") or prop_def.get("description") or "-"
            anchor_id = self.generate_id(path, prop_name)
            display_name = prop_name.replace("$", "\\$")
            prop_link = f"[{display_name}](#{anchor_id})"

            rows.append(f"| {prefix}{prop_link} | {prop_type} | {deprecated} | {definition} | {self.format_table_cell(title_desc)} |")

        return "\n".join(rows) + "\n"

    def generate_restrictions_table(self, prop: Dict[str, Any]) -> str:
        """Generate restrictions table for a property."""
        restrictions = []

        # String constraints
        if "minLength" in prop:
            restrictions.append(("**Min length**", str(prop["minLength"])))
        if "maxLength" in prop:
            restrictions.append(("**Max length**", str(prop["maxLength"])))
        if "pattern" in prop:
            pattern = prop["pattern"]
            regex_url = f"https://regex101.com/?regex={quote(pattern)}"
            restrictions.append(("**Must match regular expression**", f"```{pattern}``` [Test]({regex_url})"))

        # Number constraints
        if "minimum" in prop:
            restrictions.append(("**Minimum**", f"&ge; {prop['minimum']}"))
        if "exclusiveMinimum" in prop:
            restrictions.append(("**Minimum**", f"&gt; {prop['exclusiveMinimum']}"))
        if "maximum" in prop:
            restrictions.append(("**Maximum**", f"&le; {prop['maximum']}"))
        if "exclusiveMaximum" in prop:
            restrictions.append(("**Maximum**", f"&lt; {prop['exclusiveMaximum']}"))
        if "multipleOf" in prop:
            restrictions.append(("**Multiple of**", str(prop["multipleOf"])))
        if "format" in prop:
            restrictions.append(("**Format**", f"`{prop['format']}`"))

        if not restrictions:
            return ""

        rows = ["| Restrictions | |", "| " + " | ".join(["-" * 10] * 2) + " |"]
        rows.extend(f"| {key} | {value} |" for key, value in restrictions)
        return "\n".join(rows) + "\n"

    def generate_array_restrictions(self, prop: Dict[str, Any]) -> str:
        """Generate array restrictions table."""
        if prop.get("type") != "array":
            return ""

        restrictions = []

        # Only show meaningful values
        if "minItems" in prop:
            restrictions.append(("**Min items**", str(prop["minItems"])))
        if "maxItems" in prop:
            restrictions.append(("**Max items**", str(prop["maxItems"])))
        if prop.get("uniqueItems"):
            restrictions.append(("**Items unicity**", "True"))
        if "items" in prop:
            restrictions.append(("**Tuple validation**", "See below"))

        if not restrictions:
            return ""

        rows = ["| | Array restrictions |", "| " + " | ".join(["-" * 10] * 2) + " |"]
        rows.extend(f"| {key} | {value} |" for key, value in restrictions)
        return "\n".join(rows) + "\n"

    def generate_enum_values(self, prop: Dict[str, Any]) -> str:
        """Generate enum values list."""
        if "enum" not in prop:
            return ""

        values = "\n".join(f"* `{v}`" if isinstance(v, str) else f"* {v}" for v in prop["enum"])
        return f"\nMust be one of:\n{values}\n"

    def generate_const_value(self, prop: Dict[str, Any]) -> str:
        """Generate const value."""
        if "const" not in prop:
            return ""

        const_val = prop["const"]
        if isinstance(const_val, str):
            return f'\nSpecific value: `"{const_val}"`\n'
        return f"\nSpecific value: `{const_val}`\n"

    def generate_examples(self, prop: Dict[str, Any]) -> str:
        """Generate examples section."""
        if "examples" not in prop:
            return ""

        examples = prop["examples"]
        if not examples:
            return ""

        result = "\n**Examples:**\n\n"
        for example in examples:
            if isinstance(example, str):
                result += f'```\n"{example}"\n```\n\n'
            else:
                result += f"```\n{json.dumps(example, indent=2)}\n```\n\n"

        return result

    def generate_property_details(
        self, prop_name: str, prop: Dict[str, Any], path: str, level: int, parent_required: Optional[List[str]] = None
    ) -> str:
        """Generate detailed documentation for a property."""
        full_path = f"{path} > {prop_name}" if path else prop_name

        anchor_id = self.generate_id(path, prop_name)
        # Only show the property name itself in code ticks
        title = f"{'#' * level} <a name=\"{anchor_id}\"></a>`{prop_name}`\n\n"

        details = ""

        # Title
        if "title" in prop:
            details += f"**Title:** {prop['title']}\n\n"

        # Basic info table
        prop_type = self.type_str(prop)

        # Use parent_required if provided, otherwise check schema root
        if parent_required is None:
            parent_required = self.schema.get("required", [])
        is_required = prop_name in parent_required

        basic_table = "|              |          |\n"
        basic_table += "| ------------ | -------- |\n"
        basic_table += f"| **Type**     | `{prop_type}` |\n"
        basic_table += f"| **Required** | {'Yes' if is_required else 'No'} |\n"

        # Add format if present
        if "format" in prop:
            basic_table = basic_table.rstrip() + f"\n| **Format**   | `{prop['format']}` |\n"

        # Add default if present
        if "default" in prop:
            default_val = json.dumps(prop["default"]) if not isinstance(prop["default"], str) else f'`{prop["default"]}`'
            basic_table = basic_table.rstrip() + f"\n| **Default**  | {default_val} |\n"

        details += basic_table + "\n"

        # Description
        if "description" in prop:
            details += f"**Description:** {prop['description']}\n\n"

        # Restrictions
        restrictions = self.generate_restrictions_table(prop)
        if restrictions:
            details += restrictions + "\n"

        # Array restrictions
        array_restrictions = self.generate_array_restrictions(prop)
        if array_restrictions:
            details += array_restrictions + "\n"

        # Enum values
        details += self.generate_enum_values(prop)

        # Const value
        details += self.generate_const_value(prop)

        # Examples
        details += self.generate_examples(prop)

        # Handle nested properties
        if "properties" in prop:
            nested_props = prop["properties"]
            nested_required = prop.get("required", [])
            details += "\n**Properties:**\n\n"
            details += self.generate_property_table(nested_props, nested_required, full_path)
            details += "\n"

            # Generate details for each nested property
            for nested_name, nested_prop in nested_props.items():
                details += self.generate_property_details(
                    nested_name, nested_prop, full_path, level + 1, nested_required
                )

        # Handle pattern properties
        if "patternProperties" in prop:
            details += "\n**Pattern Properties:**\n\n"
            for pattern, pattern_def in prop["patternProperties"].items():
                pattern_required = pattern_def.get("required", [])
                details += f"Properties matching pattern `{pattern}` must conform to:\n\n"
                details += self.generate_property_details(
                    f"pattern: {pattern}", pattern_def, full_path, level + 1, pattern_required
                )

        # Handle combining schemas (allOf, anyOf, oneOf)
        for keyword, label in [("allOf", "All of (Requirements)"), ("anyOf", "Any of (Options)"), ("oneOf", "One of (Options)")]:
            if keyword in prop:
                details += f"\n**{label}:**\n\n"
                for i, subschema in enumerate(prop[keyword]):
                    item_label = subschema.get("$ref", f"Item {i}")
                    details += f"- {item_label}\n"
                details += "\n"

        # Handle array items
        if prop.get("type") == "array" and "items" in prop:
            items = prop["items"]
            details += "\n**Array Items:**\n\n"
            if "$ref" in items:
                details += f"Each item must conform to: {items['$ref']}\n\n"
            else:
                items_type = self.type_str(items)
                details += f"Each item must be of type: `{items_type}`\n\n"

        return title + details

    def generate_header(self) -> str:
        """Generate document header."""
        title = self.schema.get("title", "Schema Documentation")
        description = self.schema.get("description", "")
        schema_type = self.schema.get("type", "object")

        header = f"# {title}\n\n"
        header += f"**Title:** {title}\n\n"

        # Basic schema info table
        header += "|                           |                  |\n"
        header += "| ------------------------- | ---------------- |\n"
        header += f"| **Type**                  | `{schema_type}`         |\n"
        header += "| **Required**              | No               |\n"
        header += "| **Additional properties** | Any type allowed |\n\n"

        if description:
            header += f"**Description:** {description}\n\n"

        # Schema metadata
        if "$schema" in self.schema:
            header += f"**Schema:** {self.schema['$schema']}\n\n"
        if "$id" in self.schema:
            header += f"**ID:** {self.schema['$id']}\n\n"

        return header

    def generate_properties_section(self) -> str:
        """Generate main properties section."""
        properties = self.schema.get("properties", {})
        required = self.schema.get("required", [])

        if not properties:
            return ""

        section = self.generate_property_table(properties, required, self.schema.get("title", ""))
        section += "\n"

        return section

    def generate_all_property_details(self) -> str:
        """Generate detailed sections for all properties."""
        properties = self.schema.get("properties", {})
        if not properties:
            return ""

        details = ""
        required = self.schema.get("required", [])
        for prop_name, prop_def in properties.items():
            schema_title = self.schema.get("title", "")
            details += self.generate_property_details(prop_name, prop_def, schema_title, 2, required)
            details += "\n"

        return details

    def generate_definitions_section(self) -> str:
        """Generate definitions section."""
        if not self.defs:
            return ""

        section = "## Definitions\n\n"
        section += "The following definitions are used throughout the schema:\n\n"

        for def_name, def_schema in self.defs.items():
            section += f"### {def_name}\n\n"

            if "description" in def_schema:
                section += f"**Description:** {def_schema['description']}\n\n"

            def_type = self.type_str(def_schema)
            section += f"**Type:** `{def_type}`\n\n"

            if "properties" in def_schema:
                required = def_schema.get("required", [])
                section += self.generate_property_table(
                    def_schema["properties"], required, f"$defs/{def_name}"
                )
                section += "\n"

        return section

    def generate(self) -> str:
        """Generate complete documentation."""
        doc = self.generate_header()
        doc += self.generate_properties_section()
        doc += self.generate_all_property_details()
        doc += self.generate_definitions_section()

        # Add footer
        doc += "\n---\n\n"
        doc += "Generated using a custom JSON Schema documentation generator.\n"

        return doc


def generate_docs(schema_path: Path, output_path: Optional[Path] = None) -> str:
    """
    Generate documentation for a JSON schema file.

    Args:
        schema_path: Path to the JSON schema file
        output_path: Optional path to write the output markdown file

    Returns:
        Generated markdown documentation
    """
    with open(schema_path) as f:
        schema = json.load(f)

    generator = SchemaDocGenerator(schema)
    markdown = generator.generate()

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown)
        print(f"Documentation generated: {output_path}")

    return markdown


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate markdown documentation from JSON schemas"
    )
    parser.add_argument("schema", nargs="?", type=Path, help="Path to JSON schema file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output markdown file (default: same name as schema with .md extension)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generate docs for all schemas in the repository",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for generated docs (default: docs/schemas/)",
    )

    args = parser.parse_args()

    if args.all:
        # Find all schema.json files
        repo_root = Path(__file__).parent
        schema_files = [f for f in repo_root.glob("**/schema.json")
                       if not any(p.startswith('.') for p in f.parts)]

        print(f"Found {len(schema_files)} schema files")

        output_dir = args.output_dir or (repo_root / "docs" / "schemas")

        for schema_file in schema_files:
            # Get the directory path relative to repo root
            schema_dir = schema_file.parent.relative_to(repo_root)

            # Use parent directory name as file name (e.g., pipeline-input, plugin/v1 -> plugin-v1)
            schema_name = schema_file.stem if str(schema_dir) == "." else str(schema_dir).replace("/", "-")

            output_file = output_dir / f"{schema_name}.md"
            generate_docs(schema_file, output_file)
    else:
        if not args.schema:
            parser.error("schema argument is required when not using --all")

        output_path = args.output
        if not output_path:
            output_path = args.schema.with_suffix(".md")

        generate_docs(args.schema, output_path)


if __name__ == "__main__":
    main()
