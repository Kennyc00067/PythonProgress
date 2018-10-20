# Name: Kenneth Carman
# Date: October 18, 2018
# Desc: Loan payment calculator

# Include libraries here.

# Include functions here.
def printName():
    name = "Kenneth Carman" # My Name
    return (name)

def loanPayment(loan, numPayments):
    if loan >= 500 and loan <= 2500: # $500 - $2500
        if numPayments >= 6 and numPayments <=12: # Number of payments 6-12. 
            rate = .08/12 # Payment rate divided by 12.
            trueRate = (rate * 12) * 100 # True payment rate.
            top = rate * loan # This is the numerator to calculate the loan payment.
            bottom = 1 - ((1+rate)**-numPayments) # This is the denominator to calculate the loan payment.
            payment = round(top/bottom, 2) # This is the loan payment formula, simplified. 
            loanTotal = payment * numPayments # This is the loan payment. This is the total loan payment that will be payed over time(Includes intrest).

            print(" ") # Blank line(For better Organinization)

            print("Loan Cost: ${:.2f} \nNumber of Payments: {:.0f} \nMonlthy Payment: ${:.2f} \nIntrest Rate: {:.0f}%".format(loanTotal, numPayments, payment, trueRate)) # Data Output
        elif numPayments >= 13 and numPayments <=36: # Number of payments 13-36.
            rate = .1/12 # Payment rate divided by 12.
            trueRate = (rate * 12) * 100 # True payment rate.
            top = rate * loan # This is the numerator to calculate the loan payment.
            bottom = 1 - ((1+rate)**-numPayments) # This is the denominator to calculate the loan payment.
            payment = round(top/bottom, 2) # This is the loan payment formula, simplified.
            loanTotal = payment * numPayments # This is the loan payment. This is the total loan payment that will be payed over time(Includes intrest).

            print(" ") # Blank line(For better Organinization)

            print("Loan Cost: ${:.2f} \nNumber of Payments: {:.0f} \nMonlthy Payment: ${:.2f} \nIntrest Rate: {:.0f}%".format(loanTotal, numPayments, payment, trueRate)) # Data Output
        elif numPayments >= 37 and numPayments <=48: # Number of payments 37-48.
            rate = .12/12 # Payment rate divided by 12.
            trueRate = (rate * 12) * 100 # True payment rate.
            top = rate * loan # This is the numerator to calculate the loan payment.
            bottom = 1 - ((1+rate)**-numPayments) # This is the denominator to calculate the loan payment.
            payment = round(top/bottom, 2) # This is the loan payment formula, simplified.
            loanTotal = payment * numPayments # This is the loan payment. This is the total loan payment that will be payed over time(Includes intrest).

            print(" ") # Blank line(For better Organinization)

            print("Loan Cost: ${:.2f} \nNumber of Payments: {:.0f} \nMonlthy Payment: ${:.2f} \nIntrest Rate: {:.0f}%".format(loanTotal, numPayments, payment, trueRate)) # Data Output
    elif loan >= 2501 and loan <= 10000: # $2501 - $10000
        if numPayments >= 6 and numPayments <=12: # Number of payments 6-12.
            rate = .07/12 # Payment rate divided by 12.
            trueRate = (rate * 12) * 100 # True payment rate.
            top = rate * loan # This is the numerator to calculate the loan payment.
            bottom = 1 - ((1+rate)**-numPayments) # This is the denominator to calculate the loan payment.
            payment = round(top/bottom, 2) # This is the loan payment formula, simplified.
            loanTotal = payment * numPayments # This is the loan payment. This is the total loan payment that will be payed over time(Includes intrest).

            print(" ") # Blank line(For better Organinization)

            print("Loan Cost: ${:.2f} \nNumber of Payments: {:.0f} \nMonlthy Payment: ${:.2f} \nIntrest Rate: {:.0f}%".format(loanTotal, numPayments, payment, trueRate)) # Data Output
        elif numPayments >= 13 and numPayments <=36: # Number of payments 13-36.
            rate = .08/12 # Payment rate divided by 12.
            trueRate = (rate * 12) * 100 # True payment rate.
            top = rate * loan # This is the numerator to calculate the loan payment.
            bottom = 1 - ((1+rate)**-numPayments) # This is the denominator to calculate the loan payment.
            payment = round(top/bottom, 2) # This is the loan payment formula, simplified.
            loanTotal = payment * numPayments # This is the loan payment. This is the total loan payment that will be payed over time(Includes intrest).

            print(" ") # Blank line(For better Organinization)

            print("Loan Cost: ${:.2f} \nNumber of Payments: {:.0f} \nMonlthy Payment: ${:.2f} \nIntrest Rate: {:.0f}%".format(loanTotal, numPayments, payment, trueRate)) # Data Output
        elif numPayments >= 37 and numPayments <=48: # Number of payments 37-48.
            rate = .06/12 # Payment rate divided by 12.
            trueRate = (rate * 12) * 100 # True payment rate.
            top = rate * loan # This is the numerator to calculate the loan payment.
            bottom = 1 - ((1+rate)**-numPayments) # This is the denominator to calculate the loan payment.
            payment = round(top/bottom, 2) # This is the loan payment formula, simplified.
            loanTotal = payment * numPayments # This is the loan payment. This is the total loan payment that will be payed over time(Includes intrest).

            print(" ") # Blank line(For better Organinization)

            print("Loan Cost: ${:.2f} \nNumber of Payments: {:.0f} \nMonlthy Payment: ${:.2f} \nIntrest Rate: {:.0f}%".format(loanTotal, numPayments, payment, trueRate)) # Data Output
    elif loan >= 10001:  # $10001 and above
        if numPayments >= 6 and numPayments <=12: # Number of payments 6-12.
            rate = .05/12 # Payment rate divided by 12.
            trueRate = (rate * 12) * 100 # True payment rate.
            top = rate * loan # This is the numerator to calculate the loan payment.
            bottom = 1 - ((1+rate)**-numPayments) # This is the denominator to calculate the loan payment.
            payment = round(top/bottom, 2) # This is the loan payment formula, simplified.
            loanTotal = payment * numPayments # This is the loan payment. This is the total loan payment that will be payed over time(Includes intrest).

            print(" ") # Blank line(For better Organinization)

            print("Loan Cost: ${:.2f} \nNumber of Payments: {:.0f} \nMonlthy Payment: ${:.2f} \nIntrest Rate: {:.0f}%".format(loanTotal, numPayments, payment, trueRate)) # Data Output
        elif numPayments >= 13 and numPayments <=36: # Number of payments 13-36.
            rate = .06/12 # Payment rate divided by 12.
            trueRate = (rate * 12) * 100 # True payment rate.
            top = rate * loan # This is the numerator to calculate the loan payment.
            bottom = 1 - ((1+rate)**-numPayments) # This is the denominator to calculate the loan payment.
            payment = round(top/bottom, 2) # This is the loan payment formula, simplified.
            loanTotal = payment * numPayments # This is the loan payment. This is the total loan payment that will be payed over time(Includes intrest).

            print(" ") # Blank line(For better Organinization)

            print("Loan Cost: ${:.2f} \nNumber of Payments: {:.0f} \nMonlthy Payment: ${:.2f} \nIntrest Rate: {:.0f}%".format(loanTotal, numPayments, payment, trueRate)) # Data Output
        elif numPayments >= 37 and numPayments <=48: # Number of payments 37-48.
            rate = .07/12 # Payment rate divided by 12.
            trueRate = (rate * 12) * 100 # True payment rate.  # True payment rate.
            top = rate * loan # This is the numerator to calculate the loan payment.
            bottom = 1 - ((1+rate)**-numPayments) # This is the denominator to calculate the loan payment.
            payment = round(top/bottom, 2) # This is the loan payment formula, simplified.
            loanTotal = payment * numPayments # This is the loan payment. This is the total loan payment that will be payed over time(Includes intrest).

            print(" ") # Blank line(For better Organinization)

            print("Loan Cost: ${:.2f} \nNumber of Payments: {:.0f} \nMonlthy Payment: ${:.2f} \nIntrest Rate: {:.0f}%".format(loanTotal, numPayments, payment, trueRate)) # Data Output

