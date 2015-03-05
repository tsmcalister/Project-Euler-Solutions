import math

n = [x for x in range(1,1001)]


for a in range(0,1000):
    for b in range(0,1000):
        for c in range(0,1000):
            if a+b+c == 1000 and a**2+b**2==c**2:
                print a*b*c