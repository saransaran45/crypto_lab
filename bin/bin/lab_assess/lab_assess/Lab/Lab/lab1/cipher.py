
def encryption(text,shift_amount):
    new_str=[]

    for i in range(len(text)):
        if text[i].isalpha():
            new_str.append(chr((((ord(text[i])-ord('a'))+shift_amount)%26)+ord('a')))
        else:
            new_str.append(text[i])
    return ''.join(new_str)

def decryption(text,shift_amount):
    new_str=[]
    for i in range(len(text)):
        if text[i].isalpha():
            new_str.append(chr((((ord(text[i])-ord('a'))-shift_amount)%26)+ord('a')))
        else:
            new_str.append(text[i])
    return ''.join(new_str)


text=input("Enter the string=")
shift_amount=int (input("Enter the shift amount="))
encrypted=encryption(text,shift_amount)
print("After encryption=",encrypted)
decrypted=decryption(encrypted,shift_amount)
print("after decryption=",decrypted)