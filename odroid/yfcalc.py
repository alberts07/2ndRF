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
from datetime import datetime

# todo update to actual file location when I can.
# todo update ENR when we know it
# todo place try except block

def NoiseFig(N2,N1):

    ENR=14.85
    YF=N2/N1
    NF= ENR-10*math.log(YF-1,10)
    gpsinfo = None
    while gpsinfo == None:
        gpsinfo = GPS_runner.runner()
    gpsinfo.append(NF)
    return gpsinfo

def filewrite(data):
    path = '/home/sensor/data_archive/'
    finalpath ='NoiseFigure.xls'

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

data=NoiseFig(795.02,7.9499)
filewrite(data)
