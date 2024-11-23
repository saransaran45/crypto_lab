import socket

def encrypt_rail_fence_cipher(plaintext, rails):
    rail = [['\n' for _ in range(len(plaintext))] for _ in range(rails)]
    direction_down = False
    row, col = 0, 0
    
    for char in plaintext:
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        rail[row][col] = char
        col += 1
        row += 1 if direction_down else -1
    
    encrypted = []
    for i in range(rails):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                encrypted.append(rail[i][j])
    
    return ''.join(encrypted)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

message = input("Enter the message to encrypt: ")
rails = int(input("Enter the number of rails: "))

encrypted_message = encrypt_rail_fence_cipher(message, rails)

client_socket.send(encrypted_message.encode())
client_socket.send(str(rails).encode())

client_socket.close()
