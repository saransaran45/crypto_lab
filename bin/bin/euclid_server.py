import socket
def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    gcd, s1, t1 = extended_euclidean(b % a, a)
    s = t1 - (b // a) * s1
    t = s1
    print(f"Calculating: gcd({a}, {b}) -> gcd: {gcd}, s: {s}, t: {t}")
    return gcd, s, t

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
            data = conn.recv(1024).decode()
            a, b = map(int, data.split(','))

            print(f"Received a: {a}, b: {b}")
            gcd, s, t = extended_euclidean(a, b)
            response = f"GCD: {gcd}, s: {s}, t: {t}"
            conn.sendall(response.encode())
            print(f"GCD of {a} and {b} is {gcd}")
            print(f"Coefficients: s = {s}, t = {t}")

if __name__ == "_main_":
    main()
