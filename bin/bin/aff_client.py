import socket

def encrypt_affine_cipher(plaintext, a, b):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_start = 65 if char.isupper() else 97
            encrypted += chr(((a * (ord(char) - shift_start) + b) % 26) + shift_start)
        elif char.isdigit():
            encrypted += str((a * int(char) + b) % 10)
        else:
            encrypted += char
    return encrypted

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

message = input("Enter the alphanumeric message to encrypt: ")
a = int(input("Enter the multiplicative key (a): "))
b = int(input("Enter the additive key (b): "))

if a % 2 == 0 or a % 13 == 0:
    print("The multiplicative key 'a' is not coprime with 26, please choose a different value for 'a'.")
else:
    encrypted_message = encrypt_affine_cipher(message, a, b)

    client_socket.send(encrypted_message.encode())
    client_socket.send(str(a).encode())
    client_socket.send(str(b).encode())

    client_socket.close()
