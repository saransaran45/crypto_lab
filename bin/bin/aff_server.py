import socket

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def decrypt_affine_cipher(ciphertext, a, b):
    decrypted = ""
    a_inverse = mod_inverse(a, 26)
    if a_inverse is None:
        return "Modular inverse not found, decryption impossible"
    
    for char in ciphertext:
        if char.isalpha():
            shift_start = 65 if char.isupper() else 97
            decrypted += chr((a_inverse * ((ord(char) - shift_start) - b)) % 26 + shift_start)
        elif char.isdigit():
            decrypted += str((a_inverse * (int(char) - b)) % 10)
        else:
            decrypted += char 
    return decrypted

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

ciphertext = conn.recv(1024).decode()
a = int(conn.recv(1024).decode())
b = int(conn.recv(1024).decode())

decrypted_message = decrypt_affine_cipher(ciphertext, a, b)
print(f"Decrypted message: {decrypted_message}")

conn.close()
