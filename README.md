# ipy
module to parse and manipulate IPv4 addresses

## Examples
IPAddressv4 constructor supports and identifies:
decimal
```
IPAddressv4("192.168.0.1")
```
binary
```
IPAddressv4("10101010.11110000.00000000.00011000")
```
raw
```
IPAddressv4("10101010111100000000000000011000")
```
bits
```
IPAddressv4("24")
```

IPAddressv4 calculates and store:
```
foo = IPAddressv4("192.168.0.1")
foo.decimal
foo.binary
foo.raw
foo.bits
```

Network class:
```
foo = Network("192.168.0.1", "24")
foo.net_addr
foo.broadcast
foo.first
foo.last
foo.max
```
all addresses are IPAddressv4 objects and supports diffrent representations fe.
`foo.broadcast.decimal`

equal_subnets function:
```
foo = Network("192.168.0.1", "24")
foo2 = equal_subnets(foo, 4)
foo2[address].decimal
foo2[netmask].decimal
```

