import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=1111
s.bind((host,port))
s.listen(5)
c,a=s.accept()
while True:
    data=c.recv(1024)
    if not data:
        break
    c.sendall(data)
c.close()
