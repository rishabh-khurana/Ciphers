from utils import advArray,GridEncode

# Keyword must be an Isogram

def EncryptPlayfair(Message,Keyword):
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

    for i in altGrid:
        print(i)

    # remove spaces from message and convert it to a list
    Message=list(''.join(Message.upper().split()))
    if len(Message)%2 is not 0:
        Message.append('-')

    # Iterate the Message in pairs
    for i in range(0,len(Message),2):
        # remove repeating letters
        if(Message[i] == Message[i+1]):
            Message[i+1]='~'
        # Encode message in pairs
        Message[i],Message[i+1]=GridEncode(Message[i],Message[i+1],altGrid)

    return ''.join(Message)

if __name__ == "__main__":
    #print(EncryptPlayfair('Hey how are you','lizard'))
    print(EncryptPlayfair('balloon','lizard'))