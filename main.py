from encrypt import *

import os,sys
def cls():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
        
 print("Hill Cipher Converter Pro")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━")
def main():
    cls()
    exit=False
    print("Welcome to my program :)")
    input("Enter...")
    while True:
        try:
            cls()
            print("1. Hill Cipher Encoder\n2. Exit")
            n=int(input("\nChoose Program : "))
            if n==1:
                cls()
                Encrypt()
         
           
