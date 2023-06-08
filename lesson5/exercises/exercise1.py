import re
from rich import print

filename = "show_version.txt"
with open(filename) as f:
    show_version = f.read()

match = re.search(r"^cisco ([-\w]*) .*bytes of memory\.$", show_version, flags=re.M)
if match:
    model = match.group(1)

match = re.search(r"^Processor board ID (\w+)$", show_version, flags=re.M)
if match:
    serial_number = match.group(1)

print()
print("#" * 25)
print(f"{model=}")
print(f"{serial_number=}")
print("#" * 25)
