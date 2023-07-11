from telnetlib import Telnet
import time


def read(telnet_conn, sleep=1.5):
    time.sleep(sleep)
    data = tn.read_very_eager().decode()
    return data


if __name__ == "__main__":
    host = "cisco1.lasthop.io"
    username = "pyclass"

    # Create telnet connection
    tn = Telnet(host)

    d = read(tn)
    print(d)
