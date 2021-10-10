# Air Quality

1. Make script executable

```sh
chmod +x multi_level_data.py
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


0 8 * * * /home/ubuntu/multi_level_data.sh >> /path/to/log.file 2>&1
```
