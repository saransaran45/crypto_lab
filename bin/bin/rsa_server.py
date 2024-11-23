import socket
import random
from math import gcd

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def mod_inverse(e, phi):
    d = 0
    x1, x2, x3 = 1, 0, phi
    y1, y2, y3 = 0, 1, e
    while y3 != 1:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    return y2 % phi

def generate_keypair():
    primes = [i for i in range(100, 1000) if is_prime(i)]
    p = random.choice(primes)
    q = random.choice(primes)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n)) 

def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

def server():
    public_key, private_key = generate_keypair()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen(1)
    print("Server is listening...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    conn.send(f"{public_key[0]},{public_key[1]}".encode())

    encrypted_message = int(conn.recv(1024).decode())
    print(f"Received encrypted message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"Decrypted message: {decrypted_message}")

    conn.close()

if __name__ == "__main__":
    server()
