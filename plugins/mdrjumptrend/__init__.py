#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MDR Jump Live


from lxml import etree


def parse_playlist(data):
    playlist = []
    root = etree.fromstring(data)

    for x in range(1, 6):
        datetime = root.xpath("//TRANSMISSION/TAKE["+str(x)+"]/starttime/text()")[0].split(' ')
        date = datetime[0]
        time = datetime[1]
        artist = root.xpath("//TRANSMISSION/TAKE["+str(x)+"]/author/text()")[0]
        if ', ' in artist:
            artist_ = reversed(artist.split(','))
            artist = ' '.join(artist_).strip()

        title = root.xpath("//TRANSMISSION/TAKE["+str(x)+"]/title/text()")[0]
        duration_ = root.xpath("//TRANSMISSION/TAKE["+str(x)+"]/duration/text()")[0].split(':')
        duration = 60*60*int(duration_[0]) + 60*int(duration_[1]) + int(duration_[2])
        
        playlist.append({'date': date, 'time': time, 'artist': artist, 'title': title, 'duration': duration})
    return reversed(playlist)
