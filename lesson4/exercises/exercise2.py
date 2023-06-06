from rich import print

filename = "show_ip_int_brief.txt"
with open(filename) as f:
    data = f.read()

# Initialize larger dictionary outside the main for-loop.
intf_brief = {}
for line in data.splitlines():
    # *fields will be a list and might contain 2 or 3 entries
    # line_protocol and line_status will be in the fields list.
    intf, ip_addr, _, _, *fields = line.split()

    # Skip the header line.
    if ip_addr in ["IP-Address"]:
        continue

    # Handle the 2 or 3 entries case for fields (due to "administratively down")
    # containing a space.
    if len(fields) == 2:
        line_status, line_protocol = fields
    elif len(fields) == 3:
        line_status = f"{fields[0]}_{fields[1]}"
        line_protocol = fields[2]
    else:
        msg = "Unexpected value for number of fields in parsing 'show ip int brief'"
        raise ValueError(msg)

    # Construct inner dictionary and add it to larger dictionary.
    intf_brief[intf] = {
        "ip_addr": ip_addr,
        "line_status": line_status,
        "line_protocol": line_protocol,
    }

print(intf_brief)
