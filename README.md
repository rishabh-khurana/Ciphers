# Cipher Application

## About

This project is an advanced version of the default Playfair Cipher designed by  Charles Wheatstone in 1854. This Cipher was later used for military purposes by Lord Playfair - hence the name. I chose to implement this Cipher because it is far ahead of time in terms of complexity and allows a decent level of security with a relatively simple protocol. You can get more info about the default Cipher on the following link -> [Playfair Cipher](https://en.wikipedia.org/wiki/Playfair_cipher)

## Project

The 'encrypt.py' file has a 'PlafairEncrypt()' function which takes in two arguments and return the encrypted text as per the Playfair encoding procedure. The two arguments passed into the function is the Message itself and the Keyword which will be used to alter the grid, in order to get a *unique* Grid (Like a shared secret). 
