#!/usr/bin/python
import MySQLdb

def db_connect():
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="McoKztr5", # your password
                      db="heavyrotation") # name of the data base

    cur = db.cursor()
    return db, cur

def db_close(db, cur):
    cur.close()
    db.close()

def get_station_id(cur, settings):
    shortname = settings['shortname']
    print shortname
    cur.execute("SELECT id FROM stations WHERE shortname = %s", shortname)
    try:
        station_id = cur.fetchone()[0]
    except:
	cur.execute("INSERT INTO stations (shortname, name, description, base_url, playlist_url) VALUES(%s, %s, %s, %s, %s)", (settings['shortname'], settings['stationname'], settings['description'], settings['baseurl'], settings['playlist_url'])) 
        station_id = cur.lastrowid
    return station_id

def get_title_id(cur, title):
    cur.execute("SELECT id from titles WHERE title = %s", title)
    try:
        title_id = cur.fetchone()[0]
    except:
	cur.execute("INSERT INTO titles (title) VALUES (%s)", title)
        title_id = cur.lastrowid
    return title_id

def get_artist_id(cur, artist):
    cur.execute("SELECT id from artists WHERE artist = %s", artist)
    try:
        artist_id = cur.fetchone()[0]
    except:
	cur.execute("INSERT INTO artists (artist) VALUES (%s)", artist)
        artist_id = cur.lastrowid
    return artist_id

def get_track_id(cur, title_id, artist_id, duration):
    cur.execute("SELECT id FROM tracks WHERE title_id = %s AND artist_id = %s", (title_id, artist_id))

    try:
        track_id = cur.fetchone()[0]
    except:
        try:
            duration = int(duration)
        except:
            duration = 0
	cur.execute("INSERT INTO tracks (title_id, artist_id, duration) VALUES (%s, %s, %s)", (title_id, artist_id, duration))
        track_id = cur.lastrowid
    return track_id


def get_playlist_id(cur, datetime, station_id, track_id):
    cur.execute("SELECT id FROM playlist WHERE datetime = %s AND station_id = %s", (datetime, int(station_id)))

    try:
        playlist_id = cur.fetchone()[0]
    except:
        cur.execute("INSERT INTO playlist (datetime, station_id, track_id) VALUES (%s, %s, %s)", (datetime, station_id, track_id))
        playlist_id = cur.lastrowid
    return playlist_id


def add_entries(entries, station):
    db, cur = db_connect()

    station_id = get_station_id(cur, station)

    for entry in entries:
        title_id = get_title_id(cur, entry['title'])
        artist_id = get_artist_id(cur, entry['artist'])
        track_id = get_track_id(cur, title_id, artist_id, entry['duration'])
        playlist_id = get_playlist_id(cur, entry['datetime'], station_id, track_id)  

        print station_id, title_id, artist_id, track_id, playlist_id 
    db_close(db,cur)
