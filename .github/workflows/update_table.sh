#!/bin/bash
# Get the current directory
CURRENT_DIR=$(pwd)
# Get today's date
TODAY=$(date +"%Y-%m-%d")

#Get the arguement to run on a specific feature
COMMITS_TODAY=$(git log --since="1 day" --pretty=format:"%H" -- $MAIN_DIRECTORY | while read -r COMMIT_HASH; do echo -n "Commit Hash: $COMMIT_HASH, Modified Top-level Folder: "; MODIFIED_FOLDER=$(git diff-tree --no-commit-id --name-only -r "$COMMIT_HASH" | awk -F/ '{print $1}'); echo "$MODIFIED_FOLDER"; done | uniq | grep -i $1 | wc -l)

# Get details of the last commit
LAST_COMMIT_HASH=$(git log --format="%H" -n 1)
LAST_COMMIT_MESSAGE=$(git log --format="%s" -n 1)

# Debugging
echo "Current Directory: $CURRENT_DIR"
echo "Today's Date: $TODAY"
echo "Last Commit Message: ${LAST_COMMIT_HASH:0:7} $LAST_COMMIT_MESSAGE"
echo "Total Commits: $COMMITS_TODAY"

#Actual work
awk -v today="$TODAY" -v commits="$COMMITS_TODAY" -v hash="${LAST_COMMIT_HASH:0:7}" -v message="$LAST_COMMIT_MESSAGE" '
BEGIN {
  FS = "\\s*\\|\\s*";
  OFS = " | ";
  found = 0;
}

# Function to print a line based on its date
function printLine(date) {
  if (date == today) {
    $4 = commits;
    $5 = hash " - " message;
    found = 1;
    if (substr(dates[date], 1, 2) != "| ") {
      dates[date] = "| " dates[date];
    }
    if (substr(dates[date], length(dates[date])-1) != " |") {
      dates[date] = dates[date] " |";
    }
  }
  print dates[date];
}

# Process header line
NR == 1 {
  print $0;
  next;
}

{
  dates[$2] = $0;
}

END {
  if (!found) {
    dates[today] = today OFS commits OFS hash " - " message;
  }

  # Print the headers first
  if (dates["Date"] !~ /\| Date/ && dates["Date"] !~ /\| ---/) {
    if (substr(dates["Date"], 1, 2) != "| ") {
      dates["Date"] = "| " dates["Date"];
    }
    if (substr(dates["Date"], length(dates["Date"])-1) != " |") {
      dates["Date"] = dates["Date"] " |";
    }
  }
  
  

  # Print the dates in ascending order, skipping the header line
  asorti(dates, sorted_dates);
  for (i = 1; i <= length(sorted_dates); i++) {
    if (sorted_dates[i] != "Date") {
      printLine(sorted_dates[i]);
    }
  }
}' "$CURRENT_DIR/daily_commit_tracker.md" > tmpfile && mv tmpfile "$CURRENT_DIR/daily_commit_tracker.md"


