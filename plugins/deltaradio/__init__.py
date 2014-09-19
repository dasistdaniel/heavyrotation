#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import datetime
from time import mktime

def parse_playlist(data):
    playlist = []
    root = feedparser.parse(data)
    for entry in root.entries:
        date = datetime.date.today().strftime('%Y-%m-%d')
        time = datetime.datetime.fromtimestamp(mktime(entry.published_parsed)).strftime('%H:%M:%S')
        artist = entry.artist
        title = entry.plain_title
        duration = entry.duration
        
<<<<<<< HEAD
        title = title.decode('unicode-escape').title()
        artist = artist.decode('unicode-escape').title()
=======
        title = title.title().decode('unicode-escape')
        artist = artist.title().decode('unicode-escape')
>>>>>>> 989fc441f6f6add8575d42d9bde4672fdf047f71
        
        playlist.append ( {'date':date, 'time':time,'artist':artist,'title':title,'duration':duration} )
    return playlist
