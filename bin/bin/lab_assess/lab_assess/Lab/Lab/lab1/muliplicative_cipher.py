def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt_multiplicative_cipher(plaintext, key):
    if gcd(key, 26) != 1:
        raise ValueError("Key must be coprime to 26 for encryption.")
    
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr(((ord(char) - 65) * key) % 26 + 65)
            else:
                encrypted_char = chr(((ord(char) - 97) * key) % 26 + 97)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

def decrypt_multiplicative_cipher(ciphertext, key):
    #mod_inv = mod_inverse(key, 26)
    mod_inv = pow(key,-1,26)
    if mod_inv is None:
        raise ValueError("Multiplicative inverse does not exist. Decryption is not possible with this key.")
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr(((ord(char) - 65) * mod_inv) % 26 + 65)
            else:
                decrypted_char = chr(((ord(char) - 97) * mod_inv) % 26 + 97)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

plaintext = "HelloWorld"
key = 7  

ciphertext = encrypt_multiplicative_cipher(plaintext, key)
print(f"Ciphertext: {ciphertext}")

decrypted_text = decrypt_multiplicative_cipher(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")
