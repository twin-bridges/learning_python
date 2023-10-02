import pdbr


class ConnectionClass(object):
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password


class TelnetConnection(ConnectionClass):
    pass


class SSHConnection(ConnectionClass):
    def __init__(self, device_type, host, username, password, key_file=None):
        if key_file is not None:
            self.key_file = key_file
        return super().__init__(device_type, host, username, password)

    def __repr__(self):
        orig = super().__repr__()
        return f"{orig} --> Hello"


if __name__ == "__main__":
    ssh_conn = SSHConnection(
        device_type="cisco_ios",
        host="rtr1.domain.com",
        username="admin",
        password="cisco123",
        key_file="~/.ssh/my_ssh_key",
    )

    pdbr.set_trace()
