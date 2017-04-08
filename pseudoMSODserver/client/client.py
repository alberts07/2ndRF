import socket

# Set up the socket for the client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
print("socket made")

serverIP = "192.168.1.100" #socket.gethostbyaddr("128.138.65.210")
print("Server IP: " +serverIP)

port = 18999 # This is just a random port chosen to try to avoid other used ones
print("Port: " + str(port))

sock.connect((serverIP, port))
print("connected")

sock.send("2ndRF")
print("Sent --> 2ndRF")

resp = sock.recv(1024)
print(resp)


sock.close()
