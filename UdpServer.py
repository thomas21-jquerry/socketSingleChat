import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((socket.gethostname(),1234))
data,addr = s.recvfrom(1024)
data = data.decode("utf-8")
print(data)
data = "helloWorld"
data = data.encode("utf-8")
s.sendto(data,addr)