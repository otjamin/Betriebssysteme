import os
import socket
import json

from struct import pack, unpack


HOST = "localhost"
PORT = 50007


clear = lambda: os.system("cls" if os.name == "nt" else "clear")


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Connected to calculator server.")
        
        data = s.recv(1024)
        if not data:
            print("No ops available. Exiting.")
            return
        
        ops = json.loads(data.decode())

        while True:
            print_menu(ops)
            selected_op = int(input("Select operation: "))
            s.sendall(pack("<h", selected_op))

            if selected_op == 0:
                break

            op1 = input("Enter first operand: ")
            op2 = input("Enter second operand: ")

            if selected_op < 10:
                s.sendall(pack("<i", int(op1)))
                s.sendall(pack("<i", int(op2)))

                result = s.recv(1024)
                print("Result:", unpack("<i", result)[0])
            else:
                s.sendall(op1.encode())
                s.sendall(op2.encode())

                result = s.recv(1024)
                print("Result:", result.decode())

            input("Press Enter to continue.")


def print_menu(ops):
    clear()
    print("Available ops:")
    for op, desc in ops.items():
        print(f"{op}: {desc}")


if __name__ == "__main__":
    start_client()
