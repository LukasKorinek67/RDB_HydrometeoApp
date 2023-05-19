#!/bin/env python
# -*- coding: utf-8 -*-


import os
import json
import random

from file_utils.ConfigFileHandler import ConfigFileHandler

class TestJSONGenerator():
    """
    Třída TestJSONGenerator - pouze pro moje zkoušení! Jen tam hodím random JSON soubor, protože mi nefunguje exe
    Pak hlavně smazat!!
    """

    def __init__(self, city_name):
        """
        Konstruktor
        """
        self.city = city_name

    def _get_file_path(self, file_name):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.dirname(current_dir)
        file_path = os.path.join(parent_dir, file_name)
        return file_path


    def generate(self):
        no_names = 5
        names = ["Karel", "Petr", "Zuzana", "Kamila", "Anezka", "Jan"]

        no_surnames = 5
        surnames = ["Novak", "Smrz", "Nova", "Nejedla", "Ceska", "Zizka"]

        no_emails = 5
        emails = ["karel.novak@abc.com", "petr1@emial.com", "zuzana.nova@abc.com", "kamila.ceska@abc.com", "anezka.nejedla@eltrom.cz", "jan.zizka@eltrom.cz"]

        no_depts = 3
        departments = ["Abc", "Aka", "ABC", "eltrom"]

        no_adrs = 3
        addresses = ["Sladka", "Nova", "Uzka", "Sirkova"]

        no_adr_nums = 3
        adr_nums = ["23", "2", "545/1", "24"]

        no_adr_cities = 3
        adr_cities = ["Liberec", "Praha", "Plzen", "Brno"]

        no_phones = 6
        phones = ["+420777458547", "+420535161254", "+4206302541542", "+420777985632", "+420602458745", "+420772698452", "+420775632874"]

        no_devices = 2
        devices = ["Dev01", "Measure 1000", "tempX1"]
        deltas = ["0.1", "1", "0.01"]
        manufacturers = ["XXX", "kdoVI", "Ta12"]
        inv = ["INV-2354", "CZ1254", "AX547"]
        voltage = ["[12]", "[12,24]", "[12,24,110,230]"]

        config_file = ConfigFileHandler()
        config = config_file.read_config()
        tmp = config.split(',')
        place = tmp[0].strip()
        sfrom = tmp[1].strip()
        sto = tmp[2].strip()

        if place and sfrom and sto:
            from_time = int(sfrom)
            to_time = int(sto)
            
            filename = place

            data = {
                "place": place,
                "type": {}
            }

            manual = random.randint(0, 1)
            if manual == 1:
                #print("Manual Measurement...")
                rand = random.randint(0, no_names - 1)
                data["type"]["manual"] = {
                    "name": names[rand],
                    "surename": surnames[rand],
                    "email": emails[rand]
                }
                rand = random.randint(0, no_depts - 1)
                rand2 = random.randint(0, no_phones - 1)
                data["type"]["manual"]["deptitle"] = departments[rand]
                data["type"]["manual"]["depphone"] = phones[rand2]
                data["type"]["manual"]["depaddress"] = [addresses[rand], adr_nums[rand], adr_cities[rand]]
            else:
                #print("Auto Measurement...")
                rand = random.randint(0, no_devices - 1)
                data["type"]["auto"] = {
                    "title": devices[rand],
                    "delta": deltas[rand],
                    "manufacturer": manufacturers[rand],
                    "voltage": voltage[rand],
                    "regnum": inv[rand]
                }

            data["type"]["values"] = []

            temp = 0.0
            pressure = 1000.0
            rain = 0
            plus = 0
            delta = 0.0

            while from_time < to_time:
                plus = random.randint(0, 1)
                delta = float(random.randint(0, 10)) / 10.0
                if plus == 1:
                    temp += delta
                else:
                    temp -= delta

                plus = random.randint(0, 1)
                delta = float(random.randint(0, 100)) / 10.0
                if plus == 1 and pressure < 1084:
                    pressure += delta
                else:
                    pressure -= delta

                if plus == 0 and pressure > 870:
                    pressure -= delta
                else:
                    pressure += delta

                plus = random.randint(0, 1)
                delta = float(random.randint(0, 100)) / 10.0
                if plus == 0 and rain - delta > 0:
                    rain -= delta
                else:
                    rain += delta

                #print(from_time, end=", ")
                if from_time + 60 >= to_time:
                    data["type"]["values"].append([from_time, round(temp, 1), round(pressure, 1), rain])
                else:
                    data["type"]["values"].append([from_time, round(temp, 1), round(pressure, 1), rain])

                from_time += 60

            filename_json = filename + ".json"
            file = self._get_file_path(filename_json)

            with open(file, "w") as f_json:
                json.dump(data, f_json, indent=4)
                
            return 1
        else:
            print("Error parsing input.txt, expected place, timestamp_from, timestamp_to")
            return 10

        return 0
