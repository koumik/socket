import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("192.168.2.140",1234)
server.accept(5)
clent,addr=server.accept()
file_name=client.recv(1024)
f=open(file_name,"wb")
data=client.recv(1024)
while(len(data)!=0):
 f.write(data)
 data=client.recv(1024)

print "file received" 

f.close()

