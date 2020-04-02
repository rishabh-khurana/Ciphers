

def ConvertToBinary(Block):
    BinValue=''
    for ASCII in Block:
        binCode=bin(ASCII)[2:]
        missingTrail= 8 - len(binCode)
        if missingTrail is not 0:
            BinValue = BinValue + binCode + '0'*missingTrail
        else:
            BinValue = BinValue + binCode

    return BinValue


# the round function used
def xor(a, b):
    output=""
    for i in range(len(a)):
        #print(i, a, b)
        inter=int(a[i])+int(b[i])
        if inter==2: inter=0
        output = output+str(inter)
    return output

def EncyrptDecrypt(Message,KEY1,KEY2):

    # make sure message is divisible
    if len(Message)%2 is not 0:
        Message = Message + '-'

    cuttingPoint=int(len(Message)/2)

    # splitting into two parts
    Left=Message[0:cuttingPoint].encode()
    Right=Message[cuttingPoint:len(Message)].encode()

    # convert ascii to binary for xor function
    Left=ConvertToBinary(Left)
    Right=ConvertToBinary(Right)

    # generate two keys

    
    # first stage

    L2=Right
    R2=xor(Left,xor(Right,KEY1))

    # second stage

    L3=R2
    R3=xor(L2,xor(R2,KEY2))

    # final reverese

    L4=R3
    R4=L3
    return L4+R4


if __name__=='__main__':
    Message='himynameisrishabandilikeers'

    KEY1='1101001011000100111000101101110011001000110100101101100011010010110101101100101011001010111001001110011010110100'

    KEY2='1101101011000100111010101101110111001000110100101101100011010010110101101100101011001010111001001110011010110100'
    
    print(EncyrptDecrypt(Message,KEY1,KEY2))