import pdbr
from dataclasses import dataclass


@dataclass
class NetDevice:
    device_type: str
    host: str
    username: str
    password: str


class NetDevice:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password


rtr1 = NetDevice(
    device_type="juniper_junos",
    host="rtr1.domain.com",
    username="admin",
    password="jnpr123",
)
pdbr.set_trace()
