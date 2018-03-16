
import socket
import select
import sys

##if len(sys.argv) != 2:
##    print ("Correct usage: script, port number")
##    exit()

IP_address = '127.0.0.1'
Port = 5000##int(sys.argv[1])
login=0
while True:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((IP_address, Port))
    server.send(str(login).encode())
    if login==0:
        print("Please login")
        uname=input("Enter username: ")
        server.send(uname.encode())
        passw=input("Enter password: ")
        server.send(passw.encode())
        verify=server.recv(1024).decode()
        verify=int(verify)
        if verify==202:
            print ("successfully logged in")
            login=1
        elif verify==404:
            print ("password incorrect")

        elif verify==500:
            print ("invalid username")

    while login==1:
        print ("choice")
        print ("1.Send mail 2.check inbox 3.Logout")
        choice=input("Enter choice: ")
        choic=int(choice)
        if choic==1:
            server.send(choice.encode())
            to=input("Enter To mail id: ")
            server.send(to.encode())
            tomsg=input("Enter message: ")
            server.send(tomsg.encode())
        elif choic==2:
            server.send(choice.encode())
            l=server.recv(1024).decode()
            l=int(l)
            for i in range(0,l):
                content=server.recv(2048).decode()
                print(content)
        elif choic==3:
            server.send(choice.encode())
            login=0
            print ("successfully logged out")
        else:
            print ("Invalid choice")
    server.close()
