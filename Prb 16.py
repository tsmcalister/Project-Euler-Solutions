n = 2**1000

sum = 0

while n>1:
    num = n%10
    sum+=num
    n = (n-num)/10
print(sum)