from api import CountryApi
from db_connection import DBConnection

class Country:
    """Country class storage the information of a specific country
    
    Attributes:
    
    - api (CountryApi): CountryApi object for the connection to the API
    
    - name (string): name of the country
    
    - name (string): name of the country
    
    - capital (string): capital of the country
    
    - region (string): name of the region where the country is
    
    - population (int): number of the current population
    
    - demonym (string): way of call the habitants of the country
    
    - flag (string): storage the link of the SVG flag image
    
    - lat (float): storage the latitude of the country
    
    - lon (float): storage the longitude of the country
    
    
    Functions:
    
    - insert() : storage in the database the country
    
    - update(id , **kwargs) : update the selected country with the new information
    
    - delete(id) : delete the selected country 
    
    - get_all() : it will return all the rows in the Country table

   """       
    api = CountryApi()
    connection = DBConnection()
               
    def __init__(self, name="Mexico"):   
        self.set_country(name)
        
    def __str__(self):
        return "Country Object " + self.name
    
    def set_country(self,name):
        self.api.set_country(name)
        
        #store in a dict variable
        dictionary = self.api.get_dict()
        
        #initialize all the country information
        self.name = dictionary["name"]
        self.capital = dictionary["capital"]
        self.region = dictionary["region"]
        self.population = dictionary["population"]
        self.demonym = dictionary["demonym"]
        self.flag = dictionary["flag"]
        self.lat = dictionary["latlng"][0]
        self.lon = dictionary["latlng"][1]
        
    
    def insert(self):        
        # Creating the sql string to execute
        sql_string = ("INSERT INTO `country`" 
               "( `name`,`capital`,`region`,`population`,`demonym`,`flag`,`lat`,`lon`)"
               " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        
        # Tuple of values that will be inserted
        sql_values = (self.name, self.capital, self.region,
                      self.population, self.demonym, self.flag,
                      self.lat, self.lon)
        
        try:
            # execute the sql_string
            self.connection.execute(sql_string,sql_values)
        except Exception as e:
            print('Failed execute query: '+ str(e))        
                
    
    def delete(self, id):
        # Creating the sql string to execute
        sql_string = "DELETE FROM `country` WHERE country.id = " + str(id)
        try:
            # execute the sql_string
            self.connection.execute(sql_string)

        except Exception as e:
            print('Failed execute query: '+ str(e))          
    
    def get_all(self):
        # Creating the sql string to execute
        sql_string = "SELECT * FROM `country`"
        
        try:
            # execute the sql_string
            return self.connection.execute(sql_string)
            
        except Exception as e:
            print('Failed execute query: '+ str(e))        
        
    
    def update(self,id,**kwargs):
        # Creating the sql string to execute
        sql_string = "UPDATE `country` SET"
        
        try:
            #set all the values to the sql string
            for key, item in kwargs.items(): 
                #Check if we need the value surrounded quotation marks
                if type(item) != str:
                    sql_string += " country." + str(key) + " = " + str(item) + ","
                else:
                    sql_string += " country." + str(key) + " = '" + str(item) + "' ,"
                                
            #Delete the unnecesary last coma
            list_sql = list(sql_string)
            del list_sql[-1]
            sql_string = ''.join(list_sql)
            
            #end of the sql_string
            sql_string += " WHERE country.id = " + str(id) 
            
            # execute the sql_string            
            self.connection.execute(sql_string)
            
        except Exception as e:
            print('Failed execute query: '+ str(e))
        

        
    
        