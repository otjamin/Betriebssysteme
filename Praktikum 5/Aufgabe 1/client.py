# Echo client program
import socket
import struct

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        number_to_send = struct.pack('<h', int(input()))
        s.sendall(number_to_send)

        data = s.recv(1024)
        print('Received {}'.format(struct.unpack('<h', data)[0]))

#     s.sendall(b'Hello, world')
#     data = s.recv(1024)
# print('Received', repr(data))