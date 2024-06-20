import mysql.connector

class dbcont:
    
    # create singleton
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
    
    def get_id_value(self,value = None, id = None,sex = None ,cate = None, level = None, unit = None):
        if sex != None:
            if id != None:
                sql = 'SELECT Sex FROM sex WHERE SexID = %s'
            elif value != None:
                sql = 'SELECT SexID FROM sex WHERE Sex = %s'
            else:
                sql = "SELECT Sex FROM sex ORDER BY SexID"
        elif cate != None:
            if id != None:
                sql = 'SELECT Category FROM category WHERE CategoryID = %s'
            elif value != None:
                sql = 'SELECT CategoryID FROM category WHERE Category = %s'
            else:
                sql = "SELECT Category FROM category ORDER BY CategoryID"
        elif level != None:
            if id != None:
                sql = 'SELECT Level FROM levels WHERE LevelID = %s'
            elif value != None:
                sql = 'SELECT LevelID FROM levels WHERE Level = %s'
            else:
                sql = 'SELECT Level FROM levels ORDER BY LevelID'
        elif unit != None:
            if id != None:
                sql = 'SELECT UnitType FROM unit_type WHERE UnitTypeID = %s'
            elif value != None:
                sql = 'SELECT UnitTypeID FROM unit_type WHERE UnitType = %s'
            else:
                sql = 'SELECT UnitType FROM unit_type ORDER BY UnitTypeID'
        else:
            print('No selected table!')
            return None
        
        if id != None:
            self.mycursor.execute(sql, (id,))
            return self.mycursor.fetchone()[0]
        elif value != None:
            self.mycursor.execute(sql, (value,))
            return self.mycursor.fetchone()[0]
        else:
            self.mycursor.execute(sql)
            listed = [row[0] for row in self.mycursor]
            return listed
        
    def get_user_creds(self, User = None, Passcode = None, colint = None, Fname = None , Lname = None):
        print('db cont')
        print(Fname + Lname)
        if User != None and Passcode != None:
            sql = 'SELECT * FROM accounts'
            self.mycursor.execute(sql)
        elif Fname != None and Lname != None:
            sql = 'SELECT * FROM accounts WHERE Fname = %s AND Lname = %s'
            val = (Fname,Lname)
            self.mycursor.execute(sql,val)
        else:
            sql = 'Select * FROM accounts WHERE Uname = %s AND Passcode = %s'
            val = (User,Passcode)
            self.mycursor.execute(sql,val)
            
        if colint == None:
            print('NO COL NUM SELECTED! Fetching all columns!')
            return self.mycursor.fetchall()[0]
        else:
            return self.mycursor.fetchone()[colint][0]
        
    def get_all_names(self):
        sql = "SELECT Fname,Lname FROM accounts"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def get_all_prod(self):
        
        sql = "SELECT * FROM products"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def search_prod(self, searchstr):
        sql = """
                SELECT ProductID, ProductName, SellingPrice, Stock, ExpirationDate, Description, UnitTypeID, CategoryID FROM products
                WHERE ProductID LIKE %s
                OR ProductName LIKE %s
                OR SellingPrice LIKE %s
                OR ExpirationDate LIKE %s
                OR Stock LIKE %s
                """
        searchstr = '%' + searchstr + '%'
        val = (searchstr,searchstr,searchstr,searchstr,searchstr)
        self.mycursor.execute(sql,val)
        return self.mycursor.fetchall()
        
    def reg_user_protocol(self, LevelID, Uname, Passcode, fname, lname, sex, phono, email, Dhired, Bdate, address,  pos = None):
        sql =""" INSERT INTO accounts (LevelID, Uname, Passcode, Fname, Lname, SexID, Phono, Email, Position, HireDate, Birthdate, Address) 
                    VALUES (%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"""
        val = (LevelID, Uname, Passcode, fname, lname,sex,phono, email,pos, Dhired, Bdate,address)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
    def reg_prod_protocol(self,Pname, Sprice, Utype , Ctype ,desc = None):
        sql =""" INSERT INTO products (ProductName, SellingPrice, Description, UnitTypeID, CategoryID)
                    VALUES (%s, %s,%s ,%s,%s)"""
        val = (Pname, Sprice,desc, Utype, Ctype )
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
    def update_user_protocol(self,oldUlist, NewUlist):
        sql = """
        UPDATE accounts
        SET LevelID = %s, Uname = %s, Fname = %s, Lname = %s, SexID = %s, Phono = %s, Email = %s, Position = %s, HireDate = %s, Birthdate = %s, Address = %s
        WHERE Uname = %s AND Fname = %s AND Lname = %s;
        """
        self.mycursor.execute(sql,NewUlist + oldUlist)
        self.mydb.commit()
        
        print(self.get_all_names())
        
    def update_prod_protocol(self,oldPlist, NewPlist ):
        
        print(NewPlist)
        print(oldPlist)
        
        sql ="""
        UPDATE products
        SET ProductName = %s, SellingPrice = %s, Description = %s, QuantityTypeID = %s, ProductTypeID = %s
        WHERE ProductName = %s AND ProductID = %s;
        """
        self.mycursor.execute(sql,NewPlist + oldPlist)
        self.mydb.commit()
        
        pass
        
if __name__ == '__main__':
    
    db =dbcont('admin', 123456)
    
    # Ulist =db.get_user_creds(Fname= 'Admin' , Lname= 'Admin')
    
    # print (Ulist[4])
    
    print(db.get_id_value(sex=True,value= 1))
    
    pass