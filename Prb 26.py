import math

def isInt(n):
    if int(n) == n:
        return(True)
    return(False)

def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


def getDecimal(n):
    if(not isPrime(n)):
        return(1)

    d = 9
    while(not isInt(float(d)%n)):
        d=d*10+9
    return(d/n)

def getDecimalDigits(n):
    return(math.floor(math.log10(getDecimal(n)))+1)


max = 0
num = 0
for i in range(3,1000):
    dec = getDecimalDigits(i)
    if dec > max and dec != 17:
        max = dec
        num = i

print num,max