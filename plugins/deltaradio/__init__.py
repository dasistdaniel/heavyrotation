#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser

def parse_playlist(data):
    playlist = []
    root = feedparser.parse(data)
    # for entry in root.entries:
        # print entry.artist
        # print entry.plain_title
        # print entry.duration
        # print entry.published_parsed
    return playlist