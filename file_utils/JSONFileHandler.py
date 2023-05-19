#!/bin/env python
# -*- coding: utf-8 -*-


"""
RDB - JSONFileHandler
"""

import os
import json


class JSONFileHandler():
    """
    Třída JSONFileHandler
    """

    def __init__(self, city_name):
        """
        Konstruktor
        """
        file_name = city_name + ".json"
        self.file_path = self._get_file_path(file_name)
    
    def _get_file_path(self, file_name):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(current_dir)
        file_path = os.path.join(parent_dir, file_name)
        return file_path

    def read_file(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)

        return data
