import pdbr
from dataclasses import dataclass


@dataclass
class NetDevice:
    device_type: str
    host: str
    username: str
    password: str


rtr1 = NetDevice(
    device_type="juniper_junos",
    host="rtr1.domain.com",
    username="admin",
    password="jnpr123",
)
pdbr.set_trace()
