#!/bin/bash
# Get the current directory
# CURRENT_DIR=$(dirname "$(readlink -f "$0")")
CURRENT_DIR=$(pwd)
# Get today's date
TODAY=$(date +"%Y-%m-%d")

#Get the arguement to run on a specific feature
SEARCH_KEY=$1
echo $SEARCH_KEY
COMMITS_TODAY=$(git log --since="yesterday" --pretty=format:"%H" | while read -r COMMIT_HASH; do echo -n "Commit Hash: $COMMIT_HASH, Modified Top-level Folder: "; MODIFIED_FOLDER=$(git diff-tree --no-commit-id --name-only -r "$COMMIT_HASH" | awk -F/ '{print $1}'); echo "$MODIFIED_FOLDER"; done | uniq | grep -i $SEARCH_KEY | wc -l)


# Get details of the last commit
LAST_COMMIT_HASH=$(git log --format="%H" -n 1)
LAST_COMMIT_MESSAGE=$(git log --format="%s" -n 1)

# Debugging
echo "Current Directory: $CURRENT_DIR"
echo "Today's Date: $TODAY"
echo "Last Commit Message: ${LAST_COMMIT_HASH:0:7} $LAST_COMMIT_MESSAGE"
echo "Total Commits: $COMMITS_TODAY"

#Actual work
sed -i -E "s/\| ([0-9]{4}-[0-9]{2}-[0-9]{2}) \| ([0-9]+) \| [a-f0-9]{7} - (.*)/| $TODAY | $COMMITS_TODAY | ${LAST_COMMIT_HASH:0:7} - $LAST_COMMIT_MESSAGE |/" "$CURRENT_DIR/README.md" 


