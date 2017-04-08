

import socket
import locMessage




def putFile(buff, ip, port):
    # First connect to the server, then send the message
    sock.connect((ip,port))
    sock.send(buff)

    # Wait for the response from the server indicating it's ready
    while true:
        buff = sock.recv(1024) 
        if buff[0:5] == "READY":
            sendStr = locMessage.locMessage()###################################3333
            # print "sending" + sendStr
            # send the file
            sock.send(sendStr)
            break
        elif buff[0:5] == "ERROR":
            print "There was an error on the server."

def setupClient():
    # Tell the server to prepare to receive a file.
    sock = socket.socket()
    hostIp = socket.gethostname()
    port = 8999 # This is just a random port
    
    outFilename = "data.json"
    buff = "PUT " + outFilename
    putFile(buff, hostIp, port)
    
    # Now wait to receive another response
    buff = sock.recv(1024)
    # print buff

def killClient(fp, sock):
    fp.close()
    sock.close()
