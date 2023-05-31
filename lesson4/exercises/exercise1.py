from rich import print

filename = "show_ip_int_brief.txt"
with open(filename) as f:
    data = f.read()

interface_ips = {}
for line in data.splitlines():
    # Stuff the remaining entries into the list named "_"
    intf, ip_addr, *_ = line.split()

    # Skip any line that doesn't contain an IP address.
    if ip_addr in ["IP-Address", "unassigned"]:
        continue

    interface_ips[intf] = ip_addr

print()
print(interface_ips)
print()
