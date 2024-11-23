def mod_in(a,m):
    for i in range(1,m):
        if (a*i) % m == 1:
            return i
    return None


def __gcd(a, b):
    if(b == 0):
        return a
    else:
        return __gcd(b, a % b)

def power(x, y, m):
    if (y == 0):
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m

    return p if(y % 2 == 0) else (x * p) % m

def modInverse(a, m):
    if (__gcd(a, m) != 1):
        print("Inverse doesn't exist") 
        return None
    else:
        return power(a, m - 2, m)
def elgammal():
    '''
    p=11
    e1=2
    d=3
    r=4
    P=7
    e2 = pow(e1,d)%p
    print(e2)

    c1 = pow(e1,r)%p
    print(c1)

    c2 = (pow(e2,r)*P)%p
    print(c2)
    aa = pow(c1,d)
    ss = pow(aa,-1,11)
    print(f"ss:{ss}")
    print()
    ans = (c2*modInverse(pow(c1,d),11))%p
    print(ans)
    '''

    p = 11
    d = 3
    e1 = 2
    e2 = pow(e1,d,p)
    print(e2)
    
    r = 4
    c1 = pow(e1,r,p)
    print(c1)
    pt = 7
    c2 = (pow(e2,r,p) * pt) % p
    print(c2)

    m = pow(c1,d)
    i = pow(m,-1,p)
    original = (c2 * i) % p
    print(original)


elgammal()