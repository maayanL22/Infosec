from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment


def show_username_password():
    bind_layers(TCP, HTTP, dport=8000)
    bind_layers(TCP, HTTP, sport=8000)
    packets = rdpcap(recording_path)
    pass # print Username and Password
    for packet in packets:
        print(raw(packet))

show_username_password()
