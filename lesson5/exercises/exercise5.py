import re
from rich import print

filename = "aruba_cx_show_ipv6_intf.txt"
with open(filename) as f:
    ipv6_intf = f.read()

m = re.search(
    r"^Interface (?P<intf_name>\S+) is (?P<intf_state>\S+)$", ipv6_intf, flags=re.M
)
if m:
    intf_name = m.group("intf_name")
    intf_state = m.group("intf_state")
    print(f"{intf_name=}")
    print(f"{intf_state=}")

m = re.search(r"^Admin state is (?P<admin_state>\S+)", ipv6_intf, flags=re.M)
if m:
    admin_state = m.group("admin_state")
    print(f"{admin_state=}")

ipv6_pattern = r"[\w:/]+"
pattern = rf"^IPv6 address:\n\s+(?P<ipv6_addr>{ipv6_pattern})"
m = re.search(pattern, ipv6_intf, flags=re.M)
if m:
    ipv6_addr = m.group("ipv6_addr")
    print(f"{ipv6_addr=}")
