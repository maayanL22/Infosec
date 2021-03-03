from struct import *
packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'


def show_details():
    pass # print sender ID (decimal), message ID (decimal), the actual message (readable english text), and its checksum (decimal)
    plist = list(packet)
    p1 = b'I th'
    print("sender id: ",unpack('<I',packet[:4])[0])
    n = unpack('<I',packet[8:12])[0]
    print("message id: ",unpack('<I',packet[16:20])[0])
    print("message: ", packet[20:-4].decode('utf-8'))
    print("checksum: ",unpack('<I',packet[-4:])[0])
    
    
show_details()
