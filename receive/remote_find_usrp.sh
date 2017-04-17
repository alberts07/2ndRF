#! /bin/bash

sudo ifconfig enp3s0 192.168.130.158
sudo ufw disable
uhd_find_devices
echo "Remote Computer ip: "
ifconfig | grep "inet addr:"
