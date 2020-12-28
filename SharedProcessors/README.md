# Shared Processors

To use these processors, add the processor like this:

    com.github.ahousseini-recipes.SharedProcessors/SharedProcessor

# HomebrewCaskURL

## Description

An AutoPkg processor which reads the download url from the [Homebrew Cask API](https://formulae.brew.sh/docs/api/).

## Input Variables
- **cask\_name:**
	- **required:** True
    - **description:** Name of cask to fetch, as would be given to the `brew` command. Example: `brew install --cask firefox`.

## Output Variables
- **url:**
    - **description:** URL for the Cask's download.