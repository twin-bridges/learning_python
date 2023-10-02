import os


def print_my_ip():
    # There are various ways to obtain your IP address (Linux/MacOS specific)
    inet_data = os.popen("ifconfig -a | grep 'inet '").read()

    for line in inet_data.splitlines():
        if "127.0.0" in line:
            continue
        inet, ip_addr, *_ = line.split()
        print(f"My IP address is: {ip_addr}")
