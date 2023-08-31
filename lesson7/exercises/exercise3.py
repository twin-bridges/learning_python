from rich import print


class OSPFRouter:
    def __init__(self, instance_id, area, router_id, is_dr=False, is_bdr=False):
        self.instance_id = instance_id
        self.area = area
        self.router_id = router_id
        self.is_dr = is_dr
        self.is_bdr = is_bdr
        self._neighbors = set()

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
        self._neighbors = self._neighbors | {neighbor_rid}

    def remove_neighbor(self, neighbor_rid):
        self._neighbors = self._neighbors - {neighbor_rid}


arista2 = OSPFRouter(instance_id=42, area=0, router_id="10.220.88.29", is_dr=True)
arista2.add_neighbor("10.220.88.28")
arista2.add_neighbor("10.220.88.30")
arista2.add_neighbor("10.220.88.31")
arista2.add_neighbor("10.220.88.32")
arista2.add_neighbor("10.220.88.33")
arista2.add_neighbor("10.220.88.34")
arista2.add_neighbor("10.220.88.35")

# Add a fictional neighbor
arista2.add_neighbor("10.220.88.36")
# Remove the fictional neighor as a test
arista2.remove_neighbor("10.220.88.36")

print(arista2)
