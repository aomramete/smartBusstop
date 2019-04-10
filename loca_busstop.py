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
                stop1 = 'no.1'
                stop2 = 'no.2'
                stop3 = 'no.3'
                stop4 = 'no.4'
                return jsonify([{'Bus stop' : stop1,'Lat': stop1_lat,'Lon': stop1_lon},{'Bus stop' : stop2,'Lat': stop2_lat,'Lon': stop2_lon},{'Bus stop' : stop3,'Lat': stop3_lat,'Lon': stop3_lon},{'Bus stop' : stop4,'Lat': stop4_lat,'Lon': stop4_lon}])
api.add_resource(stop_loca, '/stoplocation')
if __name__ == '__main__':
     app.run(host = '0.0.0.0', port='8080', threaded=True, debug=True)
