#Need to initialize power measurements with the noise diode off Look into whether order matters
# Then turn the noise diode on and wait
# Now initialize power measurements with noise diode on 
# Divide the power of it on by the power of it off to get the Y FAct.
# Calculate NF by taking ENR and subtracting 10log(Yfac-1)
# ENR is  30db but will be calculated when parts in 
import math
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlutils.copy import copy

from datetime import datetime


def NoiseFig(N2,N1):

	try:
		ENR=14.85
		YF=N2/N1
		NF= ENR-10*math.log(YF-1,10)
		return (NF, str(datetime.now()))
	except TypeError:
		print("You need to enter a number")
def filewrite(data):
	path = '/home/sensor/data_archive/'

	try:
		rb = open_workbook("NoiseFigure.xls", formatting_info=True)
		r_sheet = rb.sheet_by_index(0)  # read only copy to introspect the file
		wb = copy(rb)  # a writable copy (I can't read values out of this, only write to it)
		w_sheet = wb.get_sheet(0)  # the sheet to write to within the writable copy
		row = r_sheet.nrows+1
		for i in range(len(data)):
			w_sheet.write(row-1, i, data[i])
		print(path+"NoiseFigure.xls")
		wb.save("NoiseFigure.xls")
		print("Successfully wrote %f and %s" %(data[0], data[1]))
	except:
		print("Failed to write the NoiseFigure")

data=NoiseFig(795.02,7.9499)
filewrite(data)

