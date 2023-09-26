#! /usr/bin/python3

import socket #socket enables the connection between two divices so that they can be able to communicate.

ipaddr = input("Enter an ip address:") 

s = socket.socket() #associates the socket class to the variable s so that we dont have to reference the full socket name.

s.connect((ipaddr,22))#Socket is connected to a particular ip and port number. 

answer = s.recv(1024) # reads 24 bits of data from the socket and stores it the answer variable

print(answer) # displays info

s.close # connection closed