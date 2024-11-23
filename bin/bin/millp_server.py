import socket
import random

def miller_rabin(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)  
        x = pow(a, d, n) 
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)  
            if x == n - 1:
                break
        else:
            return False  

    return True  

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
                rounds = int(params[1].strip())
                print(f"Received parameters: a = {a}, rounds = {rounds}")
                is_prime = miller_rabin(a, rounds)
                primality_result = "is probably prime." if is_prime else "is composite."
                response = f"The number {a} {primality_result} (after {rounds} rounds of testing)."
                conn.sendall(response.encode())

if __name__ == "_main_":
    main()
