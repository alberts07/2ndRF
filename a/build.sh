#! /bin/bash
gcc gpio.c -I/usr/include/python2.7/ -I../Odroid_wiringPi/wiringPi/wiringPi -Wall -Wextra -shared -fPIC -o libgpio.so 
python setup.py build
python go_gpio.py
