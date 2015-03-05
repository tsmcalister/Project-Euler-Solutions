import math
import itertools


abb = []
allnum = []
allsums = [0]

def div(n):
    f = []
    for i in range(1,n/2+1):
        if n%i == 0:
            f.append(i)
    return(f)

def sum(n):
    s = 0
    for i in range(0,len(n)):
        s += n[i]
    return(s)

for i in range(1,28124):
    if sum(div(i)) > i:
        abb.append(i)

for i in range(0,len(abb)):
    for j in range(i,len(abb)):
        allsums.append(abb[i]+abb[j])

allsums.sort();

print len(allsums)
for i in range(0,len(allsums)-1):
    if i%1000000 == 0:
        print i
    for j in range(allsums[i]+1,allsums[i+1]):
        if(j < 28124):
            allnum.append(j)




print allnum
print sum(allnum)