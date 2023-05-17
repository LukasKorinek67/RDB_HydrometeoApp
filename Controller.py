#!/bin/env python
# -*- coding: utf-8 -*-


"""
STI - Controller
"""

from datetime import date
# from RequestHandler import RequestHandler
# from DailyCasesData import DailyCasesData

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, "database")))
from DatabaseCity import DatabaseCity
from DatabaseMeasurement import DatabaseMeasurement


class Controller():
    """
    Třída Controller
    """

    def __init__(self):
        """
        Konstruktor
        """
        self.databaseMeasurement = DatabaseMeasurement()


    def updateData(self):
    	"""
        - doplní měření v době, kdy aplikace neběžela
        """
    	pass




