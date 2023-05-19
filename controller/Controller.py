#!/bin/env python
# -*- coding: utf-8 -*-


"""
RDB - Controller
"""

from file_utils.ConfigFileHandler import ConfigFileHandler
from file_utils.GeneratorFileHandler import GeneratorFileHandler
from file_utils.JSONFileHandler import JSONFileHandler
from utils.DateTimeConverter import DateTimeConverter
from database.DatabaseLocation import DatabaseLocation
from database.DatabaseMeasurement import DatabaseMeasurement

# pak smazat:
import platform
from file_utils.TestJSONGenerator import TestJSONGenerator


class Controller():
	"""
	Třída Controller
	"""

	def __init__(self):
		"""
		Konstruktor
		"""
		self.databaseLocation = DatabaseLocation()
		self.databaseMeasurement = DatabaseMeasurement()
		self.configFileHandler = ConfigFileHandler()
		self.generatorFileHandler = GeneratorFileHandler()

	def _add_records(self, city, long_from, long_to):
		self.configFileHandler.write_config(city, long_from, long_to)

		system = platform.system()
		if (system == "Darwin" or system == "Linux"):
			# Pouze pro TESTOVÁNÍ u mě na Macu:
			testGenerator = TestJSONGenerator(city)
			testGenerator.generate()
		elif system == "Windows":
			# Tohle je varianta, která se bude používat normálně
			self.generatorFileHandler.generate()
		else:
			testGenerator = TestJSONGenerator(city)
			testGenerator.generate()

		jsonFile = JSONFileHandler(city)
		data = jsonFile.read_file()
		
		# dál tady nějak uložit ty data do databáze
		# v proměnný data je python dictionary


	def update_data(self):
		"""
		- doplní měření v době, kdy aplikace neběžela
		"""
		
		# long_now = DateTimeConverter.timestamp_now()
		# all_cities = self.databaseLocation.get_all_cities()
		# for city in all_cities:
		# 	last_record = self.databaseMeasurement.get_last_record(city)
		# 	self._add_records(city, last_record, long_now)
		pass

	def same_temperatures(self):
		"""
		Popis
		"""
		return "... Probíhá nalezení všech stejných teplot pro dvě místa ...\n"

	def max_min_temperature(self):
		"""
		Popis
		"""
		# Tady vrátit něco v takovýmhle formátu - dictionary
		return {
			"Liberec" : {
				"max": 100,
				"min": 0
			},
			"Praha" : {
				"max": 100,
				"min": 0
			},
			"Plzeň" : {
				"max": 100,
				"min": 0
			},
			"Ostrava" : {
				"max": 100,
				"min": 0
			},
			"Most" : {
				"max": 100,
				"min": 0
			}, 
		}

	def add_city(self, city_name):
		"""
		Popis
		"""
		# if(self.databaseLocation.exists(city_name)):
		# 	raise ValueError("Toto město už je v databázi!")

		# Tady nastavuju od kdy budou v databázi záznamy - zvolil jsem 15.05.2023
		long_from = DateTimeConverter.date_to_timestamp(15,5,2023)
		long_now = DateTimeConverter.timestamp_now()
		self._add_records(city_name, long_from, long_now)





