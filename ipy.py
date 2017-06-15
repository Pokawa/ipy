"""Module calculating ipv4 addresses"""
import re
import math


def equal_subnets(network, number):
    """
    Returns array of equal subnets
    network takes variable of class ipy.Network
    number is int
    """
    out = []
    extra_bits = len("{0:b}".format(number - 1))
    new_bits = network.netmask.bits + extra_bits
    new_mask = IPAddressv4("1" * new_bits + "0" * (32 - new_bits))

    for i in range(0, number):
        base_ip = network.address.raw[:network.netmask.bits]
        new_ip = "{0:b}".format(i).zfill(extra_bits)
        new_address = IPAddressv4(base_ip + new_ip + "0" * (32 - new_bits))
        out.append({"address": new_address, "netmask": new_mask})
    return out


class Network():
    """Class to combine address and netmask"""

    def __init__(self, address, netmask):
        self.address = IPAddressv4(address)
        self.netmask = IPAddressv4(netmask)

        self._net = None
        self._broadcast = None
        self._first = None
        self._last = None
        self._max = None

    @property
    def net_addr(self):
        """Returns net address"""
        if self._net is None:
            self._net = self._get_net_addr()
        return self._net

    @property
    def broadcast(self):
        """Returns broadcast address"""
        if self._broadcast is None:
            self._broadcast = self._get_broadcast()
        return self._broadcast

    @property
    def first(self):
        """Returns first address"""
        if self._first is None:
            self._first = self._get_first()
        return self._first

    @property
    def last(self):
        """Returns last address"""
        if self._last is None:
            self._last = self._get_last()
        return self._last

    @property
    def max(self):
        """Returns max number of hosts"""
        if self._max is None:
            self._max = self._get_max()
        return self._max

    def _get_net_addr(self):
        """Returning net address"""
        out = ""
        for i, j in zip(self.address.raw, self.netmask.raw):
            if j == "1":
                out += i
            else:
                out += "0"
        return IPAddressv4(out)

    def _get_broadcast(self):
        """Returning broadcast address"""
        out = ""
        for i, j in zip(self.address.raw, self.netmask.raw):
            if j == "1":
                out += i
            else:
                out += "1"
        return IPAddressv4(out)

    def _get_first(self):
        """Returning first usable address"""
        return IPAddressv4("{0:b}".format(
            int(self.net_addr.raw, 2) + 1).zfill(32))

    def _get_last(self):
        """Returning last usable address"""
        return IPAddressv4("{0:b}".format(
            int(self.broadcast.raw, 2) - 1).zfill(32))

    def _get_max(self):
        """Returning number of max usable addresses"""
        return int(math.pow(2, 32 - self.netmask.bits) - 2)


class IPAddressv4:
    """IPv4 class"""

    def __init__(self, address):
        """
        Pass an ip address

        addres can be either in decimal, binary, raw or number of bits

        For example:
        192.168.0.1
        11110000.10101010.00000000.00001100
        11110000101010100000000000001100
        24
        """
        regex_dec = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
        regex_bin = r"^[0-1]{8}\.[0-1]{8}\.[0-1]{8}\.[0-1]{8}$"
        regex_raw = r"^[0-1]{32}$"

        self.binary = None
        self.raw = None
        self.decimal = None
        self.bits = None

        # if given address is decmal format
        if re.match(regex_dec, address):
            self.decimal = address
            self._decimal_to_raw()
            self._raw_to_binary()

        # if given address is binary format
        elif re.match(regex_bin, address):
            self.binary = address
            self._binary_to_decimal()
            self._decimal_to_raw()

        # if given address is raw format
        elif re.match(regex_raw, address):
            self.raw = address
            self.bits = address.count("1")
            self._raw_to_binary()
            self._binary_to_decimal()

        # if given address is number of bits
        elif len(address) < 3 and 0 <= int(address) <= 32:
            self.bits = int(address)
            self._bits_to_raw()
            self._raw_to_binary()
            self._binary_to_decimal()

        else:
            raise Exception(
                "Invalid address: {}, out of bound or bad formating".format(address))

    def _binary_to_decimal(self):
        """Calculating decimal address from binary representation"""
        self.decimal = ""
        for i in self.binary.split("."):
            self.decimal += str(int(i, 2)) + "."
        self.decimal = self.decimal[:-1]

    def _decimal_to_raw(self):
        """Calculating raw address from decimal representation"""
        self.raw = ""
        for i in self.decimal.split("."):
            self.raw += "{0:08b}".format(int(i))

    def _bits_to_raw(self):
        """Calculating raw address from bits representation"""
        self.raw = "1" * self.bits + "0" * (32 - self.bits)

    def _raw_to_binary(self):
        """Calculating binary address from raw representation"""
        self.binary = self.raw[0:8] + "." + self.raw[8:16] + \
            "." + self.raw[16:24] + "." + self.raw[24:32]
