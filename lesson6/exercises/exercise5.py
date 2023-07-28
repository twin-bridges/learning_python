from telnetlib import Telnet
import time
import re
from getpass import getpass


def read(telnet_conn, sleep=1.5):
    time.sleep(sleep)
    data = telnet_conn.read_very_eager().decode()
    return data


def write(telnet_conn, data):
    byte_data = data.encode()
    telnet_conn.write(byte_data)


def login(telnet_conn, username, password):
    debug = False
    prompt_terminator = r"#"

    data = read(telnet_conn)
    output = data
    if re.search(r"sername", data):
        write(telnet_conn, f"{username}\n")
        data = read(telnet_conn)
        output += data
    if re.search(r"ssword", data):
        write(telnet_conn, f"{password}\n")
        data = read(telnet_conn)
        output += data

    if debug:
        print(output)

    if re.search(prompt_terminator, data):
        return True
    else:
        return False


def show_cmd(telnet_conn, cmd="show ip interface brief"):
    write(telnet_conn, f"{cmd}\n")
    return read(telnet_conn)


if __name__ == "__main__":
    host = "rtr1.domain.com"
    username = "pyclass"
    password = getpass("Enter router password: ")

    # Create telnet connection
    tn = Telnet(host)

    login_status = login(telnet_conn=tn, username=username, password=password)
    output = show_cmd(tn)
    print(f"\n{output}\n")

    output = show_cmd(tn, cmd="show ip arp")
    print(f"\n{output}\n")