#__________________________________________________
# def main(): goes here
def main():
    print(printName(), "- Programming Project Number 2") # DO NOT DELETE
    print(" ") # Blank line(For better Organinization)

    loanAmount = 0 # Initial start value
    paymentMonthly = 0 # Initial start value

    while True: # Main Loop

        while loanAmount < 500: # Loan Amount Loop.
            amountLoan = input("Enter amount of loan: $") # The user inputs the loan amount.

            try:
                loan_Amount = float(amountLoan) # Checks if the user inputed a number.

                if loan_Amount >= 500: # Checks if loan is above $500.
                    loanAmount = loan_Amount # Changes initial value for further processing.
                    break # This ends current loop
                elif loan_Amount < 500: # Checks if loan is less than $500
                    print("Sorry, we do not offer loans less then $500.") # Error message. The user enter a value that was out of bounds
            
            except:
                print("Invalid Input") # Error Message

        while paymentMonthly == 0: # Number of Payments Loop
            monthlyPayment = input("Enter number of payments: ") # The user inputs the number of payments.

            try:
                payment_Monthly = float(monthlyPayment) # Checks if the user inputed a number.

                if payment_Monthly >= 6 and payment_Monthly <= 48: # Checks if the number of payments are in the range of 6-48.
                    paymentMonthly = payment_Monthly # Changes initial value for further processing.
                    break # This ends current loop
                elif payment_Monthly < 6 or payment_Monthly > 48: # Checks if the number of payments are not in the range of 6-48.
                    print("Sorry, we only accept the number of monthly payments in the range of 6-48") # Error message. The user enter a value that was out of bounds
            except:
                print("Invalid Input") # Error Message

        loanPayment(loanAmount, paymentMonthly) # The call to the function to ouput what has been processed.

        print(" ") # Blank line(For better Organinization)

        checkExit = False # Boolbean to determine if the program needs to be exited. 

        while checkExit == False:
            exit = input("Would you like exit the program(Y for Yes, N for No)? ") # Asks user if she or he wants to exit the program.

            if exit == "Y": # If the user wants to exit the program.
                checkExit = True # This changes the exit check ti prepare program to exit.
                break # This ends current loop
            elif exit == "N": # If the user does not want to exit the program.
                loanAmount = 0 # Reset for loop
                paymentMonthly = 0 #  Reset for loop
                break # This ends current loop
            else:
                print("Invalid Input. Please use 'Y' for Yes and 'N' for No.") # Error Message

        if checkExit == True: # EXITS THE PROGRAM.
            break # This ends current loop

# Call to main.
main()