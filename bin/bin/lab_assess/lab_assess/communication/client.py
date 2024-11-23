# import socket

# host='127.0.0.1'
# port=12345

# client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# client_socket.connect((host,port))

# while True:
#     message=input("Enter a message:")
#     client_socket.send(message.encode())
#     message=client_socket.recv(1024).decode()
#     print(message)

import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=12345

client_socket.connect((host,port))
try:
    while True:
        message=input("Enter the message:")
        client_socket.send(message.encode())
        message=client_socket.recv(1024).decode()
        print(message)
except KeyboardInterrupt:
    print("shutting down")

finally:
    client_socket.close()

