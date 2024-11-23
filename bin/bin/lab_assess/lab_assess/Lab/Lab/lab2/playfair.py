import string

def generate_key_matrix(key):
 
    key = ''.join(sorted(set(key), key=key.index))  
    print(f"keyss : {key}")
    alphabet = string.ascii_uppercase.replace('J', '')  
    print(f"albha :{alphabet}")
    key_matrix = []
    for char in key:
        if char not in key_matrix and char != 'J':
            key_matrix.append(char)
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
    
    key_matrix_5x5 = [key_matrix[i:i + 5] for i in range(0, 25, 5)]
    print("\nKey Matrix:")
    for row in key_matrix_5x5:
        print(' '.join(row))
    
    return key_matrix_5x5

def locate_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join([char for char in text if char in string.ascii_uppercase])

    prepared = []
    i = 0
    while i < len(text):
        prepared.append(text[i])
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared.append('X')
        i += 1
    if len(prepared) % 2 != 0:
        prepared.append('Z') 

    print("\nPrepared Text (after processing digraphs):", ''.join(prepared))
    
    return ''.join(prepared)

def encrypt_digraph(digraph, matrix):
    row1, col1 = locate_position(matrix, digraph[0])
    row2, col2 = locate_position(matrix, digraph[1])
    
    print(f"\nEncrypting digraph: {digraph} => ", end='')

    if row1 == row2:
        result = matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]

    elif col1 == col2:
        result = matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]

    else:
        result = matrix[row1][col2] + matrix[row2][col1]

    print(f"{result}")
    return result

def encrypt_playfair(plaintext, key):
    print(f"Original Plaintext: {plaintext}")
    print(f"Key: {key}")


    key_matrix = generate_key_matrix(key)

    prepared_text = prepare_text(plaintext)


    ciphertext = ''
    for i in range(0, len(prepared_text), 2):
        ciphertext += encrypt_digraph(prepared_text[i:i + 2], key_matrix)

    print("\nFinal Ciphertext:", ciphertext)
    return ciphertext

plaintext = "Hide the gold in the tree stump"
key = "PLAYFAIRCIPHER"
ciphertext = encrypt_playfair(plaintext, key)
