

def encryption(message,k):
    message=message.upper()
    k=k.upper()
    encrypted_text=[]
    newk=(k*(len(message)//len(k)))+k[:len(message)%len(k)]
    #newk = k+k[0:len(message)-len(k)]

    for i in range(len(message)):
        if message[i].isalpha():
            shift=ord(newk[i])-ord('A')
            enc_char=chr(((ord(message[i])-ord('A')+shift)%26)+ord('A'))
            encrypted_text.append(enc_char)
        else:
            encrypted_text.append(message[i])
    return "".join(encrypted_text)

def decryption(message,k):
    message=message.upper()
    k=k.upper()
    encrypted_text=[]
    newk=(k*(len(message)//len(k)))+k[:len(message)%len(k)]

    for i in range(len(message)):
        if message[i].isalpha():
            shift=ord(newk[i])-ord('A')
            enc_char=chr(((ord(message[i])-ord('A')-shift)%26)+ord('A'))
            encrypted_text.append(enc_char)
        else:
            encrypted_text.append(message[i])
    return "".join(encrypted_text)

plaintext = "ATTACKATDAWN"
keyword = "LEMON"
encrypted = encryption(plaintext, keyword)
print(f"Encrypted: {encrypted}")

decrypted = decryption(encrypted, keyword)
print(f"Decrypted: {decrypted}")