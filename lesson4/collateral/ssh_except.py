from netmiko import ConnectHandler
from netmiko import NetmikoAuthenticationException

try:
    conn = ConnectHandler(
        host="cisco3.domain.com",
        device_type="cisco_xe",
        username="admin",
        password="bogus",
    )
    print(conn.find_prompt())
except NetmikoAuthenticationException:
    print("Authentication failure gracefully handled")

print("Outside of try/except block")
