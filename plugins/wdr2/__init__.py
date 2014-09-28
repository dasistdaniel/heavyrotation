#!/usr/bin/env python
# -*- coding: utf-8 -*-
# WDR2

from lxml import html
from datetime import date as dt

def parse_playlist(data):
    playlist = []

    root = html.fromstring(data.encode('utf-8'))
    laenge = root.xpath(".//*[@id='searchPlaylistResult']/tbody/tr")

    for x in range(1, len(laenge)):
        date_time = root.xpath(".//*[@id='searchPlaylistResult']/tbody/tr["+str(x)+"]/th/text()")
        date_ = date_time[0].replace('.','-')[0:10].split('-')
        date = date_[2] + "-" + date_[1] + "-" + date_[0]
        time = date_time[1].replace('.',':')[0:5]+":00"
        title = root.xpath(".//*[@id='searchPlaylistResult']/tbody/tr["+str(x)+"]/td[1]/text()")[0].strip()
        artist =  root.xpath(".//*[@id='searchPlaylistResult']/tbody/tr["+str(x)+"]/td[1]/strong/text()")[0]
        duration = ''
   

        if len(title) > 0 and len(artist) > 0:
            playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title, 'duration': duration})
    return reversed(playlist)
