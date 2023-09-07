from dataclasses import dataclass
from typing import List


@dataclass
class RouterFacts:
    hostname: str
    vendor: str
    network_os: str
    model: str
    os_version: str
    interfaces: List[str]
    uptime_sec: int
    serial_number: str


xr_rtr = RouterFacts(
    hostname="la-rtr1",
    vendor="cisco",
    network_os="iosxr",
    model="8201-SYS",
    os_version="7.0.12",
    interfaces=[
        "HundredGigE0/0/0/24",
        "HundredGigE0/0/0/25",
        "HundredGigE0/0/0/26",
        "HundredGigE0/0/0/27",
        "HundredGigE0/0/0/28",
        "HundredGigE0/0/0/29",
        "HundredGigE0/0/0/30",
        "HundredGigE0/0/0/31",
        "HundredGigE0/0/0/32",
        "HundredGigE0/0/0/33",
        "HundredGigE0/0/0/34",
        "HundredGigE0/0/0/35",
        "MgmtEth0/RP0/CPU0/0",
    ],
    uptime_sec=93073,
    serial_number="FOC2291AVYB",
)

print(xr_rtr)
