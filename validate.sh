#!/bin/bash

shopt -s nullglob

for folder in lineage/v1beta1 module/v1 pipeline/v1 plugin/v1 task-hash/v1 ; do
  schema="$folder/schema.json"

  echo "Validating $schema ..."
  check-jsonschema --schemafile https://json-schema.org/draft/2020-12/schema "$schema"

  echo -e "\nValidating test cases..."
  failed=0
  for spec in $folder/tests/*.json $folder/tests/*.yml ; do
    echo "Testing $spec:"

    if check-jsonschema --schemafile "$schema" "$spec"; then
      # If $spec doesn't start with "invalid*" then it is a success
      if [[ $(basename "$spec") != invalid* ]]; then
        echo "✓ Valid"
      else
        failed=1
      fi
    else
      if [[ $(basename "$spec") == invalid* ]]; then
        echo "✓ Invalid"
      else
        failed=1
      fi
    fi
    echo
  done
done

# the published task hash specs are data, not test cases, but must still match the schema
echo "Validating published task hash specs..."
for spec in task-hash/v1/specs/*.json ; do
  echo "Testing $spec:"
  check-jsonschema --schemafile task-hash/v1/schema.json "$spec" || failed=1
  echo
done

exit $failed
