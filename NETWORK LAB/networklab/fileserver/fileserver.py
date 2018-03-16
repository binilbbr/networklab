
import socket
import select
import sys
from thread import *
import os.path
import os
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 

# if len(sys.argv) != 2:
#     print "Correct usage: script, port number"
#     exit()
 
IP_address = socket.gethostbyname(socket.gethostbyname())#str(sys.argv[1])
 
Port = 5000
server.bind((IP_address, Port))
server.listen(100)
 
list_of_clients = []
 
def clientthread(conn, addr):
 
    while True:
            try:
                message = conn.recv(2048)
                if message:
                    print "<" + addr[0] + "> " + message
                    message_to_send = ""
                    if os.path.exists(message.strip()):
                        reply= os.path.getsize(message.strip())
                        print reply
                        size=reply
                        s=str(os.getpid())
                        conn.send(s+":"+str(reply)+"\n")
                        infile=open(message,"r")
                        while size>0:
                           data=infile.read(2048)
                           conn.send(data)
                           size=size-2048
                        remove(conn)
                        break

                    else:
                        conn.send("File Not Found")
                    
 
                else:
                    remove(conn)
 
            except:
                continue


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
 
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print addr[0] + " connected"
    start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()
