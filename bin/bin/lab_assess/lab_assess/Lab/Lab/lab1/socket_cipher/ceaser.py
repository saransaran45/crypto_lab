
def encryption(text,shift_amount=2):
    new_str=[]

    for char in text:
        if 'a' <= char <= 'z':
            new_str.append(chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a')))
            
        elif 'A' <= char <= 'Z':
            new_str.append(chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A')))
        else:
            new_str.append(char)
    return ''.join(new_str)

def decryption(text,shift_amount=2):
    new_str=[]
    for char in text:
        if 'a' <= char <= 'z':
            new_str.append(chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a')))
        elif 'A' <= char <= 'Z':
            new_str.append(chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A')))
        else:
            new_str.append(char)
    return ''.join(new_str)

