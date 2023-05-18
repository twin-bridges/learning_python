from rich import print

filename = "show_ip_int_brief.txt"
with open(filename) as f:
    for line in f:
        if " 10.220" in line:
            fields = line.split()
            intf_name = fields[0]
            ip_addr = fields[1]

print()
print("-" * 60)
print(f"Interface: {intf_name}")
print(f"IP Addr: {ip_addr}")
print("-" * 60)
print()
