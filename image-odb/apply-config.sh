#!/bin/bash
echo -e "Applying config ..."

# Print current user
user=$(whoami)
echo -e "Current user: $user"

# Remove all databases
rm -rf `find /orientdb/databases/ -type d ! -name "OSystem" ! -name "databases"`

for app in $(<"/apps.cnf"); do
  app=$(echo $app | tr -d '\r' | tr -d '\n')
  echo -e "Copying $app …"
  dir="/apps/$app/databases"
  if [ -d $dir ]; then
    # Copy databases
    mkdir "/home/jovyan/$app"
    find $dir -type d ! -name "databases" -exec cp -pr {} "/orientdb/databases/" \;
  else
    echo -e "Error importing $dir. App does not exist."
  fi
done

echo -e "Finished."