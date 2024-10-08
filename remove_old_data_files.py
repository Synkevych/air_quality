#!/usr/bin/env python3

import os, constants
from datetime import datetime, timezone

days_interval = constants.REMOVAL_THRESHOLD_DATE
dir_name = constants.DATA_DIR
date_time_now = constants.DATE_TIME_NOW
removal_threshold_date = constants.REMOVAL_THRESHOLD_DATE
data_format = "." + constants.DATA_FORMAT

files_in_directory = os.listdir(dir_name)
filtered_files = [file for file in files_in_directory if file.endswith(data_format)]
for file in filtered_files:
   path_to_file = os.path.join(dir_name, file)
   file_access_time = datetime.fromtimestamp(os.stat(path_to_file).st_atime, tz=timezone.utc)
   if file_access_time < removal_threshold_date:
      if os.path.isfile(path_to_file):
         os.remove(path_to_file)
         print("file", file, "older that " + str(days_interval) + " days removed")
