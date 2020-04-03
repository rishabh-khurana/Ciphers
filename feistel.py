from utils import ConverToHex
import random

def GenerateKey(Length):
    KeyList=[]
    for _ in range(Length):
        bit=random.randint(0,1)
        KeyList.append(str(bit))
    
    return ''.join(KeyList)


def ConvertToBinary(Block):
    messageList=[]
    for character in Block:
        messageList.append(format(ord(character),'08b'))
    return ''.join(messageList)


# the round function used
def xor(a, b):
    output=""
    for i in range(len(a)):
        #print(i, a, b)
        inter = int(a[i]) + int(b[i])
        if inter == 2: inter = 0
        output = output+str(inter)
    return output

def Encyrpt(Message):

    # make sure message is divisible
    if len(Message)%2 is not 0:
        Message = Message + '-'

    cuttingPoint=int(len(Message)/2)

    # splitting into two parts
    Left = Message[0:cuttingPoint]
    Right = Message[cuttingPoint:len(Message)]

    # convert ascii to binary for xor function
    Left = ConvertToBinary(Left)
    Right = ConvertToBinary(Right)

    # generate two keys

    KEY1 = GenerateKey(len(Left))
    KEY2 = GenerateKey(len(Right))

    # first stage

    L2 = Right
    R2 = xor(Left,xor(Right,KEY1))

    # second stage

    L3 = R2
    R3 = xor(L2,xor(R2,KEY2))

    # final reverese

    L4 = R3
    R4 = L3

    return L4 + R4,KEY1,KEY2

def Decrypt(Message,KEY1,KEY2):

    cuttingPoint = int(len(Message)/2)

    # splitting into two parts
    Left = Message[0:cuttingPoint]
    Right = Message[cuttingPoint:len(Message)]

    # first stage

    L2 = Right
    R2 = xor(Left,xor(Right,KEY1))

    # second stage

    L3 = R2
    R3 = xor(L2,xor(R2,KEY2))

    # final reverese

    L4 = R3
    R4 = L3
    return L4+R4



if __name__=='__main__':

    Message='himynameisrishabandilikeers'

    Result,KEY1,KEY2=Encyrpt(Message)

    resultToChar = [chr(int(Result[i:i+8], 2)) for i in range(0, len(Result),8)]
    resultText=""
    for letter in resultToChar:
        resultText = resultText+letter
    
    print(resultText)

    res=Decrypt(Result,KEY2,KEY1)

    resultToChar = [chr(int(res[i:i+8], 2)) for i in range(0, len(res),8)]
    resultText=""
    for letter in resultToChar:
        resultText = resultText+letter

    print(resultText)