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
    pass



if __name__ == "__main__":

    ssh_conn = SSHConnection(
        device_type="cisco_ios",
        host="rtr1.domain.com",
        username="admin",
        password="cisco123"
    )

    pdbr.set_trace()
