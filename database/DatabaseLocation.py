#!/bin/env python
# -*- coding: utf-8 -*-

#import sqlite3
# from datetime import date
# import sys
# import os


class DatabaseLocation():

    def __init__(self):
        """
        Constructor of class DatabaseCR. Creates local database covid19 with
        covid19_CR. And string_info about waiting for data.

        Returns
        -------
        None.

        """
        pass
        #self.conn = sqlite3.connect('weather_data.db')
        #self.c = c = conn.cursor()
    
    def get_all_cities():
        return ["Liberec", "Praha", "Plzeň", "Ostrava", "Most"]
        #pass

    # Chat GPT schéma:
    # Tabulka "Location":
    # id: PRIMARY KEY
    # place: VARCHAR(255)

    # Tabulka "Contact":
    # id: PRIMARY KEY
    # name: VARCHAR(255)
    # surname: VARCHAR(255)
    # email: VARCHAR(255)
    # deptitle: VARCHAR(255)
    # depphone: VARCHAR(255)
    # depaddress_street: VARCHAR(255)
    # depaddress_number: VARCHAR(255)
    # depaddress_city: VARCHAR(255)

    # Tabulka "Measurement":
    # id: PRIMARY KEY
    # location_id: FOREIGN KEY na Location(id)
    # contact_id: FOREIGN KEY na Contact(id)
    # timestamp: INTEGER
    # temperature: FLOAT
    # pressure: FLOAT
    # humidity: INTEGER
