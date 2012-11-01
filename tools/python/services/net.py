#!/usr/bin/env python
#This is a simplest tcp-echo-server, only support one client connection
import socket, sys

class Net:
    """net event-driven engine."""
    def __init__(self)


reply=1
HOST="0.0.0.0" #localhost
PORT=5000
if len(sys.argv) >; 1:
    PORT = int(sys.argv[1])

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysocket.bind((HOST, PORT))
except socket.error:
    sys.exit("Call to bind failed, may be program already running or other program is using %d port" % PORT)

while 1:
    print 'Waitting for connection'
    mysocket.listen(1)

    conn, addr = mysocket.accept()
    print 'Connection received from:', addr[0], addr[1]
    packet = conn.recv(1024)

    if packet[:8] == 'shutdown':
        conn.close()
        break

    if reply:
        conn.send("Server Echo:\n" + packet)

    conn.close()

print 'Server shutdown....'
mysocket.close()
sys.exit(0)


def EchoServer(stream):
    stream.write("asddsf\n\n")
    stream.on

if __name__ == "__main__":
    net = Net()

    net.createServer()
