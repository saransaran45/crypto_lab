import socket

def main():
    host = '127.0.0.1'  
    port = 65432        

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        a = int(input("Enter an integer a: "))
        rounds = int(input("Enter the number of rounds for the test: "))
        client_socket.sendall(f"{a},{rounds}".encode())
        response = client_socket.recv(1024).decode()
        print("Received from server:", response)

if __name__ == "_main_":
    main()