#! /bin/bash

uhd_find_devices
echo "Odroid ip: "
ifconfig | grep "inet addr:"
