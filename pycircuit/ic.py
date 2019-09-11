#!/usr/bin/env python3

from .bit import Bit
from .pin import Pin

# Base Integrated Circuit class
class IC:
    def __init__(self, inputs, outputs):
        self.__generate__(inputs, outputs)

    def __generate__(self, num_in, num_out):
        self.inputs = []
        self.__input_keys__ = []
        self.outputs = []
        self.__output_keys__ = []

        for i in range(num_in):
            self.inputs.append(Pin(Pin.PUBLIC_WRITE))
            self.__input_keys__.append(self.inputs[i].register())
            self.inputs[i].write(Bit.UNDEFINED)

        for i in range(num_out):
            self.outputs.append(Pin(Pin.PUBLIC_READ))
            self.__output_keys__.append(self.outputs[i].register())
            self.outputs[i].write(Bit.UNDEFINED, self.__output_keys__[i])

    def connect(self, outpinidx, ic, inppinidx):
        self.outputs[outpinidx].connect(ic.inputs[inppinidx])

    def disconnect(self, outpinidx, ic, inppinidx):
        self.outputs[outpinidx].disconnect(ic.inputs[inppinidx])

    def input(self, idx, inp):
        self.inputs[idx].write(inp)

    def run(self):
        for i in range(len(self.outputs)):
            self.__calculate_pin__(i)

    def __calculate_pin__(self, idx):
        self.outputs[idx].write((~self.outputs[idx].read()).value, self.__output_keys__[idx])

    def read(self, idx):
        return self.outputs[idx].read()
