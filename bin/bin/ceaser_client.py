import socket

def encrypt_caesar_cipher(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():
            shift_start = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_start + shift) % 26 + shift_start)
        else:
            encrypted += char
    return encrypted



cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cs.connect(('localhost',12345))

mes = input("Enter the mes to encrypt:")
shift = int(input("Enter the shift amount:"))

enc = encrypt_caesar_cipher(mes,shift)
print(f"Enc :{enc}")
cs.send(enc.encode())
cs.send(str(shift).encode())

cs.close()
