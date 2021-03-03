from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment


def show_source_destination_ports():
    packets = rdpcap(recording_path)
    pass # print destination port of third packet and source port of fourth packet
    i = 1
    for packet in packets:
        print("source port of packet number:",i,"is:",packet[TCP].sport)
        print("destination port of packet number:",i,"is:",packet[TCP].dport)
        print("")
        i += 1

show_source_destination_ports()
