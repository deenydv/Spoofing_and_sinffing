import os

def change_mac(interface, new_mac):
    os.system(f"ifconfig {interface} down")
    os.system(f"ifconfig {interface} hw ether {new_mac}")
    os.system(f"ifconfig {interface} up")

print("[INFO] Changing MAC address...")
change_mac("eth0", "00:11:22:33:44:55"
