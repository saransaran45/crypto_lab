
def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key_length = len(key)
    
    for i, letter in enumerate(plaintext):
        if letter.isalpha():  
            shift = ord(key[i % key_length].lower()) - ord('a')
            if letter.islower():
                encrypted_text.append(chr((ord(letter) - ord('a') + shift) % 26 + ord('a')))
            else:
                encrypted_text.append(chr((ord(letter) - ord('A') + shift) % 26 + ord('A')))
        else:
            encrypted_text.append(letter)  
    return ''.join(encrypted_text)


def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_length = len(key)
    
    for i, letter in enumerate(ciphertext):
        if letter.isalpha():  
            shift = ord(key[i % key_length].lower()) - ord('a')
            if letter.islower():
                decrypted_text.append(chr((ord(letter) - ord('a') - shift) % 26 + ord('a')))
            else:
                decrypted_text.append(chr((ord(letter) - ord('A') - shift) % 26 + ord('A')))
        else:
            decrypted_text.append(letter)  
    
    return ''.join(decrypted_text)

# Example usage
plaintext = "Hello World"
key = "KEY"

encrypted = vigenere_encrypt(plaintext, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Original text:", plaintext)
print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)
