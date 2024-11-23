import math

def euler_totient(n):
    result=n
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            while n%i==0:
                n//=i
            result-=result//i
            print(result,i,n)
    if n>1:
        result-=result//n
    return result

def euler_toilen(n):
    result = n
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            while n% i == 0:
                n //= i
            result -= n // i
    if n > 1:
        result -= result//n
    return result




def euler_theorem(a,n):
    if math.gcd(a,n)!=1:
        return "doesn't apply"
    
    phi_n=euler_totient(n)
    result=pow(a,phi_n,n)
    return result

a=3
n=10
print(f'Euler toilent: {euler_totient(n)}')
print(f"Euler theorem: {euler_theorem(a,n)}")
# print(f"(a^{euler_totient(n)})%n")