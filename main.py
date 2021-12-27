#!/usr/bin/env python3

import subprocess, os
from datetime import datetime, timedelta

# create folder for data if not exist
path = os.getcwd() + "/data/"
is_folder_exist = os.path.exists(path)

if not is_folder_exist:
   os.makedirs(path)
   print("The new directory created!")
else:
   # Remove old files
   print("Starting removing an old files")
   subprocess.call("./remove_old_data_files.py", shell=True)

# Load single files
subprocess.call("./single_level_data_manager.py", shell=True)

# Load multilevel files
subprocess.call("./multi_level_data_manager.py", shell=True)
