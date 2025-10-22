import ipaddress

net = ipaddress.ip_network("192.168.88.1/32")

for ip in net:
    print(ip)
print(f"Your broadcast address is: {net.broadcast_address}")
