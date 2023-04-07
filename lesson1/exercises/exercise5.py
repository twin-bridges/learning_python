ip_addr = "10.12.17.1"
mac_addr = "0024.c4e9.48ae"

output = "\n" + "String concatenation" + "\n"
output += ip_addr + " --> " + mac_addr
print(output)

output = f"\nf-strings\n{ip_addr} --> {mac_addr}"
print(output)

output = "\nformat() method\n{} --> {}".format(ip_addr, mac_addr)
print(output)
