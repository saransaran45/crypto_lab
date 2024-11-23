import socket
import random

def generate_keys(p, g):
    x = random.randint(1, p - 2)
    y = pow(g, x, p)
    return x, y

def encrypt(p, g, y, m):
    k = random.randint(1, p - 2)
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    return c1, c2

def server():
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a base (g): "))
    x, y = generate_keys(p, g)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print("Server is listening...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    conn.send(f"{p},{g},{y}".encode())

    m = int(conn.recv(1024).decode())
    c1, c2 = encrypt(p, g, y, m)
    conn.send(f"{c1},{c2}".encode())

    conn.close()

if __name__ == "__main__":
    server()
