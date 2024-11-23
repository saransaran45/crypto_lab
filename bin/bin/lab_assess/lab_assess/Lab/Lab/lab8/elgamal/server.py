import socket

def mod_inv(b,a):
    n=a
    if b==0:
        return
    # print(a,b)
    q=a//b
    # print(q)
    r=a%b
    t1=0
    t2=1
    t=t1-t2*q
    a,b=b,r
    print(f"{q} {a} {b} {r} {t1} {t2} {t}")
    while b!=0:
        q=a//b
        r=a%b
        t1=t2
        t2=t
        t=t1-t2*q
        a,b=b,r
        print(f"{q} {a} {b} {r} {t1} {t2} {t}")
    if t2<0:
        t2=n+t2
    return t2

def start_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        e1 = 2
        p=11
        d=3
        e2 = pow(e1,d)%p

        print(f"Server listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")

            # while True:
            response = f"{e1},{e2},{p}"
            conn.sendall(response.encode())
            #sent the values to client
            data = conn.recv(1024)
            # if not data:
            #     break

            print(f"Received from client: {data.decode()}")
            c1,c2 = (int(x) for x in data.decode().split(','))
            inv = mod_inv(p,pow(c1,d))
            P = (c2*inv)%p
            print("The plain text is: ",P)
            # response = "Message received"
            # conn.sendall(response.encode())

            
                

if __name__ == "__main__":
    start_server()


# import socket

# def mod_inv(b, a):
#     n = a
#     if b == 0:
#         return None
#     q = a // b
#     r = a % b
#     t1 = 0
#     t2 = 1
#     t = t1 - t2 * q
#     a, b = b, r
#     while b != 0:
#         q = a // b
#         r = a % b
#         t1, t2 = t2, t
#         t = t1 - t2 * q
#         a, b = b, r
#     if t2 < 0:
#         t2 = n + t2
#     return t2

# def start_server(host='127.0.0.1', port=65432):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.bind((host, port))
#         server_socket.listen()
#         e1 = 2
#         p = 11
#         d = 3
#         e2 = pow(e1, d) % p

#         print(f"Server listening on {host}:{port}")
        
#         conn, addr = server_socket.accept()
#         with conn:
#             print(f"Connected by {addr}")

#             while True:
#                 response = f"{e1},{e2},{p}"
#                 conn.sendall(response.encode())
                
#                 try:
#                     data = conn.recv(1024)
#                     if data is None:
#                         print("No data received, closing connection.")
#                         break

#                     print(f"Received from client: {data.decode()}")
#                     c1, c2 = (int(x) for x in data.decode().split(','))
#                     inv = mod_inv(p, pow(c1, d))
#                     if inv is None:
#                         print("Modular inverse calculation failed.")
#                         continue
                    
#                     P = (c2 * inv) % p
#                     print("The plain text is: ", P)

#                 except Exception as e:
#                     print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     start_server()
