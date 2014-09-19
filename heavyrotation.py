#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import sys
import urllib2
import importlib
from ConfigParser import SafeConfigParser
from lxml import html
import sqlite3 as sqlite
 
def get_config_list():
    configs=[]
    for root, dirs, files in os.walk("./plugins"):
        for file in files:
            if file.endswith('config.ini'):
                datei = os.path.abspath(os.path.join(root, file))
                configs.append(datei)
    return configs
 
def get_configs(configs):
    sender = []
    parser = SafeConfigParser()
    
    # Welche Sektionen sind für ConfigParser auszulesen?
    for config in configs:
        shortname = os.path.split(config)[0].split('/').pop()
        shortname = os.path.split(shortname)[1]
        
        configdata = parser.read(config)
        sender.append(dict([('shortname',shortname)] + parser.items('settings')))
    return sender
    
def get_playlist(sender):
    path = os.path.abspath('./plugins/' + sender + '/config.ini')
    if os.path.isfile(path):
        parser = SafeConfigParser()
        configdata = parser.read(path)
        config = dict(parser.items('settings'))
        
        if config['playlist_url_style'] == 'dynamic':
            config['playlist_url'] = search_playlist_url(config['url'],config['playlist_url_search'])
        data = get_html(config['playlist_url'])
        
        mod = importlib.import_module("plugins." + sender)
        
        daten = mod.parse_playlist(data)
            
        for data in daten:
            print '%s [%s - %s] %s - %s [%s]' % (sender, data['date'], data['time'], data['artist'], data['title'], data['duration']) 
        
        if not args.printonly:
            if not os.path.isfile(args.database):
                database_create()
            
            database_save(sender,daten)
 
def search_playlist_url(url,search):
    data = get_html(url)
    root = html.fromstring(data)
    search = search.strip()
    
    found = str(root.xpath('//a[contains(.,"'+search+'")]/@href')[0])

    if found.startswith('http'):
        return found
    else:
        return url + found
    
def get_html(url):
        return urllib2.urlopen(url).read()

def database_create():
    print "lege neue db an"
    conn = sqlite.connect(args.database)
    c = conn.cursor()

    c.execute('''CREATE TABLE `title` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,`title` TEXT NOT NULL,`artist` INTEGER NOT NULL,`duration` INTEGER);''')
    c.execute('''CREATE TABLE `sender` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name` INTEGER NOT NULL UNIQUE);''')
    c.execute('''CREATE TABLE `playlist` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `sender_id` INTEGER NOT NULL, `title_id` INTEGER NOT NULL, `date` INTEGER NOT NULL, `time` INTEGER NOT NULL);''')
    c.execute('''CREATE TABLE `artist` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `artist` TEXT NOT NULL);''')

    conn.commit()
    conn.close()
    
def database_save(sender, daten):
    conn = sqlite.connect(args.database)
    c = conn.cursor()


    # Check ob Sender schon in der Datenbank ist 
    c.execute('SELECT id, name FROM sender WHERE name = ?', (sender,))
    sender_exist = c.fetchone()
    
    if sender_exist is None:
        c.execute('INSERT INTO sender (name) VALUES (?)', (sender,))
        sender_id = c.lastrowid
    else:
        sender_id = sender_exist[0]
        
        
    # print sender_id
    
    for data in daten:
        pass
    
    conn.commit()
    conn.close()
    
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(__file__, description='HeavyCharts, aggregriert Senderplaylisten und speichert sie ab.')
    parser.add_argument('sender', help=u'Shortname des Senders (siehe --list)', nargs='*')
    parser.add_argument('-l', '--list', help='Liste der Sender ausgeben', action='store_true')
    parser.add_argument('-a', '--all', help=u'Alle verfügbaren Sender abrufen', action='store_true')
    parser.add_argument('--printonly', help=u'Daten nur anzeigen, nicht in der Datenbank speichern', action='store_true')
    parser.add_argument('-d', '--database', help=u'Welche Datenbank Datei soll genutzt werden.', action='store', default='database/heavyrotation.sqlite')
    
    args = parser.parse_args()
    
    if len(args.sender) != 0:
        for sender in args.sender:
            playlist = get_playlist(sender)
        sys.exit()
        
    if args.all == True:
        configs = get_config_list()
        configs_descriptions = get_configs(configs)
        for sender in configs_descriptions:
            playlist = get_playlist(sender['shortname'])
        sys.exit()
        
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