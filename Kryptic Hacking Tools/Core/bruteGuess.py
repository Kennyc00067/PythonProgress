### Kryptic Studio ###

# Local Libraries

# Libraries

# Standard Libraries
import time
import sys
import hashlib
import itertools
import time
import os

# Function Deffinitions
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

def bruteGuess():
    password = input("Please enter a password: ")
    # Allowed characters
    stringType = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"
    tries, timeAmount = tryPassword(password, stringType)
    print("The password %s was cracked in %s tries and %s seconds!" % (password, tries, timeAmount))