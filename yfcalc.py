#Need to initialize power measurements with the noise diode off Look into whether order matters
# Then turn the noise diode on and wait
# Now initialize power measurements with noise diode on 
# Divide the power of it on by the power of it off to get the Y FAct.
# Calculate NF by taking ENR and subtracting 10log(Yfac-1)
# ENR is  30db but will be calculated when parts in 
import math
import numpy as np

def NoiseFig(ENR,N2,N1):
	YF=N2/N1
	print(YF)
	NF=ENR-10*math.log10(YF-1)
	data= (NF,YF)
def filewrite(data):
	
