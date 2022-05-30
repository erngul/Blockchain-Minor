# import socket
#
#
# TCP_IP = '127.0.0.1'
# TCP_PORT = 5015
# BUFFER_SIZE = 20  # Normally 1024, but we want fast response
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((TCP_IP, TCP_PORT))
# s.listen(2)
# while True:
#     conn, addr = s.accept()
#     print('server - connection address: {}'.format(addr))
#     while 1:
#         data = conn.recv(BUFFER_SIZE)
#         if not data: break
#         print("server - received data: {}".format(data))
#         conn.send(data)  # echo
#
# conn.close()


import socket, pickle
import os
from _thread import *
from Transaction import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    while True:
        print('connected')
        data = connection.recv(2048)
        inputs = pickle.loads(data)
        print(inputs)
        data = connection.recv(2048)
        outputs = pickle.loads(data)
        print(outputs)
        data = connection.recv(2048)
        sigs = pickle.loads(data)
        print(sigs)
        data = connection.recv(2048)
        reqd = pickle.loads(data)
        print(reqd)
        tx = Tx()
        tx.inputs = inputs
        tx.outputs = outputs
        tx.sigs = sigs
        tx.reqd = reqd
        check = tx.is_valid()
        print(check)

        reply = check
        if check:
            connection.sendall(bytes('1','utf-8'))
        else:
            connection.sendall(bytes('0','utf-8'))
        connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()