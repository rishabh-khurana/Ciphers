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
    if firstPos[0] is secPos[0]:
        if (firstPos[1] + 1 == 5):
            firstPos[1] = 0
        else: 
            firstPos[1] = firstPos[1] + 1
        
        if (secPos[1] + 1 == 5):
            secPos[1] = 0
        else:
            secPos[1] = secPos[1] + 1

    # same column
    elif firstPos[1] is secPos[1]:
        if (firstPos[0] + 1 == 5):
            firstPos[0] = 0
        else: 
            firstPos[0] = firstPos[0] + 1
        
        if (secPos[0] + 1 == 5):
            secPos[0] = 0
        else:
            secPos[0] = secPos[0] + 1

    # diff row and column
    else:
        secPos[1],firstPos[1]=firstPos[1],secPos[1]

    return altGrid[firstPos[0]][firstPos[1]],altGrid[secPos[0]][secPos[1]]
