#!/bin/bash
echo -e "Applying config …"

# Print current user
user=$(whoami)
echo -e "Current user: $user"

# Remove work dir
if [ -d "/home/jovyan/work" ]; then rmdir "/home/jovyan/work"; fi

# Remove all notebooks
rm -rf `find /home/jovyan/ -type d ! -name "jovyan" ! -wholename "*/.*"`

for line in $(<"/apps.cnf"); do
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
done

echo -e "Finished."