def Check(a):
    valid = 0
    isValid = True
    passes = a.split("\n")
    for line in passes:
        splitLine = line.split(" ")
        lenLine = len(splitLine)
        for word in splitLine:
            wordPos = splitLine.index(word)
            for x in range(lenLine):
                splitWord1 = list(word)
                splitWord2 = list(splitLine[x])
                splitWord1.sort()
                splitWord2.sort()
                if splitWord2 == splitWord1 and wordPos != x:
                    isValid = False
        if isValid:
            valid+=1
        else:
            isValid = True
    return valid

a = """input data here"""
print(Check(a))