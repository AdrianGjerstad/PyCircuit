#!/usr/bin/env python3

class Signal:
    HIGH = 1
    LOW = 0
    SHORT = -1
    UNDEFINED = -2

    def __init__(self, value=UNDEFINED):
        if value not in [Signal.HIGH, Signal.LOW, Signal.SHORT, Signal.UNDEFINED]:
            raise ValueError("Unkown signal value given")

        self.value = value

    def __repr__(self):
        if self.value == Signal.HIGH:
            return "Signal.HIGH"
        elif self.value == Signal.LOW:
            return "Signal.LOW"
        elif self.value == Signal.SHORT:
            return "Signal.SHORT"
        elif self.value == Signal.UNDEFINED:
            return "Signal.UNDEFINED"

        return "[DATA UNKNOWN]"
