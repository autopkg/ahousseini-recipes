#!/bin/bash

all_recipes_clean="true"
force_lint="${1}"

for recipe_path in */*.recipe; do

  recipe="$(cat "${recipe_path}")"

  lint_test="$(echo "${recipe}" | plutil -lint -)"

  if ! echo "${lint_test}" | grep -q "OK"; then

    all_recipes_clean="false"
    echo "=> Syntax error: ${recipe_path}"
    echo "${lint_test}"

  else

    optimised_recipe="$(echo "${recipe}" | plutil -convert xml1 -o - -)"

    if ! diff <(echo "${optimised_recipe}") <(echo "${recipe}"); then

      all_recipes_clean="false"
      echo "=> Off-nominal formatting: ${recipe_path}"

      if [[ "${force_lint}" = "force_lint" ]]; then
        echo "=> Flag force_lint on, linting ${recipe_path}"
        plutil -convert xml1 "${recipe_path}"
      fi

    fi

  fi

done

if [ "${all_recipes_clean}" = "false" ]; then
  exit 1
fi
