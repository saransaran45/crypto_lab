import socket
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"Inverse of {a} (mod {m}) does not exist.")
    return x % m

def chinese_remainder_theorem(a_list, n_list):
    M = 1
    for n in n_list:
        M *= n

    M_list = [M // n for n in n_list]
    inv_list = [mod_inverse(M_i, n) for M_i, n in zip(M_list, n_list)]
    
    result = sum(a * M_i * inv for a, M_i, inv in zip(a_list, M_list, inv_list))
    result %= M 
    return result, M, M_list, inv_list

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
            a_list, n_list = [], []
            data_parts = data.split(';')
            for part in data_parts:
                a, n = map(int, part.split(','))
                a_list.append(a)
                n_list.append(n)

            print(f"Received a_list: {a_list}, n_list: {n_list}")
            try:
                result, M, M_list, inv_list = chinese_remainder_theorem(a_list, n_list)
                steps = {
                    "M": M,
                    "M_list": M_list,
                    "inv_list": inv_list,
                    "result": result
                }
                response = f"CRT result: {result} (M = {M}, M_list = {M_list}, inv_list = {inv_list})"
                conn.sendall(response.encode())
                
                print("Calculation steps:")
                print(f"M: {M}")
                print(f"M_list: {M_list}")
                print(f"inv_list: {inv_list}")
                print(f"Final result: {result}")

            except Exception as e:
                conn.sendall(str(e).encode())
                print(str(e))

if __name__ == "_main_":
    main()
