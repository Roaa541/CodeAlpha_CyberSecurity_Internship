
from scapy.all import sniff, IP
def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"[*] Packet: {src_ip} is sending to {dst_ip}")

print("--- Network Sniffer Started ---")
sniff(prn=process_packet, store=0)
