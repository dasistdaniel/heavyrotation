#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Scrapes the playlist data of various radio stations """

import sys
import datetime
import simplejson
import scrapy
from scrapy.crawler import CrawlerProcess

def load_settings(station):
    """ Load the settings from the settings folder """
    with open('settings/' + station + '.json') as data_file:
        data = simplejson.load(data_file)
    return data

def get_data(song, field):
    """ Get the needed data by the type specified """
    if field['Type'] == 'css':
        return song.css(field['Search'])
    elif field['Type'] == 'xpath':
        return song.xpath(field['Search'])
    return False

class HeavyRotation(scrapy.Spider):
    """ Main Scrapy Spider Class """
    def parse(self, response):
        config = self.name
        station = self.settings['STATION']
        settings = load_settings(config)
        playlist = []

        songs = get_data(response, settings['iterator'])

        try:
            start = settings['iterator']['Start']
        except KeyError:
            start = 0

        try:
            end = settings['iterator']['End']
        except KeyError:
            end = len(songs)

        for i in range(start, end):
            song = songs[i]

            if settings['date']['Type'] != 'today':
                date = get_data(song, settings['date']).extract_first().encode('utf-8')
            else:
                date = datetime.datetime.now().strftime("%Y-%m-%d")

            time = get_data(song, settings['time']).extract_first().encode('utf-8')
            date_time = datetime.datetime.strptime(date + " " + time, settings['dtformat'])

            artist = get_data(song, settings['artist']).extract_first().encode('utf-8')
            title = get_data(song, settings['title']).extract_first().encode('utf-8')
            playlist.append({'datetime': str(date_time), 'artist': artist, 'title': title})

        infos = {'station': station, 'playlist_url': response.url}
        output = {'infos': infos, 'playlist': playlist}
        print simplejson.dumps(output, sort_keys=False, indent=4)

def get_playlist(station, config, url):
    """ starts the Crawler """
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'LOG_ENABLED': False,
        'STATION' : station
    })
    process.crawl(HeavyRotation, start_urls=[url], name=config)
    process.start()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "Usage: " + sys.argv[0] + " [stationname] [config] [url]"
        sys.exit(1)
    else:
        get_playlist(sys.argv[1], sys.argv[2], sys.argv[3])
