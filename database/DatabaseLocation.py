#!/bin/env python
# -*- coding: utf-8 -*-

#import sqlite3
# from datetime import date
# import sys
# import os

# dir_path = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))
# from DailyCasesData import DailyCasesData


class DatabaseLocation():

    def __init__(self):
        """
        Constructor of class DatabaseCR. Creates local database covid19 with
        covid19_CR. And string_info about waiting for data.

        Returns
        -------
        None.

        """
        # self.myclient = MongoClient(
        #     "mongodb+srv://Test1:Heslo123@cluster0.0gobs.mongodb.net/covid19?retryWrites=true&w=majority")
        # self.database = self.myclient["covid19"]
        # self.db_cr = self.database["covid19_CR"]
        # self.string_info = "Čeká se na data."
        

        #self.conn = sqlite3.connect('weather_data.db')
        #self.c = c = conn.cursor()
    
    def get_all_cities():
        return ["Liberec", "Praha", "Plzeň", "Ostrava", "Most"]
        #pass