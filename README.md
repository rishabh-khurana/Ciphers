# Cipher Application

## About

This project is an advanced version of the default Playfair Cipher designed by  Charles Wheatstone in 1854. This Cipher was later used for military purposes by Lord Playfair - hence the name. I chose to implement this Cipher because it is far ahead of time in terms of complexity and allows a decent level of security with a relatively simple protocol. You can get more info about the default Cipher on the following link -> [Playfair Cipher](https://en.wikipedia.org/wiki/Playfair_cipher)

## Project

The 'encrypt.py' file has a 'PlayfairEncrypt()' function which takes in two arguments and return the encrypted text as per the Playfair encoding procedure. The two arguments passed into the function is the Message itself and the Keyword which will be used to alter the grid, in order to get a *unique* Grid (Like a shared secret).The MakeGrid(Keyword) function generates this 6x6 grid and is called inside the PlayfairEncrypt() function which is used to 
encrypt the Message as per the Keyword entered by the user.

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
