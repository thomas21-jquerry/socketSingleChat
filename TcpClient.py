import socket

s = socket.socket()
port = 1234
s.connect((socket.gethostname(),port))
msg = s.recv(1024)
print(msg.decode('utf-8'))
s.close()