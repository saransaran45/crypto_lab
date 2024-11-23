import socket

def main():
    host = '127.0.0.1'  
    port = 65432        

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
    
        a = int(input("Enter an integer a (must be coprime with n): "))
        n = int(input("Enter a positive integer n: "))

        client_socket.sendall(f"{a},{n}".encode())
        response = client_socket.recv(1024).decode()
        print("Received from server:", response)

if __name__ == "_main_":
    main()