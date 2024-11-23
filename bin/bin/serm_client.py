import socket

def main():
    host = '127.0.0.1'  
    port = 65432       

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        a = int(input("Enter an integer a: "))
        p = int(input("Enter a prime number p: "))
        
        client_socket.sendall(f"{a},{p}".encode())
        data = client_socket.recv(1024)
        print("Received from server:", data.decode())

if __name__ == "_main_":
    main()