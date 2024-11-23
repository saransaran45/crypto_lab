import numpy as np

def get_matrix(key):
    key_matrix=[ord(i)-ord('A') for i in key]
    size=int(len(key)**0.5)
    return np.array(key_matrix).reshape(size,size)

def inver(a, m):
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

def mod_inverse(matrix,mod):
    d=np.linalg.det(matrix)
    c=np.zeros(matrix.shape)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            minor=np.delete(np.delete(matrix,i,axis=0),j,axis=1)
            c[i][j]=((-1)**(i+j))*int(np.round(np.linalg.det(minor)))%26
            
    adjugate=c.T
    matrix_inv=(inver(d,26)*adjugate)%26
    return matrix_inv.astype(int)


def encryption(message,key):
    key_matrix=get_matrix(key)
    size=key_matrix.shape[0]
    PT=message.replace(" ","").upper()
    print(key_matrix)
    while len(PT)%size!=0:
        PT+='X'
    CT=[]
    for i in range(0,len(PT),size):
        block = [ord(char)-ord('A') for char in PT[i:i+size]]
        encrypted_block=np.dot(key_matrix,block)%26
        CT.extend(encrypted_block)
        print(block,CT,encrypted_block)
    return ''.join(chr(num+ord('A')) for num in CT)

def decryption(message,key):
    key_matrix=get_matrix(key)
    size=key_matrix.shape[0]
    inverse_key_matrix=mod_inverse(key_matrix,26)
    print(inverse_key_matrix)
    PT=[]
    for i in range(0,len(message),size):
        block=[ord(char)-ord('A') for char in message[i:i+size]]
        decrypted_block=np.dot(inverse_key_matrix,block)%26
        PT.extend(decrypted_block)
    return ''.join(chr(num+ord('A')) for num in PT)

key="GYBNQKURP"
message="ACT"

encrypted_text=encryption(message,key)
print(f"Cipher text:{encrypted_text}")

decrypted_text = decryption(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")