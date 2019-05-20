from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from math import sin, cos, sqrt, atan2, radians
import random
import json
from flaskext.mysql import MySQL

app = Flask(__name__)
CORS(app)
api = Api(app)
mysql = MySQL()

import requests
import time

#MySQLconfig
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Tspwcrw42'
app.config['MYSQL_DATABASE_DB'] = 'gpslocation'
app.config['MYSQL_DATABASE_HOST'] = '35.186.147.96'
mysql.init_app(app)

@app.route('/busgps/')
def allsensors():
    cur = mysql.connect().cursor()
    cur.execute("select BusID,Latitude, Longitude from busgps order by ID desc limit 1;")
    data = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    for coor in data:
	lat = coor["Latitude"]
	lon = coor["Longitude"]
	return jsonify({"coordinate": [lat, lon]})

@app.route('/stops/<ID>')
def stops_byNum(ID=None):
    cur = mysql.connect().cursor()
    cur.execute("SELECT * FROM stoploc WHERE ID = %s", ID)
    data = [dict((cur.description[i][0], value)
	for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(data)

@app.route('/busstop/<ID>')
def get(ID):
		cur = mysql.connect().cursor()
		cur.execute("select * from busgps JOIN stoploc on stoploc.ID = (select ID from stoploc where ID = %s) order by busgps.ID desc limit 1;", ID)
              	data = [dict((cur.description[i][0], value)
              		for i, value in enumerate(row)) for row in cur.fetchall()]
		for coor in data:
			R = 6373.0 
			LatStop = float(coor["StopLat"]) 
			LonStop = float(coor["StopLon"])
                	lat2 = radians(LatStop)
                	lon2 = radians(LonStop)
			LatBus = float(coor["Latitude"])
			LonBus = float(coor["Longitude"])
                	lat1 = radians(LatBus)
                	lon1 = radians(LonBus)
                	dlon = lon2 - lon1
                	dlat = lat2 - lat1
                	a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
                	c = 2 * atan2(sqrt(a), sqrt(1-a))
                	distance = R * c
               		meter = distance*1000
        # Define speed and times
                	avgspeed = 2.78 # 10 km/h convert to m/s
			print ("---")
			print (meter)
                	time = (meter/avgspeed)/60
                	time = int(time)
        #4      return "Estimated arriving time: ", time
                	busstopno = coor["Latitude"],coor["Longitude"]
			dest = (coor["StopName"])
             	return jsonify({'Location of bus stop' : busstopno},{'Destination': dest},{'Arrival time in mins': str(time)})

if __name__ == '__main__':
     app.run(host = '0.0.0.0', port='8080', threaded=True, debug=True)
