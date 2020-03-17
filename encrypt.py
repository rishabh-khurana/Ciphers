from utils import MakeGrid,GridEncode

# Keyword must be an Isogram

def EncryptPlayfair(Message,Keyword):
    
    altGrid=MakeGrid(Keyword)

    # to view grid
    # for i in altGrid:
    #     print(i)

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
    print(EncryptPlayfair('Hey how are you','lizard'))
    #print(EncryptPlayfair('balloon','lizard'))