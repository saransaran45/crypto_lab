'''def encrypt(text,a,b):
    result=""
    for char in text:
        if char.isalpha():
            shift=ord('A') if char.isupper() else ord('a')
            result+=chr(((a*(ord(char)-shift)+b)%26)+shift)
        elif char.isdigit():
            result += str((a*int(char) + b)%10)
        else:
            result+=char
    return result

def mod_inverse(a,m):
    for x in range(1,m):
        if(a*x) % m == 1:
            return x
    return None



def decrypt(text,a,b):
    a_inv=pow(a,-1,26)
    result=""
    for char in text:
        if char.isalpha():
            shift=ord('A') if char.isupper() else ord('a')
            result+=chr(((a_inv*(ord(char)-shift-b))%26)+shift)
        else:
            result+=char
    return result

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def iscoprime(a,b):
    return gcd(a,b)==1

plain="HELLO WORLD"
a = int(input("Enter a value of a"))
b = int(input("Enter a value of b"))
a,b=5,8
if iscoprime(a,26)==False:
    raise ValueError(f'{a} and 26 are not co prime')
cipher=encrypt(plain,a,b)
print("Encrypted:",cipher)
print("Decrypted:",decrypt(cipher,a,b))'''

def encryption(text,a,b):
    result = ""
    for ch in text:
        if ch.isalpha():
            shift = ord('A') if ch.isupper() else ord('a')
            result += chr(((a*(ord(ch)-shift)+b)%26)+ shift)
        elif ch.isdigit():
            result += str((a*int(ch)+b) % 10)
        else :
            result += ch

    return result

def mod_inverse(a,m):
    for i in range(1,m):
        if(a*i) % m == 1:
            return i
    return None

def decryption(text,a,b):
    result = ""
    inverse = mod_inverse(a,26)
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result = chr(((mod_inverse*(ord(char)-shift-b))%26) + shift)
        if char.isdigit():
            shift = str((mod_inverse*(int(char)-b))%10)
    return result
    

def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def isCoprime(a,b):
    return gcd(a,b)

plain = "Hello World"
a = int(input("Enter a value:"))
b = int(input("Enter b value"))
if isCoprime(a,26) == False:
    raise ValueError(f'{a} and 26 are not coprime')
cipher = encryption(plain,a,b)
print("Encrypted:",cipher)
print("Decrypted:",decryption(cipher,a,b))