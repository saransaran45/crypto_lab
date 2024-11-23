
def modinverse(a,m):
    temp=a #3
    q=a//m
    r=a%m
    t0=0
    t1=1
    t=t0-t1*q
    a,m=m,r #35,3
    while m!=0:
        q=a//m
        r=a%m
        t0=t1
        t1=t
        t=t0-t1*q
        a,m=m,r

    if t1<0:
        return temp+t1
    return t1

def chinese(num,rem):
    M=1
    for i in num:
        M*=i # m1*m2*m3 105
    x=0
    for i in range(len(num)):
        M1 = M // num[i]
        M1_inv = modinverse(num[i],M1)
        x += rem[i]*M1*M1_inv
    return x% M
'''
    for i in range(len(num)):
        temp_M=M//num[i] # M1 = M // m1 35
        temp_M_inverse=modinverse(num[i],temp_M)
        print(temp_M,temp_M_inverse)
        x+=rem[i]*temp_M*temp_M_inverse
    return x%M
'''
num=[3,5,7]
rem=[2,3,2]
print(chinese(num,rem))