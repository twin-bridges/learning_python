from rich import print


# Function I do not control
def pretty_ip_printer(ip_addr1, ip_addr2, ip_addr3=None, divider="-"):
    print()
    print(divider * 50)
    print(f"{ip_addr1=}")
    print(f"{ip_addr2=}")
    if ip_addr3 is not None:
        print(f"{ip_addr3=}")
    print(divider * 50)
    print()

# Function I control
def print_ips(ip_addr1, ip_addr2, **kwargs):
    pretty_ip_printer(ip_addr1=ip_addr1, ip_addr2=ip_addr2, **kwargs)

print_ips(
    ip_addr1="192.168.100.1",
    ip_addr2="192.168.100.2",
    divider="@",
)

