#!/usr/bin/env python3
"""
Super simple schema documentation generator.
Uses json-schema-for-humans to generate markdown.
"""

import re
import subprocess
from pathlib import Path
from typing import Optional

from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration


def clean_headings(markdown: str) -> str:
    """
    Remove "Property " and "Pattern Property " prefixes from markdown headings.
    Converts: ###### <a name="..."></a>Property `name`
    To:       ###### <a name="..."></a>`name`
    """
    # Remove "Property " prefix from headings
    markdown = re.sub(
        r'(#{2,})\s+<a name="([^"]+)"></a>Property\s+(.*)$',
        r'\1 <a name="\2"></a>\3',
        markdown,
        flags=re.MULTILINE
    )

    # Remove "Pattern Property " prefix from headings
    markdown = re.sub(
        r'(#{2,})\s+<a name="([^"]+)"></a>Pattern Property\s+(.*)$',
        r'\1 <a name="\2"></a>\3',
        markdown,
        flags=re.MULTILINE
    )

    # Remove "Required | No" table rows
    markdown = re.sub(
        r'^\|\s*\*\*Required\*\*\s*\|\s*No\s*\|\s*$\n',
        '',
        markdown,
        flags=re.MULTILINE
    )

    return markdown


def generate_docs(schema_path: Path, output_path: Optional[Path] = None) -> str:
    """
    Generate documentation for a JSON schema file.
    Uses json-schema-for-humans with standard md template.
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
        footer_show_time=False,
        template_md_options={
            "show_array_restrictions": False,
            "properties_table_columns": ['Property','Type'],
            "show_heading_numbers": False,
        },
        expand_buttons=True
    )

    # Ensure output directory exists before generating
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Generate to temp location
    temp_output = output_path.parent / f"temp_{output_path.name}"
    generate_from_filename(schema_path, str(temp_output), config=config)

    # Read, clean up, and write final output
    markdown = temp_output.read_text()
    markdown = clean_headings(markdown)
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

    generated_files = []

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
            if str(schema_dir) == ".":
                output_file = output_dir / f"{schema_file.stem}.md"
            else:
                output_file = output_dir / schema_dir / f"{schema_file.stem}.md"
            generate_docs(schema_file, output_file)
            generated_files.append(output_file)
    else:
        if not args.schema:
            parser.error("schema argument is required when not using --all")
        output_file = args.output or args.schema.with_suffix(".md")
        generate_docs(args.schema, output_file)
        generated_files.append(output_file)

    # Run prek --files on all generated files
    if generated_files:
        print(f"\nRunning prek on {len(generated_files)} generated file(s)...")
        try:
            subprocess.run(
                ["prek", "--files"] + [str(f) for f in generated_files],
                capture_output=True
            )
        except FileNotFoundError:
            print("Warning: prek not found in PATH, skipping formatting")


if __name__ == "__main__":
    main()
