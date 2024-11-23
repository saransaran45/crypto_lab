import math


def __gcd(a, b):
    if b == 0:
        return a
    else:
        return __gcd(b, a % b)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def power(x, y, m):
    if y == 0:
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m

    return p if (y % 2 == 0) else (x * p) % m


def modInverse(a, m):
    if math.gcd(a, m) != 1:
        print("Inverse doesn't exist")
        return None
    else:
        # return power(a, m - 2, m)
        return pow(a, m - 1, m)


a = 3
m = 11  # p

result = modInverse(a, m)
if result:
    print(f"Modular multiplicative inverse of {a} under modulo {m} is {result}")
