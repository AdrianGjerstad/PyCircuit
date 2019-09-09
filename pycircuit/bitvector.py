#!/usr/bin/env python3

import bit

class BitVector:
    def __init__(self, vector=[], length=0):
        if len(vector) != 0:
            length = len(vector)
        elif length != 0:
            vector = []
            for i in range(length):
                vector.append(bit.Signal.LOW)

        self.length = length

        for i in range(length):
            vector[i] = bit.Signal(vector[i])

        self.vector = vector
