#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""music"""

import sqlite3

conn = sqlite3.connect('music.sql')
print("Opened database successfully")

c = conn.cursor()
# Create table
try:
	c.execute('''CREATE TABLE ArtistTracks
             		(Artist text, Album text, SongName text, TrackNumber real, LengthInSeconds real)''')
	print('table created successfully')
except sqlite3.OperationalError:
	print('table already present')
c.close()
