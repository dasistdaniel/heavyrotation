#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import requests
from lxml import html
import datetime

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
        
        counter_length = int(lxml_data.xpath(settings['counter_length']))+1

        try:
            counter_start = int(settings['counter_start'])
        except:
            counter_start = 1
        
        try: 
            counter_steps = int(settings['counter_steps'])
        except:
            counter_steps = 1
        
        logging.debug("counter_start: %s, counter_length: %s, counter_step: %s" % (counter_start, counter_length, counter_steps))
        for counter in xrange(counter_start,counter_length,counter_steps):
            try:
                date = lxml_data.xpath(construct_xpath(xpath['date'], counter)).strip()
            except:
                date = str(datetime.datetime.today().strftime("%d.%m.%Y"))
                # date = req.headers['date']
            time = lxml_data.xpath(construct_xpath(xpath['time'], counter)).strip()
            artist = lxml_data.xpath(construct_xpath(xpath['artist'], counter)).strip()
            title = lxml_data.xpath(construct_xpath(xpath['title'], counter)).strip()
            
            logging.debug("%s. [%s %s] %s - %s" % (counter, time, date, artist, title))
    
            playlist.append({'date':date, 'time': time, 'artist': artist, 'title': title})
    return playlist
    
def construct_xpath(xpath, number):
    repl = xpath.replace('%counter%', str(number))
    repl = 'string('+repl+')'
    logging.debug(repl)
    return repl
