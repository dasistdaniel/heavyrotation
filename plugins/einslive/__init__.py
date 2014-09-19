#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import html
from datetime import date as dt


def parse_playlist(data):
    playlist = []
    root = html.fromstring(data)
    for x in range(1,13):
        date = dt.today().strftime('%Y-%m-%d')
        time = root.xpath(".//*[@id='wsContentArea']/table/tbody/tr["+str(x)+"]/td[1]/text()")[0]
        artist = root.xpath(".//*[@id='wsContentArea']/table/tbody/tr["+str(x)+"]/td[2]/text()")[0]
        title = root.xpath(".//*[@id='wsContentArea']/table/tbody/tr["+str(x)+"]/td[3]/text()")[0]
        duration = ''
       
        title = title.decode('unicode-escape').title()
        artist = artist.decode('unicode-escape').title()
        
        playlist.append ( {'date':date, 'time':time,'artist':artist,'title':title,'duration':duration} )
    return playlist