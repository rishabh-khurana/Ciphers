'''Cipher Application
   by Rishabh Khurana'''

from encrypt import EncryptPlayfair
from decrypt import DecryptPlayfair
from hill import encrypt as EncryptHill
from hill import decrypt as DecryptHill
from utils import KeyMatrix
from feistel import Encyrpt as EncyrptFeistel
from feistel import Decrypt as DecryptFeistel
from feistel import ConvertToString
from pyfiglet import Figlet
import terminal_banner as DisplayMessage
import os

def InvalidInput():
    print(DisplayMessage.Banner("Invalid input, please try again\n"))


def LoadPlayfairApp():
    f = Figlet(font='big')
    print(f.renderText('Playfair'))
    Task = input(DisplayMessage.Banner("Please choose an option from the following list\n E - encrypt\n D - Decrypt\n B - back to Main Menu\n"))
    if Task in ["E","D","e","d","B","b"]:
        if Task in ["E","e"]:
            Message = input(DisplayMessage.Banner("Please Enter the string to be Encrypted\n"))
            Keyword = input(DisplayMessage.Banner("Please enter a Keyword (Isogram)\n"))
            os.system("clear")
            print(DisplayMessage.Banner(f"The encrypted string is {EncryptPlayfair(Message,Keyword)}"))
            LoadPlayfairApp()
        elif Task in ["B","b"]:
            os.system("clear")
            LoadMain()
        else:
            Message = input(DisplayMessage.Banner("Please Enter the string to be Decrypted\n"))
            Keyword = input(DisplayMessage.Banner("Please enter a Keyword (Isogram)\n"))
            os.system("clear")
            print(DisplayMessage.Banner(f"The decrypted string is {DecryptPlayfair(Message,Keyword)}"))
            LoadPlayfairApp()
    else:
        os.system("clear")
        InvalidInput()
        LoadPlayfairApp()

def LoadHillApp():
    f = Figlet(font='big')
    print(f.renderText('Hill'))
    Task = input(DisplayMessage.Banner("Please choose an option from the following list\n E - encrypt\n D - Decrypt\n B - back to Main Menu\n"))
    if Task in ["E","D","e","d","B","b"]:
        if Task in ["E","e"]:
            Message = input(DisplayMessage.Banner("Please Enter the string to be Encrypted"))
            os.system("clear")
            print(DisplayMessage.Banner(f"The encrypted string is {EncryptHill(Message,KeyMatrix)}"))
            LoadHillApp()
        elif Task in ["B","b"]:
            os.system("clear")
            LoadMain()
        else:
            Message = input(DisplayMessage.Banner("Enter the string to be Decrypted"))
            os.system("clear")
            print(DisplayMessage.Banner(f"The decrypted string is {DecryptHill(Message,KeyMatrix)}"))
            LoadHillApp()
    else:
        os.system("clear")
        InvalidInput()
        LoadHillApp()


def LoadFeistelApp():
    f = Figlet(font='big')
    print(f.renderText('Feistel'))
    Task = input(DisplayMessage.Banner("Please choose an option from the following list\n E - encrypt\n D - Decrypt\n B - back to Main Menu\n"))
    if Task in ["E","D","e","d","B","b"]:
        if Task in ["E","e"]:
            Message = input(DisplayMessage.Banner("Please Enter the string to be Encrypted\n"))
            Result,KEY1,KEY2=EncyrptFeistel(Message)
            # It is better to use binary because string might encode to new line char or some other encoding
            os.system("clear")
            print(DisplayMessage.Banner(f"The encrypted string in binary form is {Result}\nThe first Key is {KEY1}\nThe second key is {KEY2}\n"))
            LoadFeistelApp()
        elif Task in ["B","b"]:
            os.system("clear")
            LoadMain()
        else:
            DecimalMessage = input(DisplayMessage.Banner("Please Enter the binary code to be Decrypted\n"))
            KEY1 = input(DisplayMessage.Banner("Please enter the first binary key\n"))
            KEY2 = input(DisplayMessage.Banner("Please enter the second binary key\n"))
            Result=DecryptFeistel(DecimalMessage,KEY1,KEY2)
            os.system("clear")
            Final=ConvertToString(Result)
            if Final[-1]=="-":
                Final=Final[:-1]
            print(DisplayMessage.Banner(f"The decrypted string is {Final}\n"))
            LoadFeistelApp()
    else:
        os.system("clear")
        InvalidInput()
        LoadFeistelApp()


def LoadMain():
    f = Figlet(font='slant')
    print(f.renderText('Ciphers'))
    Menu = "Please choose a Cipher Type from the following list:\n 1.Playfair Cipher\n 2.Hill Cipher\n 3.Feistel Cipher\n 4.Exit\n"
    print(DisplayMessage.Banner(Menu))
    try:
        val = int(input("You chose:\n"))
        if val in [1,2,3,4]:
            if val == 1:
                os.system("clear")
                LoadPlayfairApp()
            elif val == 2:
                os.system("clear")
                LoadHillApp()
            elif val == 3:
                os.system("clear")
                LoadFeistelApp()
            else:
                os.system("clear")
                exit(0)
        else:
            raise ValueError
    except ValueError:
        os.system("clear")
        InvalidInput()
        LoadMain()


if __name__=="__main__":
    os.system("clear")
    print(f"Hi! Welcome to the Cipher Appliaction\n")
    LoadMain()

