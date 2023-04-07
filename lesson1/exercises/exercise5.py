from rich import print

arp_entry = 'Internet  10.12.17.1            42   0024.c4e9.48ae  ARPA   GigabitEthernet0/00'
show_arp = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.12.17.1            42   0024.c4e9.48ae  ARPA   GigabitEthernet0/00
Internet  10.12.17.21          135   1c6a.7aaf.576c  ARPA   GigabitEthernet0/00
Internet  10.12.17.22            -   a093.5141.b780  ARPA   GigabitEthernet0/00
Internet  10.12.17.23          191   502f.a8b1.6900  ARPA   GigabitEthernet0/00
Internet  10.12.17.28           16   00aa.fc05.b513  ARPA   GigabitEthernet0/00
Internet  10.12.17.31           97   00ac.fc59.97f2  ARPA   GigabitEthernet0/00
Internet  10.12.17.37          161   0001.00ff.0001  ARPA   GigabitEthernet0/00
Internet  10.12.17.38          216   0002.00ff.0001  ARPA   GigabitEthernet0/00
"""

output = show_arp.strip().splitlines()
print(output)
