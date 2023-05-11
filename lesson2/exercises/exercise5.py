from rich import print

intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"
intf_fields = intf.split()

intf_name = intf_fields[0]
intf_ip_addr = intf_fields[1]
intf_line_status = intf_fields[4]
intf_line_protocol = intf_fields[5]

print()
print("-" * 80)
print(f"{intf_name=}")
print(f"{intf_ip_addr=}")
print(f"{intf_line_status=}")
print(f"{intf_line_protocol=}")
print("-" * 80)
print()

status_is_up = (intf_line_status == "up")
protocol_is_up = (intf_line_protocol == "up")
print()
print("-" * 80)
print(f"{status_is_up=}")
print(f"{protocol_is_up=}")
print("-" * 80)
print()
