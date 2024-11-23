def encrypt(s,n):
    if n==1:
        return s
    rows=[""]*n

    add=0
    inc=1
    for i in s:
        rows[add]+=i
        if add==0:
            inc=1
        elif add==n-1:
            inc=-1
        add+=inc

    return "".join(rows)

def decrypt(s,n):
    if n==1:
        return s

    rows=[""]*n
    index=0
    add=0
    inc=1
    lengths=[0]*n
    for i in s:
        lengths[add] += 1
        if add == 0:
            inc = 1
        elif add == n - 1:
            inc = -1
        add += inc
    print(lengths)
    index = 0
    for i in range(n):
        rows[i] = s[index:index + lengths[i]]
        index += lengths[i]
    print(rows)
    result = []
    add = 0
    inc = 1
    for _ in range(len(s)):
        result.append(rows[add][0])
        rows[add] = rows[add][1:]
        if add == 0:
            inc = 1
        elif add == n - 1:
            inc = -1
        add += inc

    return "".join(result)


text="GeeksforGeeks "
cipher=encrypt(text,3)
print("Encrypted:",cipher)
print("Decrypted:", decrypt(cipher, 3))