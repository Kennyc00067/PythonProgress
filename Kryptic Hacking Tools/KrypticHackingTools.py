### Kryptic Studio ###

# Local Libraries
from Core import email as coreEmail
from Core import hash

# Libraries

# Standard Libraries
import os
import time

# Function Deffinitions
def printProgramInfo():
    author = "*** Kryptic Studios ***"
    program = "*** Hacking Tools ***"

    print(author)
    time.sleep(5)
    print(program)
    time.sleep(5)
    
    os.system('clear')
    return

# Main Function Deffinition
def main():
    #printProgramInfo()
    
    menu = " 1. Password Cracker\n"
    print(menu)
    userInput = input("Choose your poision: ")

    if userInput in ["1"]:
        os.system('clear')

        print("\n\nPassword Cracker")
        pcMenu = " 1. Email\n 2. Hash\n 3. Brute Guess"
        print(pcMenu)
        pcInput = input("Choose your poision: ")

        if pcInput in ["1"]:
            os.system('clear')
            print("Email Password Cracker")
            epcMenu = " 1. Gmail\n 2. Outlook (outlook, hotmail, live)\n 3. Yahoo Mail\n"
            print(epcMenu)
            epcInput = input("Choose your poision: ")

            if epcInput in ["1"]:
                print("\n\nGmail Password Cracker\n")
                coreEmail.gmail()
            
            if epcInput in ["2"]:
                print("\n\nOutlook Email Password Cracker\n")
                coreEmail.live()
            if epcInput in ["3"]:
                print("\n\Yahoo Email Password Cracker\n")
                coreEmail.yahoo()

        if pcInput in ["2"]:
            os.system('clear')
            print("Hack Password Cracker")
            hash.hash()
            






# Call to Main
main()