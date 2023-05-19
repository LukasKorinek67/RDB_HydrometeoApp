#!/bin/env python
# -*- coding: utf-8 -*-


"""
RDB - ConfigFileHandler
"""

import os


class ConfigFileHandler():
    """
    Třída ConfigFileHandler
    """

    def __init__(self):
        """
        Konstruktor
        """
        file_name = "input.txt"
        self.file_path = self._get_file_path(file_name)

    
    def _get_file_path(self, file_name):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(current_dir)
        file_path = os.path.join(parent_dir, file_name)
        return file_path
    
    def read_config(self):
        try:
            with open(self.file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Config file '{self.file_path}' not found.")
            return None

    def write_config(self, city, long_from, long_to):
        try:
            with open(self.file_path, "w") as file:
                file.write(city)
                file.write(",")
                file.write(str(long_from))
                file.write(",")
                file.write(str(long_to))
            #print("Config file updated successfully.")
        except IOError:
            print(f"Error writing to config file '{self.file_path}'.")
