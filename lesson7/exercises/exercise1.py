class NetworkDevice:
    def __init__(self, host, platform, username, password):
        self.host = host
        self.platform = platform
        self.username = username
        self.password = password

    def __str__(self):
        return f"NetworkDevice: {self.host} ({self.platform})"


rtr1 = NetworkDevice(
    host="host1.domain.com", platform="cisco_xe", username="admin", password="cisco"
)
rtr2 = NetworkDevice(
    host="host2.domain.com", platform="juniper_junos", username="admin", password="juniper123"
)

print(rtr1)
print(rtr2)
