#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
import simplejson 
import sys
import datetime      

class heavyrotation(scrapy.Spider):
    def loadSettings(self, station):
        with open('settings/' + station + '.json') as data_file:    
            data = simplejson.load(data_file)
        return data

    def getData(self, song, field):
        if field['Type'] == 'css':
            return song.css(field['Search'])
        elif field['Type'] == 'xpath':
            return song.xpath(field['Search'])
        else: 
            return False

    def parse(self, response):
        config = self.name
        station = self.settings['STATION']
        settings = self.loadSettings(config)
        
        playlist = []
        
        songs = self.getData(response, settings['iterator'])
        
        try:
            start = settings['iterator']['Start']
        except:
            start = 0
            
        try:
            end = settings['iterator']['End']
        except:
            end = len(songs)

        for i in range(start, end):
            song = songs[i]
            
            if settings['date']['Type'] != 'today':
                date   = self.getData(song, settings['date']).extract_first().encode('utf-8')
            else:
                date = datetime.datetime.now().strftime("%Y-%m-%d")
            time   = self.getData(song, settings['time']).extract_first().encode('utf-8')
            dt     = datetime.datetime.strptime(date + " " + time, settings['dtformat'] )
            
            artist = self.getData(song, settings['artist']).extract_first().encode('utf-8')
            title  = self.getData(song, settings['title']).extract_first().encode('utf-8')
            playlist.append({'datetime': str(dt), 'artist': artist, 'title': title})
        
        infos = {'station': station, 'playlist_url': response.url}
        output = {'infos': infos, 'playlist': playlist}
        print simplejson.dumps(output, sort_keys=False, indent=4)

def getPlaylist(station, config, url):        
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'LOG_ENABLED': True,
        'STATION' : station
    })
    process.crawl(heavyrotation, 
        start_urls=[url], 
        name=config)
    process.start()

if __name__ == '__main__':
    if len (sys.argv) != 4 :
        print "Usage: " + sys.argv[0] + " [stationname] [config] [url]"
        sys.exit (1)
    else:
        getPlaylist( sys.argv[1], sys.argv[2],  sys.argv[3])