import numpy as np

def mod_inverse(a, m):
    # Extended Euclidean Algorithm to find the modular inverse of a under modulo m
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
    # Calculate determinant
    det = int(np.round(np.linalg.det(mat))) % modulus
    if det == 0:
        raise ValueError("Matrix is not invertible")

    # Calculate modular inverse of the determinant
    inv_det = mod_inverse(det, modulus)
    
    # Calculate adjugate matrix
    cofactors = np.zeros(mat.shape)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            minor = np.delete(np.delete(mat, i, axis=0), j, axis=1)
            cofactors[i, j] = ((-1) ** (i + j)) * int(np.round(np.linalg.det(minor))) % modulus
    
    adjugate = cofactors.T
    # Calculate the modular inverse matrix
    matrix_inv = (inv_det * adjugate) % modulus
    return matrix_inv.astype(int)

# Given matrix
matrix = np.array([
    [6, 24, 1],
    [13, 16, 10],
    [20, 17, 15]
])

modulus = 26

# Compute the modular inverse
inverse_matrix = mod_mat_inverse(matrix, modulus)

print("Original Matrix:\n", matrix)
print("Modular Inverse Matrix:\n", inverse_matrix)
