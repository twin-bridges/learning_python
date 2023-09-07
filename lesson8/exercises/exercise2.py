class Router:
    count = 0
    all_hosts = []

    def __init__(self, host):
        self.host = host
        Router.count += 1
        Router.all_hosts.append(host)


rtr1 = Router("la1.domain.com")
rtr2 = Router("la2.domain.com")
rtr3 = Router("sf1.domain.com")
rtr4 = Router("sf2.domain.com")

print()
print(f"{Router.count=}")
print(f"{Router.all_hosts=}")
print()
