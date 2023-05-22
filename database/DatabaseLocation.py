#!/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


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
        self.conn = sqlite3.connect("sql_database.db")
        self.conn.execute("PRAGMA foreign_keys = ON")
    

    def add_data(self, data):
        #cities = self.get_all_cities()
        #print(cities)
        if "manual" in data["type"].keys():
            #print("---Manualni---")
            name = data["type"]["manual"]["name"]
            surname = data["type"]["manual"]["surename"]
            email = data["type"]["manual"]["email"]
            dep_title = data["type"]["manual"]["deptitle"]
            phone = data["type"]["manual"]["depphone"]
            depaddress = data["type"]["manual"]["depaddress"]
            street = depaddress[0]
            addr_number = depaddress[1]
            city = depaddress[2]
            # zde se zkonrolují všechny vztahy, tak aby nedošlo k porušení integrace dat a poté ze zapíše MANUAL měření
            self.check_if_relations_exist(name, surname, email, dep_title, phone, street, addr_number, city)      
        elif "auto" in data["type"].keys():
            #print("---Auto---")
            auto_title = data["type"]["auto"]["title"]
            delta = data["type"]["auto"]["delta"]
            manufacturer = data["type"]["auto"]["manufacturer"]
            voltage = data["type"]["auto"]["voltage"]
            regnum = data["type"]["auto"]["regnum"]
            # zde se zkonrolují všechny vztahy, tak aby nedošlo k porušení integrace dat a poté ze zapíše AUTO měření
            self.check_if_meter_auto_exist(auto_title, delta, manufacturer,voltage, regnum)
        return


    def get_all_cities(self):
        """
        Vrací seznam všech měst v databázi
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT city FROM cities;")
        rows = cursor.fetchall()     #[("Liberec",), ("Jablonec",), ("Beroun",)]
        cities_array = [row[0] for row in rows]     #["Liberec", "Jablonec", "Beroun"]
        return cities_array
        #return ["Liberec", "Praha", "Plzeň", "Ostrava", "Most"]
        #pass


    def add_city(self, city):
        """
        Přidá nové město do databáze
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO cities (city) VALUES (?);", (city,))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Chyba při přidávání dat do databáze.(city)", e)


    def add_meter(self, name, surname, email):    
        """
        Přidá novou osobu do databáze
        """
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO meters (type, name, surname, email) VALUES (?,?,?,?);"       
            param = ["manual", name, surname, email]                                          
            cursor.execute(query,param)
            self.conn.commit()
            #print("osoba pridana")
        except sqlite3.Error as e:
            print("Chyba při přidávání dat do databáze.(meter)", e)


    def check_if_meter_exist(self, name, surname, email):
        """
        Zkontroluje jestli osoba již v databázi existuje, pokud ne tak ji přidá
        """ 
        try:
            cursor = self.conn.cursor()
            query = "SELECT meter_id FROM meters WHERE type = ? AND name = ? AND surname = ? AND email = ?;"       
            params = ["manual", name, surname, email]                                                              
            cursor.execute(query, params)

            rows = cursor.fetchall()
            if len(rows) > 0:
                #print("Tato osoba již existuje.")
                meter_id = rows[0]
                meter_id = meter_id[0]
                return meter_id
            else:
                self.add_meter(name, surname, email)
                return self.check_if_meter_exist(name, surname, email) #[0]
        except sqlite3.Error as e:
            print("Chyba při kontrolování dat z databáze.(meter)", e)


    def add_meter_auto(self, auto_title, delta, manufacturer, voltage_id, regnum):  
        """
        Přidá nový automat do databáze.
        """ 

        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO meters (type, auto_title, delta, manufacturer, voltage_id, regnum) values (?, ?, ?, ?, ?, ?);"             
            params = ["auto", auto_title, delta, manufacturer, voltage_id, regnum]                                                          
            cursor.execute(query,params)
            self.conn.commit()
            #print("automat pridan")
        except sqlite3.Error as e:
            print("Chyba při přidávání dat do databáze.(meter-auto)", e)


    def check_if_meter_auto_exist(self, auto_title, delta, manufacturer, voltage, regnum):
        """
        Zkontroluje jestli automat již v databázi existuje, pokud ne tak ho přidá
        """ 
        try:
            cursor = self.conn.cursor()
            query = "SELECT meter_id FROM meters WHERE type = ? AND auto_title = ? AND delta = ? AND manufacturer = ? AND regnum = ?;"       
            params = ["auto", auto_title, delta, manufacturer, regnum]                                                           
            cursor.execute(query, params)
            rows = cursor.fetchall()
            if len(rows) > 0:
                #print("Tento automat již existuje.")
                meter_id = rows[0]
                return meter_id
            else:
                voltage_id=self.add_voltage(voltage)
                self.add_meter_auto(auto_title, delta, manufacturer,voltage_id, regnum)
        except sqlite3.Error as e:
            print("Chyba při kontrolování dat z databáze.(meter-auto)", e)
        

    def add_department(self, dep_title, street, addr_number, city):  
        """
        Přidá nové oddělení do databáze.
        """ 

        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO departments (dep_title, street, addr_number, city) VALUES (?, ?, ?, ?);"              
            params = [dep_title, street, addr_number, city]                                                          
            cursor.execute(query,params)
            self.conn.commit()
            #print("Oddeleni pridano")
        except sqlite3.Error as e:
            print("Chyba při přidávání dat do databáze.(department)", e)


    def check_if_department_exist(self, dep_title, street, addr_number, city):
        """
        Zkontroluje jestli oddeleni již v databázi existuje, pokud ne tak ho přidá
        """ 
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT dep_title FROM departments WHERE dep_title = ?;", (dep_title,))

            rows = cursor.fetchall()
            if len(rows) > 0:
                #print("Toto oddělení již existuje.")
                dep_title = rows[0]
                dep_title = dep_title[0].replace("(", "").replace(")", "").replace("'", "")
                return dep_title
            else:
                self.add_department(dep_title, street, addr_number, city)
                return self.check_if_department_exist(dep_title, street, addr_number, city) #[0]
        except sqlite3.Error as e:
            print("Chyba při kontrolování dat z databáze.(department)", e)

    
    def add_voltage(self, voltage):   
        """
        Přidá voltage do databáze
        """
        try:
            voltage_parts = len(voltage)
            voltage_parts = ", ".join(["voltage{}".format(i) for i in range(1, len(voltage) + 1)])
            voltage_values = ", ".join(["?" for _ in range(len(voltage))])
            cursor = self.conn.cursor()
            query = "INSERT INTO voltages ({}) VALUES ({});".format(voltage_parts, voltage_values)
            cursor.execute(query, voltage)                                
            self.conn.commit()
            #print("voltage pridano")

            query2 = "SELECT last_insert_rowid() FROM voltages"
            cursor.execute(query2)
            voltage_id = cursor.fetchone()[0]
            return voltage_id
        except sqlite3.Error as e:
            print("Chyba při přidávání dat do databáze.(voltage)", e)


    def add_phone(self, phone):  
        """
        Přidá nové oddělení do databáze.
        """ 
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO phones (phone) VALUES (?);", (phone,))                                                        
            self.conn.commit()
            #print("Telefon pridan")
        except sqlite3.Error as e:
            print("Chyba při přidávání dat do databáze.(phone)", e)


    def check_if_phone_exist(self, phone):
        """
        Zkontroluje jestli telefon již v databázi existuje, pokud ne tak ho přidá
        """ 
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT phone FROM phones WHERE phone = ?;", (phone,))
            rows = cursor.fetchall()
            if len(rows) > 0:
                #print("Toto tel.cislo již existuje.")
                phone = rows[0]
                phone = phone[0]
                return phone
            else:
                self.add_phone(phone)
                return self.check_if_phone_exist(phone)
        except sqlite3.Error as e:
            print("Chyba při kontrolování dat z databáze.(department)", e)

    
    def check_if_relations_exist(self, name, surname, email, dep_title, phone, street, addr_number, city):
        """
        Zkontroluje jestli vztah mezi osobou a oddelenim již v databázi existuje, pokud ne tak ho přidá
        """ 
        try:

            phone = self.check_if_phone_exist(phone)
            #print("final ID phone")
            #print(phone)

            dep_title = self.check_if_department_exist(dep_title, street, addr_number, city)
            #print("final ID dep")
            #print(dep_title)

            dep_phone = self.check_if_department_phone_exist(dep_title, phone)
            #print("----DEP_PHONE---")
            #print(dep_phone)


            meter_id = self.check_if_meter_exist(name, surname, email)
            #print("final ID meter")
            #print(meter_id)

            meter_dep = self.check_if_meter_department_exist(meter_id,dep_title)
            #print("----METER_DEP---")
            #print(meter_dep)
        
        except sqlite3.Error as e:
            print("Chyba při kontrolování dat z databáze.(department)", e)

    def add_department_phone(self, dep_title, phone):
        """
        Přidá nové spojení oddělení a telefonu do tabulky v databázi.
        """ 
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO department_phone (dep_title, phone) VALUES (?, ?);"       
            params = [dep_title, phone]
            cursor.execute(query, params)                                          
            self.conn.commit()
            #print("Spojeni oddeleni a telefonu pridano")
        except sqlite3.Error as e:
            print("Chyba při přidávání dat do databáze.(department_phone)", e)


    def check_if_department_phone_exist(self, dep_title, phone):
        """
        Zkontroluje jestli telefon již v databázi existuje, pokud ne tak ho přidá
        """ 
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM department_phone WHERE dep_title = ? AND phone = ?"
            params = [dep_title, phone]
            cursor.execute(query, params)
            rows = cursor.fetchall()
            if len(rows) > 0:
                #print("Toto spojeni oddeleni a telefonu již existuje.")
                department_phone = rows[0]
                return department_phone
            else:
                self.add_department_phone(dep_title, phone)
                return self.check_if_department_phone_exist(dep_title, phone)[0]
        except sqlite3.Error as e:
            print("Chyba při kontrolování dat z databáze.(department_phone)", e)


    def add_meter_department(self, meter_id,dep_title):
        """
        Přidá nové spojení osoby a  oddělení do tabulky v databázi.
        """ 
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO meter_department (meter_id, dep_title) VALUES (?, ?);"       
            params = [meter_id, dep_title]
            cursor.execute(query, params)                                          
            self.conn.commit()
            #print("Spojeni osoby aoddeleni pridano")
        except sqlite3.Error as e:
            print("Chyba při přidávání dat do databáze.(meter_department)", e)


    def check_if_meter_department_exist(self, meter_id,dep_title):
        """
        Zkontroluje jestli vztah mezi osbou a oddělenim již v databázi existuje, pokud ne tak ho přidá
        """ 
        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM meter_department WHERE meter_id = ? AND dep_title = ? "
            params = [meter_id, dep_title]
            cursor.execute(query, params)
            rows = cursor.fetchall()
            if len(rows) > 0:
                #print("Toto spojeni osoby a oddeleni již existuje.")
                department_phone = rows[0]
                return department_phone
            else:
                self.add_meter_department(meter_id,dep_title)
                return self.check_if_meter_department_exist(meter_id,dep_title)[0]
        except sqlite3.Error as e:
            print("Chyba při kontrolování dat z databáze.(meter_department)", e)
   