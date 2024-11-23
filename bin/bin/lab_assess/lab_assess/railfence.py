
def encryption(message,rails):
    if rails==1:
        return message
    rows=[""]*rails

    add=0
    inc=1
    for i in message:
        rows[add]+=i
        if add==0:
            inc=1
        elif add==rails-1:
            inc=-1
        add+=inc
    return "".join(rows)

def decryption(message,rails):
    if rails==1:
        return message
    rows=[""]*rails
    
    add=0
    inc=1
    lengths=[0]*rails
    for i in message:
        lengths[add]+=1
        if add==0:
            inc=1
        elif add==rails-1:
            inc=-1
        add+=inc
        
    print(lengths)
    index=0

    for i in range(rails):
        rows[i]=message[index:index+lengths[i]]
        index+=lengths[i]
    result=[]
    add=0
    inc=1
    for i in range(len(message)):
        result.append(rows[add][0])
        rows[add]=rows[add][1:] #remove the character
        if add==0:
            inc=1
        elif add==rails-1:
            inc=-1
        add+=inc
    return "".join(result)

message="Saravanan"
rails=3

encrypted_message = encryption(message, rails)
print(f"Encrypted: {encrypted_message}")

decrypted_message = decryption(encrypted_message, rails)
print(f"Decrypted: {decrypted_message}")