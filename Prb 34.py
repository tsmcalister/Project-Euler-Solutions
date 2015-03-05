import math

def getDigits(n):
    digits = []
    while n > 0:
        digits.append(n%10)
        n = (n-n%10)/10
    digits.reverse()
    return digits

def sumFac(n):
    faclist = [math.factorial(d) for d in getDigits(n)]
    return sum(faclist)

for i in range(0,1000000):
    if i == sumFac(i):
        print i