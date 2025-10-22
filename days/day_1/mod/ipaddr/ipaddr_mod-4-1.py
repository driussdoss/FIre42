import ipaddress

net = ipaddress.ip_network("192.168.88.0/24")


print(f"Your network is: {net}")

print(f"Your network address is: {net.network_address}")
print(f"Your broadcast address is: {net.broadcast_address}")
print(f"Your number of addresses is:{net.num_addresses}")
