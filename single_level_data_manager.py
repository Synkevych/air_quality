#!/usr/bin/env python3

import cdsapi, os, constants
from datetime import datetime, timedelta

path_to_folder = constants.AIR_QUALITY_DIR
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
           'variable': [
               'particulate_matter_10um', 'particulate_matter_2.5um',
           ],
           'date': period,
           'time': get_downloaded_time(datetime) + ":00",
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
               '99',
           ],
           'type': 'forecast',
           'format': 'netcdf_zip',
       },
       path_to_folder + file_name)

   print("File " + file_name + " successfully saved")
   log_downloads(file_name)

for i in range(2):
   formatted_date = date_time.replace(hour=int(get_downloaded_time(date_time))).strftime("%Y.%m.%d-%H:00")
   file_name = "single_level_" + formatted_date + ".netcdf_zip"

   file_exist = os.path.exists(path_to_folder + file_name)

   if file_exist:
       print("file " + file_name + " exist, try to download an old file")
   else:
       print("Strating downloads " + file_name)
       download_new_file(file_name, date_time)
   date_time = date_time - timedelta(hours=12) # date for download previous file