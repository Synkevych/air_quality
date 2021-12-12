#!/usr/bin/env python3

import cdsapi, os
from datetime import datetime, timedelta

period = datetime.now().strftime("%Y-%m-%d/%Y-%m-%d")
file_name = datetime.now().replace(hour=0, minute=0).strftime("%Y_%m_%d-%H")
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
    f"multi_level_{file_name}.netcdf_zip")

# Log a new download
datetime_now = datetime.now()

file_object = open('download_log.txt', 'a')
file_object.write('New download at ' + today_date+'\n')
file_object.close()


# Remove files that old than 14 days 

filesPath = r"/path/to/folder"

for f in os.listdir(filesPath):
  f = os.path.join(filesPath, f)
  if  datetime.fromtimestamp(os.stat(f).st_atime) < datetime_now - timedelta(days=14):
    if os.path.isfile(f):
      os.remove(os.path.join(filesPath, f))
