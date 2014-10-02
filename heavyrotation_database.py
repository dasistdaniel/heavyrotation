#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as sqlite
import os.path


def database_create(db_file):
    conn = sqlite.connect(db_file)
    c = conn.cursor()

    c.execute('''CREATE TABLE `title` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,`title` TEXT NOT NULL,`artist` INTEGER NOT NULL,`duration` INTEGER);''')
    c.execute('''CREATE TABLE `sender` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name` INTEGER NOT NULL UNIQUE);''')
    c.execute('''CREATE TABLE `playlist` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `sender_id` INTEGER NOT NULL, `title_id` INTEGER NOT NULL, `date` INTEGER NOT NULL, `time` INTEGER NOT NULL);''')
    c.execute('''CREATE TABLE `artist` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `artist` TEXT NOT NULL);''')

    conn.commit()
    conn.close()


def database_save(sender, daten,db_file):
    if not os.path.isfile(db_file):
        database_create(db_file)
        
    conn = sqlite.connect(db_file)
    c = conn.cursor()

    c.execute('SELECT id, name FROM sender WHERE name = ?', (sender,))
    sender_exist = c.fetchone()

    if sender_exist is None:
        c.execute('INSERT INTO sender (name) VALUES (?)', (sender,))
        sender_id = c.lastrowid
    else:
        sender_id = sender_exist[0]

    for data in daten:
        data['title'] = data['title'].title()
        data['artist'] = data['artist'].title()
        c.execute('SELECT id FROM playlist WHERE sender_id = ? AND date = ? AND time = ?', (sender_id, data['date'], data['time'],))
        playlist_exist = c.fetchone()
        if playlist_exist is None:
            c.execute('SELECT id FROM artist WHERE artist = ?', (data['artist'],))
            artist_exist = c.fetchone()
            if artist_exist is None:
                c.execute('INSERT INTO artist (artist) VALUES(?)', (data['artist'],))
                artist_id = c.lastrowid
            else:
                artist_id = artist_exist[0]

            c.execute('SELECT id, duration FROM title WHERE title = ?', (data['title'],))
            title_exist = c.fetchone()
            if title_exist is None:
                c.execute(
                    'INSERT INTO title (title, artist, duration) VALUES (?, ?, ?)',
                    (data['title'],
                     artist_id,
                     data['duration'],
                     ))
                title_id = c.lastrowid
            else:
                title_id = title_exist[0]
                duration = title_exist[1]
                if not duration and data['duration']:
                    c.execute('UPDATE title SET duration = ? WHERE id = ?', (data['duration'], title_id,))

            c.execute('INSERT INTO playlist (sender_id, title_id, date, time) VALUES (?, ?, ?, ?)', (sender_id, title_id, data['date'], data['time']))
            print '[n] %s [%s - %s] %s - %s [%s]' % (sender, data['date'], data['time'], data['artist'], data['title'], data['duration'])
        else:
            print '[o] %s [%s - %s] %s - %s [%s]' % (sender, data['date'], data['time'], data['artist'], data['title'], data['duration'])

    conn.commit()
    conn.close()

