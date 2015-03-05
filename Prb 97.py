
#print 28433*2**7830457+1

import math


def digits(n):
    return(math.floor(math.log10(n))+1)


n = 2

def toN(d,n):
    for i in range(0,d-1):
        n*=2
        if i % 100000 == 0:
            print i
        if(digits(n) == 11):
            n = n%10000000000
    return(n)
n= toN(7830457,n)
print n*28433+1
