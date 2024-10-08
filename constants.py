#!/usr/bin/env python3
from datetime import datetime, timedelta, timezone

DATA_DIR = "data/"
DATA_FORMAT = 'netcdf_zip'
DELAY_IN_HOURS = 6 # Delay is important for ensuring data availability
DATE_TIME_NOW = datetime.now(timezone.utc)
DATE_FOR_DOWNLOADS = DATE_TIME_NOW - timedelta(hours=DELAY_IN_HOURS)
RANGE = 1 # how much data will be downloaded counting from current day (1 per a day)
REMOVE_AFTER_DAYS=6
REMOVAL_THRESHOLD_DATE = DATE_TIME_NOW - timedelta(days=REMOVE_AFTER_DAYS)
