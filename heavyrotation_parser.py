#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html,etree
from dateutil import parser

def parse_playlist(settings, xpath, html_source):
    playlist_url = settings['playlist_url']
    type = settings['type']
    
    playlist = []
    if type == 'html':
        root = html.parse(playlist_url)
    elif type == 'xml':
        root = etree.parse(playlist_url)
    elif type == 'plugin_html':
        root = html.fromstring(html_source)
    elif type == 'plugin_xml':
        root = etree.fromstring(html_source)


    count_to = int(root.xpath(xpath['count_to'])) + 1
    count_from = int(xpath['count_from'])


    
    if count_to > 0:
        for x in reversed(range(count_from, count_to)):
            time_ = root.xpath(construct_xpath(xpath['time'],x))[0].replace('Uhr','')
            time_ = parser.parse(time_)
            
            date = time_.strftime('%Y-%m-%d')
            time = time_.strftime('%H:%M:%S')
            artist = root.xpath(construct_xpath(xpath['artist'],x))[0]
            title = root.xpath(construct_xpath(xpath['title'],x))[0]

            if xpath['duration']:
                duration = root.xpath(construct_xpath(xpath['duration'],x))[0]
                if not ':' in duration:
                    duration = duration_convert(int(duration))
            else:
                duration = ''
            
            playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title, 'duration': duration})
    return playlist
    
def construct_xpath(string, counter):
    return string.replace('%counter%', str(counter)) + '/text()'
    
def duration_convert(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)