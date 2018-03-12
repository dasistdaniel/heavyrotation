# -*- coding: utf-8 -*-
import scrapy
from libs.wdr import playlist

class WdrSpider(scrapy.Spider):
    name = 'wdr'
    allowed_domains = ['wdr.de']
    start_urls = [
        'https://www1.wdr.de/radio/1live/musik/1live-playlist/index.html',
        'https://www1.wdr.de/radio/wdr2/titelsuche-wdrzwei-124.html'
    ]

    def getData(self, song, field):
        if field['Type'] == 'css':
            return song.css(field['Search']).extract_first()
        elif field['Type'] == 'xpath':
            return song.xpath(field['Search']).extract_first()
        else: 
            return False

    def parse(self, response):
        unicode(response.body.decode(response.encoding)).encode('utf-8')

        pl = playlist()
        
        if pl.iteratorType == 'css':
            songs = response.css(pl.iteratorSearch)
        elif pl.iteratorType:
            songs = response.xpath(pl.iteratorSearch)
        
        for song in songs:
            date   = self.getData(song, pl.date).encode('utf-8')
            time   = self.getData(song, pl.time).encode('utf-8')
            artist = self.getData(song, pl.artist).encode('utf-8')
            title  = self.getData(song, pl.title).encode('utf-8')
            print response.url, date, time, artist, title
            