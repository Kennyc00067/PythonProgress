from scapy.all import *
import socket
import sys
from random import randint
import contextlib
from socket import gethostbyname
from Core import arps_spoof

def ipSpoof():
    try:
        arps_spoof.get_clients_OnLan()
        targetIP = input("Target IP: ")
        destinationIP = input("Destination IP: ")
        data = input("Packet Data(Optional): ")
        pktNum = int(input("Number of Packets to send: "))
        count = 0
        while count <= pktNum - 1:
            count += 1
            ip_layer = IP(src=targetIP, dst=destinationIP)
            tcp_layer = TCP()
            pkt = ip_layer/tcp_layer/data
            with open(os.devnull, "w") as f, contextlib.redirect_stdout(f):
                try:
                    send(pkt)
                except:
                    return
        print("\n{} packets sent from spoofed ip {} to ip {}.".format(count, targetIP, destinationIP))
    except:
        print("Packet Failed to send.")
    return