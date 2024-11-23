import socket
import random

def diffie_hellman_key_exchange(p, g):
    b = random.randint(1, p - 1)
    B = pow(g, b, p)
    return b, B

def compute_shared_secret(A, b, p):
    return pow(A, b, p)

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    data = client_socket.recv(1024).decode()
    p, g, A = map(int, data.split(','))
    print(f"Received p: {p}, g: {g}, A (server's public value): {A}")

    b, B = diffie_hellman_key_exchange(p, g)

    client_socket.send(str(B).encode())
    print(f"Sent B (client's public value): {B}")

    shared_secret = compute_shared_secret(A, b, p)
    print(f"Shared secret computed on the client: {shared_secret}")

    client_socket.close()

if __name__ == "__main__":
    client()
