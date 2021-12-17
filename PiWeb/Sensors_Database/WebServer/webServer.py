'''
	webServer.py
 	Created by Kuan Lu   
	Build the server with Flask.
'''

from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3

# Retrieve data from database
def getData():
	conn=sqlite3.connect('/home/pi/PiWeb/Sensors_Database/test.db')
	curs=conn.cursor()
	time = []
	licensePlate = []
	speed = []
	for row in curs.execute("SELECT * FROM DHT_data ORDER BY timestamp DESC LIMIT 5"):
		time.append(str(row[0]))
		licensePlate.append(row[1])
		speed.append(row[2])
	conn.close()
	return time, licensePlate, speed 

# Upload the data to html 
@app.route("/")
def index():
	
	time, licensePlate, speed = getData()
	templateData = {
	  'time'	: time,
      'license'	: licensePlate,
      'speed'		: speed
	}
	return render_template('index.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=False)
