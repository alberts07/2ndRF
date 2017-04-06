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

#from datetime import datetime

# todo update to actual file location when I can.
# todo update ENR when we know it
# todo place try except block

def readBinFile(file):

    data = numpy.fromfile(file)
    return data.mean()

def runGNU(top_block_file):

    top_block_file.main() #Brian put script here

def NoiseFig(N2,N1):

    ENR=14.85
    N2lin = 10**(N2/10)
    N1lin = 10**(N1/10)
    YF=N2lin/N1lin
    NF= ENR-10*math.log(YF-1,10)
    gpsinfo = None
    while gpsinfo == None:
        gpsinfo = GPS_runner.runner()
    gpsinfo.append(NF)
    return gpsinfo

def filewrite(data):
    path = '~/sensor/data_archive/'
    finalpath ='~/sensor/data_archive/NoiseFigure.xls'

    try:
        rb = open_workbook(finalpath, formatting_info=True)
        r_sheet = rb.sheet_by_index(0)  # read only copy to introspect the file
        wb = copy(rb)  # a writable copy (I can't read values out of this, only write to it)
        w_sheet = wb.get_sheet(0)  # the sheet to write to within the writable copy
        row = r_sheet.nrows+1
        print(data)
        for i in range(len(data)):
            w_sheet.write(row-1, i, data[i])
        wb.save(finalpath)
        print("Successfully wrote %.2f as NF at time %s at %s Lat %s Lon and %.2f Alt  \n" %(data[-1], data[0],data[1], data[2], data[3]))
    except IOError:
        print("The file name, %s, is not valid" %finalpath)

def main():

    print("The noise with the noise source off will now be calculated")
    #Call SDR
    runGNU(top_block)
    #Ends in the script

    N1 = readBinFile("Power")

    raw_input("Turn the noise source on and press enter")

    # Call SDR
    runGNU(top_block)
    # Ends in the script
    N2 = readBinFile("Power")
    data = NoiseFig(N2,N1)
    filewrite(data)
    
    return
