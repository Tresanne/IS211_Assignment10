#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""loading pets"""

import sqlite3

# Answer to Q1

conn = sqlite3.connect('pets.db')
print("Opened database successfully")

c = conn.cursor()

# Insert a row of data
try:
	c.execute("INSERT INTO person VALUES  (1, 'James', 'Smith', 41)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO person VALUES  (2, 'Diana', 'Greene', 23)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO person VALUES  (3,  'Sara', 'White', 27)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO person VALUES  (4, 'William', 'Gibson', 23)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO pet VALUES  (1, 'Rusty', 'Dalmation', 4, 1)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO pet VALUES  (2, 'Bella', 'Alaskan Malamute', 3, 0)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO pet VALUES  (3, 'Max', 'Cocker Spaniel', 1, 0)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO pet VALUES  (4, 'Rocky', 'Beagle', 7, 0)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO pet VALUES  (5, 'Rufus', 'Cocker Spaniel', 1, 0)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO pet VALUES  (6, 'Spot', 'Bloodhound', 2, 1)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO person_pet VALUES   (1,1)")
	conn.commit()
	print('inserted')
except:
	pass

try:
	c.execute("INSERT INTO person_pet VALUES   (1,2)")
	conn.commit()
	print('inserted')
except:
	pass

try:
	c.execute("INSERT INTO person_pet VALUES   (2,3)")
	conn.commit()
	print('inserted')
except:
	pass


try:
	c.execute("INSERT INTO person_pet VALUES   (2,4)")
	conn.commit()
	print('inserted')
except:
	pass
try:
	c.execute("INSERT INTO person_pet VALUES   (3,5)")
	conn.commit()
	print('inserted')
except:
	pass

try:
	c.execute("INSERT INTO person_pet VALUES   (4,6)")
	conn.commit()
	print('inserted')
except:
	pass


# Answer of Q2: person_pet table is linking the primary keys of person table and pets table
