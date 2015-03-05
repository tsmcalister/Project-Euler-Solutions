import math

def div(n):
    f = []
    for i in range(1,n/2+1):
        if n%i == 0:
            f.append(i)
    return(f)

def sum(n):
    s = 0
    for i in range(0,len(n)):
        s += n[i]
    return(s)

amic = []

for i in range(1,10000):
    n = sum(div(i))

    if i != n and sum(div(n)) == i:
        amic.append(i)

print amic
print sum(amic)