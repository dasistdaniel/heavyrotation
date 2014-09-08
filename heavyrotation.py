#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import sys
from ConfigParser import SafeConfigParser

def get_config_list():
    configs=[]
    for root, dirs, files in os.walk(".\plugins"):
        for file in files:
            if file.endswith('.ini'):
                datei = os.path.abspath(os.path.join(root, file))
                configs.append(datei)
    return configs
 
def get_configs(configs):
    sender = []
    parser = SafeConfigParser()
    
    # Welche Sektionen sind für ConfigParser auszulesen?
    for config in configs:
        configdata = parser.read(config)
        sender.append(dict(parser.items('settings')))
    return sender
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(__file__, description='HeavyCharts, aggregriert Senderplaylisten und speichert sie ab.')
    parser.add_argument('sender', help=u'Shortname des Senders (siehe --list)', nargs='*')
    parser.add_argument('-l', '--list', help='Liste der Sender ausgeben', action='store_true')
    parser.add_argument('-a', '--all', help=u'Alle verfügbaren Sender abrufen', action='store_true')
    
    args = parser.parse_args()
           
    if args.list == True:
        print u'Verfügbare Sender:'
        print 
        print 'Shortname\tName\t\tKurzbeschreibung'
        print '---------------------------------------------------------------------------'
        configs = get_config_list()
        configs_descriptions = get_configs(configs)
        # print configs_descriptions
        for sender in configs_descriptions:
            print sender['shortname'] + "\t" + sender['sendername'] + "\t" + sender['kurzbeschreibung']
        sys.exit()
   
    print args