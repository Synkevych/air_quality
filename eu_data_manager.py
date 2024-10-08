#!/usr/bin/env python3

import cdsapi, os, constants
from datetime import timedelta

path_to_folder = constants.DATA_DIR
date_time = constants.DATE_FOR_DOWNLOADS
date_time_now = constants.DATE_TIME_NOW
file_name_prefix = "cams-eu-air-quality-forecasts_"
downloads_times = constants.RANGE
data_format = constants.DATA_FORMAT

def log_downloads(file_name):
    log_file_path = os.path.join(path_to_folder, 'downloads.log')
    with open(log_file_path, 'a') as file:
        file.write(f"{date_time_now.strftime('%d.%m.%Y-%H:%M:%S')}: File {file_name} downloaded.\n")

def download_new_file(file_name, datetime):
   period = datetime.strftime("%Y-%m-%d/%Y-%m-%d")
   cds = cdsapi.Client()
   cds.retrieve(
       'cams-europe-air-quality-forecasts',
       {
           'variable': [
               'carbon_monoxide', 'nitrogen_dioxide', 'particulate_matter_10um',
               'particulate_matter_2.5um', 'sulphur_dioxide',
           ],
           'model': ['ensemble', 'mocage'],
           'level': ['0'],
           'date': [period],
           'type': ['forecast'],
           'time': ['00:00'], # only this time available for forecast type
           'leadtime_hour': [
               '0', '1', '10', '11', '12', '13',
               '14', '15', '16', '17', '18', '19',
               '2', '20', '21', '22', '23', '24',
               '25', '26', '27', '28', '29', '3',
               '30', '31', '32', '33', '34', '35',
               '36', '37', '38', '39', '4', '40',
               '41', '42', '43', '44', '45', '46',
               '47', '48', '49', '5', '50', '51',
               '52', '53', '54', '55', '56', '57',
               '58', '59', '6', '60', '61', '62',
               '63', '64', '65', '66', '67', '68',
               '69', '7', '70', '71', '72', '73',
               '74', '75', '76', '77', '78', '79',
               '8', '80', '81', '82', '83', '84',
               '85', '86', '87', '88', '89', '9',
               '90', '91', '92', '93', '94', '95',
               '96',
           ],
           'data_format': data_format,
       }).download(path_to_folder + file_name)

   print("File " + file_name + " successfully saved.")
   log_downloads(file_name)


for i in range(downloads_times):
   formatted_date = date_time.strftime("%Y%m%d")
   file_name = file_name_prefix + formatted_date + "." + data_format
   file_exist = os.path.exists(path_to_folder + file_name)

   if file_exist:
       print("file " + file_name + " exist, trying to download an old dataset")
   else:
       print("Starting downloads " + file_name)
       download_new_file(file_name, date_time)
   date_time = date_time - timedelta(days=1)
