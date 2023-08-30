from rich import print

"""
arista2#show ip ospf neighbor
Neighbor ID     Instance VRF      Pri State                  Dead Time   Address         Interface
10.220.88.34    42       default  0   FULL/DROTHER           00:00:30    10.220.88.34    Vlan1
10.220.88.35    42       default  0   FULL/DROTHER           00:00:31    10.220.88.35    Vlan1
10.220.88.33    42       default  0   FULL/DROTHER           00:00:38    10.220.88.33    Vlan1
10.220.88.32    42       default  0   FULL/DROTHER           00:00:30    10.220.88.32    Vlan1
10.220.88.31    42       default  0   FULL/DROTHER           00:00:35    10.220.88.31    Vlan1
10.220.88.30    42       default  0   FULL/DROTHER           00:00:29    10.220.88.30    Vlan1
10.220.88.28    42       default  250 FULL/BDR               00:00:36    10.220.88.28    Vlan1


arista2#show ip ospf database

            OSPF Router with ID(10.220.88.29) (Instance ID 42) (VRF default)


                 Router Link States (Area 0.0.0.0)

Link ID         ADV Router      Age         Seq#         Checksum Link count
10.220.88.28    10.220.88.28    582         0x80000008   0xa410   1
10.220.88.30    10.220.88.30    307         0x80000006   0xa40c   1
10.220.88.32    10.220.88.32    297         0x80000008   0x9c0c   1
10.220.88.34    10.220.88.34    292         0x80000006   0x9c08   1
10.220.88.31    10.220.88.31    305         0x80000005   0xa40a   1
10.220.88.33    10.220.88.33    292         0x80000006   0x9e09   1
10.220.88.29    10.220.88.29    581         0x80000007   0xa40e   1
10.220.88.35    10.220.88.35    287         0x80000006   0x9a07   1
"""


class OSPFRouter:
    def __init__(self, instance_id, area, router_id, is_dr=False, is_bdr=False):
        self.instance_id = instance_id
        self.area = area
        self.router_id = router_id
        self.is_dr = is_dr
        self.is_bdr = is_bdr
        self._neighbors = []

    def __str__(self):
        return f"""
OSPFRouter:
    Instance: {self.instance_id}
    Area: {self.area}
    Router ID: {self.router_id}
    DR: {self.is_dr}
    BDR: {self.is_bdr}

    Neighbors: {self._neighbors}

"""

    def add_neighbor(self, neighbor_rid):
        self._neighbors.append(neighbor_rid)


arista2 = OSPFRouter(instance_id=42, area=0, router_id="10.220.88.29", is_dr=True)
arista2.add_neighbor("10.220.88.28")
arista2.add_neighbor("10.220.88.30")
arista2.add_neighbor("10.220.88.31")
arista2.add_neighbor("10.220.88.32")
arista2.add_neighbor("10.220.88.33")
arista2.add_neighbor("10.220.88.34")
arista2.add_neighbor("10.220.88.35")
print(arista2._neighbors)
print(arista2)
