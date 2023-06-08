import re
from rich import print

filename = "show_lldp.txt"
with open(filename) as f:
    lldp_data = f.read()

# Tricky...you have to make the first .* non-greedy otherwise
# it will just jump all the way to the last 'Vlan ID'
# After the 'Vlan ID' you want to grab all of the remaning characters
# but not any newlines.
section_pattern = r"^Chassis id:.*?Vlan ID:[\w ]+"
# You combine flags by using a bitwise-OR operation
results = re.findall(section_pattern, lldp_data, flags=re.DOTALL|re.M)
for lldp_entry in results:
    m = re.search(r"^Port id: (\S+)", lldp_entry, flags=re.M)
    if m:
        remote_port = m.group(1)
    m = re.search(r"^Local Port id: (\S+)", lldp_entry, flags=re.M)
    if m:
        local_port = m.group(1)
    print((local_port, remote_port))

