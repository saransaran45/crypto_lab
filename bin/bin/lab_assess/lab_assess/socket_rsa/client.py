import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host='127.0.0.1'
port=12345

client_socket.connect((host,port))
e,n=client_socket.recv(1024).decode().split(",")
e=int(e)
n=int(n)
d=37
def encrypt(mess):
    ans=""
    for i in mess:
        temp=ord(i)-ord('a')
        c=pow(temp,e,n)
        ans+=chr(c+ord('a'))
    return ans

def decrypt(mess):
    ans=""
    for i in mess:
        temp=ord(i)-ord('a')
        c=pow(temp,d,n)
        ans+=chr(c+ord('a'))
    return ans

try:
    q=11
    while True:
        mess=input("Enter the message")
        if mess.lower()=='exit':
            break
        mess=encrypt(mess)
        client_socket.send(mess.encode())
        response=client_socket.recv(1024).decode()
        print(f"Response from server: {decrypt(response)}")

except KeyboardInterrupt:
    print("Shutting down")

finally:
    client_socket.close()