# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
import simplejson 
        
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
        for song in songs:
            date   = self.getData(song, settings['date']).extract_first().encode('utf-8')
            time   = self.getData(song, settings['time']).extract_first().encode('utf-8')
            artist = self.getData(song, settings['artist']).extract_first().encode('utf-8')
            title  = self.getData(song, settings['title']).extract_first().encode('utf-8')
            playlist.append({'station': station, 'date': date, 'time': time, 'artist': artist, 'title': title})
        
        print simplejson.dumps(playlist, sort_keys=True, indent=4)

def getPlaylist(station, config, url):        
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'LOG_ENABLED': False,
        'STATION' : station
    })
    process.crawl(heavyrotation, 
        start_urls=[url], 
        name=config)
    process.start()
    
getPlaylist('1Live', 'wdr', 'https://www1.wdr.de/radio/1live/musik/1live-playlist/index.html')