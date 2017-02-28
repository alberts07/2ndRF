

from socket import *
import sys
import time

remoteIp = ''
lclHostPort = 8999
filename = ""
quit = 0

# Set up the socket
socket_object = socket(AF_INET, SOCK_STREAM, 0)
socket_object.bind((remoteIp,lclHostPort))
socket_object.listen(1)
print('Listening on port: ', lclHostPort)

# Keep the socket running until 'cntl-C' is received
while quit == 0:
    # Wait to accept a connection
    remote, address = socket_object.accept()
    print('Connected to ', address)

    while quit == 0:
        # print "Waiting for request"
        buffer = ""
        buffer = remote.recv(1024)

        # If the PUT command is received, prepare to receive the file name passed
        if buffer[0:3] == "PUT":
            if len(buffer) != 0:
                print "CMD: " + buffer[0:3]     # Prints the command
                print "Filename: " + buffer[4:]   # Prints the filename
            filename = buffer[4:]
            # fp = open(filename, "wb")
            if filename:
                print "file " + buffer[4:] + " opened"
                remote.send("READY")
                # fp.close()
            # If there was an error, print the buffer received and send 'ERROR'
            else:
                remote.send("ERROR")
                print buffer
        elif buffer[0:4] == "QUIT":
            print "Quit received, quitting the server."
            quit = 1
            break

        else:
            # Next should be the file, write the buffer to the file.
            fp = open(filename, "wb")
            fp.write(buffer)
            fp.close()
        remote.send("Rx'd file")

    remote.close()
    fp.close()
    socket_object.close()












        # elif not buffer:
        #     remote.send("ERROR")
        #     print "Did not receive anything."
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
