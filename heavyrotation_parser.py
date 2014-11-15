#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
from lxml import etree
import dateutil.parser
import datetime
import yaml
import os
import sys

def get_playlist(config):
    config = os.path.join(os.getcwd(), 'configs', config + '.yaml')
    if not os.path.isfile(config):
        sys.exit('ERROR: Configfile %s was not found' % config)
    else:
        settings = get_config(config)
        playlist = parse_playlist(settings['settings'],settings['xpath'])
        return playlist

def get_config(config):
    yaml_stream = open(config,'r')
    settings = yaml.load(yaml_stream)
    return settings

def parse_playlist(settings, xpath):
    playlist = []

    date = ''
    time = ''
    artist = ''
    title = ''
    duration = ''
    dt = ''

    if settings['playlist_type'] == 'html':
        root = html.parse(settings['playlist_url'])
    elif settings['playlist_type'] == 'xml':
        root = etree.parse(settings['playlist_url'])
    else:
        root = html.parse(settings['playlist_url'])
    count_from = int(xpath['count_from']) 
    count_to = int(root.xpath(xpath['count_to'])) - 1 

    for count in reversed(range(count_from, count_to)):
        if 'datetime' in xpath:
            dt =  root.xpath(construct_xpath(xpath['datetime'],count))[0].strip()
            if '+01' in dt: # Simpler Hack für DeltaRadio
                dt = str(dateutil.parser.parse(dt, ignoretz=True).replace(second=0) + datetime.timedelta(hours=1))
            else:
                dt = str(dateutil.parser.parse(dt, ignoretz=True).replace(second=0))

        if 'date' in xpath:
            date = root.xpath(construct_xpath(xpath['date'],count))[0].strip()
        else:
            date = str(datetime.date.today())

        if 'time' in xpath:
            time = root.xpath(construct_xpath(xpath['time'],count))[0].strip()
            time = time.replace('Uhr', '').replace('.', ':').strip()

        if 'artist' in xpath:
            artist = root.xpath(construct_xpath(xpath['artist'],count))[0].strip()

        if 'title' in xpath:
            title = root.xpath(construct_xpath(xpath['title'],count))[0].strip()

        if 'duration' in xpath:
            duration = root.xpath(construct_xpath(xpath['duration'],count))[0].strip()
            duration = get_seconds(duration)

        if not dt:
            dt = str((dateutil.parser.parse(date + ' ' + time)).replace(second=0))

        playlist.append({'datetime': dt, 'artist': artist, 'title': title, 'duration': duration})
    return playlist

def construct_xpath(xpath, number):
    if xpath:
        return xpath.replace('%counter%', str(number))
    else:
        return None

def get_seconds(t):
    seconds = sum(int(x) * 60 ** i for i,x in enumerate(reversed(t.split(":"))))
    if seconds > 150:
        return seconds
    else:
        return ''

def print_data(playlist):
    for track in playlist:
        print track['datetime'], track['artist'], track['title'],track['duration']

if __name__ == "__main__":
    if len(sys.argv) <> 2 :
        sys.exit('Usage: %s configfile' % sys.argv[0])
    else:
        print_data (get_playlist(sys.argv[1]))