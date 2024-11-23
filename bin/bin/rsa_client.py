import socket

def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    public_key_data = client_socket.recv(1024).decode()
    e, n = map(int, public_key_data.split(','))
    public_key = (e, n)
    print(f"Received public key: {public_key}")

    message = int(input("Enter the message (as an integer) to encrypt: "))

    encrypted_message = encrypt(message, public_key)
    print(f"Encrypted message: {encrypted_message}")

    client_socket.send(str(encrypted_message).encode())

    client_socket.close()

if __name__ == "__main__":
    client()
