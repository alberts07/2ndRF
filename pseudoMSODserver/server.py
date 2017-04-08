

from socket import *
import sys
import time
import json


# Handle a local test
if len(sys.argv):
    if "--local" in sys.argv:
        A = {
                'mobility': 'Stationary',
                'messageType': 'Loc',
                'sensorKey': 846859034,
                'sensorId': '101010101',
                'altitude': 1659.8,
                'longitude': -105.157855,
                'environment': 'Outdoor',
                'version': '1.0.16',
                'time': 1455208202.250222,
                'latitude': 40.004285,
                'timeZone': 'America_Denver'
            }

        name = time.strftime('%Y%m%d_%H%M%S', time.gmtime(A['time']))
        # print (name)
        filename = "state_" + name[:13] + ".json"
        print (filename)
        with open(filename, "wb") as fp:
        # fp = open(filename, "wb")
            json.dump(A, fp)
        # fp.close()
        exit()


# Set up the server
remoteIp = ''
lclHostPort = 8999
filename = ""
quit = False

socket_object = socket(AF_INET, SOCK_STREAM, 0)
socket_object.bind((remoteIp,lclHostPort))
socket_object.listen(1)
print('Listening on port: ', lclHostPort)

# Keep the socket running until 'ctl-C' or EXIT is received
while quit == False:
    # Wait to accept a connection
    remote, address = socket_object.accept()
    print('Connected to ', address)

    # Maintain the connction until told to quit, this loop will exit first
    while quit == False:
        print "Waiting for request"
        buffer = ""
        buffer = remote.recv(1024)

        # If the PUT command is received, prepare to receive the file name passed
        if buffer[0:3] == "PUT":
            if len(buffer) != 0:
                print "CMD: " + buffer[0:3]     # Prints the command
                print "Filename: " + buffer[4:]   # Prints the filename
            filename = buffer[4:]

            if filename:
                print "file " + buffer[4:] + " opened"
                remote.send("READY")

            # If there was an error, print the buffer received and send 'ERROR'
            else:
                remote.send("ERROR")
                print buffer

        # Handle a command to quit the server
        elif buffer[0:4] == "QUIT":
            print "Quit received, quitting the server."
            quit = 1
            break

        # If something is received, it should be the file contents
        else:
            # Next should be the file, write the buffer to the file.
            if not len(buffer):
                print "ERROR: Received empty buffer."
                remote.send("ERROR Received empty buffer")
            else:
                # Get the time from the buffer, make a filename from it
                print "The time was: " + A['time']
                # seconds = A['time']/1000
                # name = time.strftime('%Y%m%d_%H%M', A[time], ms)
                fp = open(filename, "wb")
                fp.write(buffer)

                fp.close()
        remote.send("Rx'd file")

# Close the program down
remote.close()
fp.close()
socket_object.close()












   
