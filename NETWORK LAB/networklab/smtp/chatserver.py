import socket
import select
import sys
from _thread import *
##from threading import *
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

##if len(sys.argv) != 2:
  ##  print ("Correct usage: script, port number")
   ## exit()
lis={"ben":"hur","bbr":"20"}
IP_address ='127.0.0.1'
Port = 5000##int(sys.argv[1])
server.bind((IP_address, Port))
server.listen(100)
# verify=False 
listofmsg=[] 
def clientthread(conn, addr):
    login=conn.recv(1024).decode()
    print ("login:",login)
    verify=False
    if int(login) == 0:
        uname=conn.recv(1024).decode()
        passw=conn.recv(1024).decode()
        print("uname:",uname," passw: ",passw)
        if uname in lis:
            if lis[uname]==passw:
                conn.send("202".encode())
                verify=True
            else:
                conn.send("404".encode())
        else:
            conn.send("500".encode())        
 
    while verify:
            try:
                choice = int(conn.recv(2048))
                if choice==1:
                    to=conn.recv(1024).decode()
                    tomsg=conn.recv(2048).decode()
                    save="From:"+uname+" To:"+to+" Message: "+tomsg
                    listofmsg.append(save)
                    print (len(listofmsg))
                elif choice==2:
                    l=len(listofmsg)
                    l=str(l)
                    conn.send(l.encode())
                    for i in range(0,len(listofmsg)-1):
                        if ("To:"+uname) in listofmsg[i]:
                            print (listofmsg[i])
                            conn.send(listofmsg[i].encode())
                        else:
                            print("Inbox empty")    
                elif choice==3:
                    verify=False
                    print (uname," logged out successfully")
                else:
                    print ("Invalid choice" )
            except:
                continue
 
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print (addr[0] + " connected")
    start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()





