from api import CountryApi
import csv
import os
import xlsxwriter

class ExportCountry():
    """ExportCountry Class that with manage the creation of a CSV file for a Country list given, or a Excel doc.
    
    Attributes:

    - country_list (string): name of the country

    - api (CountryApi): CountryApi object for the connection to the API

    Functions:
    
    - set_country_list(country_list) : set the list given
    
    - add(country_name) : add the country json to the country_list

    - remove(country_name) : delete a specific country of the country_list

    - countries() : show all the current countries of the list

    - set_values() : Set all the values when a country is added
    
    - to_csv() : create a csv with the list of country_list

    - to_xlsx() : create a xlsv file with the list of country_list

   """ 
    api = CountryApi()

    def __init__(self,country_list=[]):
        self.set_country_list(country_list)
        self.header = ["name","capital","population"]
        self.values = []

    def __str__(self):
        return "CsvCountry Object"

    def countries(self):
        if self.country_list:
            countries = []
            for country in self.country_list:
                countries.append(country["name"])
            return countries
        else:
            return []

    def remove(self,name):
        if self.country_list:
            for country in self.country_list:
                if country["name"] == name:                    
                    self.country_list.remove(country)                    

    def set_country_list(self,country_list):
        self.country_list = country_list

    def set_values(self):
        val = []
        for country in self.country_list:
            for field in self.header:                    
                val.append(country[field])
            self.values.append(val)  
            val = []
   
    def add(self,country):
        self.api.set_country(country)
        self.country_list.append(self.api.get_dict())                
    
    def to_csv(self):
        csv_file = open('Countries.csv', mode='w')
        writer = csv.writer(csv_file)

        if self.country_list:
            writer.writerow(self.header)
        
        self.values = []        
        self.set_values()

        for v in self.values:
            writer.writerow(v)
            
        st = os.stat('Countries.csv')
        os.chmod('Countries.csv', st.st_mode)
        csv_file.close()

    def to_xlsx(self):
        workbook = xlsxwriter.Workbook('Countries.xlsx')
        worksheet = workbook.add_worksheet()

        self.values = []
        self.set_values()

        row, col = 1, 0
        worksheet.write(0,0,self.header[0])
        worksheet.write(0,1,self.header[1])
        worksheet.write(0,2,self.header[2])

        for v in self.values:
            worksheet.write(row,col,v[0])
            worksheet.write(row,col+1,v[1])
            worksheet.write(row,col+2,v[2])
            row += 1
        
        workbook.close()





    

