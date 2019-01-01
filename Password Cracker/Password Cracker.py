### KRYPTIC STUDIO ###
# Crack e9af612aa100a4427e071d363c8b80b1


# Include libraries here
import sys
import hashlib
import itertools
import time
import os

# Include functions here
def printProgramInfo():
    info = "*** Password Craker *** \n****Kryptic Studio****"
    return (info)

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

def timer():
    seconds = float(0)
    minutes = float(0)
    hours = float(0)
    days = float(0)
    while True:
        if seconds > 59:
            seconds = 0
            minutes +=1
        if minutes > 59:
            minutes = 0
            hours += 1
        if hours > 23:
            hours = 0
            days +=1
        os.system("clear")
        seconds += .1
        print("{}:{}:{}:{}".format(days, hours, minutes, seconds))
        time.sleep(.1)

        #if days == 365:
            #break
def dataChoiceOne(pass_in, hash):
    if hash == "sha1":
        hash = hashlib.sha1
    if hash == "sha224":
        hash = hashlib.sha224
    if hash == "sha256":
        hash = hashlib.sha256
    if hash == "sha384":
        hash = hashlib.sha384
    if hash == "sha512":
        hash = hashlib.sha512
    if hash == "md5":
        hash = hashlib.md5

    try:
        passwordFile = open("Default/default.txt", "r")
    except: 
        print("\nFile Not Found.")
        return
    
    passNumber = 0
    for password in passwordFile:
        passNumber += 1
        filehash = hash(password.strip().encode('utf')).hexdigest()
        print("Trying password number {}: {}".format(passNumber, password.strip()))

        if pass_in == filehash:
            print("\nMatch Found. \nPassword is: {}".format(password))
            passwordFile.close()
            return


    passwordFile.close()
    print("\nPassword Not Found.")
    return

def dataChoiceTwo(fileName, pass_in, hash):
    if hash == "sha1":
        hash = hashlib.sha1
    if hash == "sha224":
        hash = hashlib.sha224
    if hash == "sha256":
        hash = hashlib.sha256
    if hash == "sha384":
        hash = hashlib.sha384
    if hash == "sha512":
        hash = hashlib.sha512
    if hash == "md5":
        hash = hashlib.md5

    try:
        passwordFile = open("User List/" + fileName, "r")
    except: 
        print("\nFile Not Found.")
        return
    
    passNumber = 0
    for password in passwordFile:
        passNumber += 1
        filehash = hash(password.strip().encode('utf')).hexdigest()
        print("Trying password number {}: {}".format(passNumber, password.strip()))

        if pass_in.strip() == filehash:
            print("\nMatch Found. \nPassword is: {}".format(password))
            passwordFile.close()
            return


    passwordFile.close()
    print("\nPassword Not Found.")
    return

def dataChoiceThree(path, pass_in, hash):
    if hash == "sha1":
        hash = hashlib.sha1
    if hash == "sha224":
        hash = hashlib.sha224
    if hash == "sha256":
        hash = hashlib.sha256
    if hash == "sha384":
        hash = hashlib.sha384
    if hash == "sha512":
        hash = hashlib.sha512
    if hash == "md5":
        hash = hashlib.md5

    try:
        passwordFile = open(path, "r")
    except: 
        print("\nFile Not Found.")
        return
    
    passNumber = 0
    for password in passwordFile:
        passNumber += 1
        filehash = hash(password.strip().encode('utf')).hexdigest()
        print("Trying password number {}: {}".format(passNumber, password.strip()))

        if pass_in == filehash:
            print("\nMatch Found. \nPassword is: {}".format(password))
            passwordFile.close()
            return


    passwordFile.close()
    print("\nPassword Not Found.")
    return
def tryPassword(passwordSet, stringTypeSet):
    start = time.time()
    chars = stringTypeSet
    attempts = 0
    for i in range(1, 20):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            if letter == passwordSet:
                end = time.time()
                distance = end - start
                return (attempts, distance)
    


