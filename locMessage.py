from GPS_runner import runner
import json
import time
import numpy
def locMessage():
	strarray=runner()

	A={
	    "version": "1.0.16",
	    "messageType": "Loc",
	    "sensorId": "101010101",
	    "sensorKey": 846859034,
	    "time": time.time(),
	    "mobility": "Stationary",
	    "environment": "Outdoor",
	    "latitude": float(strarray[1]),
	    "longitude": float(strarray[2]),
	    "altitude": float(strarray[3]),
	    "timeZone": "America_Denver"
	}
	return A
