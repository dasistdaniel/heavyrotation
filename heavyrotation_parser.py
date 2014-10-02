#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
from dateutil import parser
from datetime import datetime

def parse_playlist(playlist_url, xpath):
    playlist = []
    root = html.parse(playlist_url)
    
    count_to = int(root.xpath(xpath['count_to'])) + 1
    
    count_from = int(xpath['count_from'])
    if count_to > 0:
        for x in reversed(range(count_from, count_to)):
            time_ = parser.parse(root.xpath(construct_xpath(xpath['time'],x))[0])
            
            date = time_.strftime('%Y-%m-%d')
            time = time_.strftime('%H:%M:%S')
            artist = root.xpath(construct_xpath(xpath['artist'],x))[0]
            title = root.xpath(construct_xpath(xpath['title'],x))[0]
            
            if xpath['duration']:
                duration = root.xpath(construct_xpath(xpath['duration'],x))[0]
            else:
                duration = ''
            
            playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title, 'duration': duration})
    return playlist
    
def construct_xpath(string, counter):
    return string.replace('%counter%', str(counter)) + '/text()'