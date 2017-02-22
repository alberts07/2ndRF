

from socket import *
import sys
import time

remoteIp = ''
lclHostPort = 8999

# Set up the socket
socket_object = socket(AF_INET, SOCK_STREAM, 0)
socket_object.bind((remoteIp,lclHostPort))
socket_object.listen(1)
print('Listening on port: ', lclHostPort)

# Keep the socket running until 'cntl-C' is received
while True:
    # Wait to accept a connection
    remote, address = socket_object.accept()
    print('Connected to ', address)


    while True:
        print "Waiting for request"
        buffer = remote.recv(1024)
        print "CMD: " + buffer[0:3] # Prints the command
        print "Buffer: " + buffer[4:]

        # time.sleep(1)
        # If the PUT command is received, prepare to receive the file name passed
        if buffer[0:3] == "PUT":
            fp = open(buffer[4:], "wb")
            if fp:
                print "file " + buffer[4:] + " opened"
                remote.send("READY")
            # If there was an error, print the buffer received and send 'ERROR'
            else:
                remote.send("ERROR")
                print buffer
        elif not buffer:
            remote.send("ERROR")
            print "Did not receive anything."
        else:
            # Next should be the file, write the buffer to the file.
            fp.write(buffer)
            fp.close()
        remote.send("Rx'd file")


    remote.close()
    fp.close()
    socket_object.close()






#  # = "decimal:" + str(d) + "\nfloat: " + str(x)
#
# print strng
#
# strng = "{
#     "version": "1.0.16",
#     "messageType": "Loc",
#     "sensorId": "101010101",
#     "sensorKey": 846859034,
#     "time": 987654321,
#     "mobility": "Stationary",
#     "environment": "Outdoor",
#     "latitude": 40.0,
#     "longitude": -105.26,
#     "altitude": 1655,
#     "timeZone": "America_Denver"
# }"
# print strng
