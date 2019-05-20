import time
import serial
import RPi.GPIO as gpio
import string
import re
import math
import os
import mysql.connector
import requests

gpio.setmode(gpio.BOARD)

port = "/dev/ttyAMA0" #serial port to which the pi is connected

#create a serial object

ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)

mydb = mysql.connector.connect(
    host = "35.186.147.96",
    user = "root",
    passwd = "Tspwcrw42",
    database = "gpslocation"
)
def get_gpsBus():
    mycursor = mydb.cursor()
    lat = ''
    lon = ''
    count = 0
    while True:
        try:
            data1 = ser.readline()
            data2 = str(data1)
        except:
            print("no detected")
        if data2.find("$GPGGA") != -1:
            loc = re.search('(.+),(.+),(.+),N,(.+),E',data2)

            lat = float(loc.group(3))
            lon = float(loc.group(4))

            lat1 = math.floor(lat/100)
            lon1 = math.floor(lon/100)

            lat2 = ((lat/100)-lat1)*100/60
            lon2 = ((lon/100)-lon1)*100/60

            lat = str(lat1+lat2)
            lon = str(lon1+lon2)
            print("Location: "+lat+","+lon)
            time.sleep(1)
            mycursor.execute("insert into busgps(BusID, Latitude, Longitude, ID) values( %s, %s, %s, null)", (int(1), str(lat), str(lon)))
            mydb.commit()
            time.sleep(3)

get_gpsBus()
