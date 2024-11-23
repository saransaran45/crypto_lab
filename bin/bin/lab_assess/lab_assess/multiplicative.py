
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def mul_inv(key):
    for i in range(1,26):
        if(key*i)%26==1:
            return i
    return None

def encryption(data,key):
    return ''.join([chr((((ord(i)-ord('a'))*key)%26)+ord('a')) for i in data])

def decryption(data,key):
    return ''.join([chr((((ord(i)-ord('a'))*key)%26)+ord('a')) for i in data])
data=input("Enter the message:")
key=int(input("Enter the shift amount:"))

encrypted_data = encryption(data,key)
print(encrypted_data)
inv_key=mul_inv(key)
decrypted_data = decryption(encrypted_data,inv_key)
print(decrypted_data)