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
import numpy
import time
import top_block
import socket
import scipy
import gpslib.GPS_runner as GPS_runner
import gpiolib.wiringPi as wiringPi
import struct
import csv

import decimal


#from datetime import datetime

#This is the website for the Physical Pin out for Odroid XU4
#http://odroid.com/dokuwiki/doku.php?id=en:xu3_hardware_gpio

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

# Set up the GPIO pins, and make sure they are all set low initially
def initPins():
    wiringPi.wiringPiSetup();
    wiringPi.pinMode (GPIO0, OUTPUT)
    wiringPi.pinMode (GPIO1, OUTPUT)
    wiringPi.pinMode (GPIO2, OUTPUT)

    wiringPi.digitalWrite(NS, OFF)
    wiringPi.digitalWrite(SWITCH, OFF)
    wiringPi.digitalWrite(GPIO2, OFF)



# todo place try except block

def readBinFile(file):
    f = scipy.fromfile(open(file), dtype = scipy.float32)

    return f

def runGNU(top_block_file):

    top_block_file.main()


def NoiseFig(N2,N1):

    ENR = 30


    # Testing Doug's stuff
    #Z = 50
    #N2_W = numpy.square(numpy.absolute(N2)) / Z
    #N1_W = numpy.square(numpy.absolute(N1)) / Z
    #N2mean_W = numpy.mean(N2_W)
    #N1mean_W = numpy.mean(N1_W)
    #N2mean_dBW = 10 * numpy.log10(N2mean_W)
    #N1mean_dBW = 10 * numpy.log10(N1mean_W)
    #ENR_W = numpy.power(10, ENR / 10.0)
    #YF = N2mean_W/N1mean_W
    #NF = ENR_W / (YF-1)
    #NF = 10 * numpy.log10(NF)

    #My code starts

    #N2 = N2**2 / 50
    #print(N2)
    

    
    
    #N2 = 10 * numpy.log10(N2)
    N2 = N2.mean()
    #N1 = N1**2 / 50
    print('\n')
    
    #print(N1)
    
    
    #N1 = 10 * numpy.log10(N1)
    N1 = N1.mean()
    YF=N2/N1
    print('The YFcalc is %f' %YF)
    NF= ENR-10*numpy.log10(YF-1)
    print('The noise figure is %f'%NF)

    #gpsinfo = None
    #while gpsinfo == None:
    #    gpsinfo = GPS_runner.runner()
    #gpsinfo.append(NF)
    #return gpsinfo
    return NF

#~ def filewrite(data):
    #~ path = '~/sensor/data_archive/'
    #~ finalpath ='/home/odroid/sensor/data_archive/NoiseFigure.xls'

    #~ try:
        #~ rb = open_workbook(finalpath, formatting_info=True)
        #~ r_sheet = rb.sheet_by_index(0)  # read only copy to introspect the file
        #~ wb = copy(rb)  # a writable copy (I can't read values out of this, only write to it)
        #~ w_sheet = wb.get_sheet(0)  # the sheet to write to within the writable copy
        #~ row = r_sheet.nrows+1
        #~ #for i in range(len(data)):
        #~ w_sheet.write(row-1, 0, data)
        #~ wb.save(finalpath)
        #~ #print("Successfully wrote %.2f as NF at time %s at %s Lat %s Lon and %.2f Alt  \n" %(data[-1], data[0],data[1], data[2], data[3]))
    #~ except IOError:
        #~ print("The file name, %s, is not valid" %finalpath)

    #~ rowbuff = ""
    #~ ncols = r_sheet.ncols
    #~ for col_idx in range(ncols):
        #~ cellobj = r_sheet.cell_value(row-2, col_idx)
        #~ rowbuff = rowbuff + str(cellobj)+ ' '
    #~ return rowbuff

def fileInit():
    with open('NoiseFigure.csv', 'w') as csvfile:
        csvfile.write("UTC,Lat,Long,Alt,NF")
        csvfile.write("\n")
    csvfile.close()

def filewrite(data):
    path = '~/Documents/test'
    finalpath ='/home/user/Documents/test/NoiseFigure.csv'
    row_count = sum(1 for row in csv.reader( open('NoiseFigure.csv') ) )
    if row_count < 3:
        fd = open('NoiseFigure.csv','wb')
        fd.write(data)
        fd.write("\n")
        fd.close()
    else:
        os.rename('NoiseFigure.csv','04-13-17.csv')
        fileInit()
        fd = open('NoiseFigure.csv','a')
        fd.write(data)
        fd.write("\n")
        fd.close()
    return data

def putToServer(cmd, buff):
    # First connect to the server, then send the message
    sock.connect((serverIP, port))
    sock.send(cmd)
    #print("sending: ")
    #print(cmd)
    #print(buff)

    # Wait for the response from the server indicating it's ready
    while True:
        resp = ""
        resp = sock.recv(1024)
        print("RECIEVED " + resp)
        if resp[0:5] == "READY":
            sock.send(str(buff))
            break

        # Handle a server side error
        elif resp[0:5] == "ERROR":
            print("There was an error on the server.")
            break
        # Handle unknowns
        else:
            print("Didn't understand response, killing client")
            sock.send("ERROR 2")
            killClient()

def killClient():
        sock.send("QUIT")
        sock.close()



# Set up the socket for the client, these are set Globally
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
port = 18999 # This is just a random port chosen to try to avoid a used one
serverIP = '172.21.74.177'
#serverIP = '192.168.130.100'

if __name__ == "__main__":

    fileInit()
    initPins()
    data = None
    while data == None or (data.dtype == float and numpy.isnan(data)) :
    	wiringPi.digitalWrite(SWITCH, ON)
    	time.sleep(1)
    	raw_input("Verify the switch has turned on and then press ENTER")


    	print("The noise with the noise source on will now be calculated")

        wiringPi.digitalWrite(NS, ON)
        print("5 seconds until testing")
        time.sleep(10)
        print("Continuing test")

        runGNU(top_block)
        #Ends in the script

        N2 = readBinFile("Power")
        # The system should turn the noise source on now
        raw_input("Press ENTER to turn off the noise source and continue")

        wiringPi.digitalWrite(NS, OFF)

        print("Noise source turning off")
        time.sleep(10)
        print("Continuing test")

        # Call SDR
        runGNU(top_block)
        # Ends in the script
        time.sleep(5)
        N1 = readBinFile("Power")

        data = NoiseFig(N2,N1)
        if data.dtype == float and numpy.isnan(data):
            print("The calculation was not valid, recalculating")
	    wiringPi.digitalWrite(GPIO0, OFF)
            wiringPi.digitalWrite(GPIO1, OFF)
            wiringPi.digitalWrite(GPIO2, OFF)

            continue
        print("This is data")        
        #print(data)
        #row = filewrite(data)

        #loc,NF = buildMessage(rowdata, data):

        outFilename = "data.csv"
        cmd = "PUT " + outFilename
        putToServer(cmd, data)

        # Now wait to receive another response
        buff = sock.recv(1024)
        print("Received: " + buff)
        killClient()
        wiringPi.digitalWrite(GPIO0, OFF)
        wiringPi.digitalWrite(GPIO1, OFF)
        wiringPi.digitalWrite(GPIO2, OFF)


