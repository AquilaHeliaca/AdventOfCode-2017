def calculateSquares(x,y):
    a = lst[x + 1][y + 1] + lst[x + 1][y] + lst[x + 1][y - 1] + lst[x][y + 1] + lst[x][y] + lst[x][y - 1] + lst[x - 1][y + 1] + lst[x - 1][y] + lst[x - 1][y - 1]
    return a

def kurwa(inpVar):
    for x in range(11):
        lst.append([])
        for y in range(11):
            lst[x].append(0)

    directories = {"right":0, "up": 1,"left":2,"down":3}
    magnitude = 1
    changeMagnitude = 0
    #center
    lst[5][5] = 1
    print (lst)
    OX = 5 
    OY = 5
    currentDir = 0
    for z in range(30):
        
        for x in range(magnitude):
            if currentDir == directories["right"]: OY += 1
            elif currentDir == directories["up"]: OX -= 1
            elif currentDir == directories["left"]: OY -= 1
            elif currentDir == directories["down"]: OX += 1
            
            lst[OX][OY] = calculateSquares(OX,OY)
            if lst[OX][OY] > inpVar: return lst[OX][OY]
        currentDir += 1
        if currentDir >3:currentDir = 0
        changeMagnitude+=1
        if changeMagnitude >= 2:
            changeMagnitude = 0
            magnitude +=1
            
    for line in lst:
        print(line)
lst = []
inpVar = "input data here"
print(kurwa(inpVar))