import pdbr
from dataclasses import dataclass


@dataclass
class NetDevice:
    host: str
    username: str
    password: str
    device_type: str = "cisco_ios"

rtr1 = NetDevice(
    host="rtr1.domain.com",
    username="admin",
    password="csco123",
)
pdbr.set_trace()
