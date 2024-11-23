import numpy as np

def create_matrix(key, n):
    m = len(key) // n
    mat = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            char = key[i * n + j]
            mat[i][j] = ord(char) % 65 if char.isupper() else ord(char) % 97
    return np.array(mat)

def create_matrix1(message, n):
    arr = [ord(c) - ord('A') for c in message]
    return np.array(arr).reshape(n, 1)

def encryption(mat_mes, mat_key):
    res = np.dot(mat_key, mat_mes) % 26
    return res

def mat_to_text(mat):
    return ''.join(chr(int(val) + ord('A')) for val in mat.flatten())

def mod_inverse(a, m):
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

def mod_mat_inverse(mat, modulus):
    det = int(np.round(np.linalg.det(mat))) % modulus
    if det == 0:
        raise ValueError("Matrix is not invertible")

    inv_det = mod_inverse(det, modulus)
    
    cofactors = np.zeros(mat.shape)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            minor = np.delete(np.delete(mat, i, axis=0), j, axis=1)
            cofactors[i, j] = ((-1) ** (i + j)) * int(np.round(np.linalg.det(minor))) % modulus
    
    adjugate = cofactors.T
    matrix_inv = (inv_det * adjugate) % modulus
    return matrix_inv.astype(int)

def decryption(cipher_mat, mat_key, n):
    inv=mod_mat_inverse(mat_key,26)
    res=np.dot(inv,cipher_mat)%26
    print(res)
    return res

message = "SAS"
key = "GYBNQKURP"
n = 3
mat_mes = create_matrix1(message, n)
mat_key = create_matrix(key, n)
cipher = encryption(mat_mes, mat_key)
cipher_text = mat_to_text(cipher)
print("Encrypted:", cipher_text)
decrypted = decryption(cipher, mat_key, n)
# print(decrypted)
decrypted_text = mat_to_text(decrypted)
print("Decrypted:", decrypted_text)
