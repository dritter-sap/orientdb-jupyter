#!/bin/bash
echo -e "Applying config ..."

# Print current user
user=$(whoami)
echo -e "Current user: $user"

# Remove all databases
rm -rf `find /orientdb/databases/ -type d ! -name "OSystem" ! -name "databases"`

for line in $(<"/apps.cnf"); do
  # Copy databases
  line=$(echo $line | tr -d '\r' | tr -d '\n')
  echo -e "Copying $line …"
  dir="/apps/$line/databases"
  if [ -d $dir ]; then
    mkdir "/home/jovyan/$line"
    find $dir -type d ! -name "databases" -exec cp -pr {} "/orientdb/databases/" \;
  else
    echo -e "Error importing $dir. Directory does not exist."
  fi
done

echo -e "Finished."