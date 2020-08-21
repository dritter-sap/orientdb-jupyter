#!/bin/bash
echo -e "Applying config …"

# Print current user
user=$(whoami)
echo -e "Current user: $user"

# Print python version
echo -e $(python --version)

# Remove work dir
if [ -d "/home/jovyan/work" ]; then rmdir "/home/jovyan/work"; fi

# Remove all notebooks
rm -rf `find /home/jovyan/ -type d ! -name "jovyan" ! -wholename "*/.*"`

for app in $(<"/apps.cnf"); do
  app=$(echo $app | tr -d '\r' | tr -d '\n')
  echo -e "Copying $app …"
  dir="/apps/$app/notebooks"
  if [ -d $dir ]; then
    # Copy notebooks
    mkdir "/home/jovyan/$app"
    find $dir -type f -exec cp -p {} "/home/jovyan/$app/" \;
    # Install dependencies
    /run/install-dependencies.sh "/apps/$app/libs.cnf"
  else
    echo -e "Error importing $dir. App does not exist."
  fi
done

echo -e "Finished."