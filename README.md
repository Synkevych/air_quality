# Air Quality

This script helps to download latest(today and yesterday) datasets from [Atmosphere Data Store](https://ads.atmosphere.copernicus.eu/cdsapp#!/dataset/cams-global-atmospheric-composition-forecasts?tab=form)

## Getting started

#### Prerequisites

The setups steps expect following tools installed on the system.

- git
- Python 2.7 / 3
- pip / pip3
- [cdsapi](https://cds.climate.copernicus.eu/api-how-to)

#### 1. Install _cdsapi_ library

Depending on Python version (2 or 3) use the appropriate pip version for install _cdsapi_.

For python2 `pip install cdsapi`
For python3 `pip3 install cdsapi`

#### 2. Setup _cdsapi_ API Key

Create `$HOME/.cdsapirc` and paste there your API Key:

```sh
vim $HOME/.cdsapirc
url: https://ads.atmosphere.copernicus.eu/api/v2
key: ID:API_KEY
```

#### 2. Check out the repository

```bash
git clone https://github.com/Synkevych/air_quality.git
cd air_quality
```

#### 3. Setup the project for your computer

- Make script executable

```sh
chmod +x main.sh
```

- Change path `AIR_QUALITY_DIR` in <constants.py> for your actual local path. You could get it using command `pwd`, for example:

```sh
pwd; # example of output: /home/user_name/air_quality
```

- Execute `./main.sh` to test that script work correctly

- Create crone task that start download data each day (for example at 8:00 AM)

```sh
crontab -l	#(list user's crontab)
crontab -e	#(edit user's crontab)

# 0 */6 * * * - for each 6 hours
0 */6 * * * /home/ubuntu/main.sh >> /path/to/log.file 2>&1
```

#### 4. Logging

After start <main.sh> in main folder you should see a new file <main.log>. This file created by crontab and visualize all downloading process.

Inside `data` folder located another file <downloads.log> that saves all file name that will be downloaded. For example:

```sh
$ tail -10 data/downloads.log
15.01.2022-00:01:35: File single_level_2022.01.14-12:00.netcdf_zip downloaded.
15.01.2022-00:04:09: File multi_level_2022.01.14-12:00.netcdf_zip downloaded.
15.01.2022-12:01:28: File single_level_2022.01.15-00:00.netcdf_zip downloaded.
15.01.2022-12:03:42: File multi_level_2022.01.15-00:00.netcdf_zip downloaded.

$ tail -20 main.log
2022-01-15 12:00:23,118 INFO Downloading https://download-0002.copernicus-atmosphere.eu/cache-compute-0002/cache/data7/adaptor.mars_constrained.internal-1642240820.1910667-24105-14-2078f329-32bd-4780-abce-f17540147236.zip to /home/ik/Roman/air_quality/data/single_level_2022.01.15-00:00.netcdf_zip (187.4M)
Strating downloads single_level_2022.01.15-00:00.netcdf_zip
2022-01-15 12:01:28,681 INFO Download rate 2.9M/s  
File single_level_2022.01.15-00:00.netcdf_zip successfully saved
file single_level_2022.01.14-12:00.netcdf_zip exist, try to download an old file
2022-01-15 12:01:29,237 INFO Welcome to the CDS
2022-01-15 12:01:29,237 INFO Sending request to https://ads.atmosphere.copernicus.eu/api/v2/resources/cams-global-atmospheric-composition-forecasts
2022-01-15 12:01:29,300 INFO Request is queued
2022-01-15 12:01:30,357 INFO Request is running
2022-01-15 12:01:50,440 INFO Request is completed
2022-01-15 12:01:50,441 INFO Downloading https://download-0000.copernicus-atmosphere.eu/cache-compute-0000/cache/data7/adaptor.mars_constrained.internal-1642240905.6529446-12546-11-a63827fe-e43f-4860-b555-ec2b38128459.grib to /home/ik/Roman/air_quality/data/multi_level_2022.01.15-00:00.netcdf_zip (333.6M)
Strating downloads multi_level_2022.01.15-00:00.netcdf_zip
2022-01-15 12:03:41,843 INFO Download rate 3M/s    
File multi_level_2022.01.15-00:00.netcdf_zip successfully saved.
file multi_level_2022.01.14-12:00.netcdf_zip exist, try to download an old file
files that older that 6 days removed
file single_level_2022.01.15-00:00.netcdf_zip exist, try to download an old file
file single_level_2022.01.14-12:00.netcdf_zip exist, try to download an old file
file multi_level_2022.01.15-00:00.netcdf_zip exist, try to download an old file
file multi_level_2022.01.14-12:00.netcdf_zip exist, try to download an old file
```
