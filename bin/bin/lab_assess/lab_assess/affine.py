def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def mod_inverse(a,m):
    for x in range(1,m):
        if(a*x)%m==1:
            return x
    return None

def affine_encrypt(PT,a,b):
    m=26

    if gcd(a,m)!=1:
        raise ValueError(f"The value of 'a' must be coprime with {m}")
    
    CT=''
    for char in PT:
        if char.isalpha():
            x=ord(char.upper())-ord('A')
            encrypted_char=(a*x+b)%26
            CT+=chr(encrypted_char+ord('A'))
        else:
            CT+=char
    return CT

def affine_decrypt(CT,a,b):
    m=26
    a_inv=mod_inverse(a,m)
    if a_inv is None:
        raise ValueError(f"No modular inverse exists for 'a'={a} under modulo {m}")
    
    PT=''
    for char in CT:
        if char.isalpha():
            x=ord(char.upper())-ord('A')
            decrypted_char=(a_inv*(x-b))%m
            PT+=chr(decrypted_char+ord('A'))
        else:
            PT+=char
    return PT


PT="HELLO"
a=5
b=8

print(f"Original Text: {PT}")
encrypted_text = affine_encrypt(PT, a, b)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = affine_decrypt(encrypted_text, a, b)
print(f"Decrypted Text: {decrypted_text}")