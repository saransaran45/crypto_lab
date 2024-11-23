def extended_gcd(a,b):
    if b==0:
        return a,1,0
    else:
        gcd,x1,y1=extended_gcd(b,a%b)
        print(gcd,x1,y1)
        x=y1
        y=x1-(a//b)*y1
        print(x,y)
        return gcd,x,y
    
a=161
b=28
gcd, x, y = extended_gcd(a, b)
print(f"GCD of {a} and {b} is {gcd}")
print(f"Coefficients x and y are {x} and {y}, respectively")
print(f"Verification: {a} * {x} + {b} * {y} = {gcd}")