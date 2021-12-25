import subprocess, cdsapi, os
from datetime import datetime, timedelta

path_to_folder = os.getcwd() + "/data/"

# downloaded time in hours with delay
def get_downloaded_time(date):
    delay = 3
    if (date.hour - delay) >= 12:
        return date.replace(hour=12).strftime("%H")
    else:
        return date.replace(hour=0).strftime("%H")

def log_downloads(file_name):
   file_object = open('download_log.txt', 'a')
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
               'ammonium_aerosol_mass_mixing_ratio', #'formaldehyde',
            #    'nitrogen_dioxide', 'nitric_acid', 'nitrogen_monoxide',
            #    'ozone', 'sulphur_dioxide',
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
       },
       path_to_folder + file_name)

   print("File " + file_name + " successfully saved.")
   log_downloads(file_name)

date_time = datetime.utcnow() - timedelta(hours=12)
formatted_date = date_time.replace(hour=int(get_downloaded_time(date_time))).strftime("%Y.%m.%d-%H:00")
file_name = "multi_level_" + formatted_date + ".netcdf_zip"

prev_file_exist = os.path.exists(path_to_folder + file_name)

if prev_file_exist:
    print("file exist, try to download a new file")
    date_time = datetime.utcnow()

    formatted_date = date_time.replace(hour=int(get_downloaded_time(date_time))).strftime("%Y.%m.%d-%H:00")
    new_file_name = "multi_level_" + formatted_date + ".netcdf_zip"
    download_new_file(new_file_name, date_time)
else:
    print("previous file not exist, the download starts")
    download_new_file(file_name, date_time)
