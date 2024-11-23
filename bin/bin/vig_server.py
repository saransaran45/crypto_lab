import socket

def decrypt_vigenere_cipher(ciphertext, keyword):
    decrypted = []
    keyword_repeated = (keyword * ((len(ciphertext) // len(keyword)) + 1))[:len(ciphertext)]
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift_start = 65 if char.isupper() else 97
            key_char = ord(keyword_repeated[i].upper()) - 65  # Handle both lower and uppercase
            decrypted_char = chr((ord(char) - shift_start - key_char) % 26 + shift_start)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    
    return ''.join(decrypted)

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data from the client
ciphertext = conn.recv(1024).decode()
keyword = conn.recv(1024).decode()

# Decrypt the message
decrypted_message = decrypt_vigenere_cipher(ciphertext, keyword)
print(f"Decrypted message: {decrypted_message}")

# Close the connection
conn.close()
