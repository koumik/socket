import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=1234

s.connect((host,port))
s.sendall("Yo Fucker")
data=s.recv(1024)
s.close()

print('AA Geya Behenchod',repr(data))
