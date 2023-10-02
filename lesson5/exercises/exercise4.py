import re

filename = "show_lldp.txt"
with open(filename) as f:
    lldp_data = f.read()


# You have to make the first .* non-greedy otherwise regex greedy behavior will jump all the way
# to the very last 'Vlan ID' in the file. After the 'Vlan ID' grab all of the remaining
# characters, but not any newlines.
section_pattern = r"^Chassis id:.*?Vlan ID:[\w ]+"
# You combine flags by using a bitwise-OR operation
results = re.findall(section_pattern, lldp_data, flags=re.DOTALL | re.M)
print()
for lldp_entry in results:
    # Initialize to null strings
    local_port, remote_system_name, remote_port = ("", "", "")
    m = re.search(r"^Port id: (\S+)", lldp_entry, flags=re.M)
    if m:
        remote_port = m.group(1)
    m = re.search(r"^Local Port id: (\S+)", lldp_entry, flags=re.M)
    if m:
        local_port = m.group(1)
    m = re.search(r"^System Name: (\S+)", lldp_entry, flags=re.M)
    if m:
        remote_system_name = m.group(1)

    print("-" * 25)
    print(f"Local port: {local_port}")
    print(f"  Remote System: {remote_system_name}")
    print(f"  Remote Port: {remote_port}")
    print("-" * 25)
    print()
print()
