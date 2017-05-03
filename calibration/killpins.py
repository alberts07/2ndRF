import gpiolib.wiringPi as wiringPi
import time
#Define 4 GPIO pins

ON     = 1
OFF    = 0
OUTPUT = 1
GPIO0  = 0 	# Physical pin 5
GPIO1  = 15	# Physical pin 8
GPIO2  = 21	# Physical pin 20
GPIO3  = 2      # Physical pin 13
GPIO4  = 22     # Physcial pin 19   
GPIO5  = 3      # physical pin 17
GPIO6  = 7      # Physical pin 15
GPIO7  = 5      # physical pin 2


wiringPi.wiringPiSetup()
wiringPi.pinMode (GPIO0, OUTPUT)
wiringPi.pinMode (GPIO1, OUTPUT)
wiringPi.pinMode (GPIO2, OUTPUT)
wiringPi.pinMode (GPIO3, OUTPUT)
wiringPi.pinMode (GPIO4, OUTPUT)
wiringPi.pinMode (GPIO5, OUTPUT)
wiringPi.pinMode (GPIO6, OUTPUT)
wiringPi.pinMode (GPIO7, OUTPUT)

wiringPi.digitalWrite(GPIO6, OFF)
time.sleep(2)
wiringPi.digitalWrite(GPIO1, OFF)
wiringPi.digitalWrite(GPIO2, OFF)
wiringPi.digitalWrite(GPIO3, OFF)
wiringPi.digitalWrite(GPIO4, OFF)
wiringPi.digitalWrite(GPIO5, OFF)
wiringPi.digitalWrite(GPIO0, OFF)
wiringPi.digitalWrite(GPIO7, OFF)
