import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 1233
BUFFER_SIZE = 1024
MESSAGE = b"0993651"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
    time.sleep(2)
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    # s.close()
    print("received data: {}".format(data))