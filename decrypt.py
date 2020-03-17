from utils import GridDecode,MakeGrid

def DecryptPlayfair(Message,Keyword):
    altGrid=MakeGrid(Keyword)

    Message=list(Message)

    # Iterate the Message in pairs
    for i in range(0,len(Message),2):
        # Decode message in pairs
        Message[i],Message[i+1]=GridDecode(Message[i],Message[i+1],altGrid)

    # remove end of sentence character
    if Message[len(Message)-1]=='-':
        del Message[len(Message)-1]

    # remove letter repetition character replacement
    for i in range(len(Message)):
        if Message[i] == '~':
            Message[i] = Message [i-1]

    return ''.join(Message)


if __name__ == "__main__":
    # print(DecryptPlayfair('BF!CPVRDC_NV','lizard'))
    print(DecryptPlayfair('FLR$VRP|','lizard'))
