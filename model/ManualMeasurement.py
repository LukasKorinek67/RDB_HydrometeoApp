#!/bin/env python
# -*- coding: utf-8 -*-


from model.Measurement import Measurement

class ManualMeasurement(Measurement):

    def __init__(self, person):
        """
        Konstruktor

        """
        self.person = person
