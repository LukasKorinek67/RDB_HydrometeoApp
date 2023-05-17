#!/bin/env python
# -*- coding: utf-8 -*-


# aplikační logiku
# SQL - PostgreSQL, MySQL, SQLite
# MongoDB
# - jakmile mám data který jsou kompletní, tak najít všechny stejné teploty pro dvě místa
# - vyberu třeba Liberec a Jablonec - a najdu všechny stejný teploty
# - potřebuju vygenerovat tabulku, která mi vygeneruje maxima a minima (teploty) pro jednotlivý místa - pro všechny místa


from Controller import Controller

controller = Controller()

def start_print():
	print(" | Aplikace HydrometeoApp | ")

def menu():
	print("---------------------------")
	print("- 1 - Najít všechny stejné teploty pro dvě místa")
	print("- 2 - Vygenerovat tabulku max a min teplot")
	print("- 3 - Přidat město")
	print("- 0 - Ukončit program")
	print("---------------------------")

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
	controller.same_temperatures()
	print("... Probíhá nalezení všech stejných teplot pro dvě místa ...\n")


def max_min_temperature():
	# 2
	controller.max_min_temperature()
	print("... Probíhá generování tabulky max a min teplot ...\n")


def add_city():
	# 3
	cityName = input("Zadejte název města: ")
	
	try:
		controller.add_city(cityName)
		print("Město " + cityName + " přidáno!\n")
	except ValueError as e:
		print("CHYBA: " + str(e) + "\n")


def main():
	start_print()
	controller.update_data() # doplní měření v době, kdy aplikace neběžela
	while True:
		menu()


if __name__ == "__main__":
	main()

