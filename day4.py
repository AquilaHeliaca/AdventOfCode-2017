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
                if word == splitLine[x] and wordPos != x:
                    isValid = False
        if isValid:
            valid+=1
        else:
            isValid = True
    return valid

a = """input data here"""
print(Check(a))