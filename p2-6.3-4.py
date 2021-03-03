from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

def show_source_destination_ip_address():
    packets = rdpcap(recording_path)
    pass # print the source and destination ip addresses
    i = 1
    for packet in packets:
        print("source ip address of packet number: ", i, "is: ", packet[IP].src)
        print("destination ip address of packet number: ", i, "is: ", packet[IP].dst)
        print("")
        i += 1

show_source_destination_ip_address()
