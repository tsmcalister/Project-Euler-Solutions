import math

def factor(n):
    f = []
    while(n != 1):
        for i in range(2,n+1):
            if(i > math.sqrt(n)):
                f.append(n)
                n = 1
                break
            if n%i == 0:
                f.append(i)
                n = n / i
                break
    return(f)

def divisors(n):
    f = factor(n)
    curnum = f[0]
    d = [0]
    for i in range(0,len(f)):
        if(f[i] == curnum):
            d[len(d)-1]+=1
        else:
            curnum = f[i]
            d.append(1)
    prod = 1
    for i in range(0,len(d)):
        prod*=d[i]+1
    return(prod)





def triangle(n):
    return(n*(n+1)/2)
max = 0
for i in range(2,10000):
    num = divisors(triangle(i))
    if(num > max):
        max = num
        print i,max

print max