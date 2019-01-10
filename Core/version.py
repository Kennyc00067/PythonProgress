### Kryptic Studio ###

# Local Libraries

# Libraries

# Standard Libraries
import urllib2

# Function Deffinitions
def CheckVersion():
    print("Checking for update.....")
    versionTxtF = open("version.txt", "r")

    versionLink = "https://github.com/KrypticStudio/KrypticHackingTools/blob/master/Core/version.txt"

    data = urllib2.urlopen(versionLink)

    for line in data: # files are iterable
        print (line)