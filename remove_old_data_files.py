#!/usr/bin/env python3

import os, constants
from datetime import datetime, timedelta

days_interval=6
dir = constants.AIR_QUALITY_DIR + "/data"

files_in_directory = os.listdir(dir )
filtered_files = [file for file in files_in_directory if file.endswith(".nc") or file.endswith(".netcdf_zip")]
for file in filtered_files:
   path_to_file = os.path.join(dir, file)
   if datetime.fromtimestamp(os.stat(path_to_file).st_atime) < datetime.now() - timedelta(days=days_interval):
      if os.path.isfile(path_to_file):
         os.remove(path_to_file)
         print("file", file, "older that " + str(days_interval) + " days removed")
