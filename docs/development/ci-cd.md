# CI/CD

This document describes the continuous integration and deployment setup for the Nextflow Schemas repository.

## Overview

The repository uses GitHub Actions to automatically validate schemas and test cases on every push and pull request.

## Workflows

### Schema Validation Workflow

**File**: `.github/workflows/test.yml`

**Triggers**:

- Push to any branch that modifies:
  - `*.json` files
  - `validate.sh` script
  - The workflow file itself
- Pull requests with the same file changes

**Jobs**:

#### Test Job

**Runs on**: `ubuntu-latest`

**Steps**:

1. **Checkout code**

   ```yaml
   - uses: actions/checkout@v4
   ```

2. **Set up Python**

   ```yaml
   - uses: actions/setup-python@v5
     with:
       python-version: "3.x"
   ```

3. **Install dependencies**

   ```bash
   pip install check-jsonschema
   ```

4. **Run validation**
   ```bash
   ./validate.sh
   ```

### Expected Behavior

#### ✅ Success Criteria

The workflow passes when:

- All schema files are valid JSON Schema Draft 2020-12
- All `valid_*.json` test files pass validation
- All `invalid_*.json` test files fail validation
- No syntax errors in scripts

#### ❌ Failure Scenarios

The workflow fails if:

- Schema files contain errors
- Test files don't match naming expectations
- Script execution errors occur
- `valid_*` files fail validation
- `invalid_*` files pass validation

## Validation Script

### Script Overview

The `validate.sh` script:

1. Validates each schema against JSON Schema Draft 2020-12
2. Validates test cases against their respective schemas
3. Checks that test naming matches expectations
4. Returns exit code 0 on success, 1 on failure

### Script Logic

```bash
#!/bin/bash

for folder in pipeline-input plugin ; do
  # Validate schema itself
  check-jsonschema --schemafile https://json-schema.org/draft/2020-12/schema "$folder/schema.json"

  # Validate test cases
  for spec in $folder/tests/*.json ; do
    if check-jsonschema --schemafile "$folder/schema.json" "$spec"; then
      # Should start with "valid*"
      if [[ $(basename "$spec") != invalid* ]]; then
        echo "✓ Valid"
      else
        # Failed: invalid* file passed validation
        failed=1
      fi
    else
      # Should start with "invalid*"
      if [[ $(basename "$spec") == invalid* ]]; then
        echo "✓ Invalid"
      else
        # Failed: valid* file failed validation
        failed=1
      fi
    fi
  done
done

exit $failed
```

## Docker Validation

### Docker Script

**File**: `validate-docker.sh`

Provides containerized validation for consistent environments:

```bash
./validate-docker.sh
```

**Benefits**:

- No local dependencies required
- Consistent validation environment
- Easy to reproduce CI results locally

### Implementation

```bash
#!/bin/bash

docker run --rm -v "$(pwd):/workspace" -w /workspace python:3 bash -c "
  pip install check-jsonschema && ./validate.sh
"
```

## Status Checks

### Required Checks

Pull requests must pass:

- ✅ Schema validation
- ✅ Test case validation
- ✅ Naming convention checks

### Branch Protection

Recommended settings for `main` branch:

- Require status checks before merging
- Require `test` workflow to pass
- Require up-to-date branches

## Local Validation

### Before Pushing

Always validate locally:

```bash
# Standard validation
./validate.sh

# Docker validation (matches CI)
./validate-docker.sh
```

### Pre-commit Hooks

Install pre-commit hooks to catch issues early:

```bash
uv pip install pre-commit
pre-commit install
```

Hooks will:

- Format JSON with Prettier
- Validate syntax
- Check for common issues

## Debugging CI Failures

### View Logs

1. Go to the Actions tab in GitHub
2. Click on the failed workflow run
3. Expand the failed job
4. Review the validation output

### Reproduce Locally

Use Docker to match CI environment:

```bash
./validate-docker.sh
```

### Common Issues

#### Schema Validation Errors

**Problem**: Schema file doesn't conform to JSON Schema Draft 2020-12

**Solution**: Check schema syntax against the specification

```bash
check-jsonschema --schemafile https://json-schema.org/draft/2020-12/schema pipeline-input/schema.json
```

#### Test Case Failures

**Problem**: `valid_*` file fails or `invalid_*` file passes

**Solution**:

1. Verify the test case is correct
2. Check if naming matches content
3. Validate manually to see error details

```bash
check-jsonschema --schemafile pipeline-input/schema.json --verbose pipeline-input/tests/problematic_test.json
```

#### Permission Errors

**Problem**: Script not executable

**Solution**: Make scripts executable

```bash
chmod +x validate.sh validate-docker.sh
```

#### JSON Syntax Errors

**Problem**: Malformed JSON

**Solution**: Validate JSON syntax

```bash
python -m json.tool test.json
```

## Deployment

### Documentation Deployment

To deploy documentation (when set up):

```bash
# Build documentation
uv run mkdocs build

# Deploy to GitHub Pages
uv run mkdocs gh-deploy
```

### Release Process

1. Update version numbers if applicable
2. Tag the release:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```
3. Create GitHub release from tag
4. CI will automatically validate the release

## Performance Optimization

### Caching

GitHub Actions caches Python dependencies:

```yaml
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/pyproject.toml') }}
```

### Parallel Testing

Tests run in parallel when possible:

- Schema validation runs concurrently
- Test cases are validated in batch

## Monitoring

### Workflow Status Badge

Add to README.md:

```markdown
![CI](https://github.com/nextflow-io/schemas/workflows/test/badge.svg)
```

### Notifications

Configure notifications in GitHub settings:

- Email on workflow failures
- Slack/Discord webhooks (optional)

## Best Practices

1. **Run tests locally** before pushing
2. **Keep workflows simple** and focused
3. **Cache dependencies** to speed up CI
4. **Use Docker validation** to match CI environment
5. **Monitor workflow status** regularly
6. **Update dependencies** periodically

## Future Enhancements

Potential improvements:

- [ ] Add schema linting checks
- [ ] Performance benchmarking
- [ ] Automated release notes generation
- [ ] Coverage reporting
- [ ] Multi-version Python testing
- [ ] Automated documentation deployment

## See Also

- [Testing Guide](testing.md)
- [Contributing Guidelines](contributing.md)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
