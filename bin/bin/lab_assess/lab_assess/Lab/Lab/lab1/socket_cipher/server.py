# import socket
# from ceaser import *
# def start_server(host='localhost',port=12345):
#     with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
#         server_socket.bind((host,port))
#         server_socket.listen()
#         print(f"server listening on {host}:{port}")

#         conn,addr=server_socket.accept()
#         with conn:
#             print(f"connected by {addr}")
#             while True:
#                 data =conn.recv(1024)
#                 if not data:
#                     break
#                 decrypted_data=decryption(data.decode())
#                 print(f"Received message: {decrypted_data}")
#                 encrypted_data=encryption(decrypted_data)
#                 conn.sendall(encrypted_data.encode())

# if __name__=="__main__":
#     start_server()

import socket
from ceaser import encryption, decryption

def start_server(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                try:
                    data = conn.recv(1024)
                    if not data:
                        break
                    decrypted_data = decryption(data.decode())
                    print(f"Received message: {decrypted_data}")
                    answer=input("Enter message=")
                    encrypted_data = encryption(answer)
                    conn.sendall(encrypted_data.encode())

                except Exception as e:
                    print(f"Error: {e}")
                    break

if __name__ == "__main__":
    start_server()

