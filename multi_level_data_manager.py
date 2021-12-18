#!/usr/bin/env python3

import subprocess, cdsapi, os
from datetime import datetime, timedelta

period = datetime.now().strftime("%Y-%m-%d/%Y-%m-%d")
formatted_date = datetime.now().replace(hour=0, minute=0).strftime("%Y_%m_%d-%H")

c = cdsapi.Client()

c.retrieve(
    'cams-global-atmospheric-composition-forecasts',
    {
        'date': '2021-12-17/2021-12-17',
        'type': 'forecast',
        'format': 'grib',
        'variable': [
            'ammonium_aerosol_mass_mixing_ratio', 'formaldehyde',
            'nitrogen_dioxide', 'nitric_acid', 'nitrogen_monoxide',
            'ozone', 'sulphur_dioxide',
            #'dust_aerosol_0.03-0.55um_mixing_ratio', 'dust_aerosol_0.55-0.9um_mixing_ratio', 'dust_aerosol_0.9-20um_mixing_ratio', 
        ],
        'time': [
            '00:00', '12:00',
        ],
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
    f"multi_level_{formatted_date}.netcdf_zip")

print("file single_level_"+formatted_date+".netcdf_zip successfully saved")

file_object = open('download_log.txt', 'a')
file_object.write('New download at ' + datetime.now().strftime("%d.%m.%Y-%H:%M") + '\n')
file_object.close()