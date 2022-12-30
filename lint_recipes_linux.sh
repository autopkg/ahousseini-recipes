#!/bin/bash

all_recipes_clean="true"

for recipe_path in */*.recipe; do

  recipe="$(cat "${recipe_path}")"

  if ! echo "${recipe}" | xmllint --noout -; then

    all_recipes_clean="false"
    echo "=> Syntax error: ${recipe_path}"

  else

    optimised_recipe="$(echo "${recipe}" | plistutil -i - --format xml -o -)"

    if ! diff <(echo "${optimised_recipe}") <(echo "${recipe}"); then
      all_recipes_clean="false"
      echo "=> Off-nominal formatting: ${recipe_path}"
    fi

  fi

done

if [ "${all_recipes_clean}" = "false" ]; then
  exit 1
fi
