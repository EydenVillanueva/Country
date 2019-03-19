from api import CountryApi
import json
import csv
import os

class CsvCountry():
    """CsvCountry Class that with manage the creation of a CSV file for a Country list given
    
    Attributes:

    - country_list (string): name of the country

    - api (CountryApi): CountryApi object for the connection to the API

    Functions:
    
    - set_country_list(country_list) : set the list given
    
    - add_country(country_name) : add the country json to the country_list
    
    - to_csv() : create a csv with the list of country_list

   """ 
    api = CountryApi()

    def __init__(self,country_list):
        self.set_country_list(country_list)

    def __str__(self):
        return "CsvCountry Object"

    def set_country_list(self,country_list):
        self.country_list = country_list
    
    def add_country(self,country):
        self.api.set_country(country)
        self.country_list.append(self.api.get_dict())
    
    def to_csv(self):

        csv_file = open('Countrycsv.csv', mode='w')

        writer = csv.writer(csv_file)

        values = []

        if self.country_list:
            header = self.country_list[0].keys()
            writer.writerow(header)
        
        for dic in self.country_list:
            values = []
            for item in dic.values():
                if type(item) == list:
                    if type(item[0] == dict):
                        values.append("dict")
                    else:
                        values.append(item[0])
                elif type(item) == dict:
                    values.append("dict")
                else:
                    values.append(item)
            if values:
                writer.writerow(values)
                
        st = os.stat('Countrycsv.csv')
        os.chmod('Countrycsv.csv', st.st_mode)

                




    

