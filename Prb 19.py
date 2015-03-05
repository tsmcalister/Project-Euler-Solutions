import math
import calendar

sum = 0
for i in range(0,100):
    for j in range(0,12):
        if calendar.weekday(1901+i,j+1,1) == 6:
            sum += 1
print sum