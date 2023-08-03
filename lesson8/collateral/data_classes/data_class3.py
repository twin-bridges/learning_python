import pdbr
from dataclasses import dataclass, field
from typing import List


def default_list():
    return []


@dataclass
class NetDevice:
    device_type: str
    host: str
    username: str
    password: str
    interface_ips: List[str] = field(default_factory=default_list)


rtr1 = NetDevice(
    device_type="cisco_ios",
    host="rtr1.domain.com",
    username="admin",
    password="csco123",
)
rtr1.interface_ips.append("192.168.1.1")

rtr2 = NetDevice(
    device_type="cisco_ios",
    host="rtr2.domain.com",
    username="admin",
    password="csco123",
)
pdbr.set_trace()
