import math

def FindPath(a):
    sqrtA = math.sqrt(a)
    smallerThanA = math.floor(sqrtA)**2
    biggerThanA = math.ceil(sqrtA)**2
    if biggerThanA == a: length = math.sqrt(biggerThanA) - 1
    elif smallerThanA == a: length = math.sqrt(smallerThanA) - 1
    elif abs(sqrtA - math.sqrt(smallerThanA)) > abs(sqrtA - math.sqrt(biggerThanA)):
        print("Bliżej dużej")
        if biggerThanA - a == 1:
            length = math.sqrt(biggerThanA) - 2
        else: 
            length = math.sqrt(biggerThanA) - 1 
    else:
        print("Bliżej do małej")


    return length

a = 6 # input data here
print(FindPath(a))