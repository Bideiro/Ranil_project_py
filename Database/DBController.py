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
            sql = " SELECT UID, RUID, Uname, Passcode, LevelID FROM accounts WHERE Uname = %s AND passcode = %s"
            val = (self.user, self.passwd)
            self.mycursor.execute(sql,val)
            curruser = self.mycursor.fetchone()
            self.User.set_user(UID= curruser[0], RUID= curruser[1],User= curruser[2], Pass=curruser[3],Level= curruser[4])
            self.log_login()
        return bool(res)
    
    def Restore_sql(self, backup_file):
        with open(backup_file, "r") as f:
            sql_commands = f.read().split(";\n")

        for command in sql_commands:
            if command.strip():
                self.mycursor.execute(command)
                self.mydb.commit()
                
    def Backup_sql(self):
        self.mycursor.execute("SHOW TABLES")
        return self.mycursor.fetchall()
    
    def log_login(self):
        
        sql = "SELECT NOW() "
        self.mycursor.execute(sql)
        currdate = self.mycursor.fetchone()[0]
        
        sql = """
            INSERT INTO logs (UserID, UserLevel, User , Activity , DateTime)
            VALUES (%s,%s,%s,%s,%s)
        """
        
        val = (self.User.RUID, self.get_levels(id =self.User.Level), self.User.User, 'Logged in', currdate)
        self.mycursor.execute(sql,val)
        self.mydb.commit()

    def log_logout(self):
            
            sql = "SELECT NOW() "
            self.mycursor.execute(sql)
            currdate = self.mycursor.fetchone()[0]
            
            sql = """
                INSERT INTO logs (UserID, UserLevel, User , Activity , DateTime)
                VALUES (%s,%s,%s,%s,%s)
            """ 
            
            val = (self.User.RUID, self.get_levels(id =self.User.Level), self.User.User, 'Logged Out', currdate)
            self.mycursor.execute(sql,val)
            self.mydb.commit()
    # Getting data from Tables
    
    def get_logs(self):
        
        sql = """
            SELECT UserID, UserLevel, User, Activity, DateTime FROM logs
        """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
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
        
    def get_payment_type(self,value=None, id=None, all=None):
        if value != None:
            sql = """
                SELECT PaymentTypeID FROM payment_type WHERE PaymentType = %s
            """
            self.mycursor.execute(sql, (value,))
            return self.mycursor.fetchone()[0]
        elif id != None:
            sql = """
                SELECT PaymentType FROM payment_type WHERE PaymentTypeID = %s
            """
            print(id)
            self.mycursor.execute(sql, (id,))
            return self.mycursor.fetchone()[0]
        elif all != None:
            sql = """
                SELECT PaymentType FROM payment_type ORDER BY PaymentTypeID
            """
            self.mycursor.execute(sql)
            listed = [row[0] for row in self.mycursor]
            return listed
        else:
            print('No Arguements! (Get payment Type)')
        
        
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
        
        
    # Registration
    
    def add_cate(self, cate):
        
        sql =""" INSERT INTO category (Category) VALUES (%s)"""
        self.mycursor.execute(sql,(cate,))
        self.mydb.commit()
        
    def add_unittype(self, unit):
        
        sql =""" INSERT INTO unit_type (UnitType) VALUES (%s)"""
        self.mycursor.execute(sql,(unit,))
        self.mydb.commit()
    
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
        
        
    # Transaction
    def get_prod_search(self, searchcate= None, searchstr=None, all= None):
        if all != None:
            sql = """
                SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products
            """
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        elif searchcate != -1 and searchstr == None:
            sql = """
                SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products WHERE CategoryID = %s
            """
            self.mycursor.execute(sql,(searchcate,))
            return self.mycursor.fetchall()
        elif searchstr != '' and searchcate != -1:
            sql = """
                SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products 
                    WHERE (RPID LIKE %s
                        OR ProductName LIKE %s
                        OR SellingPrice LIKE %s
                        OR ExpirationDate LIKE %s
                        OR TotalStock LIKE %s)
                    AND CategoryID = %s
            """
            searchstr = '%' + searchstr + '%'
            self.mycursor.execute(sql,(searchstr,searchstr,searchstr,searchstr,searchstr,searchcate))
            return self.mycursor.fetchall()
        elif searchstr != '' and searchcate == -1:
            sql = """
                SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products 
                    WHERE RPID LIKE %s
                    OR ProductName LIKE %s
                    OR SellingPrice LIKE %s
                    OR ExpirationDate LIKE %s
                    OR TotalStock LIKE %s 
            """
            searchstr = '%' + searchstr + '%'
            self.mycursor.execute(sql,(searchstr,searchstr,searchstr,searchstr,searchstr))
            return self.mycursor.fetchall()
        else:
            print('fok')
        
    def prod_price(self, id):
        sql = """
                    SELECT SellingPrice FROM products
                    WHERE RPID = %s
                    """
        self.mycursor.execute(sql,(id,))
        return self.mycursor.fetchone()[0]
    
    def add_sold_protocol(self,Price, PPrice, SoldProductsList, Ptype, GCashRef = None):
        print('helo')
        # Getting todays Date
        sql = "SELECT NOW() "
        self.mycursor.execute(sql)
        currdate = self.mycursor.fetchone()[0]
        # inserting into Transaction_receipts
        sql = """
            INSERT INTO transaction_receipts (RUID, Price, PaidPrice, PurchaseDate, GCashReference, PaymentTypeID)
            VALUES (%s,%s,%s,%s,%s,%s)
        """
        val = (self.User.RUID ,Price,PPrice, currdate, GCashRef,Ptype)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        ID = self.mycursor.lastrowid
        str(ID).zfill(5)
        
        receiptID = currdate.strftime('%y%m%d') + str(ID).zfill(5)
        
        sql = """
            UPDATE transaction_receipts SET TransactionReceiptID = %s 
            WHERE ID = %s
        """
        val = (receiptID, ID)
        self.mycursor.execute(sql, val)
        self.add_sold_products(SoldPlist= SoldProductsList, RID= receiptID,currdate=currdate)
        
    def add_sold_products(self, SoldPlist, RID, currdate):
        # [['00-0001', 'Royal Canin', '1']]
        
        # # getting selling price from product table
        sql1 = """
            SELECT SellingPrice FROM products WHERE RPID = %s
        """
        # setting new total stock from product table
        sql2 = """
            UPDATE products SET TotalStock = TotalStock - %s WHERE RPID = %s
        """
        # setting current stock from products_supplied table
        sql3 = """
            UPDATE products_supplied SET CurrentQuantity = CurrentQuantity - %s WHERE RPID = %s AND SupplierReceiptID = %s
        """
        sql4 = """
            INSERT INTO products_sold (ReceiptID, ProductID, Quantity, Price, Date)
            VALUES (%s,%s,%s,%s,%s)
        """

        for prod in SoldPlist:
            self.mycursor.execute(sql1, (prod[0],))
            price = self.mycursor.fetchone()[0]
            self.mycursor.execute(sql2, (prod[2], prod[0]))
            self.mycursor.execute(sql3, (int(prod[2]), prod[0], str(RID)))
            self.mycursor.execute(sql4, (RID, prod[0],prod[2], price, currdate))
            self.mydb.commit()
    
    # Getting Product Data( Inventory )
    def get_all_prod(self, inv = None , trans = None, records = None):
        if inv:
            sql = "SELECT RPID, ProductName, CategoryID, UnitTypeID, SellingPrice, ExpirationDate, TotalStock, Description FROM products"
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        else:
            sql = "SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products"
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()

    def search_prod(self, searchstr,id = None, inv = None, trans = None,receipt = None ):
        if inv:
            sql = """
                    SELECT RPID, ProductName, CategoryID, UnitTypeID, SellingPrice, ExpirationDate, TotalStock, Description FROM products
                    WHERE RPID LIKE %s
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
        
    # record
    def add_receipt(self,RefNo, TPrice ,ODate, DDate, Plist):
        
        sql = """INSERT INTO supplier_receipts (RUID, ReceiptRef, TotalPrice, OrderDate, DeliveryDate)
                VALUES (%s,%s,%s,%s,%s)"""
        val = (self.User.UID, RefNo, TPrice, ODate, DDate)
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
        
        sql = """INSERT INTO products_supplied (RPID, SupplierReceiptID, BoughtQuantity, CurrentQuantity, Date, CostPrice, ExpirationDate)
                VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        for prod in Plist:
            val = (prod[0], RefNo, prod[3], prod[3],DDate, prod[2],prod[4])
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            self.add_inven(prod[0],prod[3])
            self.set_dynamic_expdate(RPID= prod[0])
        
    def set_dynamic_expdate(self, RPID):
        
        sql = """
        SELECT
            ExpirationDate,
            ABS(DATEDIFF(ExpirationDate, NOW())) AS date_diff
        FROM
            products_supplied
        WHERE
            RPID = %s AND CurrentQuantity > 0
        ORDER BY
            date_diff
        LIMIT 1;
            """

        self.mycursor.execute(sql,(RPID,))
        latestEdate = self.mycursor.fetchone()[0]
        print('adding to products dydate')
        print(latestEdate)
        print(RPID)
        
        sql = """
            UPDATE products SET ExpirationDate = %s WHERE RPID = %s
        """
        self.mycursor.execute(sql, (latestEdate,RPID))
        self.mydb.commit()
        
    def update_user_protocol(self,UID, NewUlist):
        sql = """
        UPDATE accounts
        SET LevelID = %s, RUID = %s, Uname = %s, Fname = %s, Lname = %s, SexID = %s, Phono = %s, Email = %s, Position = %s, HireDate = %s, Birthdate = %s, Address = %s
        WHERE UID = %s;
        """
        self.mycursor.execute(sql,NewUlist + UID)
        self.mydb.commit()
        
    def update_prod_protocol(self,RPID, NewPlist ):
        
        sql ="""
        UPDATE products
        SET RPID = %s, ProductName = %s, SellingPrice = %s, Description = %s, UnitTypeID = %s, CategoryID = %s
        WHERE RPID = %s;
        """
        self.mycursor.execute(sql,NewPlist + RPID)
        self.mydb.commit()
        
    def _create_rid(self, typeID = None , id = None, date= None,RID = None,prod = None, user = None, receipt = None, new = None):
        
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
            
        elif receipt != None:
            
            
            
            pass
            
        if new: 
            if prod:
                sql = "SELECT COUNT(*) FROM products"
                self.mycursor.execute(sql)
                nextid =int(self.mycursor.fetchone()[0]) + 1
                print(nextid)
                unit_id = typeID + '-' + str(nextid).zfill(4)
                return unit_id
            elif user:
                sql = "SELECT COUNT(*) FROM accounts;"
                self.mycursor.execute(sql)
                nextid =int(self.mycursor.fetchone()[0]) + 1
                unit_id = typeID + '-' + str(nextid).zfill(3)
                return unit_id
            elif receipt:
                
                pass
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
                return True
            else:
                return False
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
        sql = "SELECT PurchaseDate, TransactionReceiptID, RUID, Price, PaidPrice, GCashReference, PaymentTypeID FROM transaction_receipts"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    # PNEINDG FICX
    
    def search_sales(self, searchstr):
        sql = """
                SELECT PurchaseDate, TransactionReceiptID, RUID, Price, PaidPrice, GCashReference, PaymentTypeID FROM transaction_receipts
                WHERE PurchaseDate LIKE %s OR
                TransactionReceiptID LIKE %s OR 
                RUID LIKE %s OR
                Price LIKE %s OR
                PaidPrice LIKE %s OR
                GCashReference LIKE %s OR
                PaymentTypeID LIKE %s
                """
        searchstr = '%' + searchstr + '%'
        
        # if searchstr == 'cash':
        #     PTID = 0
        # elif searchstr == 0:
        #     PTID == 
        
        val = (searchstr,searchstr,searchstr,searchstr,searchstr,searchstr, searchstr)
        self.mycursor.execute(sql,val)
        return self.mycursor.fetchall()
    
    def set_yearly_sales(self):
        sql = """
                SELECT 
                    YEAR(PurchaseDate) AS Year,
                    SUM(Price) AS TotalSum
                FROM 
                    transaction_receipts
                GROUP BY 
                    YEAR(PurchaseDate)
                ORDER BY 
                    Year;
                """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def get_years(self):
        sql = """
                SELECT DISTINCT YEAR(PurchaseDate) as Year FROM transaction_receipts ORDER BY Year
                """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    
    # sales and reports
    def get_inventory(self):
        sql = """
                SELECT ReceiptID, ProductID, Quantity, Price FROM products_sold
                """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def search_inventory_rec(self, SDate, EDate = None):
        if EDate == None:
            sql = "SELECT ReceiptID, ProductID, Quantity, Price FROM products_sold WHERE Date = %s"
            self.mycursor.execute(sql, (SDate,))
        else:
            sql = "SELECT ReceiptID, ProductID, Quantity, Price FROM products_sold WHERE Date = BETWEEN %s AND %s"
            self.mycursor.execute(sql, (SDate,EDate))
        
        return self.mycursor.fetchall()
    
    # def get_transactions(self, start_date, end_date):
    #     sql = "SELECT PurchaseDate, Price FROM transaction_receipts WHERE PurchaseDate BETWEEN %s AND %s"
    #     self.mycursor.execute(sql, (start_date, end_date))
    

    def get_salesR(self):
        sql = """
                SELECT PurchaseDate, Price FROM Transaction_receipts
                """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def search_sales_rep(self, SDate, EDate = None):
        if EDate == None:
            sql = "SELECT PurchaseDate, Price FROM transaction_receipts WHERE PurchaseDate = %s"
            self.mycursor.execute(sql, (SDate,))
        else:
            sql = "SELECT PurchaseDate, Price FROM transaction_receipts WHERE PurchaseDate BETWEEN %s AND %s"
            self.mycursor.execute(sql, (SDate,EDate))
        
        return self.mycursor.fetchall()
    
    # idunno wher but needs
    

    def get_algo_data(self):
        sql = "SELECT * FROM algoproddb"
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
if __name__ == '__main__':
    db =dbcont('admin', 123456)
    
    print(db._create_rid(id= 5,typeID=1,prod=True))
    
    pass