import socket

def decrypt_caesar_cipher(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            shift_start = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift_start - shift) % 26 + shift_start)
        else:
            decrypted += char
    return decrypted



ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(('localhost',12345))
ss.listen(1)

conn,addr = ss.accept()
print(f"Connected by {addr}")

ct = conn.recv(1024).decode()
shift = int(conn.recv(1024).decode())

dec = decrypt_caesar_cipher(ct,shift)
print(f"Dec : {dec}")

conn.close()
