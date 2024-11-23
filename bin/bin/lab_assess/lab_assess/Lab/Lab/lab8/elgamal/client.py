import socket

def start_client(host='127.0.0.1',port=65432):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host,port))
        # mess="hello, server!"
        # client_socket.sendall(mess.encode())

        response = client_socket.recv(1024)
        print(response.decode())
        e1,e2,p =(int(x) for x in response.decode().split(','))
        r=4
        P = 7
        c1 = pow(e1,r)%p
        c2 = (pow(e2,r)*P)%p
        client_socket.sendall(f"{c1},{c2}".encode())

        
        # print(f"Reeived freom server:{response.decode()}")
        client_socket.close()

if __name__=="__main__":
    start_client()