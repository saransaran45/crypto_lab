def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def iscoprime(a, b):
    return gcd(a, b) == 1

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr(((a * (ord(char) - shift) + b) % 26) + shift)
        else:
            result += char
    return result

def decrypt(text, a, b):
    a_inv = pow(a, -1,26)
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr(((a_inv * (ord(char) - shift - b)) % 26) + shift)
        else:
            result += char
    return result

def is_meaningful(text):
    common_words = ["HELLO", "WORLD", "THE", "IS", "A", "OF"]
    return any(word in text.upper() for word in common_words)
'''
def brute_force_attack(ciphertext):
    valid_a_values = [a for a in range(1, 26) if iscoprime(a, 26)]
    
    for a in valid_a_values:
        for b in range(26):
            try:
                decrypted_text = decrypt(ciphertext, a, b)
                if is_meaningful(decrypted_text):
                    print(f"Trying a={a}, b={b}: {decrypted_text}")
            except ValueError:
                print(f"Skipping a={a}, b={b} due to invalid modular inverse")
'''

def brute_force_affine(ciphertext):
    for a in range(1, 26):  # 'a' must be between 1 and 25
        if iscoprime(a, 26):  # 'a' must be coprime with 26
            for b in range(26):  # 'b' can be any value from 0 to 25
                try:
                    decrypted_text = decrypt(ciphertext, a, b)
                    print(f'Trying a={a}, b={b}: {decrypted_text}')
                except ValueError:
                    # This handles the case where 'a' is not invertible in mod 26
                    continue

# Test with the ciphertext obtained earlier



plain = "HELLO WORLD"
a, b = 5, 8
cipher = encrypt(plain, a, b)
print("Ciphertext:", cipher)

brute_force_affine(cipher)


