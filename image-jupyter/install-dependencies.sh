#!/bin/bash
echo -e "Installing dependencies …"

# Get app name from command line args
path=$1
echo -e "Installing dependencies from $path …"

for lib in $(<"$path"); do
  # Install dependency
  lib=$(echo $lib | tr -d '\r' | tr -d '\n')
  echo -e "Installing $lib …"
  pip3 install $lib
done

echo -e "Finished."