#! /usr/bin/env python



#The website for the Physical Pin out for Odroid XU4 is
#http://odroid.com/dokuwiki/doku.php?id=en:xu3_hardware_gpio


import math
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlutils.copy import copy
import numpy
import time
import top_block
import socket
import scipy
import gpslib.GPS_runner as GPS_runner
import gpiolib.wiringPi as wiringPi
import struct


#Define GPIO pins
ON     = 1
OFF    = 0
OUTPUT = 1
GPIO0  = 0 	# Physical pin 5
GPIO1  = 15	# Physical pin 8
GPIO2  = 21	# Physical pin 24
GPIO3  = 11	# Physical pin 20
GPIO4  = 2      # Physical pin 13
GPIO5  = 3      # physical pin 17
GPIO6  = 4      # Physcial pin 18
GPIO7  = 6      # Physcial pin 26
GPIO8  = 22     # Physcial pin 19
GPIO9  = 27     # Physical pin 15

# GPIO Pins by name
SWITCH = 15
NS     = 0
GND    = 21

# Set up the socket for the client, these are set Globally
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
port = 18999 # This is just a random port chosen to try to avoid a used one
serverIP = '192.168.130.100'


# Set up the GPIO pins, and make sure they are all set low initially
def initPins():
	wiringPi.wiringPiSetup();
	wiringPi.pinMode (GPIO0, OUTPUT)
	wiringPi.pinMode (GPIO1, OUTPUT)
	wiringPi.pinMode (GPIO2, OUTPUT)

    wiringPi.digitalWrite(NS, OFF)
    wiringPi.digitalWrite(SWITCH, OFF)
    wiringPi.digitalWrite(GPIO2, OFF)


def fileInit():
    with open('RXData.csv', 'w') as csvfile:
        csvfile.write("UTC,Lat,Long,Alt,FFT")
        csvfile.write("\n")
    csvfile.close()

def filewrite(data):
    path = '~/Documents/test'
    finalpath ='/home/user/Documents/test/RXData.csv'
    row_count = sum(1 for row in csv.reader( open('RXData.csv') ) )
    print row_count
    if row_count < 3:
        fd = open('RXData.csv','a')
        fd.write(data)
        fd.write("\n")
        fd.close()
    else:
		os.rename('RXData.csv','04-13-17.csv')
		fileInit()
		fd = open('RXData.csv','a')
		fd.write(data)
		fd.write("\n")
		fd.close()

def putToServer(cmd, buff):
    # First connect to the server, then send the message
    sock.connect((serverIP, port))
    sock.send(cmd)

    # Wait for the response from the server indicating it's ready
    while True:
        resp = ""
        resp = sock.recv(1024)
        print("RECIEVED " + resp)
        if resp[0:5] == "READY":

            # send the file
            sock.send(buff)
            break

        # Handle a server side error
        elif resp[0:5] == "ERROR":
            print("There was an error on the server.")
            break
        # Handle unknowns
        else:
            print("Didn't understand response")
            sock.send("ERROR 2")
        killClient()

def killClient():
        sock.send("QUIT")
        sock.close()

def buildMessage(rowdata, data):
        
	loc={
	        "version": "1.0.16",
	        "messageType": "Loc",
	        "sensorId": "101010101",
	        "sensorKey": 846859034,
	        "time": time.time(),
	        "mobility": "Stationary",
	        "environment": "Outdoor",
	        "latitude": float(rowdata[1]),
	        "longitude": float(rowdata[2]),
	        "altitude": float(rowdata[3]),
	        "timeZone": "America_Denver"
	}
    datastr={
			"version": "1.0.16",
	        "messageType": "Data",
	        "sensorId": "101010101",
	        "sensorKey": 846859034,
	        "time": time.time(),
	        "mobility": "Stationary",
	        "environment": "Outdoor",
	        "latitude": float(rowdata[1]),
	        "longitude": float(rowdata[2]),
	        "altitude": float(rowdata[3]),
	        "timeZone": "UTC",
			"data": data
}           
    return loc,datastr




if __name__ == "__main__":
	

	initPins()
	initFile()
	
	











	outFilename = "data.csv"
    cmd = "PUT " + outFilename
    putToServer(cmd, row)

    # Now wait to receive another response
    buff = sock.recv(1024)
    print("Received: " + buff)

    wiringPi.digitalWrite(GPIO0, OFF)
    wiringPi.digitalWrite(GPIO1, OFF)
    wiringPi.digitalWrite(GPIO2, OFF)












