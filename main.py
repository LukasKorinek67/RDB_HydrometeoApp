#!/bin/env python
# -*- coding: utf-8 -*-


from controller.Controller import Controller
from prettytable import PrettyTable

controller = Controller()

def start_print():
	print("\n ------------------------- ")
	print(" | Aplikace HydrometeoApp | ")
	print(" ------------------------- \n")

def menu():
	print("---------------------------------------------------")
	print("- 1 - Najít všechny stejné teploty pro dvě města")
	print("- 2 - Vygenerovat tabulku max a min teplot")
	print("- 3 - Přidat město\n")
	print("- 0 - Ukončit program")
	print("---------------------------------------------------\n")

	choice = input("Vyberte možnost: ")

	if choice == "1":
		same_temperatures()
	elif choice == "2":
		max_min_temperature()
	elif choice == "3":
		add_city()
	elif choice == "0":
		exit()
	else:
		print("Neplatná volba. Zkuste to znovu.")
		menu()


def same_temperatures():
	# 1
	cities_in_database = controller.get_all_cities()
	if(len(cities_in_database) < 2):
		print("V databázi není dostatečný počet měst, proto není možné najít stejné teploty pro dvě místa. Prosím přidejte města do databáze.")
	else:
		print("\nZadejte dvě požadovaná města:")
		firstCity = input("Název prvního města: ")
		check_if_end_program(firstCity)
		while firstCity not in cities_in_database:
			print("Toto město není v databázi! Zadejte prosím platné město. (V databázi jsou tyto města: " + ', '.join(cities_in_database) + ")\n")
			firstCity = input("Název prvního města: ")
			check_if_end_program(firstCity)
		
		secondCity = input("Název druhého města: ")
		check_if_end_program(secondCity)
		while (secondCity not in cities_in_database or secondCity == firstCity):
			if secondCity not in cities_in_database:
				print("Toto město není v databázi! Zadejte prosím platné město. (V databázi jsou tyto města: " + ', '.join(cities_in_database) + ")\n")
			elif secondCity == firstCity:
				print("Nelze zadat jedno město dvakrát! Zadejte prosím jiné město.\n")
			secondCity = input("Název druhého města: ")
			check_if_end_program(secondCity)

		same_temperatures = controller.same_temperatures(firstCity, secondCity)
		print_same_temperatures(same_temperatures)

def print_same_temperatures(same_temperatures):
	if(len(same_temperatures) > 100):
		print("Celkově bylo naměřeno", len(same_temperatures), "stejných hodnot. Opravdu je chcete všechny vypsat? [y/n]")
		choice = input("[y/n]: ")
		if choice == "y" or choice == "Y":
			print("\nTyto hodnoty byly naměřeny u obou měst:")
			print(', '.join(str(temperature) for temperature in same_temperatures))
	else:
		print("\nTyto hodnoty byly naměřeny u obou měst: (celkem", len(same_temperatures), "stejných hodnot)")
		print(', '.join(str(temperature) for temperature in same_temperatures))
	

def check_if_end_program(character):
	if character == "0":
		exit()

def max_min_temperature():
	# 2
	print("Tabulka maximálních a minimálních teplot všech měst:\n")
	data = controller.max_min_temperature()
	table = PrettyTable(["Město", "Max", "Min"])
	for city, values in data.items():
		max_value = values["max"]
		min_value = values["min"]
		table.add_row([city, max_value, min_value])
	print(table)
	print()


def add_city():
	# 3
	cityName = input("Zadejte název města: ")
	check_if_end_program(cityName)
	try:
		controller.add_city(cityName)
		print("Město " + cityName + " přidáno!\n")
	except ValueError as e:
		# město už je v databázi
		print("CHYBA: " + str(e) + "\n")


def main():
	start_print()
	controller.update_data()
	while True:
		menu()


if __name__ == "__main__":
	main()
