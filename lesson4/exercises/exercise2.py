from rich import print

filename = "show_ip_int_brief.txt"
with open(filename) as f:
    data = f.read()

intf_brief = {}
for line in data.splitlines():
    # Remaining entries for line_status, line_protocol might contain 2 or 3 fields.
    intf, ip_addr, _, _, *fields = line.split()

    # Skip the header line.
    if ip_addr in ["IP-Address"]:
        continue

    if len(fields) == 2:
        line_status, line_protocol = fields
    elif len(fields) == 3:
        line_status = f"{fields[0]}_{fields[1]}"
        line_protocol = fields[2]
    else:
        msg = "Number of fields isn't what I expected: ellifino"
        raise ValueError(msg)

    intf_brief[intf] = {
        "ip_addr": ip_addr,
        "line_status": line_status,
        "line_protocol": line_protocol,
    }
    # print(f"{intf=}")
    # print(f"{ip_addr=}")
    # print(f"{line_status=}")
    # print(f"{line_protocol=}")

print(intf_brief)
