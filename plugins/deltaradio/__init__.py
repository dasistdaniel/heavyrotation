#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser

def parse_playlist(data):
    playlist = []
    root = feedparser.parse(data)
    for entry in root.entries:
        date = ''
        time = ''
        artist = entry.artist
        title = entry.plain_title
        duration = entry.duration
        
        date = date.decode('unicode-escape')
        time = time.decode('unicode-escape')
        title = title.decode('unicode-escape')
        artist = artist.decode('unicode-escape')
        duration = duration.decode('unicode-escape')
        
        playlist.append ( {'date':date, 'time':time,'artist':artist,'title':title,'duration':duration} )
    return playlist