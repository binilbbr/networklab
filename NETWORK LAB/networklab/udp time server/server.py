import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "getTime"
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print "current time",data
