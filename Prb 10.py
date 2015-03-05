import math
primes = [2,3,5]
d = [n*2 for n in range(1,1000000)]
print d[12]


primes = [2]

def isPrime(n):
    for i in range(0,len(primes)):
        if(primes[i] > math.sqrt(n)):
            primes.append(n)
            return True
        if n%primes[i] == 0:
            return False


sum = 0
for i in range(2,1000000-1):
    if i%100000 == 0:
        print i
    if isPrime(d[i]):
        sum =  sum + d[i]

print sum