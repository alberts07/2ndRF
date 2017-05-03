#! /usr/bin/env python
import gpiolib.wiringPi as wiringPi
import time
#This is the website for the Physical Pin out for Odroid XU4
#http://odroid.com/dokuwiki/doku.php?id=en:xu3_hardware_gpio

#Define 4 GPIO pins

ON     = 1
OFF    = 0
OUTPUT = 1
GPIO0  = 0 	# Physical pin 5
GPIO1  = 15	# Physical pin 8
GPIO2  = 2      # Physical pin 13
GPIO3  = 7      # Physical pin 15
GPIO4  = 22     # Physcial pin 19   
GPIO5  = 23     # physical pin 22
GPIO6  = 11     # Physical pin 24

#22     # physical pin 19
#13     # physical pin 9
#21	# physical pin 20
#4      # physcial pin 18

def initPins():	
        wiringPi.wiringPiSetup();
        
        wiringPi.pinMode (GPIO0, OUTPUT)
	wiringPi.pinMode (GPIO1, OUTPUT)
	wiringPi.pinMode (GPIO2, OUTPUT)
        wiringPi.pinMode (GPIO3, OUTPUT)
        wiringPi.pinMode (GPIO4, OUTPUT)
        wiringPi.pinMode (GPIO5, OUTPUT)
        wiringPi.pinMode (GPIO6, OUTPUT)
        

        wiringPi.digitalWrite(GPIO6, OFF)
        time.sleep(2)
        wiringPi.digitalWrite(GPIO0, OFF)
        wiringPi.digitalWrite(GPIO1, OFF)
        wiringPi.digitalWrite(GPIO2, OFF)
        wiringPi.digitalWrite(GPIO3, OFF)
        wiringPi.digitalWrite(GPIO4, OFF)
        wiringPi.digitalWrite(GPIO5, OFF)


        

initPins()

val0 = OFF
val1 = OFF
val2 = OFF
val3 = OFF
val4 = OFF
val5 = OFF
val6 = OFF


while True:
    choice = raw_input("Enter pin to toggle: ")
    
    if choice[0] == 'q':
            wiringPi.digitalWrite(GPIO6, OFF)
            time.sleep(2)
            wiringPi.digitalWrite(GPIO0, OFF)
            wiringPi.digitalWrite(GPIO1, OFF)
            wiringPi.digitalWrite(GPIO2, OFF)
            wiringPi.digitalWrite(GPIO3, OFF)
            wiringPi.digitalWrite(GPIO4, OFF)
            wiringPi.digitalWrite(GPIO5, OFF)

            break

    ch = str(choice[0])
    
    if ch == str(0):
        if val0 == OFF:
                val0 = ON
                wiringPi.digitalWrite(GPIO0, ON)
                print("Pin0 ON")
        else:
                val0 = OFF
                wiringPi.digitalWrite(GPIO0, OFF)
                print("Pin0 OFF")

    elif ch == str(1):
         if val1 == OFF:
                val1 = ON
                wiringPi.digitalWrite(GPIO1, ON)
                print("Pin1 ON")
         else:
                val1 = OFF
                wiringPi.digitalWrite(GPIO1, OFF)
                print("Pin1 OFF")


    elif ch == str(2):
            if val2 == OFF:
                    val2 = ON
                    wiringPi.digitalWrite(GPIO2, ON)
                    print("Pin2 ON")
            else:
                    val2 = OFF
                    wiringPi.digitalWrite(GPIO2, OFF)
                    print("Pin2 OFF")
                    
    elif ch == str(3):
            if val3 == OFF:
                    val3 = ON
                    wiringPi.digitalWrite(GPIO3, ON)
                    print("Pin3 ON")
            else:
                     val3 = OFF
                     wiringPi.digitalWrite(GPIO3, OFF)
                     print("Pin3 OFF")
    elif ch == str(4):
             if val4 == OFF:
                     val4 = ON
                     wiringPi.digitalWrite(GPIO4, ON)
                     print("Pin4 ON")
             else:
                     val4 = OFF
                     wiringPi.digitalWrite(GPIO4, OFF)
                     print("Pin4 OFF")
    elif ch == str(5):
            if val5 == OFF:
                    val5 = ON
                    wiringPi.digitalWrite(GPIO5, ON)
                    print("Pin5 ON")
            else:
                    val5 = OFF
                    wiringPi.digitalWrite(GPIO5, OFF)
                    print("Pin5 OFF")
                    
    elif ch == str(6):
            if val6 == OFF:
                    val6 = ON
                    wiringPi.digitalWrite(GPIO6, ON)
                    print("Pin6 ON")
            else:
                    val6 = OFF
                    wiringPi.digitalWrite(GPIO6, OFF)
                    print("Pin6 OFF")

                
                    
                    

#1=green
#2=yellow
