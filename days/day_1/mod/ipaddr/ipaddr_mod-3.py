import ipaddress

net = ipaddress.ip_network("10.151.225.0/26")
ip = ipaddress.ip_address("10.151.225.32")


print(ip in net)
