# SteamFlux #
SteamFlux is an application that periodically scrapes Steam store pages to collect game prices and stores those price points in an InfluxDB bucket. You can then visualize historical price development (per game) using Grafana or any client that reads InfluxDB data.

## Disclaimer ##
This repository is not officially related to Valve/Steam in any way.

### Features ###
- Periodic scraping of Steam game pages
- Stores price points (with timestamp, game id, tags) in InfluxDB
- Example Flux queries to inspect raw and aggregate data 
- Lightweight — runs on Raspberry Pi, server, or container
-  
-  
_more features coming soon_

### Setup ###
1. ```pip install -r requirements.txt```
2. Copy ```.example.env``` to ```.env``` and paste your ```INFLUX_DB_TOKEN```

### Usage ###
Press that Green ```Run``` button in PyCharm or use the ```python main.py``` command.

