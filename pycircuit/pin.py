#!/usr/bin/env python3

import string
import random
from .bit import Bit

total_pin_count = 0

class Pin:
    PUBLIC_READ = 0b01
    PUBLIC_WRITE = 0b10

    def __init__(self, io_flags=0b00):
        self.value = Bit()
        self.io_flags = io_flags

        self.__private_key__ = ''.join(random.choice(string.ascii_letters + "0123456789+/") for _ in range(64))
        self.__private_key_lockdown__ = False

        global total_pin_count
        total_pin_count += 1

    def register(self):
        if not self.__private_key_lockdown__:
            self.__private_key_lockdown__ = True
            return self.__private_key__
        return ''.join(random.choice(string.ascii_letters + "0123456789+/") for _ in range(64))

    def write(self, value=Bit.LOW, key=None):
        if (self.io_flags & Pin.PUBLIC_WRITE) == Pin.PUBLIC_WRITE:
            self.value.set_bit(value)
        else:
            if key == self.__private_key__:
                self.value.set_bit(value)
            else:
                raise PermissionError("Pin.PUBLIC_WRITE is not active on this pin.")

    def read(self, key=None):
        if (self.io_flags & Pin.PUBLIC_READ) == Pin.PUBLIC_READ:
            return self.value.copy()
        else:
            if key == self.__private_key__:
                return self.value.copy()
            else:
                raise PermissionError("Pin.PUBLIC_READ is not active on this pin.")

    def __repr__(self):
        result = "Pin("

        if (self.io_flags & Pin.PUBLIC_READ) == Pin.PUBLIC_READ:
            result += "Pin.PUBLIC_READ"
            if (self.io_flags & Pin.PUBLIC_WRITE) == Pin.PUBLIC_WRITE:
                result += "|"

        if (self.io_flags & Pin.PUBLIC_WRITE) == Pin.PUBLIC_WRITE:
            result += "Pin.PUBLIC_WRITE"

        return result + ")"

    def __str__(self):
        result = str(self.value) + ", "

        if (self.io_flags & Pin.PUBLIC_READ) == Pin.PUBLIC_READ:
            result += "r"
        else:
            result += "-"

        if (self.io_flags & Pin.PUBLIC_WRITE) == Pin.PUBLIC_WRITE:
            result += "w"
        else:
            result += "-"

        result += "-rwd "

        result += "0" * (16-(len(hex(total_pin_count))-2))
        result += hex(total_pin_count)[2:]

        return result

