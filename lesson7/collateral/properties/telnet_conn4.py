from telnetlib import Telnet
import time
import re
from socket import gethostbyname
from getpass import getpass


class TelnetConn:
    def __init__(self, host, username, password):
        self._host = host
        self.username = username
        self.password = password

        # Create telnet connection
        self._open()

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        if value != self._host:
            ip_addr = gethostbyname(value)  # noqa
            self._host = value
            del self.telnet_conn
            self._open()

    def _open(self):
        """Create telnet connection."""
        self.telnet_conn = Telnet(self._host)
        self.login()

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
    username = "pyclass"
    password = getpass("Enter router password: ")

    tc = TelnetConn(host="rtr2.domain.com", username=username, password=password)
    tc.write("\n")
    data = tc.read()
    print(data)

    import pdbr

    pdbr.set_trace()
