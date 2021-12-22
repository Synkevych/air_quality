#!/usr/bin/env python3

import os
from datetime import datetime, timedelta

days_interval=14
files_path = r"/home/ik/Roman/air_quality/data"
os.chdir('/home/ik/Roman/air_quality/data')

for f in os.listdir(files_path):
    f = os.path.join(files_path, f)
    if  datetime.fromtimestamp(os.stat(f).st_atime) < datetime.now() - timedelta(days=days_interval):
      if os.path.isfile(f):
        os.remove(os.path.join(files_path, f))

print("files that older that "+str(days_interval)+" days removed")