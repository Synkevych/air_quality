#!/usr/bin/env python3

import cdsapi, os, constants
from datetime import timedelta

path_to_folder = constants.DATA_DIR
date_time_now = constants.DATE_TIME_NOW
date_time = constants.DATE_FOR_DOWNLOADS
downloads_times = constants.RANGE
file_name_prefix = "multi_level_"
data_format = constants.DATA_FORMAT

def log_downloads(file_name):
    log_file_path = os.path.join(path_to_folder, 'downloads.log')
    with open(log_file_path, 'a') as file:
        file.write(f"{date_time_now.strftime('%d.%m.%Y-%H:%M:%S')}: File {file_name} downloaded.\n")

def download_new_file(file_name, date_time):
   period = date_time.strftime("%Y-%m-%d/%Y-%m-%d")
   cds = cdsapi.Client()

   cds.retrieve(
       'cams-europe-air-quality-forecasts',
       {
           'variable': [
               'ammonia', 'formaldehyde',
               'nitrogen_dioxide', 'nitrogen_monoxide',
               'ozone', 'sulphur_dioxide',
           ],
           'model': ['ensemble', 'mocage'],
           'level': ['0'],
           'date': [period],
           'type': ['forecast'],
           'time': ["00:00"], # only this time available for forecast type
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
           'data_format': data_format,
       },
       os.path.join(path_to_folder, file_name)
       )

   print(f"File {file_name} successfully saved.")
   log_downloads(file_name)

for i in range(downloads_times):
   formatted_date = date_time.strftime("%Y%m%d")
   file_name = file_name_prefix + formatted_date + "." + data_format

   file_path = os.path.join(path_to_folder, file_name)
   file_exist = os.path.exists(file_path)

   if file_exist:
       print("file " + file_name + " exist, trying to download an old dataset")
   else:
       print("Starting downloads " + file_name)
       download_new_file(file_name, date_time)
   date_time = date_time - timedelta(hours=12) # date for download previous file
