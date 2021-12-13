import sqlite3

conn = sqlite3.connect("/home/pi/PiWeb/Sensors_Database/test.db")
curs = conn.cursor()

def add_data(license, num):
    curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (license, num))
    conn.commit()

def addOCRToDatabase(speed, plate):
    add_data(plate, speed)

addOCRToDatabase(25, "ABCDEFGH")
conn.close()
