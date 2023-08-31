from rich import print


class Interface:
    def __init__(
        self,
        intf_name,
        intf_mode="access",
        access_vlan=None,
        speed="1Gbps",
        duplex="full",
    ):
        self.intf_name = intf_name

        if intf_mode in ("access", "trunk"):
            self.intf_mode = intf_mode
        else:
            raise ValueError(f"Invalid value for intf_mode: {intf_mode}")

        if intf_mode == "access":
            if not isinstance(access_vlan, int):
                raise ValueError("Access VLAN must be an integer")
            self.access_vlan = access_vlan
        elif intf_mode == "trunk":
            self.access_vlan = None

        self.speed = speed
        self.duplex = duplex

    def __str__(self):
        if self.intf_mode == "trunk":
            return (
                f"Interface: {self.intf_name} ({self.speed}/{self.duplex}, "
                f"Mode: {self.intf_mode})"
            )
        else:
            return (
                f"Interface: {self.intf_name} ({self.speed}/{self.duplex}, Mode: {self.intf_mode}, "
                f"Vlan: {self.access_vlan})"
            )


if __name__ == "__main__":
    print()
    print("-" * 50)
    eth1 = Interface(intf_name="Et1", intf_mode="access", access_vlan=1)
    eth2 = Interface(intf_name="Et2", intf_mode="access", access_vlan=2)
    eth3 = Interface(intf_name="Et3", intf_mode="access", access_vlan=3)
    eth4 = Interface(intf_name="Et4", intf_mode="access", access_vlan=4)
    eth5 = Interface(intf_name="Et5", intf_mode="access", access_vlan=5)
    eth6 = Interface(intf_name="Et6", intf_mode="access", access_vlan=6)
    eth7 = Interface(intf_name="Et7", intf_mode="trunk")

    for intf in (eth1, eth2, eth3, eth4, eth5, eth6, eth7):
        print(intf)
    print("-" * 50)
    print()
