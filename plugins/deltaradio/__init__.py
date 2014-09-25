#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import datetime

def parse_playlist(data):
    playlist = []
    items = json.loads(data)
    
    for item in items:
        artist = item['artist'].title()
        title = item['plain_title'].title()
        duration = item['duration']
        date = datetime.datetime.fromtimestamp(item['date']).strftime('%Y-%m-%d')
        time =  datetime.datetime.fromtimestamp(item['date']).strftime('%H:%M:%S')
        
        playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title, 'duration': duration})
    return reversed(playlist)