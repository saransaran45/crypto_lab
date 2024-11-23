
def mod_inv(a,m):
    temp=a
    t0=0
    t1=1
    q=a//m
    r=a%m
    t=t0-t1*q
    a,m=m,r
    print(f"{q} {a} {m} {r} {t0} {t1} {t}")
    while m!=0:
        q=a//m
        r=a%m
        t0=t1
        t1=t
        t=t0-t1*q
        a,m=m,r
        print(f"{q} {a} {m} {r} {t0} {t1} {t}")
    if(t1<0):
        return temp+t1
    return t1

a=7
m=26
print(f"{a}*{mod_inv(m,a)}=1(mod{m})")