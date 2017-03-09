swig -python wiringPi.i

gcc -O2 -fPIC -c wiringPi.c

gcc -O2 -fPIC -c wiringPi_wrap.c -I/usr/include/python2.7/ -I/home/odroid/Documents/2ndRF/Odroid_wiringPi/wiringPi/wiringPi

gcc -shared wiringPi.o wiringPi_wrap.o -I/home/odroid/Documents/2ndRF/Odroid_wiringPi/wiringPi/wiringPi -lwiringPi  -o _wiringPi.so
