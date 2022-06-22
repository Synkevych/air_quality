#!/usr/bin/env python3

import cdsapi
import subprocess, cdsapi, os, constants
from datetime import datetime, timedelta

path_to_folder = constants.AIR_QUALITY_DIR + "\data"
delay = 6
date_time = datetime.utcnow() - timedelta(hours=delay)

# downloaded time in hours with delay
def get_downloaded_time(date):
    if (date.hour) >= 12:
        return date.replace(hour=12).strftime("%H")
    else:
        return date.replace(hour=0).strftime("%H")

def log_downloads(file_name):
   file_object = open(path_to_folder + 'downloads.log', 'a')
   file_object.write(datetime.now().strftime("%d.%m.%Y-%H:%M:%S") + ": File " + file_name + " downloaded.\n")
   file_object.close()

def download_new_file(file_name, datetime):
   period = datetime.strftime("%Y-%m-%d/%Y-%m-%d")
   c = cdsapi.Client()

   c.retrieve(
       'cams-global-atmospheric-composition-forecasts',
       {
           'date': period,
           'type': 'forecast',
           'format': 'grib',
           'variable': [
               'ammonium_aerosol_mass_mixing_ratio', 'formaldehyde',
               'nitrogen_dioxide', 'nitric_acid', 'nitrogen_monoxide',
               'ozone', 'sulphur_dioxide',
           ],
           'time': get_downloaded_time(datetime) + ":00",
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
           'model_level': '137',
           'format': 'netcdf_zip',
       },
       path_to_folder + file_name)

   print("File " + file_name + " successfully saved.")
   log_downloads(file_name)

for i in range(2):
   formatted_date = date_time.replace(hour=int(get_downloaded_time(date_time))).strftime("%Y.%m.%d-%H:00")
   file_name = "multi_level_" + formatted_date + ".netcdf_zip"

   file_exist = os.path.exists(path_to_folder + file_name)

   if file_exist:
       print("file " + file_name + " exist, trying to download an old dataset")
   else:
       print("Starting downloads " + file_name)
       download_new_file(file_name, date_time)
   date_time = date_time - timedelta(hours=12) # date for download previous file
