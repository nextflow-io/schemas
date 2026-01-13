#!/usr/bin/env python3
"""
Super simple schema documentation generator.
Uses json-schema-for-humans to generate markdown, then post-processes headings.
"""

import re
from pathlib import Path
from typing import Optional

from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration


def fix_headings(markdown: str) -> str:
    """
    Post-process markdown to fix headings:
    - Remove numbering from headings
    - Keep only leaf property names
    - Wrap property names in backticks
    """
    lines = []

    for line in markdown.split('\n'):
        # Fix headings: ## 1.2.3 Property `name` or ## 1. Property `name`
        heading_match = re.match(r'^(#{2,})\s+<a name="([^"]+)"></a>[\d.]+\.\s+(.*)$', line)
        if not heading_match:
            heading_match = re.match(r'^(#{2,})\s+[\d.]+\.\s+(.*)$', line)

        if heading_match:
            if len(heading_match.groups()) == 3:
                level, anchor, rest = heading_match.groups()
            else:
                level, rest = heading_match.groups()
                anchor = None


            # Extract property name
            # Patterns: "Property `name`" or just "`name`" or "name items"
            prop_match = re.search(r'Property\s+`([^`]+)`|`([^`]+)`', rest)
            if prop_match:
                prop_name = prop_match.group(1) or prop_match.group(2)
                # Just use the property name as-is (already a leaf in jsfh output)
                if anchor:
                    line = f"{level} <a name=\"{anchor}\"></a>`{prop_name}`"
                else:
                    line = f"{level} `{prop_name}`"
            else:
                # Handle "xxx items" headings - keep them as-is but remove numbering
                line = f"{level} {rest}"

        lines.append(line)

    return '\n'.join(lines)


def generate_docs(schema_path: Path, output_path: Optional[Path] = None) -> str:
    """
    Generate documentation for a JSON schema file.
    Uses json-schema-for-humans, then fixes the headings.
    """
    if not output_path:
        output_path = schema_path.with_suffix('.md')

    # Use json-schema-for-humans to generate markdown
    config = GenerationConfiguration(
        template_name="md",
        show_breadcrumbs=False,
        show_toc=False,
        collapse_long_descriptions=False,
        link_to_reused_ref=True,
        footer_show_time=False
    )

    # Generate to temp location
    temp_output = output_path.parent / f"temp_{output_path.name}"
    generate_from_filename(schema_path, str(temp_output), config=config)

    # Read and post-process
    markdown = temp_output.read_text()
    markdown = fix_headings(markdown)

    # Write final output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown)

    # Clean up temp file
    temp_output.unlink()

    print(f"Documentation generated: {output_path}")
    return markdown


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate markdown documentation from JSON schemas"
    )
    parser.add_argument("schema", nargs="?", type=Path, help="Path to JSON schema file")
    parser.add_argument("-o", "--output", type=Path, help="Output markdown file")
    parser.add_argument("--all", action="store_true", help="Generate docs for all schemas")
    parser.add_argument("--output-dir", type=Path, help="Output directory (default: docs/schemas/)")

    args = parser.parse_args()

    if args.all:
        repo_root = Path(__file__).parent
        schema_files = [
            f for f in repo_root.glob("**/schema.json")
            if not any(p.startswith('.') for p in f.parts)
        ]

        print(f"Found {len(schema_files)} schema files")
        output_dir = args.output_dir or (repo_root / "docs" / "schemas")

        for schema_file in schema_files:
            schema_dir = schema_file.parent.relative_to(repo_root)
            schema_name = schema_file.stem if str(schema_dir) == "." else str(schema_dir).replace("/", "-")
            generate_docs(schema_file, output_dir / f"{schema_name}.md")
    else:
        if not args.schema:
            parser.error("schema argument is required when not using --all")
        generate_docs(args.schema, args.output or args.schema.with_suffix(".md"))


if __name__ == "__main__":
    main()
