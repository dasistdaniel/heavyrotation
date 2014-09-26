#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HR4


from lxml import html

def parse_playlist(data):
    playlist = []

    root = html.fromstring(data)

    laenge = len(root.xpath('//tr'))
    for x in range(3, laenge):
        date_ = root.xpath("//tr["+str(x)+"]/td[1]/text()")[0].split('.')
        date = date_[2] + "-" + date_[1] + "-" + date_[0]
        time = root.xpath("//tr["+str(x)+"]/td[2]/text()")[0] + ':00'
        artist = root.xpath("//tr["+str(x)+"]/td[3]/text()")[0]
        title = root.xpath("//tr["+str(x)+"]/td[4]/text()")[0]
        duration = ''
        
        playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title, 'duration': duration})
    return reversed(playlist)
