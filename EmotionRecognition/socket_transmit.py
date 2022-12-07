import socket

host = '6c:79:b8:a9:45:7b'
#port = 1

for port in range(100):
    try:
        sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        sock.connect((host, port))
        print("~~~ Connection successful on port "+str(port)+ " ~~~")
    except:
        print("Connection failed on port "+str(port))
        

# s_sock = sock.accept()
# print ("Accepted connection from "+s_sock)

# data = s_sock.recv(1024)
# print ("received [%s]" % data)

# sock.listen(1)