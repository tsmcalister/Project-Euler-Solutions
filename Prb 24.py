import math
import itertools

n = [d for d in range(0,10)]

def forNChooseK(s, n, k, communicator, func):
    for i in range(s,n):
        newCom = list(communicator)
        newCom.append(i)
        if(k>1):
            forNChooseK(i+1,n,k-1,newCom,func)
        else:
            func(newCom)


d = itertools.permutations(n)

for i in range(0,999999):
    d.next()
print d.next()