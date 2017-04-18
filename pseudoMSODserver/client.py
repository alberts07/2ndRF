import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)

serverIP = "128.138.65.210"

port = 18997

if sock.connect((serverIP,port)):
    print("connected")

sock.send("2ndRF")

resp = sock.recv(1024)

print(resp)

sock.close()
