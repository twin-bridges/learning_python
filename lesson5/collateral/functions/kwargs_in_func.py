from rich import print


def print_ips(**kwargs):
    print(type(kwargs))
    print(kwargs)


print_ips(ip_addr1="192.168.100.1", ip_addr2="192.168.100.2", ip_addr3="192.168.100.3")
