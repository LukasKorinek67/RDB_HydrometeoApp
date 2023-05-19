#!/bin/env python
# -*- coding: utf-8 -*-

from model.Measurement import Measurement

class AutoMeasurement(Measurement):

    def __init__(self, title, delta, manufacturer, voltage, regnum):
        """
        Konstruktor

        """
        self.title = title
        self.delta = delta
        self.manufacturer = manufacturer
        self.voltage = voltage
        self.regnum = regnum
