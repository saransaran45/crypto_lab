import random


def power(x, y, p):
    res = 1 
    x = x % p  

    while y > 0:
        
        if (y & 1) == 1:
            res = (res * x) % p

        y = y >> 1  
        x = (x * x) % p  
    return res


def miller_test(d, n): # 15,61
    a = 2 + random.randint(1, n - 4) # 57

    x = power(a, d, n) 
    print(f"{x}\n")

    if x == 1 or x == n - 1:
        return True

    
    while d != n - 1: #15,60
        x = (x * x) % n
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False

def is_prime(n, k):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    d = n - 1
    while d % 2 == 0:
        d //= 2
 # k =5
    for _ in range(k):
        if not miller_test(d, n):
            return False

    return True

k = 5  

n = 61  
if is_prime(n, k):
    print(f"{n} is probably prime.")
else:
    print(f"{n} is composite.")
