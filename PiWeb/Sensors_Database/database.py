'''
	database.py
 	Created by Kuan Lu   
	Creat database with SQLite.
'''

import sqlite3 as lite
import sys
con = lite.connect('test.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS data")
    cur.execute("CREATE TABLE DHT_data(timestamp DATETIME, license TEXT, speed NUMERIC)")
