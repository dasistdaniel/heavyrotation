#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import heavyrotation_parser as hr_parser
import datetime
from lxml import html

def parse_playlist(settings, xpath, html):
    settings['playlist_url'] = get_playlist_url(settings['url'])
    settings['type'] = 'html'
    
    playlist_data = hr_parser.parse_playlist(settings, xpath, html)
    return playlist_data
    
def get_playlist_url(url):
    root = html.parse(url)
    link = root.xpath("//a[@title='Die letzten 13 Titel auf SWR3']/@href")[0]
    return link