#__________________________________________________
# def main(): goes here
def main():
    print("{}".format(printProgramInfo())) #Do not Delete

    # Main loop
    while True:
        bruteorGuess = input("\n Would like to: \n 1. Brute Attack \n 2. Enter a Hash\n>>>")
        if bruteorGuess.lower() in ["1"]:
            password = input("Please enter a password: ")
            # Allowed characters
            stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
            tries, timeAmount = tryPassword(password, stringType)
            print("The password %s was cracked in %s tries and %s seconds!" % (password, tries, timeAmount))
        elif bruteorGuess in ["2"]:
            while True:
                hashtype = input("\nWhat type of hash(MD5, SHA256, Etc...): ")
                hashTypeList = ["sha1", "sha224", "sha256", "sha384", "sha512", "md5"]
                if hashtype.lower() in hashTypeList:
                    break
                else:
                    print("\nHash Type Not Found.")
            while True:
                haveHash = input("\nDo you have a Hash String(Yes or No)? ")
                if haveHash.lower() in ["yes", "y"]:
                    user_password = input("\nPlease enter the {} Hash: ".format(hashtype.upper()))
                    break
                elif haveHash.lower() in ["no", "n"]:
                    hash_pass = input("\nPlease enter a password: ")
                    if hashtype.lower() == "sha1":
                        hash = hashlib.sha1
                    if hashtype.lower() == "sha224":
                        hash = hashlib.sha224
                    if hashtype.lower() == "sha256":
                        hash = hashlib.sha256
                    if hashtype.lower() == "sha384":
                        hash = hashlib.sha384
                    if hashtype.lower() == "sha512":
                        hash = hashlib.sha512
                    if hashtype.lower() == "md5":
                        hash = hashlib.md5
                    realHash = hash(hash_pass.strip().encode('utf')).hexdigest()
                    user_password = realHash
                    print("\nThe password {} : {} -> {}".format(hash_pass.strip(), hashtype, realHash))
                    exitcontinue = False
                    while True:
                        pointexit = input("\nWould you like to exit(Yes) or continue(No)? ")
                        if pointexit.lower() in ["yes", "y"]:
                            try:
                                sys.exit()
                            except:
                                print("\nError: The program could not exit.")
                        elif pointexit.lower() in ["no", "n"]:
                            exitcontinue = True
                            break
                        else:
                            print("\nInvalid Input")
                else:
                    print("Invalid Input")
                if exitcontinue == True:
                    break

            dataChoice = None
            while dataChoice == None:
                choice = input("\nPlease chose file method \n 1. Default \n 2. Custom File (/User List) \n 3. Custom Path \n>>> ")

                choice1 = ["1", "default", "Default", "standard", "Standard", "regular", "Regular"]
                choice2 = ["2", "custom file", "customfile", "Custom File", "Custom file", "CustomFile", "customFile", "Customfile", "custom File"]
                choice3 = ["3", "custom path", "custompath", "Custom Path", "Custom path", "CustomPath", "customPath", "Custompath", "custom Path"]
                if choice in choice1:
                    dataChoice = 1
                    break
                elif choice in choice2:
                    dataChoice = 2
                    break
                elif choice in choice3:
                    dataChoice = 3
                    break
                else:
                    print("\nInvalid Input. Please use '1' for default file, '2' for custom file(/User List), or '3' for custom path")
            if dataChoice == 1:
                dataChoiceOne(user_password, hashtype.lower())
            if dataChoice == 2:
                user_FileName = input("\nPlease enter File Name(.txt): ")
                dataChoiceTwo(user_FileName, user_password, hashtype.lower())
            if dataChoice == 3:
                user_Path = input("\nPlease enter File(.txt) Path: \n   Path: ")
                dataChoiceThree(user_Path, user_password, hashtype.lower())

        #passwordCounter = 1
        if exitProgram() == True:
            try:
                sys.exit(0) # Exit program.
            except:
                break # Ends main while true loop

# Call to main
main()
