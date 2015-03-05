import math
from collections import OrderedDict

primes = []

def sortedDigitList(n):
    list = []
    while n > 0:
        list.append(n%10)
        n = (n-n%10)/10
    list.sort()
    return list



def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

for i in range(1000,10000):
    if isPrime(i):
        primes.append(i)

mainlist = []

candidates = []

for i in range(0,len(primes)):
    curlist = []
    for j in range(0,len(primes)):
        if sortedDigitList(primes[i]) == sortedDigitList(primes[j]):
                curlist.append(primes[j])
    curlist.sort()
    if len(curlist)>2:
        diff = []
        cand = False
        for i in range(0,len(curlist)-1):
            for j in range(i+1, len(curlist)):
                if (curlist[j] + curlist[j]-curlist[i]) in curlist:
                    print curlist[j] + curlist[j]-curlist[i], curlist
                    cand = True
        if cand:
            print curlist
            candidates.append(curlist)

candidates.sort()
print candidates
