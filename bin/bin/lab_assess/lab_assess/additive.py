mod=26
def encryption(data,shift):
    global mod
    return ''.join([chr(((ord(i)-ord('a')+shift)%mod)+ord('a')) for i in data])

    #return ''.join([chr(((ord(i)-ord('a')+shift)%mod)+ord('a')) for i in data])


def decryption(data,shift):
    global mod
    return ''.join([chr(((ord(i)-ord('a')-shift)%mod)+ord('a')) for i in data])

data=input("Enter the message:")
shift=int(input("Enter the shift amount:"))

encrypted_data = encryption(data,shift)
print(encrypted_data)
decrypted_data = decryption(encrypted_data,shift)
print(decrypted_data)