# Contributing Guidelines

Thank you for your interest in contributing to Nextflow Schemas! This guide will help you get started.

## Getting Started

### Prerequisites

- Git
- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager
- Docker (optional, for containerized validation)

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR-USERNAME/schemas.git
cd schemas
```

3. Add the upstream repository:

```bash
git remote add upstream https://github.com/nextflow-io/schemas.git
```

### Install Dependencies

```bash
# Install all dependencies including dev tools
uv sync

# Install pre-commit hooks
uv pip install pre-commit
pre-commit install
```

## Development Workflow

### 1. Create a Branch

Create a feature branch for your changes:

```bash
git checkout -b feature/my-new-feature
```

Use descriptive branch names:

- `feature/add-new-format` - New features
- `fix/validation-error` - Bug fixes
- `docs/update-examples` - Documentation updates

### 2. Make Changes

#### Modifying Schemas

When modifying `pipeline-input/schema.json` or `plugin/schema.json`:

1. Update the schema file
2. Add test cases (both valid and invalid)
3. Run validation to ensure correctness
4. Update documentation if needed

#### Adding Test Cases

Add test files to the appropriate `tests/` directory:

**Valid test cases** (should pass validation):

```bash
# Name files with valid_ prefix
touch pipeline-input/tests/valid_my_test.json
```

**Invalid test cases** (should fail validation):

```bash
# Name files with invalid_ prefix
touch pipeline-input/tests/invalid_my_test.json
```

The validation script automatically checks:

- Files starting with `valid_` must pass validation
- Files starting with `invalid_` must fail validation

### 3. Format Code

Pre-commit hooks will automatically format JSON files with Prettier:

```bash
# Run manually on all files
pre-commit run --all-files

# Or commit to trigger hooks
git commit -m "Your commit message"
```

### 4. Validate Changes

Run the validation script:

```bash
./validate.sh
```

This validates:

- Schema files against JSON Schema Draft 2020-12
- All test cases against their respective schemas
- Test case naming conventions

Expected output:

```
Validating pipeline-input/schema.json ...
ok -- validation done, no errors

Validating test cases...
Testing pipeline-input/tests/valid_schema.json:
ok -- validation done, no errors
✓ Valid

Testing pipeline-input/tests/invalid_schema.json:
ValidationError: ...
✓ Invalid
```

### 5. Run Docker Validation (Optional)

Test in a clean environment:

```bash
./validate-docker.sh
```

### 6. Update Documentation

If your changes affect usage:

1. Update relevant documentation in `docs/`
2. Build docs locally to verify:

```bash
uv sync --extra docs
uv run mkdocs serve
```

3. Check the docs at `http://127.0.0.1:8000`

### 7. Commit Changes

Write clear, descriptive commit messages:

```bash
git add .
git commit -m "Add new format validation for date-time-local

- Add date-time-local to allowed formats
- Include test cases for valid and invalid inputs
- Update documentation with examples"
```

Good commit messages:

- Use the imperative mood ("Add feature" not "Added feature")
- Keep the first line under 50 characters
- Provide details in the body if needed
- Reference issues if applicable (#123)

### 8. Push and Create PR

```bash
git push origin feature/my-new-feature
```

Then create a Pull Request on GitHub.

## Pull Request Guidelines

### PR Description

Include in your PR description:

- **Purpose**: What does this PR do?
- **Changes**: What files/functionality changed?
- **Testing**: How did you test the changes?
- **Breaking Changes**: Any breaking changes?
- **Related Issues**: Link to related issues

### PR Checklist

Before submitting:

- [ ] Code follows existing style and conventions
- [ ] All tests pass (`./validate.sh`)
- [ ] New test cases added for changes
- [ ] Documentation updated if needed
- [ ] Commit messages are clear and descriptive
- [ ] Pre-commit hooks pass
- [ ] No merge conflicts with main branch

### Review Process

1. Automated CI checks will run on your PR
2. Maintainers will review your changes
3. Address any feedback or requested changes
4. Once approved, a maintainer will merge your PR

## Testing Guidelines

### Writing Good Tests

**Valid test cases** should:

- Cover common use cases
- Test edge cases within valid bounds
- Include all required properties
- Use realistic example data

**Invalid test cases** should:

- Test each validation rule
- Cover missing required properties
- Test invalid types
- Test constraint violations (min/max, pattern, etc.)

### Test Naming

Use descriptive names that indicate what is being tested:

```
valid_minimal_schema.json
valid_full_featured_schema.json
valid_with_parameter_groups.json
invalid_missing_required_type.json
invalid_wrong_format.json
invalid_exceeds_maximum.json
```

## Code Style

### JSON Formatting

- Use 2 spaces for indentation
- Use double quotes for strings
- Include trailing commas where allowed
- Keep arrays/objects readable

Prettier will enforce these automatically.

### Schema Conventions

- Use descriptive property names
- Provide clear descriptions for all properties
- Include examples where helpful
- Document custom keywords

## Reporting Issues

### Bug Reports

Include:

- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Schema/test file that demonstrates the issue
- Environment details (OS, Python version, etc.)

### Feature Requests

Include:

- Clear description of the feature
- Use cases and benefits
- Examples of how it would work
- Any alternative solutions considered

## Getting Help

- **GitHub Issues**: Ask questions or report problems
- **Discussions**: Discuss ideas or get feedback
- **Nextflow Community**: Join the broader community

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## Recognition

Contributors will be recognized in the project's release notes and GitHub contributors page.

Thank you for contributing to Nextflow Schemas! 🎉
