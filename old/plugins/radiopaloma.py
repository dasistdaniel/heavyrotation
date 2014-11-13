#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import heavyrotation_parser as hr_parser
import datetime

def parse_playlist(settings, xpath, html):
    html = get_html(settings['playlist_url'])
    playlist_data = hr_parser.parse_playlist(settings, xpath, html)
    return playlist_data
    
def get_html(url):
    dt_ = datetime.datetime.now()
    post_data = {'Vorschau':'Suchen', 's_day':'0', 's_min':dt_.minute, 's_month':dt_.month, 's_std':dt_.hour,'s_year':dt_.year}
    r = requests.post(url, data=post_data)
    return r.content
