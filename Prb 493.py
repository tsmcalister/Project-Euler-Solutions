from decimal import *
import math

getcontext().prec = 20

friendsList = []
foesList = [0, 1, 2, 3, 4, 5, 6]
container = foesList * 10
prob = [1, 1]

globalProb = []


class bag:
    friendslist = None
    foesList = None
    container = None

    def __init__(self, friendsList, foesList, container):
        self.friendsList = list(friendsList)
        self.foesList = list(foesList)
        self.container = list(container)

    def getNCount(self, n):
        count = 0
        for i in range(0, len(self.container)):
            if self.container[i] == n:
                count += 1
        return (count)

    def getDrawCount(self):
        return (70 - len(self.container))

    def friendPossible(self):
        for i in range(0, len(self.friendsList)):
            if self.getNCount(self.friendsList[i]) > 0:
                return True
        return False

    def foePossible(self):
        for i in range(0, len(self.foesList)):
            if self.getNCount(self.foesList[i]) > 0:
                return True
        return False

    def getFriendProb(self):
        friendCount = 0
        for i in range(0, len(self.friendsList)):
            friendCount += self.getNCount(self.friendsList[i])
        return [friendCount, len(self.container)]

    def getFoeProb(self):
        foeCount = 0
        for i in range(0, len(self.foesList)):
            foeCount += self.getNCount(self.foesList[i])
        return [foeCount, len(self.container)]

    def getFriendBag(self):
        newCont = list(self.container)
        newFriendsList = list(self.friendsList)
        newFoesList = list(self.foesList)
        for i in range(0, len(newCont)):
            if newCont[i] in self.friendsList:
                newCont.pop(i)
                newBag = bag(newFriendsList, newFoesList, newCont)
                return (newBag)

    def getFoeBag(self):
        newCont = list(self.container)
        newFriendsList = list(self.friendsList)
        newFoesList = list(self.foesList)
        for i in range(0, len(newCont)):
            if newCont[i] in self.foesList:
                foe = newCont[i]
                newFoesList.remove(foe)
                newFriendsList.append(foe)
                newCont.pop(i)
                newBag = bag(newFriendsList, newFoesList, newCont)
                return (newBag)


class node:
    global globalProb
    sac = None
    probability = None
    uniqueCount = None
    friendNode = None
    foeNode = None
    Level = None

    def __init__(self, sac, probability, uniqueCount, level):
        self.sac = sac
        self.probability = probability
        self.uniqueCount = uniqueCount
        self.level = level
        self.dispatch()

    def dispatch(self):
        if self.uniqueCount == 7 or self.sac.getDrawCount() == 20:
            self.doLeafTask()
        else:
            self.spawnChildren()

    def spawnChildren(self):
        count = 0
        if self.sac.friendPossible():
            count += 1
            friendB = self.sac.getFriendBag()
            newProb = self.sac.getFriendProb()
            newProb[0] = newProb[0] * self.probability[0]
            newProb[1] = newProb[1] * self.probability[1]
            newUnique = len(friendB.friendsList)
            self.friendNode = node(friendB, newProb, newUnique, self.level + 1)
        if self.sac.foePossible():
            count += 1
            foeB = self.sac.getFoeBag()
            newProb = self.sac.getFoeProb()
            newProb[0] = newProb[0] * self.probability[0]
            newProb[1] = newProb[1] * self.probability[1]
            newUnique = len(foeB.friendsList)
            self.foeNode = node(foeB, newProb, newUnique, self.level + 1)
        if count == 0:
            self.doLeafTask()

    def doLeafTask(self):
        globalProb.append([self.uniqueCount, self.probability])

    def printNode(self):
        print "Level:", self.level
        print "Probability:", self.probability
        print "Unique:", self.uniqueCount


startBag = bag(friendsList, foesList, container)
root = node(startBag, prob, 0, 0)
print len(globalProb)

finalProb = Decimal(0)
for i in range(0, len(globalProb)):
    finalProb += Decimal(globalProb[i][0]) * Decimal(globalProb[i][1][0]) / Decimal(globalProb[i][1][1])
print finalProb


