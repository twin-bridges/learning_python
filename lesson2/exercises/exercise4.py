from rich import print

filename = "show_arp.txt"
with open(filename) as f:
    show_arp = f.readlines()

# a - Print out python data type
print(f"\nData type of 'show_arp' variable: {type(show_arp)}")

# b - Print out the length of show arp
print(f"\nLength of list: {len(show_arp)}")

# c - Header line
header = show_arp[0]
print(f"\nHeader line:\n{header}")

# d - Tabular data (first and last line)
print(f"First line of tabular show_arp:\n{show_arp[1]}")
print(f"Last line of tabular show_arp:\n{show_arp[-1]}")

# e - Fields of the header line
fields = header.split()
print(f"Header fields: {fields}")

# f - Python data type of fields variable
print(f"\nData type of 'fields' variable: {type(fields)}")

# g - Number of fields
print(f"\nNumber of fields: {len(fields)}")

# h - First field, last field
print(f"\nFirst field: {fields[0]}")
print(f"\nLast field: {fields[-1]}")

# i - Fixing the fields
del fields[3]
new_fields = f"{fields[3]}_{fields[4]}"
fields[3] = new_fields
del fields[4]
print(f"\nFields after corrections:\n{fields}\n")
