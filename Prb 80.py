import math
from decimal import *

getcontext().prec = 102

sum = 0

for i in range(1,100):
    if int(math.sqrt(i)) != math.sqrt(i):
        num = Decimal(i).sqrt()
        print i
        print num
        num = num * 10**99
        cursum = 0
        for j in range(0,100):
            digit = int(num%10)
            num=int(num/10)
            cursum +=digit
            print digit
        print cursum
        sum += cursum

print sum