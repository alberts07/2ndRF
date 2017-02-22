from GPS_Routine import subroutine
def runner():
	MSODobject=None
	while (MSODobject is None):
		MSODobject=subroutine("msod")
	#print(str(MSODobject.timestamp))
	strarray= [str(MSODobject.timestamp), MSODobject.lat, MSODobject.lon, MSODobject.altitude]	
	print(strarray)
	return strarray
