import socket
import numpy as np
from sympy import mod_inverse

def matrix_mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det, mod)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    return (det_inv * adjugate) % mod

def encrypt(key_matrix, plaintext_matrix):
    mod = 26
    encrypted_matrix = (key_matrix @ plaintext_matrix) % mod
    return encrypted_matrix

def decrypt(key_matrix, ciphertext_matrix):
    mod = 26
    key_matrix_inv = matrix_mod_inverse(key_matrix, mod)
    decrypted_matrix = (key_matrix_inv @ ciphertext_matrix) % mod
    return decrypted_matrix

def get_key_matrix_from_text(key_text, size):
    key_vector = [ord(char) - ord('A') for char in key_text.upper() if char.isalpha()]
    
    if len(key_vector) != size * size:
        raise ValueError("The key text must have exactly {} characters.".format(size * size))
    
    key_matrix = np.array(key_vector).reshape(size, size)
    print(f"Generated Key Matrix ({size}x{size}):\n{key_matrix}")
    return key_matrix

def get_ciphertext_vector(size):
    ciphertext = input("Enter the ciphertext: ").upper()
    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
    
    while len(ciphertext_vector) % size != 0:
        ciphertext_vector.append(0)  
   
    ciphertext_matrix = np.array(ciphertext_vector).reshape(-1, size).T
    print(f"Ciphertext Matrix ({size}x{size}):\n{ciphertext_matrix}")
    
    return ciphertext_matrix

def handle_client(conn):
    with conn:
        print('Connected by', conn.getpeername())
        size = int(input("Enter matrix size (2 for 2x2 or 3 for 3x3): "))
        
        key_text = input("Enter key for Hill cipher ({} characters): ".format(size * size))
        key_matrix = get_key_matrix_from_text(key_text, size)

        if np.linalg.det(key_matrix) == 0:
            print("The key matrix is not invertible. Please provide a different matrix.")
            return
        
        encrypted_message = conn.recv(1024).decode()
        print(f"Received encrypted message: {encrypted_message}")

        ciphertext_matrix = get_ciphertext_vector(size)
        decrypted_matrix = decrypt(key_matrix, ciphertext_matrix)
        decrypted_text = ''.join(chr(num + ord('A')) for num in decrypted_matrix.T.flatten() if num >= 0).rstrip('A')
        
        print("Decrypted Matrix:")
        print(decrypted_matrix)
        print("Decrypted Text:", decrypted_text)

def start_server():
    host = '127.0.0.1'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print('Server is listening...')
        conn, addr = s.accept()
        handle_client(conn)

if __name__ == "__main__":
    start_server()
