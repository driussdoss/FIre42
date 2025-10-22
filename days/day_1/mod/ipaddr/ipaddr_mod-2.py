import ipaddress

net = ipaddress.ip_network("192.168.88.0/24")
ip = ipaddress.ip_address("192.168.88.243")

print(ip in net)
