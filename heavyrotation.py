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
    availables = []
    sender = []
    parser = SafeConfigParser()

    # Welche Sektionen sind für ConfigParser auszulesen?
    for config in configs:
        availables.append(os.path.splitext(os.path.basename(config))[0])

    configdata = parser.read(configs)
    for sections in availables:
        sender.append(dict([('sender', sections)] + parser.items(sections)))
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
        configs = get_config_list()
        configs_descriptions = get_configs(configs)
        for sender in configs_descriptions:
            print sender['sender'] + "\t" + sender['sendername'] + "\t" + sender['kurzbeschreibung']
        sys.exit()
    
    print args