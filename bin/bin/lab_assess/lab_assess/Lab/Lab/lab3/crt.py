
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
'''
def modInverse(a, m):
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
'''
def modInverse(a,m):
    for i in range(1,m):
        if (a*i) % m == 1: 
            return i
    return None

def chinese_remainder_theorem(num, rem):
    N = 1
    for n in num:
        N *= n

    x = 0

    for i in range(len(num)):
        Ni = N // num[i] #Mi
        Mi = modInverse(Ni, num[i]) 
        x += rem[i] * Ni * Mi


    return x % N

num = [3, 5, 7]  
rem = [2, 3, 2]  

result = chinese_remainder_theorem(num, rem)
print(f"Solution of the system of congruences is x = {result}")
