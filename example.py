import ipy

NETWORK = ipy.Network("10.32.64.3", "8")
SUBNETS = 2

print("IP address")
print("decimal: {}".format(NETWORK.address.decimal))
print("binary:  {}".format(NETWORK.address.binary))
print("")

print("Netmask")
print("decimal: {}".format(NETWORK.netmask.decimal))
print("binary:  {}".format(NETWORK.netmask.binary))
print("")

print("Net address")
print("decimal: {}".format(NETWORK.net_addr.decimal))
print("binary:  {}".format(NETWORK.net_addr.binary))
print("")

print("Broadcast")
print("decimal: {}".format(NETWORK.broadcast.decimal))
print("binary:  {}".format(NETWORK.broadcast.binary))
print("")

print("First host")
print("decimal: {}".format(NETWORK.first.decimal))
print("binary:  {}".format(NETWORK.first.binary))
print("")

print("Last host")
print("decimal: {}".format(NETWORK.last.decimal))
print("binary:  {}".format(NETWORK.last.binary))
print("")

print("Max:     {}".format(NETWORK.max))
print("")

for i, val in enumerate(ipy.equal_subnets(NETWORK, SUBNETS)):
    print("Subnet number {}.".format(i + 1))
    print("Net address")
    print("decimal: {}".format(val["address"].decimal))
    print("binary:  {}".format(val["address"].binary))
    print("Netmask")
    print("decimal: {}".format(val["netmask"].decimal))
    print("binary:  {}".format(val["netmask"].binary))
    print("")
