import socket

def sniff_packets():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    s.bind(("0.0.0.0", 0))

    while True:
        packet, addr = s.recvfrom(65535)
        print(f"Packet from {addr}: {packet}")

print("[INFO] Sniffing started...")
sniff_packets(
