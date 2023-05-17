#!/bin/env python
# -*- coding: utf-8 -*-


"""
RDB - ConfigFileHandler
"""

import sys
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
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_generator_folder = os.path.join(dir_path, "RDBFileGenerator")
        file = os.path.join(file_generator_folder, file_name)
        self.file_path = file

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






