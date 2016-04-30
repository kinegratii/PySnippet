import socket
import sys
import random
import threading

local_address = '127.0.0.1', 9005

remote_address = '127.0.0.1'

remote_address = sys.argv[1]

connect_port = int(sys.argv[2])

mode = sys.argv[3]



socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(local_address)
socket.connect((remote_address,connect_port))
if mode == 'read':
    while True:
        try:
            data = socket.recv(1024)
            print 'recv data ', data
        except Exception:
            pass
else:
    while True:
        try:
            data = str(random.randint(0,10))
            socket.sendall(data)
            threading.sleep(3)
        except Exception:
            pass

