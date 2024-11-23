def encrypt_caesar_cipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) + shift - 65) % 26 + 65)
            else:
                new_char = chr((ord(char) + shift - 97) % 26 + 97)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext

def decrypt_caesar_cipher(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                new_char = chr((ord(char) - shift - 97) % 26 + 97)
            plaintext += new_char
        else:
            plaintext += char
    return plaintext

def brute_force_caesar(ciphertext):
    for shift in range(1, 26):
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

plaintext = "This is a Caesar cipher test"
shift = 3

ciphertext = encrypt_caesar_cipher(plaintext, shift)
print(f"Ciphertext: {ciphertext}")

brute_force_caesar(ciphertext)
