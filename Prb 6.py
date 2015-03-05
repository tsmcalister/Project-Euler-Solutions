import math

l1 = [x for x in range(1,101)]
l2 = [x*x for x in range(1, 101)]

suml1 = 0
for i in range(0,len(l1)):
    suml1 += l1[i]

suml2 = 0
for i in range(0,len(l2)):
    suml2 += l2[i]
suml1 **= 2

print suml1, suml2
print(suml1 - suml2)