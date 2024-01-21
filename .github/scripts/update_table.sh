#!/bin/bash

# Get the current directory (assuming the script is in .github/scripts)
CURRENT_DIR=$(dirname "$(readlink -f "$0")")

# Get today's date
TODAY=$(date +"%Y-%m-%d")

# Get the current number of commits for today
COMMITS_TODAY=$(git log --since="today" --format="%H" | wc -l)

# Get details of the last commit
LAST_COMMIT_HASH=$(git log --format="%H" -n 1)
LAST_COMMIT_MESSAGE=$(git log --format="%s" -n 1)
sed -i -E "s/\| ([0-9]{4}-[0-9]{2}-[0-9]{2}) \| ([0-9]+) \| [a-f0-9]{7} - (.*)/| $TODAY | $COMMITS_TODAY | ${LAST_COMMIT_HASH:0:7} - $LAST_COMMIT_MESSAGE |/" "README.md" 


