from rich import print


def print_ips(ip_addr1, ip_addr2):
    print(f"{ip_addr1=}")
    print(f"{ip_addr2=}")


ips = {
    "ip_addr1": "192.168.100.1",
    "ip_addr2": "192.168.100.2",
}

print_ips(**ips)
