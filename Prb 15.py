import math

def t(n):
    return(n*(n+1)/2)

d = [d for d in range(1,22)]

def next(n):
    nn = []
    for i in range(0,len(n)):
        sum = 0
        for j in range(0,i+1):
            sum+=n[j]
        nn.append(sum)
    return(nn)

for i in range(0, 20):
    print i, d
    d = next(d)