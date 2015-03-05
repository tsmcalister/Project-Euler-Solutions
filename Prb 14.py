import math

def collhatz(n):
    seq = [1]
    while n!=1:
        if n%2==0:
            n/=2
            seq.append(n)
        else:
            n=3*n+1
            seq.append(n)
    return len(seq)

max = 0

for i in range(10,1000000):
    length = collhatz(i)
    if(length > max):
        max = length
        print i, length