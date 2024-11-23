def decryption(s, k):
    n = len(s)
    rail = [["\n" for _ in range(n)] for _ in range(k)]

    down = False
    row, col = 0, 0

    # Mark the positions in the rail where the characters will be placed
    for i in range(n):
        if row == 0 or row == k - 1:
            down = not down
        rail[row][col] = "*"
        col += 1
        if down:
            row += 1
        else:
            row -= 1

    # Fill the rail matrix with the characters of the encrypted string
    ind = 0
    for i in range(k):
        for j in range(n):
            if rail[i][j] == "*" and ind < n:
                rail[i][j] = s[ind]
                ind += 1

    # Read the characters from the zigzag pattern
    ans = []
    row, col = 0, 0
    down = False
    for i in range(n):
        if row == 0 or row == k - 1:
            down = not down
        if rail[row][col] != "*":
            ans.append(rail[row][col])
            col += 1
        if down:
            row += 1
        else:
            row -= 1

    return "".join(ans)


def encryption(s, k):
    n = len(s)
    rail = [["\n" for _ in range(n)] for _ in range(k)]
    #rail2 = [["\n" for _ in range(n)] for _ in range(k)]

    down = False
    row, col = 0, 0

    # Place the characters in the zigzag pattern
    for i in range(n):
        if row == 0 or row == k - 1:
            down = not down
        rail[row][col] = s[i]
        col += 1
        if down:
            row += 1
        else:
            row -= 1

    # Read the characters row by row to form the encrypted string
    ans = []
    for i in rail:
        for j in i:
            if j != "\n":
                ans.append(j)

    return "".join(ans)


if __name__ == "__main__":
    s = "trust the process"
    k = 3
    encrypt = encryption(s, k)
    decrypt = decryption(encrypt, k)

    print("Encrypted text:", encrypt)
    print("Decrypted text:", decrypt)
