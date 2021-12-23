import subprocess, cdsapi, os
from datetime import datetime, timedelta

path = os.getcwd() + "/data/"

isExist = os.path.exists(path)

if not isExist:
  os.makedirs(path)
  print("The new directory \"data\" is created!")

def get_downloaded_time(date):
    delay = 3 # in hours from cds
    if (date.hour - delay) >= 12:
        return date.replace(hour=12).strftime("%H")
    else:
        return date.replace(hour=0).strftime("%H")

period = datetime.now().strftime("%Y-%m-%d/%Y-%m-%d")
downloaded_time = get_downloaded_time(datetime.utcnow())

formatted_date = datetime.now().replace(hour=int(downloaded_time), minute=0).strftime("%Y.%m.%d-%H:%M")
file_name = "multi_level_" + formatted_date + ".netcdf_zip"

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
        'time': downloaded_time + ":00",
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
    path + file_name)

print("file " + file_name + " successfully saved.")

file_object = open('download_log.txt', 'a')
file_object.write('New download at ' + datetime.now().strftime("%d.%m.%Y-%H:%M") + '\n')
file_object.close()
