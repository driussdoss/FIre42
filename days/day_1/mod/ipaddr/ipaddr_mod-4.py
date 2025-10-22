import ipaddress

net = ipaddress.ip_network("192.168.100.0/24")

print(net.network_address)
print(net.broadcast_address)
print(net.num_addresses)
