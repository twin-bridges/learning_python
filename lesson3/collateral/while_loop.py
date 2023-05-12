base_addr = "172.31"
third_octet = 0
while third_octet < 10:
    last_octet = 2
    while last_octet < 255:
        ip_addr = f"{base_addr}.{third_octet}.{last_octet}"
        print(f"IP Address: {ip_addr}")
        last_octet += 1
    third_octet += 1
