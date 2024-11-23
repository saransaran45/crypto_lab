from cryptography.hazmat.primitives.ciphers import algorithms

# Get the S-Box
S_BOX = algorithms.AES._SBOX  # Accessing the S-Box directly

# Initialize the inverse S-Box
S_BOX_INV = [0] * 256

# Fill the inverse S-Box
for i in range(256):
    S_BOX_INV[S_BOX[i]] = i

R_CON = [
    0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36
]

def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = S_BOX[state[i][j] >> 4][state[i][j] & 0x0F]
    return state

def inv_sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = S_BOX_INV[state[i][j] >> 4][state[i][j] & 0x0F]
    return state
def shift_rows(state):
    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]
    return state

def inv_shift_rows(state):
    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]
    return state

def mix_columns(state):
    for i in range(4):
        a = state[i]
        state[i] = [
            gf_mult(a[0], 2) ^ gf_mult(a[1], 3) ^ a[2] ^ a[3],
            a[0] ^ gf_mult(a[1], 2) ^ gf_mult(a[2], 3) ^ a[3],
            a[0] ^ a[1] ^ gf_mult(a[2], 2) ^ gf_mult(a[3], 3),
            gf_mult(a[0], 3) ^ a[1] ^ a[2] ^ gf_mult(a[3], 2)
        ]
    return state

def inv_mix_columns(state):
    for i in range(4):
        a = state[i]
        state[i] = [
            gf_mult(a[0], 14) ^ gf_mult(a[1], 11) ^ gf_mult(a[2], 13) ^ gf_mult(a[3], 9),
            gf_mult(a[0], 9) ^ gf_mult(a[1], 14) ^ gf_mult(a[2], 11) ^ gf_mult(a[3], 13),
            gf_mult(a[0], 13) ^ gf_mult(a[1], 9) ^ gf_mult(a[2], 14) ^ gf_mult(a[3], 11),
            gf_mult(a[0], 11) ^ gf_mult(a[1], 13) ^ gf_mult(a[2], 9) ^ gf_mult(a[3], 14)
        ]
    return state

def add_round_key(state, round_key):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]
    return state

def gf_mult(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        carry = a & 0x80
        a = (a << 1) & 0xFF
        if carry:
            a ^= 0x1b
        b >>= 1
    return p

def key_expansion(key):
    expanded_key = [list(key[i:i + 4]) for i in range(0, len(key), 4)]
    for i in range(4, 44):
        temp = expanded_key[i - 1][:]
        if i % 4 == 0:
            temp = [S_BOX[b >> 4][b & 0x0F] for b in temp[1:] + temp[:1]]
            temp[0] ^= R_CON[(i // 4) - 1]
        expanded_key.append([expanded_key[i - 4][j] ^ temp[j] for j in range(4)])
    return expanded_key

def aes_encrypt(block, key):
    round_keys = key_expansion(key)

    state = [list(block[i:i + 4]) for i in range(0, len(block), 4)]
    state = add_round_key(state, round_keys[:4])

    for round in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state, round_keys[round * 4: (round + 1) * 4])

    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, round_keys[40:])

    return [byte for row in state for byte in row]

def aes_decrypt(cipher_text, key):
    round_keys = key_expansion(key)
    state = [list(cipher_text[i:i + 4]) for i in range(0, len(cipher_text), 4)]
    state = add_round_key(state, round_keys[40:])

    for round in range(9, 0, -1):
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, round_keys[round * 4: (round + 1) * 4])
        state = inv_mix_columns(state)

    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    state = add_round_key(state, round_keys[:4])

    return [byte for row in state for byte in row]

key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0xcf, 0x89, 0x24, 0x3b, 0xe8, 0xb6]
block = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]

cipher_text = aes_encrypt(block, key)
print(cipher_text)

# Decrypting
decrypted_text = aes_decrypt(cipher_text, key)
print("Decrypted text:", decrypted_text)
