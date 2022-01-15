#!/usr/bin/env python3

import subprocess, sys, os, constants
from datetime import datetime, timedelta

# create folder for data if not exist
path = constants.AIR_QUALITY_DIR

if path == "/path/to/air_quality":
   sys.exit("Please change the default path in file constants.py to real")

is_folder_exist = os.path.exists(path + "/data/")

if not is_folder_exist:
   os.makedirs(path + "/data/")
   print("The new data directory created!")
else:
   # Remove old files
   subprocess.call(path + "/remove_old_data_files.py", shell=True)

# Load single files
subprocess.call(path + "/single_level_data_manager.py", shell=True)

# Load multilevel files
subprocess.call(path + "/multi_level_data_manager.py", shell=True)