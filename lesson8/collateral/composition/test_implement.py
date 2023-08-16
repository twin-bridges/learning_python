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


class Connection:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

        self.channel = self.open()

class SSHConn(Connection):
    def __repr__(self):
        return "SSHConn Object"

    def open(self):
        """Establish SSH connection."""
        ssh_pre = paramiko.SSHClient()
        ssh_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_pre.connect(
            self.host,
            username=self.username,
            password=self.password,
            # Hard-code to simplify example
            look_for_keys=False,
            allow_agent=False,
        )
        # Paramiko SSH oddity--must save the 'ssh_pre' object or it will get
        # garbage collected
        self._pre_conn = ssh_pre
        return ssh_pre.invoke_shell()

    def write(self, data):
        self.channel.send(data.encode())

    def read(self):
        """Quite a few things missing here from a real read() implementation."""
        time.sleep(1.5)
        buffer_size = 65535
        data = self.channel.recv(buffer_size).decode()
        return data


# Dictionary to look up the class
dispatcher = {
    "xe": CiscoXE,
    "junos": Junos,
    "eos": EOS,
}

if __name__ == "__main__":
    device_type = "xe"
    ssh_conn = SSHConn(
        host="rtr1.domain.com",
        username="admin",
        password=getpass(),
    )
    # Look up the right class using the dispatcher
    PlatformND = dispatcher[device_type]
    nd = PlatformND(ssh_conn)
    print(nd.read())

    nd.write("show ip interface brief\n")
    print(nd.read())
