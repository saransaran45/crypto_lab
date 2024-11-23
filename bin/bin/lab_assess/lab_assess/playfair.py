def create_matrix(key):
    alphabet=''.join([chr(i) for i in range(ord('a'),ord('z')+1) if chr(i)!='j'])
    keyword=''.join(sorted(set(key),key=key.index)).lower()
    matrix=keyword+''.join([c for c in alphabet if c not in key])
    return [matrix[i:i+5] for i in range(0,25,5)]


def digraphs(data):
    data=data.lower().replace('j','i').replace(' ','')
    newdata=[]
    i=0
    while(i<len(data)):
        a=data[i]
        b=data[i+1] if(i+1)<len(data) else 'z'
        if a==b:
            newdata.append(a+'x')
        else:
            newdata.append(a+b)
            i+=1
        i+=1
    return newdata

def find_position(mat,letter):
    for i in range(5):
        for j in range(5):
            if(mat[i][j]==letter):
                return (i,j)
    return None

def encryption(data,key):
    mat=create_matrix(key)
    data=digraphs(data)
    CT=""
    for digraph in data:
        row1,col1=find_position(mat,digraph[0])
        row2,col2=find_position(mat,digraph[1])

        if row1==row2:
            CT+=mat[row1][(col1+1)%5]+mat[row2][(col2+1)%5]
        elif col1==col2:
            CT+=mat[(row1+1)%5][col1]+mat[(row2+1)%5][col2]
        else:
            CT+=mat[row1][col2]+mat[row2][col1]
    return CT

def decryption(ciphertext, keyword):
    matrix = create_matrix(keyword)
    formatted_text = digraphs(ciphertext)
    plaintext = ""
    
    for digraph in formatted_text:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])
        
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    
    return plaintext

data=input("Enter the data:")
key=input("Enter the key:")

encrypted_data = encryption(data,key)
print(encrypted_data)
decrypted_data = decryption(encrypted_data,key)
print(decrypted_data)