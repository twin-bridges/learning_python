import re
from rich import print

filename = "show_ip_bgp_neighbors.txt"
with open(filename) as f:
    bgp_neighbors = f.read()

pattern = (
    r"^BGP neighbor is (?P<bgp_neighbor>[\d\.]+),\s+remote AS (?P<remote_as>\d+),.*$"
)
match = re.search(pattern, bgp_neighbors, flags=re.M)
if match:
    bgp_neighbor = match.group("bgp_neighbor")
    remote_as = match.group("remote_as")

pattern = (
    r"^\s+BGP version (?P<bgp_version>\d+), remote router ID (?P<remote_rid>\S+).*$"
)
match = re.search(pattern, bgp_neighbors, flags=re.M)
if match:
    bgp_version = match.group("bgp_version")
    remote_router_id = match.group("remote_rid")

pattern = r"^\s+BGP state = (?P<bgp_state>\S+),"
match = re.search(pattern, bgp_neighbors, flags=re.M)
if match:
    bgp_state = match.group("bgp_state")

print()
print(f"{bgp_neighbor=}")
print(f"{remote_as=}")
print(f"{bgp_version=}")
print(f"{remote_router_id=}")
print(f"{bgp_state=}")
print()
