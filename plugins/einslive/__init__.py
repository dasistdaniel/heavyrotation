#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import html

def parse_playlist(data):
    playlist = []
    root = html.fromstring(data)
    for x in range(1,13):
        uhrzeit = root.xpath(".//*[@id='wsContentArea']/table/tbody/tr["+str(x)+"]/td[1]/text()")
        interpret = root.xpath(".//*[@id='wsContentArea']/table/tbody/tr["+str(x)+"]/td[2]/text()")
        titel = root.xpath(".//*[@id='wsContentArea']/table/tbody/tr["+str(x)+"]/td[3]/text()")
        playlist.append({'uhrzeit':uhrzeit , 'interpret':interpret, 'title':titel})
        
    return playlist