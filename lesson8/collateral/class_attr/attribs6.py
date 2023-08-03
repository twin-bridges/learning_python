from rich import print

class NetDevice:
    addresses = {
        "sf1": "365 Main Street, San Francisco, CA 94105",
        "sf2": "200 Paul Avenue, San Francisco, CA 94124",
        "la1": "600 West 7th Street, Los Angeles, CA 90017",
    }

    def __init__(
        self,
        device_type,
        host,
        username,
        password,
        data_center,
    ):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

        self.data_center = data_center
        self.address = NetDevice.addresses[data_center]


rtr1 = NetDevice(
    device_type="juniper_junos",
    host="rtr1.domain.com",
    username="admin",
    password="jnpr123",
    data_center="la1",
)

print()
print(f"RTR1 DC: {rtr1.data_center}")
print(f"RTR1 Address: {rtr1.address}")
print()
