import wiringPi

#This is the website for the Physical Pin out for Odroid XU4
#http://odroid.com/dokuwiki/doku.php?id=en:xu3_hardware_gpio

#Define 4 GPIO pins

ON     = 1
OFF    = 0
OUTPUT = 1
GPIO0  = 0 	# Physical pin 5
GPIO1  = 15	# Physical pin 8
GPIO2  = 21	# Physical pin 24
GPIO3  = 11	# Physical pin 20
GPIO4  = 2  # Physical pin 13
GPIO5  = 3  # physical pin 17
GPIO6  = 4  # Physcial pin 18
GPIO7  = 6  # Physcial pin 26
GPIO8  = 22 # Physcial pin 19
GPIO9  = 27 # Physical pin 15


def initPins():	
	wiringPi.wiringPiSetup();
	wiringPi.pinMode (GPIO0, OUTPUT)
	wiringPi.pinMode (GPIO1, OUTPUT)
	wiringPi.pinMode (GPIO2, OUTPUT)
	wiringPi.pinMode (GPIO3, OUTPUT)


initPins()

wiringPi.digitalWrite(GPIO0,ON)
raw_input("Should see pin 15 on")
wiringPi.digitalWrite(GPIO0,OFF)
raw_input("Should see pin 15 off")

wiringPi.digitalWrite(GPIO1,ON)
raw_input("Should see pin 8 on")
wiringPi.digitalWrite(GPIO1,OFF)
raw_input("Should see pin 8 off")

wiringPi.digitalWrite(GPIO2,ON)
raw_input("Should see pin 24 on")
wiringPi.digitalWrite(GPIO2,OFF)
raw_input("Should see pin 24 off")

# wiringPi.digitalWrite(GPIO0,ON)
# raw_input("Should see pin 5 on")
# wiringPi.digitalWrite(GPIO0,OFF)
# raw_input("Should see pin 5 off")


val0 = OFF
val1 = OFF
val2 = OFF


while True:
    choice = raw_input("Enter pin to toggle: ")
    print(choice[0])
    ch = str(choice[0])

    
    if ch == str(0):
        if val0 == OFF:
                val0 = ON
                wiringPi.digitalWrite(GPIO0, ON)
        else:
                val0 = OFF
                wiringPi.digitalWrite(GPIO0, OFF)


    if ch == str(1):
        if val1 == OFF:
                val1 = ON
                wiringPi.digitalWrite(GPIO2, ON)
        else:
                val1 = OFF
                wiringPi.digitalWrite(GPIO2, OFF)
 #       print("val1 is "+val1)
        wiringPi.digitalWrite(GPIO1,val1)

    if ch == str(2):
        if val2 == OFF:
                val2 = ON
        else:
                val2 = OFF
  #      print("val2 is "+val2)
        wiringPi.digitalWrite(GPIO2,val2)
