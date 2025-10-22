import ipaddress


net = ipaddress.ip_network("10.151.0.0/16")

for ip in net:
    print(ip)
print(f"Network address: {net.network_address}")
print(f"Broadcast address: {net.broadcast_address}")
print(f"Number of addresses: {net.num_addresses}")
