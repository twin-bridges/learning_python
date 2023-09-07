class Channel:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def connect(self):
        pass

    def read(self):
        print("Fictional read")

    def write(self, data):
        print(f"Fictional write --> {data}")


class SSHChannel(Channel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transport = "ssh"

    def connect(self):
        print(f"Fictional {self.transport} connection to {self.host}")


class TelnetChannel(Channel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transport = "telnet"

    def connect(self):
        print(f"Fictional {self.transport} connection to {self.host}")


class Router:
    def __init__(self, host, device_type, username, password, transport="ssh"):
        self.host = host
        self.device_type = device_type

        if transport == "ssh":
            self.channel = SSHChannel(host, username, password)
            self.channel.connect()
        elif transport == "telnet":
            self.channel = TelnetChannel(host, username, password)
            self.channel.connect()

    def read(self):
        self.channel.read()

    def write(self, data):
        self.channel.write(data)


rtr1 = Router(
    host="rtr1.domain.com",
    device_type="arista_eos",
    username="arista",
    password="arista123",
)
rtr1.write("whatever")
rtr1.read()
