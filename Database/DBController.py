import mysql.connector
from Database.User_Manager import UserMana

# Due to time constraints this will be the most un optimized code. ever.
class dbcont(object):
    
    _instance = None
    User = UserMana()
    mydb = mysql.connector.connect(
            host="localhost",
            user= "root",
            passwd= "password",
            database="ranil_proj")
    
    mycursor = mydb.cursor()
    
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super(dbcont, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, user = None,passwd = None):
        if not hasattr(self,'initialized'):
            self.initialized = True
        self.user = user
        self.passwd = passwd
    
    def login(self):
        sql = " SELECT EXISTS (SELECT 1 FROM accounts WHERE BINARY Uname = %s AND BINARY passcode = %s) AS is_found"
        val = (self.user, self.passwd)
        self.mycursor.execute(sql,val)
        res = self.mycursor.fetchone()[0]
        
        if bool(res):
            sql = " SELECT UID, Uname, Passcode, LevelID FROM accounts WHERE Uname = %s AND passcode = %s"
            val = (self.user, self.passwd)
            self.mycursor.execute(sql,val)
            curruser = self.mycursor.fetchone()
            self.User.set_user(UID= curruser[0],User= curruser[1], Pass=curruser[2],Level= curruser[3])
        return bool(res)
    
    # Getting data from Tables
    
    def get_cate(self, value= None, id=None,all = None):
        if value != None:
            sql = """
                SELECT CategoryID FROM category WHERE Category = %s
            """
            self.mycursor.execute(sql, (value,))
            return self.mycursor.fetchone()[0]
        elif id != None:
            sql = """
                SELECT category FROM category WHERE CategoryID = %s
            """
            self.mycursor.execute(sql, (id,))
            return self.mycursor.fetchone()[0]
        elif all != None:
            sql = """
                SELECT Category FROM Category ORDER BY CategoryID
            """
            self.mycursor.execute(sql)
            listed = [row[0] for row in self.mycursor]
            return listed
        else:
            print('No Arguements! (Get Cate)')
            
    def get_levels(self, value= None, id= None, all= None):
        if value != None:
            sql = """
                SELECT LevelID FROM levels WHERE Level = %s
            """
            self.mycursor.execute(sql, (value,))
            return self.mycursor.fetchone()[0]
        elif id != None:
            sql = """
                SELECT Level FROM levels WHERE LevelID = %s
            """
            self.mycursor.execute(sql, (id,))
            return self.mycursor.fetchone()[0]
        elif all != None:
            sql = """
                SELECT Level FROM levels ORDER BY LevelID
            """
            self.mycursor.execute(sql)
            listed = [row[0] for row in self.mycursor]
            return listed
        else:
            print('No Arguements! (Get levels)')
            
    def get_sex(self,value= None,id=None, all=None):
        if value != None:
            sql = """
                SELECT SexID FROM sex WHERE Sex = %s
            """
            self.mycursor.execute(sql, (value,))
            return self.mycursor.fetchone()[0]
        elif id != None:
            sql = """
                SELECT Sex FROM sex WHERE SexID = %s
            """
            self.mycursor.execute(sql, (id,))
            return self.mycursor.fetchone()[0]
        elif all != None:
            sql = """
                SELECT Sex FROM sex ORDER BY SexID
            """
            self.mycursor.execute(sql)
            listed = [row[0] for row in self.mycursor]
            return listed
        else:
            print('No Arguements! (Get sex)')
        
    def get_unittype(self,value=None, id=None, all=None):
        if value != None:
            sql = """
                SELECT UnitTypeID FROM unit_type WHERE UnitType = %s
            """
            self.mycursor.execute(sql, (value,))
            return self.mycursor.fetchone()[0]
        elif id != None:
            sql = """
                SELECT UnitType FROM unit_type WHERE UnitTypeID = %s
            """
            self.mycursor.execute(sql, (id,))
            return self.mycursor.fetchone()[0]
        elif all != None:
            sql = """
                SELECT UnitType FROM unit_type ORDER BY UnitTypeID
            """
            self.mycursor.execute(sql)
            listed = [row[0] for row in self.mycursor]
            return listed
        else:
            print('No Arguements! (Get Unit Type)')
        
    # Getting User Data
    def get_user_creds(self, User = None, Passcode = None, colint = None, Fname = None , Lname = None):
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
        
    # Getting Product Data
    def get_all_prod(self, inv = None , trans = None):
        
        if inv:
            sql = "SELECT RPID, ProductName,SellingPrice, TotalStock, ExpirationDate, Description, UnitTypeID, CategoryID FROM products"
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        else:
            sql = "SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products"
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        
    def prod_price(self, id):
        sql = """
                    SELECT SellingPrice FROM products
                    WHERE RPID LIKE %s
                    """
        self.mycursor.execute(sql,(id,))
        return self.mycursor.fetchone()[0]

    def search_prod(self, searchstr,id = None, inv = None, trans = None,receipt = None ):
        
        if inv:
            sql = """
                    SELECT ProductID, ProductName, SellingPrice, TotalStock, ExpirationDate, Description, UnitTypeID, CategoryID FROM products
                    WHERE ProductID LIKE %s
                    OR ProductName LIKE %s
                    OR SellingPrice LIKE %s
                    OR ExpirationDate LIKE %s
                    OR TotalStock LIKE %s
                    """
            searchstr = '%' + searchstr + '%'
            val = (searchstr,searchstr,searchstr,searchstr,searchstr)
            self.mycursor.execute(sql,val)
            return self.mycursor.fetchall()
        elif trans:
            sql = """
                    SELECT ProductID, ProductName, SellingPrice, TotalStock, ExpirationDate FROM products
                    WHERE ProductID LIKE %s
                    OR ProductName LIKE %s
                    OR SellingPrice LIKE %s
                    OR ExpirationDate LIKE %s
                    OR TotalStock LIKE %s
                    """
            searchstr = '%' + searchstr + '%'
            val = (searchstr,searchstr,searchstr,searchstr,searchstr)
            self.mycursor.execute(sql,val)
            return self.mycursor.fetchall()
        elif id:
            sql = """
                    SELECT RPID, ProductName, SellingPrice, TotalStock, ExpirationDate FROM products
                    WHERE RPID LIKE %s
                    """
            self.mycursor.execute(sql,(searchstr,))
            return self.mycursor.fetchone()
        elif receipt:
            sql = """
                    SELECT RPID, ProductName FROM products
                    WHERE RPID LIKE %s
                    """
            self.mycursor.execute(sql,(searchstr,))
            return self.mycursor.fetchone()

        print("huh")
        return 0
        
    def reg_user_protocol(self, LevelID, Uname, Passcode, fname, lname, sex, phono, email, Dhired, Bdate, address,  pos = None):
        sql =""" INSERT INTO accounts (LevelID, RUID, Uname, Passcode, Fname, Lname, SexID, Phono, Email, Position, HireDate, Birthdate, Address) 
                    VALUES (%s,%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"""
        val = (LevelID, self._create_rid(id= LevelID, user=True, new=True),Uname, Passcode, fname, lname,sex,phono, email,pos, Dhired, Bdate,address)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
    def reg_prod_protocol(self,Pname, Sprice, Utype , Ctype ,desc = None):
        sql =""" INSERT INTO products (RPID, ProductName, SellingPrice, Description, TotalStock,UnitTypeID, CategoryID)
                    VALUES (%s, %s, %s,%s ,%s,%s,%s)"""
        val = (self._create_rid(typeID=Ctype,prod=True,new=True),Pname, Sprice,desc, 0,Utype, Ctype )
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
    def add_receipt(self,RefNo, TPrice ,ODate, DDate, PType, Plist, GCashRef = None):
        
        sql = """INSERT INTO supplier_receipts (User, ReceiptRef, TotalPrice, PaymentTypeID, OrderDate, DeliveryDate, GCashRef)
                VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        val = ('dei', RefNo, TPrice, PType, ODate, DDate, GCashRef)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
        self.add_supplied_products(RefNo= RefNo, DDate= DDate, Plist= Plist)
        
    def add_inven(self, RPID, Quantity):
        
        sql ="""SELECT TotalStock FROM products
                WHERE RPID = %s
            """
        self.mycursor.execute(sql,(RPID,))
        
        passtock = self.mycursor.fetchone()[0]
        newstock = int(passtock) + int(Quantity)
        sql = """
                UPDATE products SET TotalStock = %s
                WHERE RPID = %s
            """
        self.mycursor.execute(sql,(newstock,RPID))
        self.mydb.commit()
        
        sql ="""SELECT * FROM products"""
        self.mycursor.execute(sql)
        print(self.mycursor.fetchall())
        
    def add_supplied_products(self,RefNo,DDate, Plist):
        
        sql = """INSERT INTO products_supplied (ProductID, SupplierReceiptID, Quantity, StartingQuantity, Date, CostPrice)
                VALUES (%s,%s,%s,%s,%s,%s)"""
        for prod in Plist:
            val = (prod[0], RefNo, prod[3], prod[3],DDate, prod[2])
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            self.add_inven(prod[0],prod[3])
        
    def update_user_protocol(self,UID, NewUlist):
        sql = """
        UPDATE accounts
        SET LevelID = %s, RUID = %s, Uname = %s, Fname = %s, Lname = %s, SexID = %s, Phono = %s, Email = %s, Position = %s, HireDate = %s, Birthdate = %s, Address = %s
        WHERE UID = %s;
        """
        self.mycursor.execute(sql,NewUlist + UID)
        self.mydb.commit()

    def add_sold_receipt(self,Price, PPrice, SoldProductsList, GCashRef = None):
        sql = "SELECT NOW() "
        self.mycursor.execute(sql)
        currdate = self.mycursor.fetchone()[0]
        
        sql = """
            INSERT INTO receipts (UID, Price, PaidPrice, PurchaseDate, GCashReference )
            VALUES (%s,%s,%s,%s,%s)
        """
        val = (self.User.UID, Price,PPrice, currdate, GCashRef)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
        sql = """
        SELECT ID FROM receipts 
        WHERE UID = %s AND
        Price = %s AND 
        PaidPrice = %s AND 
        PurchaseDate = %s 
        """
        val = (self.User.UID, Price,PPrice, currdate)
        self.mycursor.execute(sql,val)
        try:
            receiptID = self.mycursor.fetchone()[0]
            print(receiptID)
        except:
            print('rID')
            print(receiptID)
        self.add_sold_products(SoldPlist= SoldProductsList, RID= receiptID,currdate=currdate)
        
    def add_sold_products(self, SoldPlist, RID, currdate):
        
        
        sql1 = """
            SELECT TotalStock, SellingPrice FROM products WHERE RPID = %s
        """
        
        sql2 = """
            UPDATE products SET TotalStock = %s WHERE RPID = %s
        """
        sql3 = """INSERT INTO products_sold (ProductID, ReceiptID, Quantity, Price,Date)
                VALUES (%s,%s,%s,%s,%s)"""
                
        for prod in SoldPlist:
            self.mycursor.execute(sql1, (prod[0],))
            currprod = list(self.mycursor.fetchone())
            print('curr')
            print(currprod)
            currprod[0] = currprod[0] - int(prod[2]) 
            self.mycursor.execute(sql2, (currprod[0],prod[0]))
            self.mycursor.execute(sql3, (prod[0],RID, prod[2], currprod[1], currdate))
            self.mydb.commit()
        
    def update_prod_protocol(self,RPID, NewPlist ):
        
        sql ="""
        UPDATE products
        SET RPID = %s, ProductName = %s, SellingPrice = %s, Description = %s, UnitTypeID = %s, CategoryID = %s
        WHERE RPID = %s;
        """
        self.mycursor.execute(sql,NewPlist + RPID)
        self.mydb.commit()
        
    def _create_rid(self, typeID = None , id = None ,RID = None,prod = None, user = None, new = None):
        
        if RID != None:
            if user != None:
                sql = 'Select UID FROM accounts WHERE RUID = %s'
            elif prod != None:
                sql = 'Select ProductID FROM products WHERE RPID = %s'
            self.mycursor.execute(sql ,(RID,))
            id = self.mycursor.fetchone()[0]
        
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
            if prod:
                sql = "SELECT COUNT(*) FROM products"
                self.mycursor.execute(sql)
                nextid =int(self.mycursor.fetchone()[0]) + 1
                print(nextid)
                unit_id = typeID + '-' + str(nextid).zfill(4)
                return unit_id
            else:
                sql = "SELECT COUNT(*) FROM accounts;"
                self.mycursor.execute(sql)
                nextid =int(self.mycursor.fetchone()[0]) + 1
                unit_id = typeID + '-' + str(nextid).zfill(3)
                return unit_id
        else:
            unit_id = typeID + '-' + id
            return unit_id
    
    def get_RUID_user(self, uname ,email,check = None):
        if check:
            sql = """
            SELECT RUID
            FROM accounts
            WHERE Uname = %s AND Email = %s;
            """
            self.mycursor.execute(sql, (uname,email))
            result = self.mycursor.fetchone()
            if result:
                return True # Return the passcode
            else:
                return False  # Handle case where user is not found or passcode is not retrieved
        else:
            sql = """
            SELECT RUID
            FROM accounts
            WHERE Uname = %s AND Email = %s;
            """
            self.mycursor.execute(sql, (uname,email))
            return self.mycursor.fetchone()[0]
        
    def update_passcode(self,RUID, passcode):
        sql = """
        UPDATE accounts
        SET Passcode = %s
        WHERE RUID = %s;
        """
        self.mycursor.execute(sql, (passcode,RUID))
        self.mydb.commit()

    # temp
    def get_all_supp_receipts(self):
        
        sql = """
            SELECT * FROM supplier_receipts
        """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
            
    # sales db
        
    def get_all_sales(self):
        
        sql = "SELECT * FROM sales"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def search_sales(self, searchstr):
        sql = """
                SELECT DateTime, User, Total, ReferenceNo FROM sales
                WHERE DateTime LIKE %s
                OR User LIKE %s
                OR Total LIKE %s
                OR ReferenceNo LIKE %s
                """
        searchstr = '%' + searchstr + '%'
        val = (searchstr,searchstr,searchstr,searchstr)
        self.mycursor.execute(sql,val)
        return self.mycursor.fetchall()
    
    def set_yearly_sales(self):
        sql = """
                SELECT 
                    YEAR(DateTime) AS Year,
                    SUM(Total) AS TotalSum
                FROM 
                    ranil_proj.sales
                GROUP BY 
                    YEAR(DateTime)
                ORDER BY 
                    Year;
                """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def get_years(self):
        sql = """
                SELECT DISTINCT YEAR(DateTime) as Year FROM sales ORDER BY Year
                """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    
    # User log functions
    
    
if __name__ == '__main__':
    db =dbcont('admin', 123456)
    
    print(db._create_rid(id= 5,typeID=1,prod=True))
    
    pass