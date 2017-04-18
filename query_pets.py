#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pets query"""


import sqlite3

conn = sqlite3.connect('pets.db')
print("Opened database successfully")
c = conn.cursor()


user_id=0

while user_id != -1:
	person_id = int(raw_input('Enter the person id: '))
	c.execute('SELECT * FROM person WHERE id=?', (person_id,))
	person_data = c.fetchall()
	if person_id == -1:
		break
	if len(person_data)!=0:
		for row in person_data:
			person_firstname = row[1]
			person_lastname = row[2]
			person_age = row[3]
			print(row[1] + ' '+ row[2] + ', ' + str(row[3]) + ' years old')

		c.execute('SELECT * FROM person_pet WHERE person_id=?', (person_id,))
		for pet_id_obj in c.fetchall() :
			c.execute('SELECT * FROM pet WHERE id=?', (pet_id_obj[1],))
			for row_ in c.fetchall():
				print(person_firstname + ' ' + person_lastname + ' owned ' + row_[1] + ' , a ' + row_[2] + ' , that was ' + str(row_[3]) + ' years old' )
	else:
		print('no such person')
