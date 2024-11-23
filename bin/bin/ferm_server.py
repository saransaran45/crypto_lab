import socket

def fermat_little_theorem(a, p):
    if p <= 1 or a % p == 0:
        return None, False  
    result = pow(a, p - 1, p)
    
    is_a_prime = (result == 1)
    return result, is_a_prime

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
                p = int(params[1].strip())
                
                print(f"Received parameters: a = {a}, p = {p}")
                result, is_a_prime = fermat_little_theorem(a, p)
                if result is None:
                    response = "Not a Prime"
                else:
                    print(f"Calculating Fermat's Little Theorem: {a}^{p-1} mod {p}")
                    primality = "is a prime." if is_a_prime else "is not a prime."
                    response = (f"Fermat's Little Theorem: {a}^{p-1} ≡ {result} (mod {p}) "
                                f"And {a} {primality}")

                conn.sendall(response.encode())

if __name__ == "_main_":
    main()