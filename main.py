#!/bin/env python
# -*- coding: utf-8 -*-


# aplikační logiku
# SQL - PostgreSQL, MySQL, SQLite
# MongoDB
# - jakmile mám data který jsou kompletní, tak najít všechny stejné teploty pro dvě místa
# - vyberu třeba Liberec a Jablonec - a najdu všechny stejný teploty
# - potřebuju vygenerovat tabulku, která mi vygeneruje maxima a minima (teploty) pro jednotlivý místa - pro všechny místa

# zkouska git branch

from Controller import Controller

def startPrint():
	print("-------- Aplikace HydrometeoApp --------")

def printMenu():
	print("----------------------")
	print("- 1 - Najít všechny stejné teploty pro dvě místa")
	print("- 2 - Vygenerovat tabulku max a min teplot")
	print("- 3 - Přidat město")
	print("----------------------")

def main():
	startPrint()
	Controller.updateData() # doplní měření v době, kdy aplikace neběžela
	printMenu()
	# zjistit jakou volbu zadal uživatel a pak provést
	

	# 1
	Controller.sameTemperatures()

	# 2
	Controller.maxMinTemperature()

	# 3
	cityName = "City"
	Controller.addCity(cityName)
	


if __name__ == "__main__":
    main()