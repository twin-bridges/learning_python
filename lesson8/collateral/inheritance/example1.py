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
