#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Radio Bielefeld


from lxml import html
from datetime import date as dt

def parse_playlist(data):
    playlist = []

    root = html.fromstring(data)

    for x in range(2, 6):
        date = dt.today().strftime('%Y-%m-%d')
        time = root.xpath('//div[contains(@class, "playlist")]/table/tr['+str(x)+']/td[1]/text()')[0]
        title =  root.xpath('//div[contains(@class, "playlist")]/table/tr['+str(x)+']/td[4]/text()')[0]
        artist =  root.xpath('//div[contains(@class, "playlist")]/table/tr['+str(x)+']/td[3]/text()')[0]
        duration_ =  root.xpath('//div[contains(@class, "playlist")]/table/tr['+str(x)+']/td[2]/text()')[0].split(':')
        duration = int(duration_[0])*60*60 + int(duration_[1])*60 + int(duration_[2])
        
        if duration < 60:
            duration = ''
            
        playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title, 'duration': duration})
    return reversed(playlist)
    
