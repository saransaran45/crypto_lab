import socket
def main():
    host = '127.0.0.1'  
    port = 65432      

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        a = int(input("Enter the first integer (a): "))
        b = int(input("Enter the second integer (b): "))
        data_to_send = f"{a},{b}"
        client_socket.sendall(data_to_send.encode())
        response = client_socket.recv(1024).decode()
        print("Received from server:", response)

if __name__ == "_main_":
    main()