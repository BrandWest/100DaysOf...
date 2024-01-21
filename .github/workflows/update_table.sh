#!/bin/bash
# Get the current directory
# CURRENT_DIR=$(dirname "$(readlink -f "$0")")
CURRENT_DIR=$(pwd)
# Get today's date
TODAY=$(date +"%Y-%m-%d")

# Get the current number of commits for today
COMMITS_TODAY=$(git log --since="today" --format="%H" | wc -l)

# Get details of the last commit
LAST_COMMIT_HASH=$(git log --format="%H" -n 1)
LAST_COMMIT_MESSAGE=$(git log --format="%s" -n 1)

# Debugging
echo "Current Directory: $CURRENT_DIR"
echo "Today's Date: $TODAY"
echo "Last Commit Message: ${LAST_COMMIT_HASH:0:7} $LAST_COMMIT_MESSAGE"

#Actual work
sed -i -E "s/\| ([0-9]{4}-[0-9]{2}-[0-9]{2}) \| ([0-9]+) \| [a-f0-9]{7} - (.*)/| $TODAY | $COMMITS_TODAY | ${LAST_COMMIT_HASH:0:7} - $LAST_COMMIT_MESSAGE |/" "$CURRENT_DIR/README.md" 


