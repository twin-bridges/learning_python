import pdbr


class NetworkDevice:
    def __init__(
        self,
        connection,
    ):
        self.device_type = connection.device_type
        self.connection = connection

    def __repr__(self):
        return f"NetworkDevice Object: {self.device_type}/{self.connection.host}"


class SSHConn:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

    def __repr__(self):
        return "SSHConn Object"


if __name__ == "__main__":
    ssh_conn = SSHConn(
        device_type="cisco_ios",
        host="rtr1.domain.com",
        username="admin",
        password="cisco123",
    )
    nd = NetworkDevice(ssh_conn)

    pdbr.set_trace()
