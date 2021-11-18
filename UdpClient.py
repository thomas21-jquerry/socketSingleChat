import socket
c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = "hello India"
data = data.encode("utf-8")
c.sendto(data,(socket.gethostname(),1234))
data,addr = c.recvfrom(1024)
data = data.decode('utf-8')
print(data)