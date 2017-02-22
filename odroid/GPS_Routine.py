import pynmea2
import serial
import sys
import xlwt
import csv

import os
import fcntl
import time

# ********************************************************

# This code was written Feb 9th 2017 by Austin Alberts
# it is written for python 2 as the xlwt will not cooperate with python3

#This code could be updated by: 
#Making a user input exit for the excel, text, and csv options


def subroutine(choice):
	if(choice=='cmd'):
	
# ********************************************************
	
# Printing to command line
		fl = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
		fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, fl | os.O_NONBLOCK)
		print("Press q to quit collecting information\n")
		while(1):
	
# Check to see if the user attempted to terminate the program

			try:
				stdin = sys.stdin.read()
				if "q" in stdin:
					break
			except IOError:
				pass
			time.sleep(.1)


			with serial.Serial('/dev/ttyUSB0', 4800) as ser:	#The USB port may change with your device. Baud rate of 4800
				s0 = ser.read()
				if(s0 == '$'):					#Look for first char sent by NMEA Standards 
					s1 = ser.readline()        		#When found, read the line because NMEA ends with new line char
					msg = pynmea2.parse(s1, 4800)		#Pynmea2 allows you to parse the string and put data in the object specified
					if (s1[2:5] == 'GGA'):			#This is the NMEA packet we want, there are about 5 different packets sent by this device.
						print("The time is %s \t The location is %s %s %s %s at %.2f %s of elevation with %s satellites in view\n" %(str(msg.timestamp), msg.lat, msg.lat_dir, msg.lon, msg.lon_dir,msg.altitude,msg.altitude_units,msg.num_sats))

	elif(choice=='msod'):
		

# ********************************************************
	
# Sending to another function (MSOD spec)
		with serial.Serial('/dev/ttyUSB0', 4800) as ser:	#The USB port may change with your device. Baud rate of 4800
			s0 = ser.read()
			if(s0 == '$'):					#Look for first char sent by NMEA Standards 
				
				s1 = ser.readline()        		#When found, read the line because NMEA ends with new line char
				if (s1[2:5] == 'GGA'):
					msg = pynmea2.parse(s1, 4800)		#Pynmea2 allows you to parse the string and put data in the object specified
					print(msg.lat)
					msg.lat=float(msg.lat)/100
					msg.lon=float(msg.lon)/100
					if(msg.lat_dir=='S'):
						msg.lat=float(msg.lat)*-1
					if(msg.lon_dir=='W'):
						msg.lon=float(msg.lon)*-1

					return msg
	elif(choice=='excel'):

# *********************************************************
		0
# Write to an excel file
		print("Press Ctl + c to quit collecting information\n")
		wb = xlwt.Workbook()						
		ws = wb.add_sheet("TimeStamps")				#Edit TimeStamps to whatever you would like to name your file

# ******* Setting up Headers ******************************

		ws.write(0, 0, "Time")						
		ws.write(0, 1, "Lat")
		ws.write(0, 2, "Dir")
		ws.write(0, 3, "Lon")
		ws.write(0, 4, "Dir")
		ws.write(0, 5, "Alt")
		ws.write(0, 6, "Alt units")
		ws.write(0, 7, "Num of Sats")

# *********************************************************

		wb.save("Timestamps.xls")
		row=1							# Starts at 1 because we added in the headers in row 0
		while(1):

# Check to see if the user attempted to terminate the program

			with serial.Serial('/dev/ttyUSB0', 4800) as ser:	#The USB port may change with your device. Baud rate of 4800
				s0 = ser.read()
				if(s0 == '$'):					#Look for first char sent by NMEA Standards
					s1 = ser.readline()        		#When found, read the line because NMEA ends with new line char
					msg = pynmea2.parse(s1, 4800)		#Pynmea2 allows you to parse the string and put data in the object specified
					if (s1[2:5] == 'GGA'):			#This is the NMEA packet we want, there are about 5 different packets sent by this device.
						cols= [str(msg.timestamp), msg.lat, msg.lat_dir, msg.lon, msg.lon_dir, str(msg.altitude), msg.altitude_units,msg.num_sats]
						for jcols in range(len(cols)):
							ws.write(row, jcols, cols[jcols])	#Write to the row and the col jcols with the element cols[jcols]
						row = row + 1				
						wb.save("Timestamps.xls")	#Save the workbook after each row operation finishes. If the workbook crashes and it is not saved it loses all 									 the data


	elif(choice=='text'):
	
# *********************************************************

# Write to a text file
		print("Press Ctl + c to quit collecting information\n")
		f = open('Timestamps', 'w')					#Change Timestamps to whatever you want to call your text file
		while(1):

# Check to see if the user attempted to terminate the program

			with serial.Serial('/dev/ttyUSB0', 4800) as ser:	#The USB port may change with your device. Baud rate of 4800
				s0 = ser.read()
				if(s0 == '$'):					#Look for first char sent by NMEA Standards
					s1 = ser.readline()        		#When found, read the line because NMEA ends with new line char
					msg = pynmea2.parse(s1, 4800)		#Pynmea2 allows you to parse the string and put data in the object specified
					if (s1[2:5] == 'GGA'):			#This is the NMEA packet we want, there are about 5 different packets sent by this device.
						f.write("The time is %s \t The location is %s %s %s %s at %.2f %s of elevation with %s satellites in view\n" %(str(msg.timestamp), msg.lat, msg.lat_dir, msg.lon, msg.lon_dir,msg.altitude,msg.altitude_units,msg.num_sats))

	elif(choice=='csv'):
	

# *********************************************************

# Write to a CSV file

		print("Press Ctl + c to quit collecting information\n")
		with open('Timestamps.csv', 'wb') as fp:			#Change Timestamps to whatevert you want to call your CSV file

			while(1):


# Check to see if the user attempted to terminate the program

				with serial.Serial('/dev/ttyUSB0', 4800) as ser:
								#The USB port may change with your device. Baud rate of 4800
					s0 = ser.read()
					if(s0 == '$'):				#Look for first char sent by NMEA Standards
						s1 = ser.readline()        	#When found, read the line because NMEA ends with new line char
						msg = pynmea2.parse(s1, 4800)	#Pynmea2 allows you to parse the string and put data in the object specified
						if (s1[2:5] == 'GGA'):		#This is the NMEA packet we want, there are about 5 different packets sent by this device.
							cols= [str(msg.timestamp), msg.lat, msg.lat_dir, msg.lon, msg.lon_dir, str(msg.altitude), msg.altitude_units,msg.num_sats]
				
							a = csv.writer(fp, delimiter=',')
							a.writerow(cols)
	
	else:
		print("The correct argument was not given. Please enter cmd|excel|text|csv as an input\n")	



