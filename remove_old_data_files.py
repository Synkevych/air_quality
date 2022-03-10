#!/usr/bin/env python3

import os, constants
from datetime import datetime, timedelta

days_interval=6
path_to_folder = constants.AIR_QUALITY_DIR
os.chdir(path_to_folder)

for f in os.listdir(path_to_folder):
    f = os.path.join(path_to_folder, f)
    if  datetime.fromtimestamp(os.stat(f).st_atime) < datetime.now() - timedelta(days=days_interval):
      if os.path.isfile(f):
        os.remove(os.path.join(path_to_folder, f))
      print("files that older that " + str(days_interval) + " days removed")
