import ipaddress

try:
    net = ipaddress.ip_address(input("Print you address"))
    print(net)
except ValueError:
    print("Invalid value")
