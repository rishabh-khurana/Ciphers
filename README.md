# Cipher Application

## About

The Cipher Application is a python based project that allows users to encrpyt/decrypt Messages using popular cipher mechanisms used in the past and enables the user to understand the implementation of the encrypting/decrypting process.

## Project

### Playfair Cipher

This project includes an advanced version of the default Playfair Cipher designed by  Charles Wheatstone in 1854. This Cipher was later used for military purposes by Lord Playfair - hence the name. I chose to implement this Cipher because it is far ahead of time in terms of complexity and allows a decent level of security with a relatively simple protocol. You can get more info about the default Cipher on the following link -> [Playfair Cipher](https://en.wikipedia.org/wiki/Playfair_cipher)


The `encrypt.py` file has a `PlayfairEncrypt()` function which takes in two arguments and return the encrypted text as per the Playfair encoding procedure. The two arguments passed into the function is the Message itself and the Keyword which will be used to alter the grid, in order to get a *unique* Grid (Like a shared secret).The `MakeGrid(Keyword)` function generates this 6x6 grid and is called inside the `PlayfairEncrypt()` function which is used to encrypt the Message as per the Keyword entered by the user.

```
$ python3
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from encrypt import EncryptPlayfair
>>> EncryptPlayfair('Hi I am Kryptos','lizard')
'CDZRNMI?MWKV'
>>> from decrypt import DecryptPlayfair
>>> DecryptPlayfair('CDZRNMI?MWKV','lizard')
'HIIAMKRYPTOS'
```

Notice the use of special character in the cryptic message this is because the new grid supports 10 characters for encoding however the default playfair implementation uses only Letters A-Z (26 letters). This way we can modify the grid to increase the complexity of encrypted message and make it harder to decrypt.

### Hill Cipher 

Another Cipher mechanism that I find quite interesting is the simple implementation of the Hill Cipher which was invented by Lester S. Hill in 1929 using principles of linear algebra. In the encryption process we use a 2x2 matrix with very unique properties which is used as a secret. The inverse modulo 26 of this matrix is used as the key to decrypt the cipher. The way this encryption process works is, we divide the message in blocks of 2s, convert it into ASCII code and multiply with the 'secret matrix'. We decrypt the message using the inverse of this matrix and multiply it with encrypted message the same way(in blocks of 2 letters at a time) and we get back our original message. The only drawback in this method is to find a key matrix that has a inverse modulo of 26.

The `hill.py` file uses the key matrix from `utils.py` and the `encrypt()` function takes in the message and the key Matrix and gives the encrypted message as the output. However, this method uses Block encryption without shuffling the encrypted blocks which is a vulnerability.
The `decrypt()` function works in a similar way as well, except it takes the encrypted message and converts the Key Matrix to the inverse modulo 26 of itself for decryption. 

```
$ python3
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from hill import encrypt,decrypt
>>> from utils import KeyMatrix
>>> encrypt('I am Kryptos',KeyMatrix)
'DWTCYEDBXU'
>>> decrypt('DWTCYEDBXU',KeyMatrix)
'IAMKRYPTOS'

```

### Feistel Cipher