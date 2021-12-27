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
   subprocess.call("./remove_old_data_files.py", shell=True)

# downloaded time in hours with delay
def get_downloaded_time(date):
    delay = 3
    if (date.hour - delay) >= 12:
        return date.replace(hour=12).strftime("%H")
    else:
        return date.replace(hour=0).strftime("%H")

def log_downloads(file_name):
   file_object = open('download_log.txt', 'a')
   file_object.write(datetime.now().strftime("%d.%m.%Y-%H:%M:%S") + ": File " + file_name + " downloaded.\n")
   file_object.close()

# Load single files
subprocess.call("./single_level_data_manager.py", shell=True)

# Load multilevel files
subprocess.call("./multi_level_data_manager.py", shell=True)
