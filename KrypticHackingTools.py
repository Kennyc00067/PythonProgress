### Kryptic Studio ###

# Local Libraries
from Core import email as coreEmail
from Core import hash
from Core import bruteGuess
from Core import arps_spoof
from Core import IPspoof
from Core import urlIP
# Libraries

# Standard Libraries
import os
import time


# check whether user is root
#if os.geteuid() != 0:
#    print("\nERROR: Kryptic Hacking Tools must be run with root privileges. Try again with sudo: sudo python3 KrypticHackingTools.py3\n")
#    os._exit(1)

# Function Deffinitions
def printProgramInfo():
    author = "*** Kryptic Studios ***"
    program = "*** Hacking Tools ***"

    print(author)
    print(program)
    
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
        menu = " 1. Password Cracker\n 2. Spoofing\n"
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
                print("Hash Password Cracker")
                hash.hash()

            if pcInput in ["3"]:
                os.system('clear')
                print("Brute Force Password Cracker(WIP)")
                bruteGuess.bruteGuess()
        if userInput in ["2"]:
            os.system('clear')

            print("\nSpoofer")
            spoofMenu = " 1. Get Clients\n 2. Monitor Clients\n 3. Sniff Client Traffic\n 4. DDos Attack\n 5. IP Spoofing\n 6. URL IP Grabber"
            print(spoofMenu)
            spoofInput = input("Choose your poision: ")

            if spoofInput in ["1"]:
                os.system('clear')
                print("(W)LAN Clients")
                arps_spoof.get_clients_OnLan()

            if spoofInput in ["2"]:
                os.system('clear')
                print("Monitor (W)LAN Clients")
                arps_spoof.monitor_clients_OnLan()

            if spoofInput in ["3"]:
                os.system('clear')
                print("Sniff Client Traffic")
                arps_spoof.traffic_sniff()

            if spoofInput in ["4"]:
                os.system('clear')
                print("DDos Attack")
                arps_spoof.ddosAttack()
            
            if spoofInput in ["5"]:
                os.system('clear')
                print("IP Spoofing")
                IPspoof.ipSpoof()
            if spoofInput in ["6"]:
                os.system('clear')
                print("URL IP Grabber")
                urlIP.get_ip_address()

        if exitProgram() == True:
            try:
                exit() # Exit program.
            except:
                break # Ends main while true loop
            






# Call to Main
main()