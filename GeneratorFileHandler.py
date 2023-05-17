#!/bin/env python
# -*- coding: utf-8 -*-


"""
RDB - GeneratorFileHandler
"""

import sys
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
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_generator_folder = os.path.join(dir_path, "RDBFileGenerator")
        file = os.path.join(file_generator_folder, file_name)
        self.file_path = file

    def generate(self):
        process = subprocess.Popen(self.file_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print("Proces byl úspěšně dokončen.")
        else:
            print("Proces skončil s chybou.")

        # Výpis výstupu
        print("Výstup:")
        print(stdout.decode())

        # Výpis chybového výstupu
        print("Chybový výstup:")
        print(stderr.decode())






