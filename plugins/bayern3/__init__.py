#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bayern 3


from lxml import html
from datetime import date as dt

def parse_playlist(data):
    playlist = []

    root = html.fromstring(data)
    laenge = len(root.xpath('.//*[@id="content"]/div[1]/div[2]/dl/dt'))
    for x in range(1, laenge+1):
        date = dt.today().strftime('%Y-%m-%d')
        time = root.xpath('.//*[@id="content"]/div[1]/div[2]/dl/dt['+str(x)+']/text()')[0] + ':00'
        artist = root.xpath('.//*[@id="content"]/div[1]/div[2]/dl/dd['+str(x)+']/ul/li/span[1]/text()')[0]
        title = root.xpath('.//*[@id="content"]/div[1]/div[2]/dl/dd['+str(x)+']/ul/li/span[2]/text()')[0]
        duration = ''
        
        playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title, 'duration': duration})
    return reversed(playlist)
