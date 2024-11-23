# import socket
# from ceaser import *

# def start_client(host='localhost', port=12345):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         client_socket.connect((host, port))
#         message = "Hello, Server!"
#         message=encryption(message)
#         client_socket.sendall(message.encode())
#         data = client_socket.recv(1024)
#         print(f"Received from server: {decryption(data.decode())}")

# if __name__ == "__main__":
#     start_client()

import socket
from ceaser import encryption, decryption

def start_client(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        while True:
            try:
                message = input("Enter the message=")
                encrypted_message = encryption(message)
                client_socket.sendall(encrypted_message.encode())
                data = client_socket.recv(1024)
                print(f"Received from server: {decryption(data.decode())}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    start_client()
