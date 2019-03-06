import requests
import json

class CountryApi:
    """CountryAPI class will connect to the restcountries api
    
    Attributes:
    
    - name (string): name of the country we want information back
    
    - api_link_string (string): link of the API to request

    Functions:
    
    - get_dict() : return the information in a dictionary
    
    - set_country(string) : sets or change the country 

   """    
    name = ''
    __api_link_string = ''
    
    def __init__(self, name="mexico"):
        self.name = name
        self.__api_link_string = 'https://restcountries.eu/rest/v2/name/{}?fullText=true'.format(self.name)
    
    def __str__(self):
        return "Country class"
    
    def get_dict(self):
        return requests.get(self.__api_link_string).json()[0]
    
    def set_country(self,name):
        self.name = name
        self.__api_link_string = 'https://restcountries.eu/rest/v2/name/{}?fullText=true'.format(self.name)