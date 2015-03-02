#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import requests
from lxml import html

def parse_playlist(config_data):

    playlist = []
    
    settings = config_data['settings']
    xpath = config_data['xpath']
    informations = config_data['informations']
    
    logging.info ('Loading %s' % settings['playlist_url'])
    req = requests.get(settings['playlist_url'])
    logging.debug (req)
    logging.debug (req.headers)
    
    
    logging.info ('Check for Playlist Type')
    if settings['playlist_type'] == 'html':
        logging.info("Playlist Type html")
        lxml_data = html.fromstring(req.text.encode("utf-8"))
        
        length = int(lxml_data.xpath(xpath['length']))
        
        for counter in xrange(1,length + 1):
            time = lxml_data.xpath(construct_xpath(xpath['time'], counter)).strip()
            date = lxml_data.xpath(construct_xpath(xpath['date'], counter)).strip()
            artist = lxml_data.xpath(construct_xpath(xpath['artist'], counter))[0].strip()
            title = lxml_data.xpath(construct_xpath(xpath['title'], counter))[0].strip()
            
            logging.debug("%s. [%s %s] %s - %s" % (counter, time, date, artist, title))
    
            playlist.append({'date':date, 'time': time, 'artist': artist, 'title': title})
    return playlist
    
def construct_xpath(xpath, number):
    repl = xpath.replace('%counter%', str(number))
    return repl
