class NetworkDevice:
    def __init__(self, host, platform, username, password):
        self.host = host
        self.platform = platform
        self.username = username
        self._password = password

    def __str__(self):
        return f"NetworkDevice: {self.host} ({self.platform})"

    @property
    def password(self):
        return "*" * len(self._password)

    @password.setter
    def password(self, new_passwd):
        if new_passwd == self._password:
            raise ValueError("New password not allowed")


if __name__ == "__main__":
    rtr1 = NetworkDevice(
        host="host1.domain.com", platform="cisco_xe", username="admin", password="cisco"
    )
    rtr2 = NetworkDevice(
        host="host2.domain.com",
        platform="juniper_junos",
        username="admin",
        password="juniper123",
    )
    print(rtr1)
    print(rtr2)

    print("\nSetting new password")
    try:
        rtr2.password = "juniper123"
    except ValueError:
        pass

    rtr2.password = "new123"

    print(f"\nrtr2 password: {rtr2.password}\n")
