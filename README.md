# Air Quality

This script helps to download latest(today and yesterday) datasets from [Atmosphere Data Store](https://ads.atmosphere.copernicus.eu/cdsapp#!/dataset/cams-global-atmospheric-composition-forecasts?tab=form)  

1. Make script executable

```sh
chmod +x main.sh
```

2. Create `$HOME/.cdsapirc` and paste there your API Key:

```sh
url: https://ads.atmosphere.copernicus.eu/api/v2
key: ID:API_KEY
```

3. Create crone task that start download yesterdays data at 8:00 AM

```sh
crontab -l	#(list user's crontab)
crontab -e	#(edit user's crontab)


0 8 * * * /home/ubuntu/main.sh >> /path/to/log.file 2>&1
```

4. Change path `path_to_folder` in <multi_level_data_manager.py>, <single_level_data_manager.py>, <remove_old_data_files.py> for your loval path. You could get them using command `pwd`, for example:

```bash
pwd 
/home/user_name/air_quality/data/
```

5. Execute `./main.sh` to test that script work correctly

6. Logging: