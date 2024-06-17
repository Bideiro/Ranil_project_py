import mysql.connector

class dbcont:
    
    def __init__(self, user,passwd):
        self.user = user
        self.passwd = passwd
        self.mydb = mysql.connector.connect(
            host="localhost",
            user= "root",
            passwd= "password",
            database="ranil_proj"
        )
        self.mycursor = self.mydb.cursor()
        
    def login(self):
        try:
            sql = " SELECT EXISTS (SELECT 1 FROM accounts WHERE Uname = %s AND passcode = %s) AS is_found;"
            val = (self.user, self.passwd)
        except:
            print("invalid credentials")
            return False
        self.mycursor.execute(sql,val)
        res = self.mycursor.fetchone()[0]
        
        return bool(res)
    
    def get_unit_types(self):
        self.mycursor.execute("SELECT UnitType FROM unit_type ORDER BY UnitTypeID")
        listed = [row[0] for row in self.mycursor]
        return listed
    
    def get_cate_types(self):
        self.mycursor.execute("SELECT Category FROM product_category ORDER BY CategoryID")
        listed = [row[0] for row in self.mycursor]
        return listed
    

    def get_sex(self):
        self.mycursor.execute("SELECT Sex FROM sex ORDER BY SexID")
        listed = [row[0] for row in self.mycursor]
        return listed
    
    def reg_user_protocol(self, LevelID, Uname, Passcode, fname, lname, sex, phono, email, Dhired, Bdate, address,  pos = None):
        sql =" INSERT INTO accounts (LevelID, Uname, Passcode, Fname, Lname, SexID, Phono, Email, Position, HireDate, Birthdate, Address) VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        val = (LevelID, Uname, Passcode, fname, lname,sex,phono, email,pos, Dhired, Bdate,address)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
    def reg_prod_protocol(self,Pname, Sprice, Utype , Ctype ,desc = None):
        sql =" INSERT INTO products (ProductName, SellingPrice, Description, QuantityTypeID, ProductTypeID) VALUES (%s, %s,%s ,%s,%s)"
        val = (Pname, Sprice,desc, Utype, Ctype )
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
        
