import math
import time

def isPrime(n):
    for i in range(0,len(primes)):
        if n % primes[i] == 0:
            return False
        if primes[i] > math.sqrt(n):
            primes.append(n)
            return True
    primes.append(n)
    return True

def getDigits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = (n-n%10)/10
    return digits

def allComb(arr):
    combs = []
    for i in range(1,len(arr)):
        forward = 0
        backward = 0
        for j in range(i, len(arr)):
            forward += arr[j]*10**(j-i)
            backward += arr[len(arr)-1-j]*10**(j-i)
        combs.append(forward)
        combs.append(reverse(backward))
    return combs

def reverse(n):
    num = []
    while n > 0:
        num.append(n%10)
        n = (n-n%10)/10
    newnum = 0
    for i in range(0,len(num)):
        newnum = newnum+ num[len(num)-1-i]*10**i
    return newnum

primes = list([2])

speclist = []

for i in range(2,1000):
    if i %100000 == 0:
        print i
    isPrime(i)


for i in range(0,len(primes)):
    combs = allComb(getDigits(primes[i]))
    istype = True
    for j in range(0,len(combs)):
        if combs[j] not in primes:
            istype = False
    if istype:
        speclist.append(primes[i])


print primes
print speclist

print sum([23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397])





