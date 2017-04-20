#! /usr/bin/env python
# Need to initialize power measurements with the noise diode off Look into whether order matters
# Then turn the noise diode on and wait
# Now initialize power measurements with noise diode on
# Divide the power of it on by the power of it off to get the Y FAct.
# Calculate NF by taking ENR and subtracting 10log(Yfac-1)
# ENR is  30db but will be calculated when parts in
import math
from xlrd import open_workbook  # http://pypi.python.org/pypi/xlrd
from xlutils.copy import copy
import numpy
import time
import socket
import scipy
import struct

# from datetime import datetime

# This is the website for the Physical Pin out for Odroid XU4
# http://odroid.com/dokuwiki/doku.php?id=en:xu3_hardware_gpio



# Set up the GPIO pins, and make sure they are all set low initially



# todo update to actual file location when I can.
# todo update ENR when we know it
# todo place try except block

def readBinFile(file):
    f = scipy.fromfile(open(file), dtype=scipy.float32)

    return f


def runGNU(top_block_file):
    top_block_file.main()


def NoiseFig(N2, N1):
    # ENR = 30

    ENR = 14.85

    # Testing Doug's stuff
    # Z = 50
    # N2_W = numpy.square(numpy.absolute(N2)) / Z
    # N1_W = numpy.square(numpy.absolute(N1)) / Z
    # N2mean_W = numpy.mean(N2_W)
    # N1mean_W = numpy.mean(N1_W)
    # N2mean_dBW = 10 * numpy.log10(N2mean_W)
    # N1mean_dBW = 10 * numpy.log10(N1mean_W)
    # ENR_W = numpy.power(10, ENR / 10.0)
    # YF = N2mean_W/N1mean_W
    # NF = ENR_W / (YF-1)
    # NF = 10 * numpy.log10(NF)

    # My code starts

    # N2 = N2**2 / 50
    # print(N2)
    N2 = N2.mean()
    # N2 = 10 * numpy.log10(N2)

    # N1 = N1**2 / 50
    # print(N1)
    N1 = N1.mean()
    # N1 = 10 * numpy.log10(N1)

    N2lin = 10 ** (N2 / 10)
    N1lin = 10 ** (N1 / 10)
    YF = N2lin / N1lin
    print('The YFcalc is %f' % YF)
    NF = ENR - 10 * numpy.log10(YF - 1)
    print('The noise figure is %f' % NF)

    # gpsinfo = None
    # while gpsinfo == None:
    #    gpsinfo = GPS_runner.runner()
    # gpsinfo.append(NF)
    # return gpsinfo
    return NF


# ~ def filewrite(data):
# ~ path = '~/sensor/data_archive/'
# ~ finalpath ='/home/odroid/sensor/data_archive/NoiseFigure.xls'

# ~ try:
# ~ rb = open_workbook(finalpath, formatting_info=True)
# ~ r_sheet = rb.sheet_by_index(0)  # read only copy to introspect the file
# ~ wb = copy(rb)  # a writable copy (I can't read values out of this, only write to it)
# ~ w_sheet = wb.get_sheet(0)  # the sheet to write to within the writable copy
# ~ row = r_sheet.nrows+1
# ~ #for i in range(len(data)):
# ~ w_sheet.write(row-1, 0, data)
# ~ wb.save(finalpath)
# ~ #print("Successfully wrote %.2f as NF at time %s at %s Lat %s Lon and %.2f Alt  \n" %(data[-1], data[0],data[1], data[2], data[3]))
# ~ except IOError:
# ~ print("The file name, %s, is not valid" %finalpath)

# ~ rowbuff = ""
# ~ ncols = r_sheet.ncols
# ~ for col_idx in range(ncols):
# ~ cellobj = r_sheet.cell_value(row-2, col_idx)
# ~ rowbuff = rowbuff + str(cellobj)+ ' '
# ~ return rowbuff

def fileInit():
    with open('NoiseFigure.csv', 'w') as csvfile:
        csvfile.write("UTC,Lat,Long,Alt,NF")
        csvfile.write("\n")
    csvfile.close()


def filewrite(data):
    path = '~/Documents/test'
    finalpath = '/home/user/Documents/test/NoiseFigure.csv'
    row_count = sum(1 for row in csv.reader(open('NoiseFigure.csv')))
    print(row_count)
    if row_count < 3:
        fd = open('NoiseFigure.csv', 'a')
        fd.write(data)
        fd.write("\n")
        fd.close()
    else:
        os.rename('NoiseFigure.csv', '04-13-17.csv')
        fileInit()
        fd = open('NoiseFigure.csv', 'a')
        fd.write(data)
        fd.write("\n")
        fd.close()