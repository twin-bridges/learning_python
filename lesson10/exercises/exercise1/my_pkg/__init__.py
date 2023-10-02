import os

def print_my_ip():
    inet_data = os.popen("ifconfig -a | grep 'inet '").read()

    for line in inet_data.splitlines():
        if "127.0.0" in line:
            continue
        inet, ip_addr, *_ = line.split()
        print(f"My IP address is: {ip_addr}")


print_my_ip()
