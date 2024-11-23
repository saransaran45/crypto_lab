import socket
import random

def diffie_hellman_key_exchange(p, g):
    a = random.randint(1, p - 1)
    A = pow(g, a, p)
    return a, A

def compute_shared_secret(B, a, p):
    return pow(B, a, p)

def server():
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a base (g): "))
    a, A = diffie_hellman_key_exchange(p, g)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print("Server is listening...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    conn.send(f"{p},{g},{A}".encode())

    B = int(conn.recv(1024).decode())
    print(f"Received B (client's public value): {B}")

    shared_secret = compute_shared_secret(B, a, p)
    print(f"Shared secret computed on the server: {shared_secret}")

    conn.close()

if __name__ == "__main__":
    server()
