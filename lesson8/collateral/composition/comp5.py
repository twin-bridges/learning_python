import paramiko
from getpass import getpass
import time
import pdbr


class NetworkDevice:
    def __init__(
        self,
        connection,
    ):
        self.connection = connection

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name} Object: {self.connection.host}"

    def write(self, data):
        self.connection.write(data)

    def read(self):
        return self.connection.read()


class CiscoXEND(NetworkDevice):
    pass


class JunosND(NetworkDevice):
    pass


class EOSND(NetworkDevice):
    pass


dispatcher = {
    "xe": CiscoXEND,
    "junos": JunosND,
    "eos": EOSND,
}


class SSHConn:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

        self.channel = self.open()
        pass
        pass

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
        pdbr.set_trace()
        self._pre_conn = ssh_pre
        return ssh_pre.invoke_shell()

    def write(self, data):
        self.channel.send(data.encode())

    def read(self):
        # In practice, I would not put this sleep here.
        time.sleep(1.5)
        buffer_size = 65535
        data = self.channel.recv(buffer_size).decode()
        return data


if __name__ == "__main__":
    ssh_conn = SSHConn(
        device_type="cisco_ios",
        host="rtr1.domain.com",
        username="pyclass",
        password=getpass(),
    )
    nd = NetworkDevice(ssh_conn)

    pdbr.set_trace()
