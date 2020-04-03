'''defaultGrid=[['A','B','C','D','E'],
             ['F','G','H','I','K'],
             ['L','M','N','O','P'],
             ['Q','R','S','T','U'],
             ['V','W','X','Y','Z']]'''

'''advGrid=[['A','B','C','D','E','F'],
            ['G','H','I','J','K','L'],
            ['M','N','O','P','Q','R'],
            ['S','T','U','V','W','X'],
            ['Y','Z','_','.','?','!'],
            ['$','@','/','|','~','-']]'''

advArray=['A','B','C','D','E','F',
            'G','H','I','J','K','L',
            'M','N','O','P','Q','R',
            'S','T','U','V','W','X',
            'Y','Z','_','.','?','!',
            '$','@','/','|','~','-']

# for hill Cipher
KeyMatrix=[[3,3],
           [2,5]]

alphabet=list('abcdefghijklmnopqrstuvwxyz'.upper())

def MakeGrid(Keyword):

    resultArr=list(Keyword.upper().strip())
    # Make new array with Keyword and advArray
    for letter in advArray:
        if len(resultArr) < 36:
            if letter not in resultArr:
                resultArr.append(letter)
        else:
            break
    
    # Make a 6x6 grid with new array
    altGrid=[]
    subArr=[]
    count=0
    for i in resultArr:
        if count<6: 
            subArr.append(i)
            count=count+1
        else:
            altGrid.append(subArr)
            count=0
            subArr=[]
            subArr.append(i)
            count=count+1

    altGrid.append(subArr)

    return altGrid


# takes any two letters and ecodes it according to the 6x6 Grid
def GridEncode(First,Second,altGrid):
    firstPos=[]
    secPos=[]
    for i in range(6):
        for j in range(6):
            if altGrid[i][j] == First:
                firstPos=[i,j]
                break

    for i in range(6):
        for j in range(6):  
            if altGrid[i][j] == Second:
                secPos=[i,j]
                break
    # same row         
    if firstPos[0] == secPos[0]:
        if (firstPos[1] + 1 > 5):
            # wrap around
            firstPos[1] = 0
        else: 
            firstPos[1] = firstPos[1] + 1
        
        if (secPos[1] + 1 > 5):
            # wrap around
            secPos[1] = 0
        else:
            secPos[1] = secPos[1] + 1

    # same column
    elif firstPos[1] == secPos[1]:
        if (firstPos[0] + 1 > 5):
            # wrap around
            firstPos[0] = 0
        else: 
            firstPos[0] = firstPos[0] + 1
        
        if (secPos[0] + 1 > 5):
            # wrap around
            secPos[0] = 0
        else:
            secPos[0] = secPos[0] + 1

    # diff row and column
    else:
        secPos[1],firstPos[1]=firstPos[1],secPos[1]

    return altGrid[firstPos[0]][firstPos[1]],altGrid[secPos[0]][secPos[1]]


# reverse engineer GridEncode
def GridDecode(First,Second,altGrid):
    firstPos=[]
    secPos=[]
    for i in range(6):
        for j in range(6):
            if altGrid[i][j] == First:
                firstPos=[i,j]
                break

    for i in range(6):
        for j in range(6):  
            if altGrid[i][j] == Second:
                secPos=[i,j]
                break
    
    # same row         
    if firstPos[0] == secPos[0]:
        if (firstPos[1] - 1 < 0):
            # wrap around
            firstPos[1] = 5
        else: 
            firstPos[1] = firstPos[1] - 1
        
        if (secPos[1] - 1 < 0):
            # wrap around
            secPos[1] = 5
        else:
            secPos[1] = secPos[1] - 1

    # same column
    elif firstPos[1] == secPos[1]:
        if (firstPos[0] - 1 < 0):
            # wrap around
            firstPos[0] = 5
        else: 
            firstPos[0] = firstPos[0] - 1
        
        if (secPos[0] - 1 < 0):
            # wrap around
            secPos[0] = 5
        else:
            secPos[0] = secPos[0] - 1

    # diff row and column
    else:
        secPos[1],firstPos[1]=firstPos[1],secPos[1]

    return altGrid[firstPos[0]][firstPos[1]],altGrid[secPos[0]][secPos[1]]

    
def ConverToHex(binary):
    res="0x"
    hexList = [hex(int(binary[i:i+8], 2))[2:] for i in range(0, len(binary),8)]
    for hexa in hexList:
        if len(hexa)==1: hexa ="0"+hexa
        res = res + hexa
    return res