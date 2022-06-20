#!/usr/bin/env python3

import cdsapi
import subprocess
import cdsapi
import os
import constants
from datetime import datetime, timedelta

path_to_folder = constants.AIR_QUALITY_DIR
delay = 6
date_time = datetime.utcnow() - timedelta(hours=delay)

# downloaded time in hours with delay


def log_downloads(file_name):
   file_object = open(path_to_folder + '/data/' + 'downloads.log', 'a')
   file_object.write(datetime.now().strftime(
       "%d.%m.%Y-%H:%M:%S") + ": File " + file_name + " downloaded.\n")
   file_object.close()


def download_new_file(file_name, datetime):
   period = datetime.strftime("%Y-%m-%d/%Y-%m-%d")
   c = cdsapi.Client()

   c.retrieve(
       'cams-europe-air-quality-forecasts',
       {
           'model': [
               'ensemble', 'mocage',
           ],
           'date': period,
           'variable': [
               'carbon_monoxide', 'nitrogen_dioxide', 'particulate_matter_10um',
               'particulate_matter_2.5um', 'sulphur_dioxide',
           ],
           'level': '0',
           'type': 'forecast',
           'leadtime_hour': [
               '0', '1', '10',
               '11', '12', '13',
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
               '96',
           ],
           'time': '00:00',
           'format': 'netcdf',
       },
       path_to_folder + "/data/" + file_name)

   print("File " + file_name + " successfully saved.")
   log_downloads(file_name)


for i in range(2):
   formatted_date = date_time.strftime("%Y-%m-%d")
   file_name = "cams-eu-air-quality-forecasts_" + formatted_date + ".nc"
   file_exist = os.path.exists(path_to_folder + "/data/" + file_name)

   if file_exist:
       print("file " + file_name + " exist, trying to download old dataset")
   else:
       print("Strating downloads " + file_name)
       download_new_file(file_name, date_time)
   date_time = date_time - timedelta(days=1)
