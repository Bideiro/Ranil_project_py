import mysql.connector

class dbcont:
    
    def __init__(self, user,passwd):
        self.user = user
        self.passwd = passwd
        
    def conn(self):
        try:
            mysql.connector.connect(
            host="localhost",
            user= self.user,
            passwd= self.passwd,
            database="ranil_proj"
        )
        except Exception as e:
            print(e)
            
        

