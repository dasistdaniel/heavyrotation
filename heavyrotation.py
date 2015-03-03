#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os.path
import json
import logging
import heavyrotation_parser

VER = 0.2
DEBUG = logging.CRITICAL
#DEBUG = logging.DEBUG

def print_help():
    print "heavyrotation %s" % VER
    print ""
    print "heavyrotation trys to parse the playlist data of different radio Websites"
    print "and outputs it as json"
    print ""
    print "Usage: %s configfile" % sys.argv[0]
    print ""
    
if __name__ == "__main__":
    logging.basicConfig(level=DEBUG)
    
    output = []
        
    logging.info ('checking arguments')
    if len(sys.argv) <> 2 :
        logging.info ('found %s arguments, needed 1' % (len(sys.argv) - 1))
        print_help()
        sys.exit()
    else:
        config_file = sys.argv[1]
        file = os.path.basename(config_file)
        logging.info ('check if "%s" exists"' % config_file)
        if os.path.isfile(config_file):
            logging.info ('file "%s" exists' % file)
            fileName, fileExtension = os.path.splitext(config_file)
            logging.info ('check if config is a .json file')
            if fileExtension == '.json':
                logging.info ('found .json extension')
                logging.info ('loading %s' % file)
                fh = open(config_file)
                config_data = json.load(fh)
                fh.close()
            else:
                logging.info ('wrong extension. found %s' %fileExtension)
                print "No recognised File Extension. Only .json files are allowed."
                sys.exit()
            
            logging.info ('Loading Parser')
            playlist = heavyrotation_parser.parse_playlist(config_data)
            logging.info ('Parsed Data: \n %s' %playlist)
            
            output.append({'informations':config_data['informations'], 'playlist' : playlist})
            print json.dumps(output,  sort_keys=True,indent=4, separators=(',', ': '))
        else: 
            logging.info ('"%s" does not exist"' % file)
            print "Could'n find the Configfile."
            sys.exit()