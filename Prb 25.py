import math

map  = [1,1]

def digits(n):
    return(math.floor(math.log10(n))+1)

def fib(n):
    if n <= len(map):
        return(map[n-1])
    else:
        calc = fib(n-2)+fib(n-1)
        map.append(calc)
        return(calc)


d = 1
while(digits(fib(d)) < 1000):
    d+=1
print fib(d)
print d