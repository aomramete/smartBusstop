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
app.config['MYSQL_DATABASE_DB'] = 'stoploca'
app.config['MYSQL_DATABASE_HOST'] = '35.186.147.96'
mysql.init_app(app)

@app.route('/allstops/')
def allsensors():
    cur = mysql.connect().cursor()
    cur.execute("select Name,Latitude,Longitude from stoploc")
    data = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(data)

@app.route('/stops/<ID>')
def stops_byNum(ID=None):
    cur = mysql.connect().cursor()
    cur.execute("SELECT * FROM stoploc WHERE ID = %s", ID)
    data = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(data)

class busstop1(Resource):
        def get(self):
                R = 6373.0 
                lat1 = radians(13.727154)
                lon1 = radians(100.774713)
                lat2 = radians(13.727208)
                lon2 = radians(100.776801)
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
                c = 2 * atan2(sqrt(a), sqrt(1-a))
                distance = R * c
                meter = distance*1000
        # Define speed and times
                speed = meter/300 # 300 is seconds (arriving in time)
                time = (meter/speed)/60
                time = int(time)
        #4      return "Estimated arriving time: ", time
                busstopno = 'Smart bus Stop (Gas station)' 
                return jsonify({'name' : busstopno},{'Destination': 'Bus stop - Port'},{'time': str(time)})
                
class busstop2(Resource):
        def get(self):
                R = 6373.0
                lat1 = radians(13.727208)
                lon1 = radians(100.776801)
                lat2 = radians(13.726481)
                lon2 = radians(100.776855)
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
                c = 2 * atan2(sqrt(a), sqrt(1-a))
                distance = R * c
                meter = distance*1000
        # Define speed and times
                speed = meter/150 # 150 is seconds (arriving in time)
                time = (meter/speed)/60
                time = int(time)
        #4      return "Estimated arriving time: ", time
                busstopno = 'Smart bus Stop (Port)'
                return jsonify({'name' : busstopno},{'Destination': 'Bus stop - Companies'},{'time': { 'Estimated arriving time in minutes' : str(time) }})


class busstop3(Resource):
        def get(self):
                R = 6373.0
                lat1 = radians(13.726481)
                lon1 = radians(100.776855)
                lat2 = radians(13.726424)
                lon2 = radians(100.774677)
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
                c = 2 * atan2(sqrt(a), sqrt(1-a))
                distance = R * c
                meter = distance*1000
        # Define speed and times
                speed = meter/450 # 450 is seconds (arriving in time)
                time = (meter/speed)/60
                time = int(time)
        #4      return "Estimated arriving time: ", time
                busstopno = 'Companies' 
                return jsonify({'name' : busstopno},{'Destination': 'Bus stop - Hospital'},{'time': { 'Estimated arriving time in minutes' : str(time) }})


class busstop4(Resource):
        def get(self):
                R = 6373.0
                lat1 = radians(13.726424)
                lon1 = radians(100.774677)
                lat2 = radians(13.727154)
                lon2 = radians(100.774713)
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
                c = 2 * atan2(sqrt(a), sqrt(1-a))
                distance = R * c
                meter = distance*1000
        # Define speed and times
                speed = meter/200 # 200 is seconds (arriving in time)
                time = (meter/speed)/60
                time = int(time)
        #4      return "Estimated arriving time: ", time
                busstopno = 'Hospital' 
                return jsonify({'name' : busstopno},{'Destination': 'Bus stop - Gas station'},{'time':{'Estimated arriving time in minutes' : str(time)}})

@app.route('/busstops/<ID>')
def get_latbus(ID=None):
	url = "http://104.196.38.182:8080/stops/" + ID
	response = requests.get(str(url))
        ID = response.json()
	data = []
	for i in ID:
		new_data = {'Latitude': ID[i]["Latitude"],'Longitude': ID[i]["Longitude"]}
		data.append(new_data)
	return json.dumps(data)

api.add_resource(busstop1, '/gasstation')
api.add_resource(busstop2, '/port')
api.add_resource(busstop3, '/companies')
api.add_resource(busstop4, '/hospital')
if __name__ == '__main__':
     app.run(host = '0.0.0.0', port='8080', threaded=True, debug=True)
