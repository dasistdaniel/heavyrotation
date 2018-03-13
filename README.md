# heavyrotation.py

**Description:**
Reads the playlist sites of different Radio Stations (currently only German ones) and gives back the Playlist in json format. 
Depends on scrapy

**Usage:**
heavyrotation.py [stationname] [configfile] [playlisturl]

**Warning:**
Currently no input validation, use at your own risk

**Working Scraper:**

(wdr)
```
heavyrotation.py 1Live wdr https://www1.wdr.de/radio/1live/musik/1live-playlist/index.html
heavyrotation.py "1Live Diggi" wdr https://www1.wdr.de/radio/1live-diggi/onair/1live-diggi-playlist/index.html
heavyrotation.py WDR2 wdr https://www1.wdr.de/radio/wdr2/titelsuche-wdrzwei-124.html
heavyrotation.py WDR3 wdr https://www1.wdr.de/radio/wdr3/titelsuche-wdrdrei-104.html
heavyrotation.py WDR4 wdr https://www1.wdr.de/radio/wdr4/titelsuche-wdrvier-102.html
heavyrotation.py WDR5 wdr https://www1.wdr.de/radio/wdr5/musik/titelsuche-wdrfuenf-104.html
heavyrotation.py Cosmo wdr https://www1.wdr.de/radio/cosmo/musik/playlist/index.html
heavyrotation.py Kiraka wdr https://www1.wdr.de/kinder/radio/kiraka/musik/playlist/index.html (Warning: displayed two times)
```
