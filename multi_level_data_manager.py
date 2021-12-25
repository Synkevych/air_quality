import subprocess, cdsapi, os
from datetime import datetime, timedelta

path_to_data = os.getcwd() + "/data"

def prev_file_exist(file_name):
   is_file_exist = os.path.exists(path_to_data + file_name)

   if not is_file_exist:
      formatted_date = datetime.now().replace(hour=int(get_downloaded_time())).strftime("%Y.%m.%d-%H:00")
      file_name = "multi_level_" + formatted_date + ".netcdf_zip"
      download_new_file(file_name)

def create_data_dir():
   # create data folder if not exist
   is_data_exist = os.path.exists(path_to_data)

   if not is_data_exist:
      os.makedirs(path_to_data)
      print("The new directory \"data\" created!")

def get_downloaded_time():
    # in hours from cds api recomendation
    date = datetime.utcnow()
    delay = 3
    if (date.hour - delay) >= 12:
        return date.replace(hour=12).strftime("%H")
    else:
        return date.replace(hour=0).strftime("%H")

def download_new_file(file_name):
   period = datetime.now().strftime("%Y-%m-%d/%Y-%m-%d")

   create_data_dir()
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
           'time': get_downloaded_time() + ":00",
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
       path_to_data + file_name)
   print("File " + file_name + " successfully saved.")

file_object = open('download_log.txt', 'a')
file_object.write('New download at ' + datetime.now().strftime("%d.%m.%Y-%H:%M:%S") + '\n')
file_object.close()
