from telnetlib import Telnet
import time
import re
from getpass import getpass


class TelnetConn:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

        # Create telnet connection
        self.telnet_conn = Telnet(self.host)

    def write(self, data):
        byte_data = data.encode()
        self.telnet_conn.write(byte_data)

    def read(self, sleep=1.5):
        time.sleep(sleep)
        data = self.telnet_conn.read_very_eager().decode()
        return data

    def login(self):
        debug = False
        prompt_terminator = r"#"

        data = self.read()
        output = data
        if re.search(r"sername", data):
            self.write(self.username + "\n")
            data = self.read()
            output += data
        if re.search(r"ssword", data):
            self.write(self.password + "\n")
            data = self.read()
            output += data

        if debug:
            print(output)

        if re.search(prompt_terminator, data):
            return True
        else:
            return False


if __name__ == "__main__":
    host1 = "cisco1.lasthop.io"
    host2 = "cisco2.lasthop.io"
    username = "pyclass"
    password = getpass("Enter router password: ")

    tc1 = TelnetConn(
        host=host1,
        username=username,
        password=password
    )

    tc2 = TelnetConn(
        host=host2,
        username=username,
        password=password
    )

    tc1.login()
    tc2.login()

