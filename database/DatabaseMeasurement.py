#!/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient


MONGO_URI = "mongodb+srv://username01:passwordRDB01@measurements.rxjnsaj.mongodb.net/?retryWrites=true&w=majority"
#username01
#passwordRDB01

class DatabaseMeasurement():

    def __init__(self):
        """
        Constructor of class DatabaseMeasurement. Creates local database ??name?? with

        Returns
        -------
        None.

        """
        self.client = MongoClient(MONGO_URI)
        self.database = self.client["measurements"]
        self.collection = self.database["measurements"]
        self.collection.create_index([("values.1", 1)])


    def add_measurements(self, city, measurements):
        """
        Přidání dat
        """
        try:
            query = {
                "city": city
            }
            result = self.collection.find_one(query)

            if result == None:
                self.add_city(city)

            records = {
                "$push": {
                    "values": { 
                        "$each": measurements
                    }
                }
            }
            self.collection.update_one(query, records)
            #print("Přidány všechny měření - celkově " + str(len(measurements)) + " měření")
        except Exception as e:
            msg = "Chyba při přidávání dat do databáze."
            print(msg)

    def add_city(self, city):
        record = {
            "city": city,
            "values": []
        }
        self.collection.insert_one(record)
        #print("Město " + city + " přidáno do databáze!")


    def get_last_record(self, city):
        try:
            query = {
                "city": city
            }
            result = self.collection.find_one(query)

            if result is not None and "values" in result:
                last_value = result["values"][-1][0]
                #print("Poslední hodnota města", city, "je:", last_value)
                return int(last_value)
            else:
                print("Město", city, "nenalezeno nebo neobsahuje žádná data.")
                raise ValueError("Nenalezeno nebo neobsahuje žádná data!")
        except Exception as e:
            msg = "Chyba při získávání dat z databáze."
            print(msg)
            return 0

    def get_all_cities(self):
        cities = self.collection.distinct("city")
        return cities


    def get_max_min_temp(self, city):
        pipeline = [
            { "$match": { "city": city } },
            { "$unwind": "$values" },
            { "$sort": { "values.1": -1 } }
        ]
        result = self.collection.aggregate(pipeline)
        result = list(result)
        max_temperature = result[0]["values"][1]
        min_temperature = result[-1]["values"][1]
        return {
            "max": max_temperature,
            "min": min_temperature
		}

    def get_max_temp(self, city):
        pipeline = [
            { "$match": { "city": city } },
            { "$unwind": "$values" },
            { "$sort": { "values.1": -1 } }
        ]

        result = self.collection.aggregate(pipeline)
        result = list(result)
        max_temperature = result[0]["values"][1]

        return max_temperature
    
    def get_min_temp(self, city):
        pipeline = [
            { "$match": { "city": city } },
            { "$unwind": "$values" },
            { "$sort": { "values.1": 1 } }
        ]

        result = self.collection.aggregate(pipeline)
        result = list(result)
        min_temperature = result[0]["values"][1]

        return min_temperature

    def get_same_temperatures(self, first_city, second_city):
        pipeline = [
            {
                '$match': {
                    'city': {
                        '$in': [
                            first_city, second_city
                        ]
                    }
                }
            }, {
                '$unwind': '$values'
            }, {
                '$replaceWith': {
                    'city': '$city', 
                    'temperature': {
                        '$arrayElemAt': [
                            '$values', 1
                        ]
                    }
                }
            }, {
                '$group': {
                    '_id': '$temperature', 
                    'cities': {
                        '$addToSet': '$city'
                    }
                }
            }, {
                '$addFields': {
                    'numCities': {
                        '$size': '$cities'
                    }
                }
            }, {
                '$match': {
                    'numCities': {
                        '$gt': 1
                    }
                }
            }, {
                '$replaceWith': {
                    'temperature': '$_id', 
                    'cities': '$cities', 
                    'numCities': '$numCities'
                }
            }, {
                '$sort': {
                    'temperature': 1
                }
            }
        ]
        result = self.collection.aggregate(pipeline)
        result = list(result)
        temperatures = [obj['temperature'] for obj in result]
        return temperatures
