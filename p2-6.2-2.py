from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment


def show_mac_address():
    packets = rdpcap(recording_path)
    pass # print mac address
    i = 1
    for packet in packets:
        print("source mac for packet number:",i, "is:",packet.src)
        i += 1

show_mac_address()
