#!/usr/bin/env python3

from ..bit import Bit
from ..pin import Pin
from ..ic import IC

class OrIC(IC):
    def __init__(self):
        super().__init__(2, 1)

    def __calculate_pin__(self, idx):
        if idx == 0: # Calculate Value of OutPin0
            self.outputs[idx].write((self.inputs[0].read(self.__input_keys__[0]) | self.inputs[1].read(self.__input_keys__[1])).value, self.__output_keys__[idx])
        else:
            raise IndexError("OrIC: No OutPin" + str(idx) + " exists.")
