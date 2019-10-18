#SERVER
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname("")
port=5000
s.bind((host,port))
s.listen(5)

while True:
    c, addr=s.accept()
    print(f"got connected to {addr}")
    c.send(bytes("Hi this message is from Server", "utf-8 "))
