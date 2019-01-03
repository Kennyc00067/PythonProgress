### Kryptic Studio ###

# Local Libraries

# Libraries

# Standard Libraries
import sys
import hashlib
import itertools
import time
import os

# Function Deffinitions
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
        passwordFile = open("./Default/default.txt", "r")
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
        passwordFile = open("./User List/" + fileName, "r")
    except: 
        print("\nFile Not Found.aaa")
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
    return

def hash():
    while True:
        hashtype = input("\nHash Type(MD5, SHA256, Etc...): ")
        hashTypeList = ["sha1", "sha224", "sha256", "sha384", "sha512", "md5"]
        if hashtype.lower() in hashTypeList:
            break
        else:
            print("\nHash Type Not Found.")

    user_password = input("\n{} Hash: ".format(hashtype.upper()))

    choice = input("\nLists\n 1. Default \n 2. Custom List (../User List) ")

    if choice in ["1"]:
        dataChoiceOne(user_password, hashtype.lower())
    if choice in ["2"]:
        user_FileName = input("\nPassword List: ")
        if ".txt" not in user_FileName or ".lst" not in user_FileName:
            try:
                user_FileName += ".txt"
                dataChoiceTwo(user_FileName, user_password, hashtype.lower())
            except:
                user_FileName += ".lst"
                dataChoiceTwo(user_FileName, user_password, hashtype.lower())

    return