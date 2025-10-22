import ipaddress

addr = ipaddress.ip_address("192.168.88.1")
lol = ipaddress.ip_address(addr)
print(lol)

ipaddress.IPv4Address("192.168.88.88")


ipaddress.version(lol)
