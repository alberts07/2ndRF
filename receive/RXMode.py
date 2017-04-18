#! /usr/bin/env python



#The website for the Physical Pin out for Odroid XU4 is
#http://odroid.com/dokuwiki/doku.php?id=en:xu3_hardware_gpio

import math
import numpy
import time
import top_block
import socket
import scipy

import struct
import gpslib.GPS_runner as GPS_runner
import gpiolib.wiringPi as wiringPi

import gzip
import shutil

from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlutils.copy import copy


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
	wiringPi.wiringPiSetup()
	wiringPi.pinMode (GPIO0, OUTPUT)
	wiringPi.pinMode (GPIO1, OUTPUT)
	wiringPi.pinMode (GPIO2, OUTPUT)

    wiringPi.digitalWrite(NS, OFF)
    wiringPi.digitalWrite(SWITCH, OFF)
    wiringPi.digitalWrite(GPIO2, OFF)


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


if __name__ == "__main__":

    # gpsinfo = GPS_runner.runner()  # gpsinfo = [str(MSODobject.timestamp), MSODobject.lat, MSODobject.lon, MSODobject.altitude]

    gpsinfo = "GPS data goes right here"
    gpsinfo = gpsinfo + "\n\r"
    data = numpy.fromfile("RXfile")
    outFilename = "data.csv"


    with open(outFilename, 'wb') as csvfile:
        csvfile.write(gpsinfo)
        csvfile.write("\n")
        csvfile.write(data)


    cmd = "PUT " + outFilename
    putToServer(cmd, data)

    # Now wait to receive another response
    buff = sock.recv(1024)
    print("Received: " + buff)

    wiringPi.digitalWrite(GPIO0, OFF)
    wiringPi.digitalWrite(GPIO1, OFF)
    wiringPi.digitalWrite(GPIO2, OFF)
