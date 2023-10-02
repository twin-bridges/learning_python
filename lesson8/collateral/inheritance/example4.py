import pdbr


class ConnectionClass(object):
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password


class TelnetConnection(ConnectionClass):
    def print_host(self):
        print(f"Telnet Connection to: {self.host}")


class SSHConnection(ConnectionClass):
    def print_host(self):
        print(f"SSH Connection to: {self.host}")


if __name__ == "__main__":
    ssh_conn = SSHConnection(
        device_type="cisco_ios",
        host="rtr1.domain.com",
        username="admin",
        password="cisco123",
    )
    ssh_conn.print_host()

    pdbr.set_trace()
