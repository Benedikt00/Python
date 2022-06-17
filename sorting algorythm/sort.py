import random


randList = []

for i in range(20):
    randList.append(i)

random.shuffle(randList)

def swap(list, a, b):
    n1 = list[a]
    n2 = list[b]

    list[a] = n2
    list[b] = n1
    return list


for x in range(len(randList)):
    for i in range(0, len(randList)-1):
        a = randList[i]
        b = randList[i+1]
        if a > b:
            swap(randList, i, i+1)















