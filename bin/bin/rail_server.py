import socket

def decrypt_rail_fence_cipher(ciphertext, rails):
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction_down = None
    row, col = 0, 0
    
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1
    
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1
    
    decrypted = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        if rail[row][col] != '\n':
            decrypted.append(rail[row][col])
            col += 1
        row += 1 if direction_down else -1
    
    return ''.join(decrypted)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

ciphertext = conn.recv(1024).decode()
rails = int(conn.recv(1024).decode())

decrypted_message = decrypt_rail_fence_cipher(ciphertext, rails)
print(f"Decrypted message: {decrypted_message}")

conn.close()
