#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from time import sleep
import importlib

import heavyrotation_configs as hr_configs
import heavyrotation_parser as hr_parser
import heavyrotation_database as hr_database

import sys

def print_list(settings):
    config =  {}
    for setting in settings:
        config['shortname'] =  setting[0:-7]
        config['name'] = settings[setting]['settings']['sendername']
        config['short_description'] = settings[setting]['settings']['kurzbeschreibung']
        config['url'] = settings[setting]['settings']['url']
        
        print ('%s\t%s\t%s\t%s\t' % (calc_tabs(config['shortname']), config['name'], config['short_description'], config['url']))
        
def calc_tabs(string):
    if len(string) < 8:
        return string + '\t'
    else:
        return string
        
def get_playlist(config_file):
    config = hr_configs.read_configs([config_file])[config_file]
    if not config['settings']['type'] == 'plugin_html' or config['settings']['type'] == 'plugin_xml':
        playlist_data = hr_parser.parse_playlist(config['settings'], config['xpath'],None)
    else:
        plugin = importlib.import_module("plugins." + config['settings']['plugin'])
        playlist_data = plugin.parse_playlist(config['settings'], config['xpath'], None)
        
    hr_database.database_save(config['settings']['dbname'], playlist_data, args.database)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(__file__, description='heavyrotation, get data of played songs from differnt radio station websites', epilog='programmed by dasistdaniel')
    parser.add_argument('--version', action='version', version='%(prog)s 0.5')
    parser.add_argument('stations', help=u'which station config should be loaded? See --list', nargs='*')
    parser.add_argument('-l', '--list', help='list all stations', action='store_true')
    parser.add_argument('-a', '--all', help=u'use all availabe station', action='store_true')
    parser.add_argument('--printonly', help=u'only show the data, don\'t save it to the database', action='store_true')
    parser.add_argument('-db', '--database', help=u'which database file should be used', action='store', default='database/heavyrotation.sqlite')
    parser.add_argument('--loop', help=u'simple loop daemon mode', action='store_true')
    args = parser.parse_args()

    if args.list:
        config_files = hr_configs.list_configs()
        config_settings = hr_configs.read_configs(config_files)
        print_list(config_settings)
        
    if args.stations:
        for station in args.stations:
            config_file = station + '.config'
            try:
                get_playlist(config_file)
            except:
                e = sys.exc_info()
                print e 
                print "Could not parse Station: " + station
            
    if args.all:
        config_files = hr_configs.list_configs()
        for config_file in config_files:
            try:
                get_playlist(config_file)
            except:
                print "Could not parse Station: " + config_file
            
    if args.loop:
        config_files = hr_configs.list_configs()
        while True:
            for config_file in config_files:
                try:
                    get_playlist(config_file)
                except:
                    print "Could not parse Station: " + config_file
            print 'wait for 5 minutes'
            sleep(300)
