from settings import DATABASE
import pymysql.cursors

class DBConnection:
    """DBConection class for connect with a MySql database
    
    Attributes:
    
    - host (string): host of the database service
    
    - user (string): user of the database
    
    - password (string): user password to connect
    
    - db_name (string): name of the database
    
    - charset (string): collation of the database

    Functions:
    
    - connect() : connect to the database from settings file

   """
    
    def __init__(self):
        #Control flag to know the state of the connection
        self.connected = False
        
        #Set a None value to connection
        self.connection = None
        
        #Set the values of file settings
        self.db_name = DATABASE["db"]
        self.host = DATABASE["host"]
        self.user = DATABASE["user"]
        self.password = DATABASE["password"]
        self.charset = DATABASE["charset"]
    
    def connect(self):
        #Make the database connection
        self.connection = pymysql.connect( host = self.host, 
                                      user = self.user,
                                      password = self.password, 
                                      db = self.db_name,
                                      charset = self.charset)
    
    def execute(self, sql_string, arguments=()):
        #We make sure we are connected to the database
        if not(self.connected):
            self.connect()        
        try:
            with self.connection.cursor() as cursor:                
                #We are going to execute the sql_string passed
                cursor.execute(sql_string, arguments)
            
            #Commit to see the changes in the bd
            self.connection.commit()        
            
            #Get the result of the commit
            result = cursor.fetchall()
            
            #return it (it will be None unless it is a select query)
            return result
        
        finally:
            #We close the connection to avoid errors
            self.connection.close()
            
        
    