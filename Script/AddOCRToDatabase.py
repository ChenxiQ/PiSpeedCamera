import sqlite3

def addOCRToDatabase(speed, plate):
    def add_data(license, num):
        curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (license, num))
        conn.commit()
    
    conn = sqlite3.connect("/home/pi/PiWeb/Sensors_Database/test.db")
    curs = conn.cursor()
    add_data(plate, speed)
    conn.close()
