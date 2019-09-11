#!/usr/bin/env python3

from ..bit import Bit
from ..pin import Pin
from ..ic import IC
from .andic import AndIC
from .notic import NotIC

class NandIC(IC):
    def __init__(self):
        super().__init__(2, 1)

        self.andgate = AndIC()
        self.notgate = NotIC()

    def run()
