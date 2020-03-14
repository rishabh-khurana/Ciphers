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
    
    secPos[1],firstPos[1]=firstPos[1],secPos[1]

    return altGrid[firstPos[0]][firstPos[1]],altGrid[secPos[0]][secPos[1]]
