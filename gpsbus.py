import mysql.connector
import requests
import time

mydb = mysql.connector.connect(
    host = "35.186.147.96",
    user = "root",
    passwd = "Tspwcrw42",
    database = "gpslocation"
)

def get_gpsBus():
    mycursor = mydb.cursor()
    response = requests.get("https://www.aismagellan.io/api/things/pull/0c065280-7164-11e9-96dd-9fb5d8a71344")
    busGps = response.json()
    count = 0
    mycursor.execute("insert into busgps(BusID, BusLat, BusLon) values( %s, %s, %s)", (str(busGps["BusID"]),str(busGps["Latitude"]), str(busGps["Longitude"])))
    mydb.commit()
    return

while True:
	get_gpsBus()
	time.sleep(2000)
