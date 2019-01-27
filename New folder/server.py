import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.0.103",12345))
s.listen(5)
while True:
    c,a=s.accept()
    c.send("Hello")
    c.close()
    print("Message sent")
    
