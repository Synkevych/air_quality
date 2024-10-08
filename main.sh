#!/bin/bash

# The path where the scripts will be executed
path="/path/to/air_quality"
pid_file="$path/main.pid"  # File to store the PID of the current process

# Check if the PID file already exists
if [ -f "$pid_file" ]; then
  echo "Script is already running (PID file exists: $pid_file)."
  exit 1
else
  echo $$ > "$pid_file"
fi

# Check if the default path is set
if [ "$path" == "/path/to/air_quality" ]; then
  echo "Please change the default path in file constants.py to the actual path."
  exit 1
fi

# Navigate to the specified directory
cd "$path" || { echo "Failed to navigate to $path"; exit 1;}

# Activate the virtual environment
if [ ! -f "myenv/bin/activate" ]; then
  echo "Virtual environment not found in $path/myenv trying to setup"
  python3 -m venv myenv
  if [ ! -f "myenv/bin/activate"]; then
    echo "Virtual environment could'nt be created, terminate the script"
    exit 1
  fi
fi

source myenv/bin/activate
if ! pip show cdsapi > /dev/null 2>&1; then
  echo "Installing cdsapi>=0.7.2..."
  pip install 'cdsapi>=0.7.2' setuptools
fi

# Run the Python scripts
#./remove_old_data_files.py
./single_level_data_manager.py
./multi_level_data_manager.py
./eu_data_manager.py

# Deactivate the virtual environment
deactivate

# Remove the PID file after the script finishes
rm -f "$pid_file"
