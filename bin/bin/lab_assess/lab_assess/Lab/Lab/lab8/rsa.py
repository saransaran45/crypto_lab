import random

def mod_inv(b,a): #13,60
    n=a
    if b==0:
        return
    # print(a,b)
    q=a//b
    # print(q)
    r=a%b
    t1=0
    t2=1
    t=t1-t2*q
    a,b=b,r
    print(f"{q} {a} {b} {r} {t1} {t2} {t}")
    while b!=0:
        q=a//b
        r=a%b
        t1=t2
        t2=t
        t=t1-t2*q
        a,b=b,r
        print(f"{q} {a} {b} {r} {t1} {t2} {t}")
    if t2<0:
        t2=n+t2
    return t2

def encrypt(P,e,n):
    return pow(P,e,n)

def rsa(p,q):
    n=p*q
    euler_totient=(p-1)*(q-1)
    e=13 #1<e<O(n)
    #e = random.randint(2,euler_totient)
    d=mod_inv(e,euler_totient)
    # print(d)
    P=int(input("Enter the plain text:"))
    cipher=encrypt(P,e,n)
    original=encrypt(cipher,d,n)
    print(f"cipher={cipher} , decrypt={original}")

p=int(input("Enter the value for p:"))
q=int(input("Enter the value for q:"))
rsa(p,q)