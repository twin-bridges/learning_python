from rich import print

filename = "show_ip_int_brief.txt"
with open(filename) as f:
    ip_addresses = []
    interfaces = []
    for line in f:
        if " 10." in line:
            line = line.strip()
            # Create intf_name, ip_addr vars; stuff everything else into a list named fields
            intf_name, ip_addr, *fields = line.split()
            ip_addresses.append(ip_addr)
            interfaces.append(intf_name)

print()
print("-" * 60)
print(f"Interfaces: {interfaces}")
print(f"IP Addresses: {ip_addresses}")
print("-" * 60)
print()

