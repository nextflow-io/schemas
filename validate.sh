#!/bin/bash

for folder in pipeline-input plugin ; do
  schema="$folder/schema.json"

  echo "Validating $schema ..."
  check-jsonschema --schemafile https://json-schema.org/draft/2020-12/schema "$schema"

  echo -e "\nValidating test cases..."
  failed=0
  for spec in $folder/tests/*.json ; do
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

exit $failed
