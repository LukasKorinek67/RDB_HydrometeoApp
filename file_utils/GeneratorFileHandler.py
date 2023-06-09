#!/bin/env python
# -*- coding: utf-8 -*-


"""
RDB - GeneratorFileHandler
"""

import os
import subprocess


class GeneratorFileHandler():
    """
    Třída GeneratorFileHandler
    """

    def __init__(self):
        """
        Konstruktor
        """
        file_name = "RDBFileGenerator.exe"
        self.file_path = self._get_file_path(file_name)
    
    def _get_file_path(self, file_name):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(current_dir)
        file_path = os.path.join(parent_dir, file_name)
        return file_path

    def generate(self):
        subprocess.call(self.file_path) 

