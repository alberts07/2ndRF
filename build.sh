#! /bin/bash
gcc say.c -I/usr/include/python2.7/ -Wall -Wextra -shared -fPIC -o libsay.so 
python setup.py build
python saySomething.py
