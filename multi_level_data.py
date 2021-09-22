#!/usr/bin/env python3

import cdsapi
from datetime import datetime, timedelta

day = timedelta(1)
today = (datetime.now() - day).strftime("%Y-%m-%d/%Y-%m-%d")

file_name = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")

c = cdsapi.Client()

c.retrieve(
    'cams-global-atmospheric-composition-forecasts',
    {
        'variable': [
            'carbon_monoxide', 'formaldehyde', 'methane',
            'nitrogen_dioxide', 'ozone', 'sulphur_dioxide',
        ],
        'date': today,
        'time': '00:00',
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
        'type': 'forecast',
        'format': 'netcdf_zip',
        'model_level': '137',
    },
    f"multi_level_{file_name}.netcdf_zip")


