from rich import print

filename = "junos_show_arp.txt"
print("\nJunos ARP table:")
print("-" * 50)
with open(filename) as f:
    for line in f:
        # Skip header line and trailer lines
        if "MAC Address" in line or "Total entries" in line:
            continue
        mac_addr, ip_addr, _, _, _ = line.split()
        alt_mac_addr = mac_addr.replace(":", "-")
        print(f"{ip_addr:14} --> {alt_mac_addr}")

print("-" * 50)
print()
