import mysql.connector

class dbcont:
    
    def __init__(self, user,passwd):
        self.user = user
        self.passwd = passwd
        try:
            mydb = mysql.connector.connect(
            host="localhost",
            user= self.user,
            passwd= self.passwd,
            database="ranil_proj"
        )
        except Exception as e:
            print(e)
        
        self.cursor = mydb.cursor()
        
    def reg_protocol(self):
            print()
