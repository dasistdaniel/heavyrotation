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
**working**
heavyrotation.py 1Live wdr https://www1.wdr.de/radio/1live/musik/1live-playlist/index.html
heavyrotation.py "1Live Diggi" wdr https://www1.wdr.de/radio/1live-diggi/onair/1live-diggi-playlist/index.html
heavyrotation.py WDR2 wdr https://www1.wdr.de/radio/wdr2/titelsuche-wdrzwei-124.html
heavyrotation.py WDR3 wdr https://www1.wdr.de/radio/wdr3/titelsuche-wdrdrei-104.html
heavyrotation.py WDR4 wdr https://www1.wdr.de/radio/wdr4/titelsuche-wdrvier-102.html
heavyrotation.py WDR5 wdr https://www1.wdr.de/radio/wdr5/musik/titelsuche-wdrfuenf-104.html
heavyrotation.py Cosmo wdr https://www1.wdr.de/radio/cosmo/musik/playlist/index.html

**working with special settings**
heavyrotation.py Kiraka wdr_kiraka https://www1.wdr.de/kinder/radio/kiraka/musik/playlist/index.html
```

(ndr)
```
**working**
heavyrotation.py "NDR1 Niedersachsen" ndr https://www.ndr.de/ndr1niedersachsen/programm/titelliste1210.html
heavyrotation.py "NDR1 Radio MV" ndr https://www.ndr.de/radiomv/programm/titelliste1206.html
heavyrotation.py "NDR1 Welle Nord" ndr https://www.ndr.de/wellenord/programm/titelliste1204.html
heavyrotation.py "NDR 90,3" ndr https://www.ndr.de/903/programm/titelliste1208.html
heavyrotation.py "NDR2" ndr https://www.ndr.de/ndr2/programm/titelliste1202.html
heavyrotation.py "NDR Kultur" ndr https://www.ndr.de/ndrkultur/programm/titelliste1212.html
heavyrotation.py "NDR Blue" ndr https://www.ndr.de/ndrblue/programm/titelliste1214.html
heavyrotation.py "NDR Plus" ndr https://www.ndr.de/ndrplus/programm/titelliste1230.html
heavyrotation.py "NJOY" ndr https://www.n-joy.de/musik/titelliste/index.html
```

(rbb)
```
**working**
heavyrotation.py "Antenne Brandenburg" rbb http://playlisten.rbb-online.de/antenne_brandenburg/main/index.php
heavyrotation.py "radioBERLIN 88,8" rbb http://playlisten.rbb-online.de/radioberlin/main/
```

(br) Currently Broken
```
heavyrotation.py "Bayern1" br http://www.br.de/radio/bayern-1/welle110.html
heavyrotation.py "Bayern2" br http://www.br.de/radio/bayern2/welle106.html
heavyrotation.py "Bayern3" br http://www.br.de/radio/bayern-3/bayern-3-playlist-musiktitel-recherche/index.html
heavyrotation.py "Bayern Plus" br http://www.br.de/radio/bayern-plus/welle118.html

```
