import socket

# AF_INET is an address family that is used to designate the type
# of addresses that your socket can communicate with
# (in this case, Internet Protocol v4 addresses).
# SOCK_STREAM is a constant indicating the type of socket
# (TCP), as opposed to SOCK_DGRAM (UDP).
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
