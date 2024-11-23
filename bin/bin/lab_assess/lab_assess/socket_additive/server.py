import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host='127.0.0.1'

port=12345

server_socket.bind((host,port))

server_socket.listen(5)

print(f"Server listening on {host}:{port}")
try:
    client_socket,addr=server_socket.accept()
    print(f"Got a connection from {addr}")
    client_socket.send(b"connection established.Please send your message!")

    while True:

        data=client_socket.recv(1024).decode()
        print(f"Received from client:{data}")
        data=input("Enter the message:")
        # client_socket.send(b"Data received by server!")
        client_socket.send(data.encode())

except KeyboardInterrupt:
    print("\nServer is shutting Down...")

finally:
    if client_socket:
        client_socket.close()

    server_socket.close()
    print("connection closed")