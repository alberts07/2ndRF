#! /bin/bash
sudo ifconfig eth0 192.168.130.158
sudo ufw disable
uhd_find_devices

#ifconfig | grep "inet addr:"
