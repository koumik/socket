import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("192.168.43.112",1234))
r=client.recv(1024)
client.close()

print("New Message=",r)
