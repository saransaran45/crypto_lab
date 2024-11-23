def gcd(a,b):
    while b!=0:
        a,b=b,a%b
        print(a,b)
    return a

a=6
b=24
print(f"GCD of {a} and {b} is {gcd(a, b)}")