#!/usr/bin/env python3

import cdsapi, os, constants
from datetime import timedelta

path_to_folder = constants.DATA_DIR
date_time = constants.DATE_FOR_DOWNLOADS
date_time_now = constants.DATE_TIME_NOW
file_name_prefix = "single_level_"
downloads_times = constants.RANGE
data_format = constants.DATA_FORMAT

# downloaded time in hours with delay
def get_nearest_download_hour(date):
    if (date.hour) >= 12:
        return date.replace(hour=12, minute=0)
    else:
        return date.replace(hour=0, minute=0)

def log_downloads(file_name):
    log_file_path = os.path.join(path_to_folder, 'downloads.log')
    with open(log_file_path, 'a') as file:
        file.write(f"{date_time_now.strftime('%d.%m.%Y-%H:%M:%S')}: File {file_name} downloaded.\n")

def download_new_file(file_name, date_time):
   period = date_time.strftime("%Y-%m-%d/%Y-%m-%d")
   time = date_time.strftime("%H:%m")
   cds = cdsapi.Client()

   cds.retrieve(
       'cams-global-atmospheric-composition-forecasts',
       {
           'variable': [
               'particulate_matter_2.5um',
               'particulate_matter_10um'
           ],
           'date': [period],
           'time': [time],
           'leadtime_hour': [
               '0', '1', '10',
               '100', '101', '102',
               '103', '104', '105',
               '106', '107', '108',
               '109', '11', '110',
               '111', '112', '113',
               '114', '115', '116',
               '117', '118', '119',
               '12', '120', '13',
               '14', '15', '16',
               '17', '18', '19',
               '2', '20', '21',
               '22', '23', '24',
               '25', '26', '27',
               '28', '29', '3',
               '30', '31', '32',
               '33', '34', '35',
               '36', '37', '38',
               '39', '4', '40',
               '41', '42', '43',
               '44', '45', '46',
               '47', '48', '49',
               '5', '50', '51',
               '52', '53', '54',
               '55', '56', '57',
               '58', '59', '6',
               '60', '61', '62',
               '63', '64', '65',
               '66', '67', '68',
               '69', '7', '70',
               '71', '72', '73',
               '74', '75', '76',
               '77', '78', '79',
               '8', '80', '81',
               '82', '83', '84',
               '85', '86', '87',
               '88', '89', '9',
               '90', '91', '92',
               '93', '94', '95',
               '96', '97', '98',
               '99'
           ],
           'type': ['forecast'],
           "data_format": data_format
       }).download(path_to_folder + file_name)

   print("File " + file_name + " successfully saved")
   log_downloads(file_name)

for i in range(downloads_times):
   nearest_download_time = get_nearest_download_hour(date_time)
   file_name = file_name_prefix + nearest_download_time.strftime("%Y%m%d-%H00") + "." + data_format

   file_exist = os.path.exists(path_to_folder + file_name)

   if file_exist:
       print("file " + file_name + " exist, try to download an old file")
   else:
       print("Starting downloads " + file_name)
       download_new_file(file_name, nearest_download_time)
   date_time = date_time - timedelta(hours=12) # date for download previous file
