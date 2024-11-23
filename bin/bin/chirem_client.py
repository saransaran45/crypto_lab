import socket

def main():
    host = '127.0.0.1'  
    port = 65432        

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        n = int(input("Enter the number of equations: "))
        a_list = []
        n_list = []
        
        for i in range(n):
            a = int(input(f"Enter a{i + 1} (remainder): "))
            n = int(input(f"Enter n{i + 1} (modulus): "))
            a_list.append(a)
            n_list.append(n)
        data_to_send = ';'.join([f"{a},{n}" for a, n in zip(a_list, n_list)])
        client_socket.sendall(data_to_send.encode())
        response = client_socket.recv(1024).decode()
        print("Received from server:", response)

if __name__ == "_main_":
    main()