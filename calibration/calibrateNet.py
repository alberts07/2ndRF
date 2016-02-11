#! /usr/bin/env python
#Need to initialize power measurements with the noise diode off Look into whether order matters
# Then turn the noise diode on and wait
# Now initialize power measurements with noise diode on
# Divide the power of it on by the power of it off to get the Y FAct.
# Calculate NF by taking ENR and subtracting 10log(Yfac-1)
# ENR is  30db but will be calculated when parts in
import math
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlutils.copy import copy
import GPS_runner
import numpy
import time
import top_block
import socket
import time
import wiringPi

#This is the website for the Physical Pin out for Odroid XU4
#http://odroid.com/dokuwiki/doku.php?id=en:xu3_hardware_gpio

#Define 4 GPIO pins

ON     = 1
OFF    = 0
OUTPUT = 1
GPIO0  = 0 	# Physical pin 5
GPIO1  = 15	# Physical pin 8
GPIO2  = 21	# Physical pin 24
GPIO3  = 11	# Physical pin 20
GPIO4  = 2  # Physical pin 13
GPIO5  = 3  # physical pin 17
GPIO6  = 4  # Physcial pin 18
GPIO7  = 6  # Physcial pin 26
GPIO8  = 22 # Physcial pin 19
GPIO9  = 27 # Physical pin 15


#from datetime import datetime

# todo update to actual file location when I can.
# todo update ENR when we know it
# todo place try except block

def readBinFile(file):

    data = numpy.fromfile(file)
    return data.mean()

def runGNU(top_block_file):

    top_block_file.main()


def NoiseFig(N2,N1):
    ENR=14.85
    N2lin = 10**(N2/10)
    N2lin  = 2 ################### DIPSHIT REMOVE THIS
    N1lin = 10**(N1/10)
    YF=N2lin/N1lin
    NF= ENR-10*math.log(YF-1,10)
    gpsinfo = None
    while gpsinfo == None:
        gpsinfo = GPS_runner.runner()
    gpsinfo.append(NF)
    return gpsinfo



def putToServer(cmd, buff):
    # First connect to the server, then send the message
    sock.connect((serverIP, port))
    sock.send(cmd)

    # Wait for the response from the server indicating it's ready to receive
    while True:
        resp = ""
        resp = sock.recv(1024)

        if resp[0:5] == "READY":

            # print("sending: " + buff)
            
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


def killClient():
    sock.send("QUIT")
    sock.close()


def initPins():	
	wiringPi.wiringPiSetup();
	wiringPi.pinMode (GPIO0, OUTPUT)
	# wiringPi.pinMode (GPIO1, OUTPUT)
	# wiringPi.pinMode (GPIO2, OUTPUT)
	# wiringPi.pinMode (GPIO3, OUTPUT)


# Set up the socket for the client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
port = 18999 # This is just a random port chosen to try to avoid other used ones
serverIP = '192.168.130.100'

if __name__ == "__main__":

    initPins()
    wiringPi.digitalWrite(GPIO0, OFF)

    
    print("The noise with the noise source off will now be calculated")
    #Call SDR
    runGNU(top_block)
    #Ends in the script

    N1 = readBinFile("Power")

    # The system should turn the noise source on now
    raw_input("Press ENTER to start the noise source and continue")
    wiringPi.digitalWrite(GPIO0, ON)
    print("Noise source warming up")
    time.sleep(5)
    
    # Call SDR
    runGNU(top_block)
    # Ends in the script
    N2 = readBinFile("Power")
#    data = NoiseFig(N2,N1)
#    row = filewrite(data)



    row = "GPS DATA HERE"
    wiringPi.digitalWrite(GPIO0, OFF)

    
    # setup the filename and send the data to the server
    outFilename = "rowdata.txt"
    cmd = "PUT " + outFilename
    putToServer(cmd, row)

    # Now wait to receive another response
    buff = sock.recv(1024)
    print("Received: " + buff)

    # Finally shut the program down
    killClient()





""" The code below is likely not needed, but might be needed in the future"""
# def filewrite(data):
#     path = '~/sensor/data_archive/'
#     finalpath ='/home/odroid/sensor/data_archive/NoiseFigure.xls'

#     try:
#         rb = open_workbook(finalpath, formatting_info=True)
#         r_sheet = rb.sheet_by_index(0)  # read only copy to introspect the file
#         wb = copy(rb)  # a writable copy (I can't read values out of this, only write to it)
#         w_sheet = wb.get_sheet(0)  # the sheet to write to within the writable copy
#         row = r_sheet.nrows+1
#         for i in range(len(data)):
#             w_sheet.write(row-1, i, data[i])
#         wb.save(finalpath)
#         print("Successfully wrote %.2f as NF at time %s at %s Lat %s Lon and %.2f Alt  \n" %(data[-1], data[0],data[1], data[2], data[3]))
#     except IOError:
#         print("The file name, %s, is not valid" %finalpath)

#     rowbuff = ""
#     ncols = r_sheet.ncols
#     for col_idx in range(ncols):
#         cellobj = r_sheet.cell_value(row-2, col_idx)
#         rowbuff = rowbuff + str(cellobj)+ ' '
#     return rowbuff
