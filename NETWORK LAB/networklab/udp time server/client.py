import socket
from time import gmtime, strftime

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
      data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
      if data=="getTime":
         print "received request from:", addr
         time=strftime("%Y-%m-%d %H:%M:%S", gmtime())
         sock.sendto(time, addr)
      
