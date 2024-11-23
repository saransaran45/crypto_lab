import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    data = client_socket.recv(1024).decode()
    p, g, y = map(int, data.split(','))
    
    m = int(input("Enter the message (as an integer): "))
    client_socket.send(str(m).encode())

    c1, c2 = map(int, client_socket.recv(1024).decode().split(','))
    print(f"Ciphertext: c1 = {c1}, c2 = {c2}")

    client_socket.close()

if __name__ == "__main__":
    client()
