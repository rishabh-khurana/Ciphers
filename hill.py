from utils import KeyMatrix,alphabet
import numpy as np

def encrypt(Message,Key=KeyMatrix):
    Message=list(''.join(Message.upper().split()))

    if len(Message)%2 is not 0:
        Message.append('X')

    # replace letters with numbers
    for i in range(len(Message)):
        Message[i]=alphabet.index(Message[i]) + 1 

    # covert the matrix to numpy array
    Key=np.array(Key)
    for i in range(0,len(Message),2):
        sub=[Message[i],Message[i+1]]
        sub=np.array(sub)
        sub.shape = (2,1)
        new=Key.dot(sub)
        Message[i]=alphabet[new[0][0]%26]
        Message[i+1]=alphabet[new[1][0]%26]
    
    return ''.join(Message)

if __name__ == "__main__":
    print(encrypt('how are you',KeyMatrix))