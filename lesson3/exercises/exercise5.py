from rich import print

filename = "junos_show_arp.txt"
with open(filename) as f:
    for line in f:
        # Skip header line and trailer lines
        if "MAC Address" in line or "Total entries" in line:
            continue
        mac_addr, ip_addr, _, _, _ = line.split()
        print(f"{mac_addr=}")
        print(f"{ip_addr=}")

        alt_mac_format = mac_addr.replace(":", "-")
        print(f"{alt_mac_format=}")
