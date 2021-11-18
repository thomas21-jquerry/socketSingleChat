import socket

s = socket.socket()
print("server")
port = 1234
s.bind((socket.gethostname(),port))
s.listen(5)
k,a = s.accept()
print("connection has been established from  `${a}`")
k.send(bytes("hello", "utf-8"))
k.close()