import socket
import select
import sys
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if len(sys.argv) != 2:
#     print "Correct usage: script, port number"
#     exit()
IP_address = socket.gethostbyname(socket.gethostbyname())#str(sys.argv[1])
Port = 5000#int(sys.argv[1])
server.connect((IP_address, Port))
server.send("temp.txt")
flag=True
outfile=open("a"+"temp.txt","w")
size=0
while flag:
 
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    
    
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            #print message
            message=message.split(":")
            print message[0]
            size=int(message[1].strip())
            while size>0:
               message = socks.recv(2048)
               outfile.write(message)
               size=size-2048
            flag=False
            break
           
            if message.strip()=="File Not Found":
               flag=False
               break
outfile.close()
server.close()
