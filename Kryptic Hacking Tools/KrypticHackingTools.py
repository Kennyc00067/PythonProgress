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

def exitProgram(): # Exit Program Function Deffinition.
    exitCheck = False # If false, the program loops. If true, the program will quit.

    while exitCheck == False: # Checks if exitCheck is false.
        user_exit = input("Would you like to exit? 'Y' for Yes or 'N' for No: ") # User input for exit question.

        if user_exit == "Y" or user_exit == "y" or user_exit == "Yes" or user_exit == "yes": # Checks if the user said yes.
            exitCheck = True # Sets exitCheck to true, so the program can exit.
        elif user_exit == "N" or user_exit == "n" or user_exit == "No" or user_exit == "no": # Checks if the user said no.
            # Reset variables(If needed)

            break # Ends exit while loop
        else:
            print("Invalid Input. Please use 'Y' for Yes or 'N' for No. ") # Error message

    return(exitCheck) # Returns the value of exitCheck for the if statment that determines to exit the program in def main.

# Main Function Deffinition
def main():
    printProgramInfo()
    
    while True:
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
        if exitProgram() == True:
            try:
                exit() # Exit program.
            except:
                break # Ends main while true loop
            






# Call to Main
main()