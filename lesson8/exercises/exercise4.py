class NetworkDevice:
    def __init__(self, host):
        self.host = host

class Router(NetworkDevice):
    def __init__(self, host, model=None):
        super().__init__(host)
        if model is not None:
            self.model = model

    def __repr__(self):
        return f"Router('{self.host}')"

    def print_model(self):
        if self.model is not None:
            print(f"Model is: {self.model}")

class Switch(NetworkDevice):
    def __repr__(self):
        return f"Switch('{self.host}')"

class AccessPoint(NetworkDevice):
    def __repr__(self):
        return f"AccessPoint('{self.host}')"



rtr1 = Router(host="sf1.domain.com", model="ASR-9904")
print()
print(rtr1.host)
print(rtr1.model)
print(rtr1)
rtr1.print_model()

sw1 = Switch(host="sf1-sw1.domain.com")
print()
print(sw1.host)
print(sw1)

ap1 = AccessPoint(host="sf1-ap1.domain.com")
print()
print(ap1.host)
print(ap1)

