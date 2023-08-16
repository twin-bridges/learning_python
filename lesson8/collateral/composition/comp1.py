import pdbr


class NetworkDevice:
    def __init__(
        self,
        device_type,
        host,
        username,
        password,
        conn_type="ssh"
    ):
        self.device_type = device_type
        self.host = host

        if conn_type == "ssh":
            self.connection = SSHConn(device_type, host, username, password)
        elif conn_type == "telnet":
            self.connection = TelnetConn(device_type, host, username, password)

    def __repr__(self):
        return "NetworkDevice Object"


class TelnetConn:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

    def __repr__(self):
        return "TelnetConn Object"

class SSHConn:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

    def __repr__(self):
        return "SSHConn Object"


if __name__ == "__main__":
    nd = NetworkDevice(
        device_type="cisco_ios",
        host="rtr1.domain.com",
        username="admin",
        password="cisco123",
        conn_type="ssh",
    )

    pdbr.set_trace()
