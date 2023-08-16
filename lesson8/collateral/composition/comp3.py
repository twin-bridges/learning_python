import paramiko
from getpass import getpass
import time


class NetworkDevice:
    def __init__(
        self,
        connection,
    ):
        self.connection = connection

    def write(self, data):
        self.connection.write(data)

    def read(self):
        return self.connection.read()


class CiscoXE(NetworkDevice):
    """Cisco XE Specific Behaviors"""

    pass


class Junos(NetworkDevice):
    """Junos Specific Behaviors"""

    pass


class EOS(NetworkDevice):
    """EOS Specific Behaviors"""

    pass


dispatcher = {
    "xe": CiscoXE,
    "junos": Junos,
    "eos": EOS,
}


class SSHConn:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

        self.channel = self.open()

    def open(self):
        """Establish SSH connection."""
        pass

    def write(self, data):
        self.channel.send(data.encode())

    def read(self):
        """Quite a few things missing here from a real read() implementation."""
        time.sleep(1.5)
        buffer_size = 65535
        data = self.channel.recv(buffer_size).decode()
        return data


class TelnetConn:
    def __init__(self, device_type, host, username, password):
        pass

    def open(self):
        """Establish Telnet connection."""
        pass

    def write(self, data):
        pass

    def read(self):
        pass


if __name__ == "__main__":
    import pdbr

    pdbr.set_trace()
    ssh_conn = SSHConn(
        device_type="cisco_ios",
        host="rtr1.domain.com",
        username="admin",
        password=getpass(),
    )
    nd = NetworkDevice(ssh_conn)
    print(nd.read())
