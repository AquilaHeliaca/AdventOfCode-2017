def Reallocation(a):
    prevAlloc = []
    inputLength = len(a)
    counter = 0
    while a not in prevAlloc:
        prevAlloc.append(a[:])
        maxValue = max(a)
        i = posNumber = a.index(maxValue)
        a[posNumber] = 0
        while maxValue > 0:
            maxValue -= 1
            i += 1
            if i == inputLength: i = 0
            a[i] += 1
        counter += 1
    return counter
a = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]
print(Reallocation(a))