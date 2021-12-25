#!/usr/bin/env python3

import cdsapi, os
from datetime import datetime, timedelta

# change folder for downloaded file, cron use by defaulr $PATH
path = os.getcwd() + "/data/"

period = datetime.now().strftime("%Y-%m-%d/%Y-%m-%d")

formatted_date = datetime.now().replace(hour=int(downloaded_time), minute=0).strftime("%Y.%m.%d-%H:%M")
file_name = "multi_level_" + formatted_date + ".netcdf_zip"

c = cdsapi.Client()

c.retrieve(
    'cams-global-atmospheric-composition-forecasts',
    {
        'variable': [
            'carbon_monoxide', 'formaldehyde', 'methane',
            'nitrogen_dioxide', 'ozone', 'sulphur_dioxide',
        ],
        'date': period,
        'time': '00:00',
        'leadtime_hour': [
            '0', '102', '105',
            '108', '111', '114',
            '117', '12', '120',
            '15', '18', '21',
            '24', '27', '3',
            '30', '33', '36',
            '39', '42', '45',
            '48', '51', '54',
            '57', '6', '60',
            '63', '66', '69',
            '72', '75', '78',
            '81', '84', '87',
            '9', '90', '93',
            '96', '99',
        ],
        'type': 'forecast',
        'format': 'netcdf_zip',
        'model_level': '137',
    },
    file_name)

# log this event to file

file_object = open('download_log.txt', 'a')
file_object.write('New download at ' + datetime.now().strftime("%Y.%m.%d %H:%M") + '\n')
file_object.close()

# Remove files that old than 14 days
filesPath = r"/path/to/folder"

for f in os.listdir(filesPath):
  f = os.path.join(filesPath, f)
  if  datetime.fromtimestamp(os.stat(f).st_atime) < datetime.now() - timedelta(days=14):
    if os.path.isfile(f):
      os.remove(os.path.join(filesPath, f))
