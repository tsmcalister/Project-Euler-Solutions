import math
import itertools

max = 1000
primes = [2,3,5]

def isPrime(n):
    for i in range(0,len(primes)):
        if(primes[i] > math.sqrt(n)):
            primes.append(n)
            return True
        if n%primes[i] == 0:
            return False

for i in range(6,max):
    isPrime(i)

plen = len(primes)

print plen

for i in range(0,plen):
    for j in range(0, plen):
        for k in range(0,plen):
            for l in range(0,plen):
                for m in range(0,plen):
                    arr = [primes[i],primes[j],primes[k],primes[l],primes[m]]
                    test = itertools.permutations(arr)

print "done"

