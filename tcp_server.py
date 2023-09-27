#! /usr/bin/python3

tcp_ip = "ip address"
tcp_port = 'port number'
buffer_size = 'any number'

# creating a socket
s= sockei.socket(socket.AF_INET, socket.SOCK_STREAM)

# coverting the socket to a server so as to listen for incoming connections.
s.listen(1)

#waits for an incoming connections so as to accept it and stores it in the connection and the client ip address.
conn,addr = s.accept()

#prints out the client address
print(addr)

#This while loop receives the data in small chunks and then resends it
while 1:
  
  data = conn.recv(buffer_size)
  if not data:
    break
  print("received data",data)
  conn.send(data)  # send back the data to the client
conn.close

