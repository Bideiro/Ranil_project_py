import mysql.connector
from Database.User_Manager import UserMana

# from User_Manager import UserMana

class dbcont:
    
    UMana = UserMana()
    
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
        sql = " SELECT EXISTS (SELECT 1 FROM accounts WHERE Uname = %s AND passcode = %s) AS is_found"
        val = (self.user, self.passwd)
        self.mycursor.execute(sql,val)
        res = self.mycursor.fetchone()[0]
        
        if bool(res):
            sql = " SELECT UID, Uname, Passcode, LevelID FROM accounts WHERE Uname = %s AND passcode = %s"
            val = (self.user, self.passwd)
            self.mycursor.execute(sql,val)
            curruser = self.mycursor.fetchone()
            self.UMana.set_user(UID= curruser[0],User= curruser[1], Pass=curruser[2],Level= curruser[3])
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
        
    def get_all_prod(self, inv = None , trans = None):
        
        if inv:
            sql = "SELECT * FROM products"
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        else:
            sql = "SELECT RPID , ProductName, SellingPrice, Stock, ExpirationDate FROM products"
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        
    def prod_price(self, id):
        sql = """
                    SELECT SellingPrice FROM products
                    WHERE RPID LIKE %s
                    """
        self.mycursor.execute(sql,(id,))
        return self.mycursor.fetchone()[0]

    def search_prod(self, searchstr, inv = None, trans = None, id = None):
        
        if inv:
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
        elif trans:
            sql = """
                    SELECT ProductID, ProductName, SellingPrice, Stock, ExpirationDate FROM products
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
        elif id:
            sql = """
                    SELECT RPID, ProductName, SellingPrice, Stock, ExpirationDate FROM products
                    WHERE RPID LIKE %s
                    """
            self.mycursor.execute(sql,(searchstr,))
            return self.mycursor.fetchone()
        print("huh")
        return 0
        
    def reg_user_protocol(self, LevelID, Uname, Passcode, fname, lname, sex, phono, email, Dhired, Bdate, address,  pos = None):
        sql =""" INSERT INTO accounts (LevelID, RUID, Uname, Passcode, Fname, Lname, SexID, Phono, Email, Position, HireDate, Birthdate, Address) 
                    VALUES (%s,%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"""
        val = (LevelID, self._create_rid(id= LevelID, user=True),Uname, Passcode, fname, lname,sex,phono, email,pos, Dhired, Bdate,address)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
    def reg_prod_protocol(self,Pname, Sprice, Utype , Ctype ,desc = None):
        sql =""" INSERT INTO products (RPID, ProductName, SellingPrice, Description, UnitTypeID, CategoryID)
                    VALUES (%s, %s, %s,%s ,%s,%s)"""
        val = (self._create_rid(id=Ctype,prod=True),Pname, Sprice,desc, Utype, Ctype )
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
    def update_user_protocol(self,UID, NewUlist):
        print('dbcont')
        sql = """
        UPDATE accounts
        SET LevelID = %s, RUID = %s, Uname = %s, Fname = %s, Lname = %s, SexID = %s, Phono = %s, Email = %s, Position = %s, HireDate = %s, Birthdate = %s, Address = %s
        WHERE UID = %s;
        """
        self.mycursor.execute(sql,NewUlist + UID)
        print('execute')
        self.mydb.commit()
        
        print(self.get_all_names())
        
    def update_prod_protocol(self,RPID, NewPlist ):
        
        print(NewPlist)
        print(RPID)
        # update sql about product id
        
        sql ="""
        UPDATE products
        SET ProductID = %s, ProductName = %s, SellingPrice = %s, Description = %s, UnitTypeID = %s, CategoryID = %s
        WHERE ProductID = %s;
        """
        self.mycursor.execute(sql,NewPlist + RPID)
        self.mydb.commit()
        
    def _create_rid(self, id ,typeID ,prod = None, user = None, new = None):
        
        if user != None:
            if typeID == 0:
                typeID = 'AD'
            else:
                typeID = 'EMP'
            id = str(id).zfill(3)
        elif prod != None:
            typeID = str(typeID).zfill(2)
            id = str(id).zfill(4)
            
        if new: 
            sql = ''
            
            self.mycursor.execute(sql)
            nextid = self.mycursor.fetchone()[0]
            unit_id = typeID + '-' + nextid
            return unit_id
        else:
            unit_id = typeID + '-' + id
            return unit_id
        
        
    def log_out(self):
        self.UMana.reset_UserMana()  
        
        

    def update_user_passcode(self,Uname, NewPcode):
        sql = """
        UPDATE accounts
        SET Passcode = %s
        WHERE Uname = %s;
        """    
        self.mycursor.execute(sql, (NewPcode, Uname))
        self.mydb.commit()


    def update_prod_protocol(self,oldPlist, NewPlist):
        
        print(NewPlist)
        print(oldPlist)
        
        sql ="""
        UPDATE products
        SET ProductName = %s, SellingPrice = %s, Description = %s, QuantityTypeID = %s, ProductTypeID = %s
        WHERE ProductName = %s AND ProductID = %s;
        """
        self.mycursor.execute(sql, (NewPlist + oldPlist))
        self.mydb.commit()
        
        pass
    
    def fetch_old_passcode_from_db(self, uname):
        # Implement your logic to fetch old passcode from database based on uname
        sql = """
        SELECT Passcode
        FROM accounts
        WHERE Uname = %s;
        """
        self.mycursor.execute(sql, (uname,))
        result = self.mycursor.fetchone()
        if result:
            return result[0]  # Return the passcode
        else:
            return None  # Handle case where user is not found or passcode is not retrieved
        
if __name__ == '__main__':
    db =dbcont('admin', 123456)
    
    print(db._create_rid(id= 5,typeID=1,prod=True))
    
    pass