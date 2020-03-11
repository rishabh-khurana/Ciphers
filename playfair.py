'''defaultGrid=[['A','B','C','D','E'],
             ['F','G','H','I','K'],
             ['L','M','N','O','P'],
             ['Q','R','S','T','U'],
             ['V','W','X','Y','Z']]'''

alphabetArray=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

altGrid=[]


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


print(altGrid)