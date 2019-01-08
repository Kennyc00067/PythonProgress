### Kryptic Studio ###

# Local Libraries

# Libraries
from scapy.all import *
# Standard Libraries
import socket
import sys
from random import randint
from socket import gethostbyname

# Function Deffinitions
def get_ip_address():
    url = input("Enter URL: ")
    hostIP = gethostbyname(url)
    print("URL: {} \t IP: {}".format(url, hostIP))