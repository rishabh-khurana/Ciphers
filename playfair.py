'''defaultGrid=[['A','B','C','D','E'],
             ['F','G','H','I','K'],
             ['L','M','N','O','P'],
             ['Q','R','S','T','U'],
             ['V','W','X','Y','Z']]'''

alphabetArray=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

altGrid=[]

Message='Hey how are you'

# TODO check if word is an Isograms
KeyWord='lizard'

resultArr=list(KeyWord.upper().strip())

# add alphabets to the array except the ones already present
for letter in alphabetArray:
    if len(resultArr) < 25:
        if letter not in resultArr:
            resultArr.append(letter)
    else:
        break


# create new 5x5 grid based on keyword 
subArr=[]
count=0
for i in resultArr:
    if count<5: 
        subArr.append(i)
        count=count+1
    else:
        altGrid.append(subArr)
        count=0
        subArr=[]
        subArr.append(i)
        count=count+1

altGrid.append(subArr)


# print(altGrid)

# remove spaces from message
Message=list(''.join(Message.upper().split()))

# TODO add an X at the end of the list if the number of letters is odd

for i in altGrid:
    print(i)

# horizontally opposite corners
def GridEncode(First,Second):
    firstPos=[]
    secPos=[]
    for i in range(5):
        for j in range(5):
            if altGrid[i][j] == First:
                firstPos=[i,j]
                break

    for i in range(5):
        for j in range(5):  
            if altGrid[i][j] == Second:
                secPos=[i,j]
                break
    
    secPos[1],firstPos[1]=firstPos[1],secPos[1]

    print(firstPos)
    print(secPos)
    print('###########')

    return altGrid[firstPos[0]][firstPos[1]],altGrid[secPos[0]][secPos[1]]
    
    # print(firstPos)
    # print(secPos)
    # print('###########')
    # # for the same subgrid
    # return First,Second

# Iterate the Message in pairs
for i in range(0,len(Message),2):
    # remove repeating letters
    if(Message[i] == Message[i+1]):
        Message[i+1]='X'
    # Encode message in pairs
    Message[i],Message[i+1]=GridEncode(Message[i],Message[i+1])


print(Message)