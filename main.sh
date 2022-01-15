#!/usr/bin/env python3

import subprocess, os, constants
from datetime import datetime, timedelta

# create folder for data if not exist
path = constants.AIR_QUALITY_DIR

is_folder_exist = os.path.exists(path + "/data/")

if not is_folder_exist:
   os.makedirs(path + "/data/")
   print("The new directory created!")
else:
   # Remove old files
   subprocess.call(path + "/remove_old_data_files.py", shell=True)

# Load single files
subprocess.call(path + "/single_level_data_manager.py", shell=True)

# Load multilevel files
subprocess.call(path + "/multi_level_data_manager.py", shell=True)