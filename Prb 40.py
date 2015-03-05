import math

text = ""

for i in range(0,1000000):
    text += str(i)

prod = int(text[1])*int(text[10])*int(text[100])*int(text[1000])*int(text[10000])*int(text[100000])*int(text[1000000])
print prod