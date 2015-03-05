import math

def sum(arr):
    sv = 0
    for i in range(0,len(arr)):
        sv += arr[i]
    return(sv)

def to2(n):
    bin = []
    while n > 0:
        if n %2 == 0:
            bin.append(0)
        else:
            bin.append(1)
        n/=2
    newnum = 0
    for i in range(0,len(bin)):
        newnum += bin[i]*10**i
    return newnum

def reverse(n):
    num = []
    while n > 0:
        num.append(n%10)
        n = (n-n%10)/10
    newnum = 0
    for i in range(0,len(num)):
        newnum = newnum+ num[len(num)-1-i]*10**i
    return newnum

palinds = []


for i in range(0,1000000):
    bin = to2(i)
    if i == reverse(i) and bin == reverse(bin):
        palinds.append(i)

print palinds
print sum(palinds)
