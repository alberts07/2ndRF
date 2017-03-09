#Need to initialize power measurements with the noise diode off Look into whether order matters
# Then turn the noise diode on and wait
# Now initialize power measurements with noise diode on 
# Divide the power of it on by the power of it off to get the Y FAct.
# Calculate NF by taking ENR and subtracting 10log(Yfac-1)
# ENR is  30db but will be calculated when parts in 
import math
import numpy as np
import xlwt
from datetime import datetime


def NoiseFig(N2,N1):

	try:
		ENR=15
		YF=N2/N1
		NF= ENR-10*math.log(YF-1,10)
		return (NF, str(datetime.now()))
	except TypeError:
		print("You need to enter a number")
def filewrite(data):
	path = '/home/sensor/data_archive/'
	wb = xlwt.Workbook()
	ws = wb.add_sheet("Noise Figure")  # Edit TimeStamps to whatever you would like to name your file

	# ******* Setting up Headers ******************************
	print("Attempting to write to file")
	try:
		ws.write(0, 0, "Noise Figure")
		ws.write(0, 1, "Time")

	# *********************************************************

		wb.save(path+"NoiseFigure.xls")
		row=1
		for i in range(len(data)):
			ws.write(row, i, data[i])
		row = row + 1
		print(path+"NoiseFigure.xls")
		wb.save(path+"NoiseFigure.xls")
		print("Successfully wrote %f and %s" %(data[0], data[1]))
	except:
		print("Failed to write the NoiseFigure")

data=NoiseFig(795.02,7.9499)
filewrite(data)

