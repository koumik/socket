import socket
file_name="lolmanav.jpg"
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("192.168.43.112",456))
client.sendall(file_name)
f=open(file_name,"rb")
data=f.read(1024)
while(len(data)!=0):
 client.sendall(data)
 data=f.read(1024)

print "file sent successfully"
f.close()

 
 


