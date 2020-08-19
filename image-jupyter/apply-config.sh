#!/bin/bash

echo -e "Applying config …"

# Print current user
user=$(whoami)
echo -e "Current user: $user"

# Remove work dir
if [ -d "/home/jovyan/work" ]; then rmdir "/home/jovyan/work"; fi

while read -r line; do
  # Copy notebooks
  line=$(echo $line | tr -d '\r' | tr -d '\n')
  echo -e "Copying $line …"
  dir="/apps/$line/notebooks"
  if [ -d $dir ]; then
    mkdir "/home/jovyan/$line"
    find $dir -type f -exec cp -p {} "/home/jovyan/$line/" \;
  else
    echo -e "Error importing $dir. Directory does not exist."
  fi
done < "/apps.cnf"

echo -e "Finished."