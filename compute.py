from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from math import sin, cos, sqrt, atan2, radians
import random
import json

app = Flask(__name__)
api = Api(app)

import requests
import time


class stop_loca(Resource):
        def get(self):
                stop1_lat = 13.727154
                stop1_lon = 100.774713
                stop2_lat = 13.727208
                stop2_lon = 100.776801
                stop3_lat = 13.726471
                stop3_lon = 100.776849
                stop4_lat = 13.726429
                stop4_lon = 100.774671
                stop1 = 'Companies'
                stop2 = 'Gas station'
                stop3 = 'Hospital'
                stop4 = 'Port'
                return jsonify([{'Bus stop' : stop1,'Lat': stop1_lat,'Lon': stop1_lon},{'Bus stop' : stop2,'Lat': stop2_lat,'Lon': stop2_lon},{'Bus stop' : stop3,'Lat': stop3_lat,'Lon': stop3_lon},{'Bus stop' : stop4,'Lat': stop4_lat,'Lon': stop4_lon}])


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
                return jsonify({'name' : busstopno},{'Destination': 'Bus stop - Port'},{'time': { 'Estimated arriving time in minutes' : str(time) }})
                
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

api.add_resource(busstop1, '/gasstation')
api.add_resource(busstop2, '/port')
api.add_resource(busstop3, '/companies')
api.add_resource(busstop4, '/hospital')
if __name__ == '__main__':
     app.run(host = '0.0.0.0', port='8080', threaded=True, debug=True)
