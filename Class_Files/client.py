#CLIENT
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostbyname(""),5000))

while True:
    msg=s.recv(128)
    print(msg.decode("utf-8"))
    break
