#!/usr/bin/env python3

import cdsapi, os, time, sys
from datetime import datetime, timedelta

today_date = datetime.now().strftime("%Y-%m-%d/%Y-%m-%d")

file_name = datetime.now().replace(hour=0, minute=0).strftime("%Y_%m_%d-%H")

c = cdsapi.Client()

c.retrieve(
    'cams-global-atmospheric-composition-forecasts',
    {   
        'variable': [
            'carbon_monoxide', 'formaldehyde', 'methane',
            'nitrogen_dioxide', 'ozone', 'sulphur_dioxide',
        ],  
        'date': today_date,
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
    f"multi_level_{file_name}.netcdf_zip")

# Log a new download

file_object = open('download_log.txt', 'a')
file_object.write('New download at ' + today_date+'\n')
file_object.close()


# Remove files that old than 14 days 

filesPath = r"/home/roman/Documents/IMMSP/air_quality/test_removing"

now = time.time()

for f in os.listdir(filesPath):
  f = os.path.join(filesPath, f)
  if os.stat(f).st_mtime < now - 14 * 86400:
    if os.path.isfile(f):
      os.remove(os.path.join(filesPath, f))