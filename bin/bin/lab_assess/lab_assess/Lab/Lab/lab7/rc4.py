import numpy as np
def find_s_array(s,k):
    if len(s)>len(k):
        k = k+k[0:len(s)-len(k)]
        print(k)
    j=0
    for i in range(len(s)):
        j=(j+s[i]+k[i])%len(s)
        s[i],s[j]=s[j],s[i]
    return s

def find_t_array(PT,s):
    i,j=0,0
    t_array=[]
    for k in range(len(PT)):
        i=(i+1)%len(s)
        j=(j+s[i])%len(s)
        s[i],s[j]=s[j],s[i]
        t=(s[i]+s[j])%len(s)
        t_array.append(s[t])
        print(t_array)
    return t_array

def encryption(ks,PT):
    val = np.array(PT)^np.array(ks)
    return [int(i) for i in val]


s=[0,1,2,3,4,5,6,7]
k=[3,1,4,1,5]
PT=[6,1,5,4]
s_array = find_s_array(s,k)
t_array = find_t_array(PT,s_array)

CT = encryption(t_array,PT)
print(CT)
PT = encryption(CT,t_array)
print(PT)
