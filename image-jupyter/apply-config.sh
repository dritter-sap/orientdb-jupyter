#!/bin/bash

echo "Applying config ..."

# Remove work dir
if [ -d "~/work" ]; then rmdir "~/work"; fi

input="/apps.cnf"
while IFS= read -r line
do
  # Copy notebooks
  echo "Copying $line ..."
  CURRENT_DIR="/apps/$line/notebooks"
  if [ -d "$CURRENT_DIR" ]; then
    cp /apps/$line/notebooks ~
  else
    echo "Error importing $line. Directory does not exist."
  fi
done < "$input"

echo "Finished."