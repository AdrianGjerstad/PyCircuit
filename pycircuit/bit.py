#!/usr/bin/env python3

class Bit:
    HIGH = 1
    LOW = 0
    SHORT = -1
    UNDEFINED = -2

    def __init__(self, value=UNDEFINED):
        if value not in [Bit.HIGH, Bit.LOW, Bit.SHORT, Bit.UNDEFINED]:
            raise ValueError("Unknown Bit value given")

        self.value = value

    def __and__(self, other):
        if not isinstance(other, Bit):
            raise TypeError("unsupported operand type(s) for &: 'Bit' and '"
                            +
                            type(other).__name__ + "'")

        if other.value in [Bit.SHORT, Bit.UNDEFINED]:
            return Bit(other.value)
        if self.value in [Bit.SHORT, Bit.UNDEFINED]:
            return Bit(self.value)

        return Bit(self.value & other.value)

    def __or__(self, other):
        if not isinstance(other, Bit):
            raise TypeError("unsupported operand type(s) for |: 'Bit' and '"
                            +
                            type(other).__name__ + "'")

        if other.value in [Bit.SHORT, Bit.UNDEFINED]:
            return Bit(other.value)
        if self.value in [Bit.SHORT, Bit.UNDEFINED]:
            return Bit(self.value)

        return Bit(self.value | other.value)

    def __xor__(self, other):
        if not isinstance(other, Bit):
            raise TypeError("unsupported operand type(s) for ^: 'Bit' and '"
                            +
                            type(other).__name__ + "'")

        if other.value in [Bit.SHORT, Bit.UNDEFINED]:
            return Bit(other.value)
        if self.value in [Bit.SHORT, Bit.UNDEFINED]:
            return Bit(self.value)

        return Bit(self.value ^ other.value)

    def __invert__(self):
        if self.value in [Bit.SHORT, Bit.UNDEFINED]:
            return Bit(self.value)

        if self.value == Bit.LOW:
            return Bit(Bit.HIGH)
        return Bit(Bit.LOW)

    def __str__(self):
        if self.value == Bit.HIGH:
            return "Bit.HIGH"
        elif self.value == Bit.LOW:
            return "Bit.LOW"
        elif self.value == Bit.SHORT:
            return "Bit.SHORT"
        elif self.value == Bit.UNDEFINED:
            return "Bit.UNDEFINED"

        return "[STRING UNKNOWN]"

    def __repr__(self):
        result = ""
        if self.value == Bit.HIGH:
            result = "Bit.HIGH"
        elif self.value == Bit.LOW:
            result = "Bit.LOW"
        elif self.value == Bit.SHORT:
            result = "Bit.SHORT"
        elif self.value == Bit.UNDEFINED:
            result = "Bit.UNDEFINED"
        else:
            return "[DATA UNKNOWN]"

        return "Bit(" + result + ")"
