#!/bin/env python
# -*- coding: utf-8 -*-


"""
RDB - Controller
"""

from datetime import date
# from RequestHandler import RequestHandler
# from DailyCasesData import DailyCasesData

import sys
import os

from ConfigFileHandler import ConfigFileHandler
from GeneratorFileHandler import GeneratorFileHandler

from DateTimeConverter import DateTimeConverter

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, "database")))
from DatabaseLocation import DatabaseLocation
from DatabaseMeasurement import DatabaseMeasurement


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

		# Tady pak vygeneruju ten JSON a data z toho je pak potřeba nějak uložit do databáze
		#self.generatorFileHandler.generate()


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
		pass

	def max_min_temperature(self):
		"""
		Popis
		"""
		pass

	def add_city(self, city_name):
		"""
		Popis
		"""
		#if(self.databaseLocation.exists(city_name)):
		if(city_name == "Liberec"):	#Jen pro testování
			raise ValueError("Toto město už je v databázi!")

		# Tady nastavuju od kdy budou v databázi záznamy - zvolil jsem 15.05.2023
		long_from = DateTimeConverter.date_to_timestamp(15,5,2023)
		long_now = DateTimeConverter.timestamp_now()
		self._add_records(city_name, long_from, long_now)





