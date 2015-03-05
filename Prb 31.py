import math
import itertools
import time


coins = [1,2,5,10,20,50,100,200]

totalcount = 1

start = time.time()
for a in range(0,3):
    newam = a*100
    if newam == 200:
        totalcount += 1
    elif newam < 200:
        for b in range(0,5):
            newam = a*100 + b*50
            if newam == 200:
                totalcount += 1
            elif newam < 200:
                for c in range(0,11):
                    newam = a*100 + b*50 + c*20
                    if newam == 200:
                        totalcount += 1
                    elif newam < 200:
                        for d in range(0,21):
                            newam = a*100 + b*50 + c*20 + d*10
                            if newam == 200:
                                totalcount += 1
                            elif newam < 200:
                                for e in range(0,41):
                                    newam = a*100 + b*50 + c*20 + d*10 + e*5
                                    if newam == 200:
                                        totalcount += 1
                                    elif newam < 200:
                                        for f in range(0,101):
                                            newam = a*100 + b*50 + c*20 + d*10 + e*5 + f*2
                                            if newam == 200:
                                                totalcount += 1
                                            elif newam < 200:
                                                for g in range(0,201):
                                                    newam = a*100 + b*50 + c*20 + d*10 + e*5 + f*2 + g*1
                                                    if newam == 200:
                                                        totalcount += 1
end = time.time()
print end-start
print "done"
print totalcount