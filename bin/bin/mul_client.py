import socket

def encrypt_multiplicative_cipher(plaintext, key):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_start = 65 if char.isupper() else 97
            encrypted += chr(((ord(char) - shift_start) * key) % 26 + shift_start)
        else:
            encrypted += char
    return encrypted

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

message = input("Enter the message to encrypt: ")
key = int(input("Enter the multiplicative key: "))

if key % 2 == 0 or key % 13 == 0:
    print("Key is not coprime with 26, choose a different key.")
else:
    encrypted_message = encrypt_multiplicative_cipher(message, key)

    client_socket.send(encrypted_message.encode())
    client_socket.send(str(key).encode())

    client_socket.close()
