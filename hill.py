from utils import KeyMatrix,alphabet
import numpy as np
from egcd import egcd

def encrypt(Message,Key=KeyMatrix):
    Message=list(''.join(Message.upper().split()))

    if len(Message)%2 is not 0:
        Message.append('X')

    # replace letters with numbers
    for i in range(len(Message)):
        Message[i]=alphabet.index(Message[i]) + 1 

    # covert the matrix to numpy array
    Key=np.array(Key)

    # encode message as per key matrix
    for i in range(0,len(Message),2):
        sub=[Message[i],Message[i+1]]
        sub=np.array(sub)
        sub.shape = (2,1)
        new=Key.dot(sub)
        Message[i]=alphabet[(new[0][0]%26)-1]
        Message[i+1]=alphabet[(new[1][0]%26)-1]
    
    return ''.join(Message)

def decrypt(Message,Key=KeyMatrix):
    Message=list(''.join(Message.upper().split()))

    # calculate decryption key

    # determinant
    det = int(np.round(np.linalg.det(Key))) 
    # inverse of determin
    det_inv = egcd(det, 26)[1] % 26
    # matrix modulus inverse
    matrix_modulus_inv = det_inv * np.round(det*np.linalg.inv(Key)).astype(int) % 26
    # covert the matrix to numpy array
    matrix_modulus_inv=np.array(matrix_modulus_inv)
    
    # replace letters with numbers
    for i in range(len(Message)):
        Message[i]=alphabet.index(Message[i]) + 1 


    # decode message as per key matrix
    for i in range(0,len(Message),2):
        sub=[Message[i],Message[i+1]]
        sub=np.array(sub)
        sub.shape = (2,1)
        new=matrix_modulus_inv.dot(sub)
        Message[i]=alphabet[(new[0][0]%26)-1]
        Message[i+1]=alphabet[(new[1][0]%26)-1]

        if Message[len(Message)-1] is 'X':
            del Message[len(Message)-1]

    return ''.join(Message)

if __name__ == "__main__":
    #print(encrypt('how are you',KeyMatrix))
    print(decrypt('QMTYQIPUEF',KeyMatrix))