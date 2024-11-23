import socket
import random
import numpy

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host='127.0.0.1'
port=12345

# server_socket.bind((host,port))
# server_socket.listen(5)

# try:
#     while True:
#         client_socket,addr=server_socket.accept()
#         print(f"Connected to {addr}")
#         while True:
#             message = client_socket.recv(1024).decode()
#             print(message)
#             message=input("Enter a message:")
#             client_socket.send(message.encode())

# except KeyboardInterrupt:
#     print("Shutting down")


server_socket.bind((host,port))
server_socket.listen(5)

try:
    while True:
        client_socket,addr=server_socket.accept()
        print(f"Connected to {addr}")
        try:
            client_socket.settimeout(10)
            while True:
                message=client_socket.recv(1024).decode()
                print(message)
                message=input("Enter the message:")
                client_socket.send(message.encode())
        except KeyboardInterrupt:
            print("client disconnected")
        finally:
            client_socket.close()

except KeyboardInterrupt:
    print("Server disconnected")

finally:
    server_socket.close()