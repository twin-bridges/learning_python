from rich import print


# Function I do not control
def pretty_ip_printer(ip_addr1, ip_addr2):
    print()
    print("-" * 50)
    print(f"{ip_addr1=}")
    print(f"{ip_addr2=}")
    print("-" * 50)
    print()

# Function I control
def print_ips(ip_addr1, ip_addr2):
    pretty_ip_printer(ip_addr1=ip_addr1, ip_addr2=ip_addr2)

print_ips(
    ip_addr1="192.168.100.1",
    ip_addr2="192.168.100.2",
)

