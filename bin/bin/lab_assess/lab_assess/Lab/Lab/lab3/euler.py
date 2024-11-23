import math

def euler_totient(n):
    ans=0
    for i in range(1,n):
        if math.gcd(n,i) == 1:
            ans+=1
    return ans

def eulers_theorem(a, n):
    if math.gcd(a, n) != 1:
        return f"{a} and {n} are not coprime, Euler's Theorem doesn't apply."

    phi_n = euler_totient(n)
    
    result = pow(a, phi_n, n)
    return result

a = 6
n = 35
print(f"(a^{euler_totient(n)}) % n = {eulers_theorem(a, n)}")
