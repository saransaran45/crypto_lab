import socket

def encrypt_rc4(secret_message, secret_key, n):
    S = [i for i in range(0, 2 ** n)]
    key_list = [secret_key[i:i + n] for i in range(0, len(secret_key), n)]

    for i in range(len(key_list)):
        key_list[i] = int(key_list[i], 2)

    pt = [secret_message[i:i + n] for i in range(0, len(secret_message), n)]
    for i in range(len(pt)):
        pt[i] = int(pt[i], 2)

    diff = len(S) - len(key_list)
    if diff != 0:
        for i in range(diff):
            key_list.append(key_list[i])

    def key_scheduling_algorithm():
        j = 0
        N = len(S)

        for i in range(N):
            j = (j + S[i] + key_list[i]) % N
            S[i], S[j] = S[j], S[i]

    key_scheduling_algorithm()

    def pseudo_random_generation_algorithm():
        N = len(S)
        i = j = 0
        key_stream = []

        for k in range(len(pt)):
            i = (i + 1) % N
            j = (j + S[i]) % N
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % N
            key_stream.append(S[t])

        return key_stream

    key_stream = pseudo_random_generation_algorithm()

    cipher_text = []
    for i in range(len(pt)):
        c = key_stream[i] ^ pt[i]
        cipher_text.append(c)

    encrypted_to_bits = ""
    for i in cipher_text:
        encrypted_to_bits += '0' * (n - len(bin(i)[2:])) + bin(i)[2:]

    return encrypted_to_bits


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

secret_message = input('Enter the secret message (in binary): ')
secret_key = input('Enter the secret key (in binary): ')
n = int(input('Enter the number of bits (n): '))

encrypted_message = encrypt_rc4(secret_message, secret_key, n)

client_socket.send(encrypted_message.encode())
client_socket.send(secret_key.encode())
client_socket.send(str(n).encode())

client_socket.close()
