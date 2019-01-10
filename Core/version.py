### Kryptic Studio ###

# Local Libraries

# Libraries

# Standard Libraries
import urllib.request
import curses
import webbrowser

# Function Deffinitions
def CheckVersion():
    print("Checking for update.....")
    versionTxtF = open("Core/version.txt", "r")

    versionLink = "https://raw.githubusercontent.com/KrypticStudio/KrypticHackingTools/master/Core/version.txt"

    uptodatev = urllib.request.urlopen(versionLink)
    liveversion = None
    version = None
    for line in uptodatev: # files are iterable
        liveversion = line[9:]

    liveversion = liveversion.decode()
    for line in versionTxtF:
        version = line[9:]

    if version == liveversion:
        print("Kryptic Hacking Tools is up to date!")
    elif version != liveversion:
        print("***UPDATE {} AVAILABLE*** \n - Some features may not work as intended until you update to the newest version.\n - Visit https://github.com/KrypticStudio/KrypticHackingTools to update! \n".format(liveversion))
        webbrowser.open("https://github.com/KrypticStudio/KrypticHackingTools")
