import time
import re
import os
from telnetlib import Telnet
from getpass import getpass


def read(telnet_conn, sleep=1.5):
    DEBUG = True
    time.sleep(1.5)
    data = telnet_conn.read_very_eager().decode()
    if DEBUG:
        print(data)

    return data


def write(telnet_conn, data):
    byte_data = data.encode()
    return telnet_conn.write(byte_data)


def login(telnet_conn, username, password, check=r"#"):
    data = read(telnet_conn)
    if re.search(r"sername", data):
        write(telnet_conn, f"{username}\n")
        data = read(telnet_conn)
    if re.search(r"ssword", data):
        write(telnet_conn, f"{password}\n")
        data = read(telnet_conn)

    if re.search(check, data):
        print("Hooray!!!")
        return True
    else:
        return False


if __name__ == "__main__":
    host = "cisco1.domain.com"
    username = "pyclass"
    if os.getenv("TN_PASSWORD"):
        password = os.getenv("TN_PASSWORD")
    else:
        password = getpass()

    # Create telnet connection
    tn = Telnet(host)
    login(tn, username, password)
