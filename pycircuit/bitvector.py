#!/usr/bin/env python3

from .bit import Bit

class BitVector:
    def __init__(self, vector=[], length=0):
        if len(vector) != 0:
            length = len(vector)
        elif length != 0:
            vector = []
            for i in range(length):
                vector.append(Bit.LOW)

        self.length = length

        for i in range(length):
            vector[i] = Bit(vector[i])

        self.vector = vector

    def set_vector(self, vector=[]):
        if len(vector) != self.length:
            raise Exception("cannot assign values to BitVector without same length.")

        for i in range(self.length):
            vector[i] = Bit(vector[i])

        self.vector = vector

    def set(self, idx):
        self.vector[idx].set()

    def reset(self, idx):
        self.vector[idx].reset()

    def __and__(self, other):
        if not isinstance(other, BitVector):
            raise TypeError("unsupported operand type(s) for &: 'BitVector'" +
                            " and '" +
                            type(other).__name__ + "'")
        if other.length != self.length:
            raise Exception("second operand to operation '&' does not have length " + self.length)

        result = []
        for i in range(self.length):
            result.append((self.vector[i] & other.vector[i]).value)

        return BitVector(result, length=self.length)

    def __or__(self, other):
        if not isinstance(other, BitVector):
            raise TypeError("unsupported operand type(s) for |: 'BitVector'" +
                            " and '" +
                            type(other).__name__ + "'")
        if other.length != self.length:
            raise Exception("second operand to operation '|' does not have length " + self.length)

        result = []
        for i in range(self.length):
            result.append((self.vector[i] | other.vector[i]).value)

        return BitVector(result, length=self.length)

    def __xor__(self, other):
        if not isinstance(other, BitVector):
            raise TypeError("unsupported operand type(s) for ^: 'BitVector'" +
                            " and '" +
                            type(other).__name__ + "'")
        if other.length != self.length:
            raise Exception("second operand to operation '^' does not have length " + self.length)

        result = []
        for i in range(self.length):
            result.append((self.vector[i] ^ other.vector[i]).value)

        return BitVector(result, length=self.length)

    def __invert__(self):
        result = []
        for i in range(self.length):
            result.append((~self.vector[i]).value)
        return BitVector(result, length=self.length)

    def __lshift__(self, other):
        if not isinstance(other, int):
            raise TypeError("unsupported operand type(s) for <<: 'BitVector'" +
                            " and '" +
                            type(other).__name__ + "'")
        if other < 0:
            raise ValueError("cannot leftshift by a negative number.")

        result = self.vector.copy()

        for i in range(other):
            result.pop(0)

        for i in range(other):
            result.append(Bit(Bit.LOW))

        for i in range(self.length):
            result[i] = result[i].value

        return BitVector(result, length=self.length)

    def __rshift__(self, other):
        if not isinstance(other, int):
            raise TypeError("unsupported operand type(s) for >>: 'BitVector'" +
                            " and '" +
                            type(other).__name__ + "'")
        if other < 0:
            raise ValueError("cannot rightshift by a negative number.")

        result = self.vector.copy()

        for i in range(other):
            result.pop()

        for i in range(other):
            result.insert(0, Bit(Bit.LOW))

        for i in range(self.length):
            result[i] = result[i].value

        return BitVector(result, length=self.length)

    def __str__(self):
        result = ""

        for i in range(self.length):
            if self.vector[i].value in [Bit.UNDEFINED, Bit.SHORT]:
                return "[INVALID BIT %s]" % (str(self.vector[i]))
            result += str(self.vector[i].value)

        return result

    def __repr__(self):
        result = "BitVector(["

        for i in range(self.length):
            result += str(self.vector[i])
            result += ", "

        result = result[:len(result)-2]
        result += "], length="
        result += str(self.length)
        result += ")"

        return result
