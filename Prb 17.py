nums = ["one", "two", "three", "four", "five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
m10 = ["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

whole = ""

def text(n):
    string = ""
    if n == 1000:
        return("onethousand")
    if n > 99:
        string += nums[(n-n%100)/100-1]
        string += "hundred"
    next = n%100
    if next < 20 and next > 0:
        if(n>99):
            string += "and"
        string+=nums[next-1]
    elif next > 0:
        if(n > 99):
            string += "and"
        string+= m10[(next-next%10)/10-1]
        if(n%10 != 0):
            string+= nums[next%10-1]
    return string

for i in range(1,1001):
    whole+=text(i)

print(len(whole))