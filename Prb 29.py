import math
import time


mylist = []

start = time.time()
for i in range(2,101):
    for j in range(2,101):
        mylist.append(i**j)

answer = len(list(set(mylist)))
time = time.time()-start
print time, answer