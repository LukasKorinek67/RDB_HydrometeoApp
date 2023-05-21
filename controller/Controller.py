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
		# Ověřovací výpis
		# print("Město:", city)
		# print("Od: ", DateTimeConverter.timestamp_to_datetime(long_from))
		# print("Do: ", DateTimeConverter.timestamp_to_datetime(long_to))
		#
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
		
		measurements = data["type"]["values"]
		self.databaseMeasurement.add_measurements(data["place"], measurements)

		# dál to tady ještě uložit do relační databáze
		# v proměnný data je python dictionary
		# tzn. něco jako databaseLocation.save() atd. atd.


	def update_data(self):
		"""
		- doplní měření v době, kdy aplikace neběžela
		"""
		long_now = DateTimeConverter.timestamp_now()
		all_cities = self.get_all_cities()
		for city in all_cities:
			last_record = self.databaseMeasurement.get_last_record(city)
			if last_record != 0:
				self._add_records(city, last_record, long_now)

	def get_all_cities(self):
		"""
		- vrátí všechna města, které jsou v databázi
		"""
		# Teď to tady vracím z Monga, ale správně to budeme muset tady vracet z relační databáze!
		return self.databaseMeasurement.get_all_cities()
		# return self.databaseLocation.get_all_cities()

	def same_temperatures(self, first_city, second_city):
		"""
		- vrátí list stejných naměřených teplot pro dvě zvolená města
		"""
		return self.databaseMeasurement.get_same_temperatures(first_city, second_city)

	def max_min_temperature(self):
		"""
		- vrátí dictionary - max a min teploty pro všechny města
		"""
		cities = self.get_all_cities()
		max_min_dict = dict()
		for city in cities:
			max_min_dict[city] = self.databaseMeasurement.get_max_min_temp(city)
		return max_min_dict

	def add_city(self, city_name):
		"""
		- přidá město do databáze a zavolá metodu _add_records, která se postará o stažení záznamů od počátečního data
		"""
		# Tady nějak získat z relační!
		# if(self.databaseLocation.exists(city_name)):
		if(city_name in self.get_all_cities()):
			raise ValueError("Toto město už je v databázi!")

		# Tady nastavuju od kdy budou v databázi záznamy - zvolil jsem 18.05.2023
		long_from = DateTimeConverter.date_to_timestamp(18,5,2023)
		long_now = DateTimeConverter.timestamp_now()
		self._add_records(city_name, long_from, long_now)





