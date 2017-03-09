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
wiringPi.digitalWrite(GPIO1,OFF)
wiringPi.digitalWrite(GPIO2,ON)
wiringPi.digitalWrite(GPIO3,OFF)
raw_input("Press enter")

wiringPi.digitalWrite(GPIO0,OFF)
wiringPi.digitalWrite(GPIO1,ON)
wiringPi.digitalWrite(GPIO2,OFF)
wiringPi.digitalWrite(GPIO3,ON)
raw_input("Press enter")

wiringPi.digitalWrite(GPIO0,ON)
wiringPi.digitalWrite(GPIO1,ON)
wiringPi.digitalWrite(GPIO2,OFF)
wiringPi.digitalWrite(GPIO3,OFF)
raw_input("Press enter")

wiringPi.digitalWrite(GPIO0,OFF)
wiringPi.digitalWrite(GPIO1,OFF)
wiringPi.digitalWrite(GPIO2,ON)
wiringPi.digitalWrite(GPIO3,ON)
raw_input("Press enter")

print("Complete")


