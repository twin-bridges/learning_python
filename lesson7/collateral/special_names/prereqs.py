

class NetDevice:
    def __init__(self, device_type, host, username, password, port=22):
        # Name mangling
        self.__device_type_ = device_type
        self.host = host
        # private attrs (somewhat private)
        self._username = username
        self._password = password
        self.port = port

    def __str__(self):
        return f"NetDevice Object {self.host}:{self.port}"


nd = NetDevice(
    host="test1.domain.com",
    device_type="cisco_ios",
    username="admin",
    password="cisco123"
)
import pdbr; pdbr.set_trace()

