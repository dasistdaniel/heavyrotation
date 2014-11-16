#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import heavyrotation_parser
import heavyrotation_mysql
import json

def print_json(playlist):
    print json.dumps(playlist,sort_keys=True, indent=4, separators=(',', ': '))

def print_data(playlist):
    for track in playlist:
        print track['datetime'], track['artist'], track['title'],track['duration']

if __name__ == "__main__":
    if len(sys.argv) <> 2 :
        sys.exit('Usage: %s configfile' % sys.argv[0])
    else:
	shortname = sys.argv[1]
	settings = heavyrotation_parser.get_config(shortname)
	playlist = heavyrotation_parser.get_playlist(shortname)
        print_data(playlist)
	heavyrotation_mysql.add_entries(playlist, settings['settings'])
