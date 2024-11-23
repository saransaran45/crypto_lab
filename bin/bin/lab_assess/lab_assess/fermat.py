
def isprime(p):
    for i in range(2,p):
        if p%i==0:
            return False
    return True

def fermat(a,p):
    if(isprime(p) and a>0 and a%p!=0):
        print(pow(a,p-1,p))
    else:
        print("Not Possible")

a=2
p=7
fermat(a,p)