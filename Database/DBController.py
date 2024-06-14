import mysql.connector

class dbcont:
    
    def __init__(self, user,passwd):
        self.user = user
        self.passwd = passwd
        
    def login(self):
        

        mydb = mysql.connector.connect(
            host="localhost",
            user= "root",
            passwd= "password",
            database="ranil_proj"
        )
        
        mycursor = mydb.cursor()
        
        try:
            
            sql = " SELECT EXISTS (SELECT 1 FROM accounts WHERE Uname = %s AND passcode = %s) AS is_found;"
            val = (self.user, self.passwd)
            
        except:
            print("invalid credentials")
            return False
        mycursor.execute(sql,val)
        
        res = mycursor.fetchone()[0]
        
        return bool(res)
        
        
    def reg_protocol(self, fname, lname, uname, email, loa, bday, gender, pos, phono, Dhired, address, passcode):
        mydb = mysql.connector.connect(
            host="localhost",
            user= self.user,
            passwd= self.passwd,
            database="ranil_proj"
        )
        
        mycursor = mydb.cursor()
        
        sql =" INSERT INTO accounts (Fname, Lname, Uname, Email, LevelID, Bday, GenderID, Position, Phono, HireDate, address,Passcode) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        val = (fname, lname, uname, email, loa, bday, gender, pos, phono, Dhired, address, passcode)
        mycursor.execute(sql,val)

        mydb.commit()
        
        
    def reg_prod_protocol(self,Pname, Sprice,Cprice, Edate, quantity,desc):
        mydb = mysql.connector.connect(
            host="localhost",
            user= self.user,
            passwd= self.passwd,
            database="ranil_proj"
        )
        
        mycursor = mydb.cursor()
        
        sql =" INSERT INTO products (ProductName, SellingPrice, CostPrice, ExpDate, Quantity, Description) VALUES (%s,%s, %s,%s, %s,%s)"
        val = (Pname, Sprice,Cprice, Edate, quantity,desc)
        mycursor.execute(sql,val)

        mydb.commit()
        
        
