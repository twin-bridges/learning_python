from rich import print


def print_ips(ip_addr1, ip_addr2):
    print(f"{ip_addr1=}")
    print(f"{ip_addr2=}")


sf_addresses = ["10.1.1.1", "10.1.1.2"]
print_ips(*sf_addresses)


