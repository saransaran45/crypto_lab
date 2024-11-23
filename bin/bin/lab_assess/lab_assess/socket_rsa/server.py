import socket
import random
import math

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='127.0.0.1'
port=12345

def euler_totient(n):
    result=n
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            while n%i==0:
                n//=i
            result-=result//i
    if n>1:
        result-=result//n
    return result
        

server_socket.bind((host,port))
server_socket.listen(5)
print("Server is listening...")

def decrypt(mess):
    ans=""
    for i in mess:
        temp=ord(i)-ord('a')
        c=pow(temp,d,n)
        ans+=chr(c+ord('a'))
    return ans

def encrypt(mess):
    ans=""
    for i in mess:
        temp=ord(i)-ord('a')
        c=pow(temp,e,n)
        ans+=chr(c+ord('a'))
    return ans

try:
    while True:
        client_socket,addr=server_socket.accept()
        print(f"Connected to:{addr}")
        p,q=7,11
        n=p*q
        # e=random.randint(1,euler_totient(n))
        e=13
        d=37
        client_socket.send(f"{e},{n}".encode())
        while True:
            message=client_socket.recv(1024).decode()
            if not message:
                break
            message=decrypt(message)
            print(f"Received:{message}")
            message=input("Enter the message")
            message=encrypt(message)
            client_socket.send(message.encode())
        client_socket.close()
        print("Client disconnected.")
except KeyboardInterrupt:
    print("Shutting down")

finally:
    server_socket.close()
