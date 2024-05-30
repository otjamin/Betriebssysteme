import socket
import json
import multiprocessing

from struct import pack, unpack


HOST = "localhost"
PORT = 50007

OPCODES = {
    "1": "Add two numbers",
    "2": "Multiply two numbers",
    "11": "Concatenate two strings",
    "0": "Exit"
}

def handle_client(conn):
    with conn:
        conn.sendall(json.dumps(OPCODES).encode())
        
        while True:
            data = conn.recv(1024)

            selected_op = unpack("<h", data)[0]
            if selected_op == 0:
                print("Client requested to exit.")
                break

            elif selected_op < 10:
                op1 = unpack("<i", conn.recv(1024))[0]
                op2 = unpack("<i", conn.recv(1024))[0]

                match selected_op:
                    case 1:
                        result = op1 + op2
                    case 2:
                        result = op1 * op2
                
                conn.sendall(pack("<i", result))

            else:
                op1 = conn.recv(1024).decode()
                op2 = conn.recv(1024).decode()

                match selected_op:
                    case 11:
                        result = op1 + op2

                conn.sendall(result.encode())


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            proc = multiprocessing.Process(target=handle_client, args=(conn,))
            proc.start()
            print("Delegated to process", proc.pid)


if __name__ == "__main__":
    start_server()
