from rich import print
import emoji

# Life is better with emojis
celebration = emoji.emojize(":confetti_ball: ")
party = emoji.emojize(":party_popper: ")
balloons = emoji.emojize(":balloon: ")

base_addr = "192.168.254."
last_octet = 0

prefix_length = int(input("\nEnter a subnet prefix length(25-30): "))
subnet_size_bin = 32 - prefix_length
subnet_size = 2**subnet_size_bin
number_of_subnets = 256 // subnet_size
lost_hosts = 2  # network_number and broadcast
number_of_hosts = subnet_size - lost_hosts
first_address = f"{base_addr}1"
last_address = f"{base_addr}{number_of_hosts}"
first_subnet = f"{base_addr}0"
second_subnet = f"{base_addr}{subnet_size}"

banner_chars = "-" * 80
banner = f"[deep_sky_blue4]{banner_chars}[/deep_sky_blue4]"
print()
print(banner)
print(f"Number of hosts per subnet: [deep_sky_blue4]{number_of_hosts}[/deep_sky_blue4]")

print("\nSubnets:")
print(f" Number of subnets: [deep_sky_blue4]{number_of_subnets}[/deep_sky_blue4]")
for subnet_num in range(number_of_subnets):
    subnet = f"{base_addr}{subnet_num * subnet_size}"
    print(f" Subnet Number: [deep_sky_blue4]{subnet}[/deep_sky_blue4]")

print(f"\nFirst subnet: {first_subnet}")
print(f" First Address: [deep_sky_blue4]{first_address}[/deep_sky_blue4]")
print(f" Last Address: [deep_sky_blue4]{last_address}[/deep_sky_blue4]")
print(banner)

print(f"\n{celebration}{party}{balloons}\n")
