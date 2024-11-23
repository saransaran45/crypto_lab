import socket
from math import gcd

def euler_totient(n):
    result = n  
    p = 2      
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p  
        p += 1
    if n > 1:
        result -= result // n
    return result

def main():
    host = '127.0.0.1'  
    port = 65432        

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print("Server is listening...")
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                params = data.decode().split(',')
                a = int(params[0].strip())
                n = int(params[1].strip())
                print(f"Received parameters: a = {a}, n = {n}")

                if gcd(a, n) != 1:
                    response = f"The numbers {a} and {n} are not coprime. Euler's theorem cannot be applied."
                else:
                    phi_n = euler_totient(n)
                    response = f"Euler's theorem: {a}^{phi_n} ≡ 1 (mod {n})"
                conn.sendall(response.encode())

if __name__ == "_main_":
    main()