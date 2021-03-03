from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

def show_domain_ip_address():
    packets = rdpcap(recording_path)
    pass # print resolved domain and ip address
    for packet in packets:
        print(packet[DNS].summary())
        print("lilili")
        for x in range(packet[DNS].ancount):
            print (packet[DNSRR][x].rdata)
        print("lululu")
        print("")

show_domain_ip_address()
