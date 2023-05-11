from rich import print

ip_addresses = ["10.1.1.1", "172.16.1.1", "172.31.1.1", "192.168.1.1", "10.254.1.1"]
print(f"\nInitial IP addresses:\n{ip_addresses}")

# a. Add individual addresses using append()
ip_addresses.append("192.168.100.1")
ip_addresses.append("192.168.100.2")

# b. Add a list of new addresses using extend()
ip_addresses.extend(["172.16.100.1", "172.16.100.2"])

# c. Let's concatenate as well...
ip_addresseses = ip_addresses + ["10.254.100.1", "10.254.100.2"]

# c*. Alternate form of concatenation (since we are expanding 'ip_addresses' variable)
ip_addresses += ["10.254.100.3", "10.254.100.4"]

# d. Printing
print(f"\nIP addresses after all additions:\n{ip_addresses}")

print(f"\nFirst address: {ip_addresses[0]}")
print(f"Last address: {ip_addresses[-1]}")

# e. Remove some addresses
old_first_address = ip_addresses.pop(0)
old_last_address = ip_addresses.pop()

# f. Change the new first address
ip_addresses[0] = "2.2.2.2"

# g. Print out final list of addresses.
print(f"\nFinal list of addresses:\n{ip_addresses}")
