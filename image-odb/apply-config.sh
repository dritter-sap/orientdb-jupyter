#!/bin/bash

echo "Applying config ..."

# Print current user
user=$(whoami)
echo -e "Current user: $user"

while read -r line; do
  # Copy databases
  line=$(echo $line | tr -d '\r' | tr -d '\n')
  echo -e "Copying $line …"
  dir="/apps/$line/databases"
  if [ -d $dir ]; then
    mkdir "/home/jovyan/$line"
    find $dir -type d -exec cp -pr {} "/orientdb/databases/" \;
  else
    echo -e "Error importing $dir. Directory does not exist."
  fi
done < "/apps.cnf"

echo "Finished."