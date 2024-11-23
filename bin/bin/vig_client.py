import socket

def encrypt_vigenere_cipher(plaintext, keyword):
    encrypted = []
    keyword_repeated = (keyword * ((len(plaintext) // len(keyword)) + 1))[:len(plaintext)]
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift_start = 65 if char.isupper() else 97
            key_char = ord(keyword_repeated[i].upper()) - 65
            encrypted_char = chr((ord(char) - shift_start + key_char) % 26 + shift_start)
            encrypted.append(encrypted_char)
        else:
            encrypted.append(char)
    
    return ''.join(encrypted)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

message = input("Enter the message to encrypt: ")
keyword = input("Enter the keyword: ")

encrypted_message = encrypt_vigenere_cipher(message, keyword)

client_socket.send(encrypted_message.encode())
client_socket.send(keyword.encode())

client_socket.close()
