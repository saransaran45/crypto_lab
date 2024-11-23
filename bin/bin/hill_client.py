import socket
import numpy as np

def encrypt(key_matrix, plaintext_matrix):
    mod = 26
    encrypted_matrix = (key_matrix @ plaintext_matrix) % mod
    return encrypted_matrix

def get_key_matrix_from_text(key_text, size):
    key_vector = [ord(char) - ord('A') for char in key_text.upper() if char.isalpha()]
    
    if len(key_vector) != size * size:
        raise ValueError("The key text must have exactly {} characters.".format(size * size))
    
    key_matrix = np.array(key_vector).reshape(size, size)
    print(f"Generated Key Matrix ({size}x{size}):\n{key_matrix}")
    return key_matrix

def get_plaintext_vector(size):
    plaintext = input("Enter the plaintext: ").upper()
    plaintext = ''.join(filter(str.isalpha, plaintext))
    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    
    while len(plaintext_vector) % size != 0:
        plaintext_vector.append(0)  # Padding with 0 (equivalent to 'A')
    
    plaintext_matrix = np.array(plaintext_vector).reshape(-1, size).T
    print(f"Plaintext Matrix ({size}x{size}):\n{plaintext_matrix}")
    
    return plaintext_matrix

def main():
    size = int(input("Enter the size of the key matrix (e.g., 3 for a 3x3 matrix): "))
    
    key_text = input("Enter key for Hill cipher ({} characters): ".format(size * size))
    key_matrix = get_key_matrix_from_text(key_text, size)

    plaintext_matrix = get_plaintext_vector(size)
    encrypted_matrix = encrypt(key_matrix, plaintext_matrix)
    encrypted_text = ''.join(chr(num + ord('A')) for num in encrypted_matrix.T.flatten() if num >= 0)
    
    print("Encrypted Matrix:")
    print(encrypted_matrix)
    print("Encrypted Text:", encrypted_text)

    # Send the encrypted message to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 65432))
        s.sendall(encrypted_text.encode())

if __name__ == "__main__":
    main()