
from cgi import print_arguments
from math import pi
import sys
import re
from unittest import result
import mysql.connector
from mysql.connector import errorcode
from numpy import record, rint
from Database.User_Manager import UserMana
import hashlib

# Due to time constraints this will be the most un optimized code. ever.
# Adjusting to make it runaable while can add additional columns regardless of column order ( not using SELECT *)

# changing colum arrangement will affect the following modules:
# User Information(showing of info)
# User Information(edit dialog and its update db func)

class dbcont(object):
    _instance = None
    mydb = None
    mycursor = None
    uname = None
    passwd = None
    User = UserMana()
    
        # elif err.errno == errorcode.ER_BAD_DB_ERROR:
        #     print("Error: The specified database does not exist.")
        # elif err.errno == errorcode.ER_NO_SUCH_TABLE:
        #     print("Error: The specified table does not exist.")
        # elif err.errno == errorcode.ER_DUP_ENTRY:
        #     print("Error: Duplicate entry.")
        # elif err.errno == errorcode.ER_PARSE_ERROR:
        #     print("Error: SQL syntax error.")
        # elif err.errno == errorcode.ER_WRONG_DB_NAME:
        #     print("Error: Incorrect database name.")
        # elif err.errno == errorcode.ER_BAD_FIELD_ERROR:
        #     print("Error: Unknown column in field list.")
        # else:
        #     print(f"Error: {err}")
    
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super(dbcont, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self,'initialized'):
            self.initialized = True
        try:
            self.mydb = mysql.connector.connect(
                    host="localhost",
                    user= "root",
                    passwd= "password",
                    database="ranil_proj")
            self.mycursor = self.mydb.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.CR_CONN_HOST_ERROR:
                print('Database is not running!')
                sys.exit()
    
    def login(self, User, passwd):
        self.uname = User
        self.passwd = passwd
        sql = " SELECT EXISTS (SELECT 1 FROM accounts WHERE (BINARY Uname = %s AND BINARY passcode = %s) AND (Status = 1 OR Status = 3)) AS is_found"
        val = (self.uname, hashlib.sha256(self.passwd.encode()).hexdigest() )
        self.mycursor.execute(sql,val)
        res = self.mycursor.fetchone()[0]
        
        if bool(res):
            sql = " SELECT UID, RUID, Uname, Passcode, LevelID FROM accounts WHERE Uname = %s AND passcode = %s"
            val = (self.uname, hashlib.sha256(self.passwd.encode()).hexdigest() )
            self.mycursor.execute(sql,val)
            curruser = self.mycursor.fetchone()
            
            
            
            sql=" SELECT * FROM accounts WHERE RUID = %s"
            self.mycursor.execute(sql,(curruser[1],))
            result = self.mycursor.fetchone()
            if result[8] != 0:
                suffix = self.get_suffix(id= result[8])
            else:
                suffix = ''
            if result[7] == None or result[7] == '':
                whole_name = str(result[5]) + ' ' + str(result[6]) + ' ' + str(suffix)
            else:
                whole_name = str(result[5]) + ' ' + str(result[7]) + ' ' + str(result[6]) + ' ' + str(suffix)
            
            self.User.set_user(UID= curruser[0], RUID= curruser[1],User= curruser[2], Pass=curruser[3],Level= curruser[4] ,Wname= whole_name)
            self.log_action(action='Logged In')
        return bool(res)
    
    def Restore_sql(self, backup_file):
        with open(backup_file, "r") as f:
            sql_commands = f.read().split(";\n")

        for command in sql_commands:
            if command.strip():
                self.mycursor.execute(command)
                self.mydb.commit()
    
    def log_action(self, action):
        
        sql = "SELECT NOW() "
        self.mycursor.execute(sql)
        currdate = self.mycursor.fetchone()[0]
        
        sql = """
            INSERT INTO logs (UserID, UserLevel, User , Activity , DateTime)
            VALUES (%s,%s,%s,%s,%s)
        """
        
        val = (self.User.RUID, self.get_levels(id =self.User.Level), self.User.User, action, currdate)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
    
    # RID CREATOR
    # none for rid
    def _create_rid(self, typeID = None , id = None, date= None,RID = None,prod = None, user = None, receipt = None, new = None):
        
        if RID != None:
            if user != None:
                sql = 'Select UID FROM accounts WHERE RUID = %s'
            elif prod != None:
                sql = 'Select ProductID FROM products WHERE RPID = %s'
            self.mycursor.execute(sql ,(RID,))
            id = self.mycursor.fetchone()[0]
        
        if user != None:
            if typeID == 0 or typeID == '0':
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
    
    # Getting data from Tables
    
    def get_logs(self):
        
        sql = """
            SELECT UserID, UserLevel, User, Activity, DateTime FROM logs
            ORDER BY DateTime DESC
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
    
    def get_suffix(self,value=None, id=None, all=None):
        if value != None:
            sql = """
                SELECT SuffixID FROM suffix WHERE Suffix = %s
            """
            self.mycursor.execute(sql, (value,))
            return self.mycursor.fetchone()[0]
        elif id != None:
            sql = """
                SELECT Suffix FROM suffix WHERE SuffixID = %s
            """
            self.mycursor.execute(sql, (id,))
            return self.mycursor.fetchone()[0]
        elif all != None:
            sql = """
                SELECT Suffix FROM suffix ORDER BY SuffixID
            """
            self.mycursor.execute(sql)
            listed = [row[0] for row in self.mycursor]
            return listed
        else:
            print('No Arguements! (Get suffix)')
    
    # Adding data to tables
    
    def add_cate(self, cate):
        
        sql =""" INSERT INTO category (Category) VALUES (%s)"""
        self.mycursor.execute(sql,(cate,))
        self.mydb.commit()
        
    def add_unittype(self, unit):
        
        sql =""" INSERT INTO unit_type (UnitType) VALUES (%s)"""
        self.mycursor.execute(sql,(unit,))
        self.mydb.commit()
    
    # verifying things Checking availability
    
    def verify_username(self, uname):
        
        sql = """
            SELECT 1 WHERE EXISTS (SELECT 1 FROM accounts WHERE Uname = %s)
        """
        self.mycursor.execute(sql, (uname,))
        return bool(self.mycursor.fetchone()[0])
    
    # User Data Manipulation
    # Getting User Data
    
    def get_RUID_user(self, uname ,email,check = None):
        if check:
            sql = """
            SELECT RUID
            FROM accounts
            WHERE BINARY Uname = %s AND Email = %s;
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
    
    def get_all_users(self):
        self.mycursor.execute("SELECT * FROM accounts")
        return self.mycursor.fetchall()

    def get_user_creds(self, User = None, Passcode = None, RUID = None, colint = None):
        if User != None and Passcode != None:
            sql = 'SELECT * FROM accounts'
            self.mycursor.execute(sql)
        elif RUID != None:
            sql = 'Select * FROM accounts WHERE RUID = %s'
            self.mycursor.execute(sql,(RUID,))
            
        else:
            sql = 'Select * FROM accounts WHERE Uname = %s AND Passcode = %s'
            val = (User,Passcode)
            self.mycursor.execute(sql,val)
            
        if colint == None:
            print('NO COL NUM SELECTED! Fetching all columns!')
            return self.mycursor.fetchall()[0]
        else:
            return self.mycursor.fetchone()[colint][0]
    
    def access_status_user(self, RUID, status = None):
        if status == None:
            sql = "SELECT Status FROM accounts WHERE RUID = %s"
            self.mycursor.execute(sql, (RUID,))
            return self.mycursor.fetchone()[0]
        else:
            sql = "UPDATE accounts SET Status = %s WHERE RUID = %s"
            self.mycursor.execute(sql, (status, RUID))
            self.mydb.commit()
    
    # Modifying Data
    def update_passcode(self,RUID, passcode):
        hashedPass = hashlib.sha256(passcode.encode()).hexdigest() 
        
        sql = """
        UPDATE accounts
        SET Passcode = %s
        WHERE RUID = %s;
        """
        self.mycursor.execute(sql, (hashedPass,RUID))
        self.mydb.commit()

    def reg_user_protocol(self, LevelID, Uname, Passcode, fname, lname, mname, sex, phono, email, Dhired, Bdate, address,  pos = None, suffix = None):
        hashedPass = hashlib.sha256(Passcode.encode()).hexdigest() 
        
        sql =""" INSERT INTO accounts (LevelID, RUID, Uname, Passcode, Fname, Lname, Mname, SuffixID, SexID, Phono, Email, Position, HireDate, Birthdate, Address) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (LevelID, self._create_rid(typeID= LevelID, user=True, new=True), Uname, hashedPass, fname, lname, mname, suffix, 
            sex, phono, email, pos, Dhired, Bdate, address)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
    
    def update_user_protocol(self,UID, NewUlist):
        print(NewUlist)
        if NewUlist[14] != '':
            hashedPasscode = hashlib.sha256(NewUlist[14].encode()).hexdigest()
            
            print(NewUlist)
            
            NewUlist = [hashedPasscode if x == NewUlist[14] else x for x in NewUlist]
            
            print(NewUlist)
            sql = """
            UPDATE accounts
            SET LevelID = %s, RUID = %s, Uname = %s, Fname = %s, Lname = %s, Mname = %s, SuffixID = %s, SexID = %s, Phono = %s, Email = %s, Position = %s, HireDate = %s, Birthdate = %s, Address = %s ,Passcode = %s
            WHERE UID = %s;
            """
        else:
            if NewUlist[5] == '':
                occurrence_count = 0
                for i in range(len(NewUlist)):
                    if NewUlist[i] == NewUlist[14]:
                        occurrence_count += 1
                        if occurrence_count == 2:
                            del NewUlist[i]
                            break
            else:
                NewUlist.remove(NewUlist[14])
            sql = """
            UPDATE accounts
            SET LevelID = %s, RUID = %s, Uname = %s, Fname = %s, Lname = %s, Mname = %s, SuffixID = %s, SexID = %s, Phono = %s, Email = %s, Position = %s, HireDate = %s, Birthdate = %s, Address = %s 
            WHERE UID = %s;
            """
            
        self.mycursor.execute(sql,NewUlist + UID)
        self.mydb.commit()
    
    # Product Data Manipulation
    # Get Product Data
    def search_prod(self, searchstr,id = None, inv = None, trans = None,receipt = None):
        if inv:
            sql = """
                    SELECT RPID, ProductName, CategoryID, UnitTypeID, SellingPrice, ExpirationDate, TotalStock, Description, Active FROM products
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
                    WHERE (ProductID LIKE %s
                    OR ProductName LIKE %s
                    OR SellingPrice LIKE %s
                    OR ExpirationDate LIKE %s
                    OR TotalStock LIKE %s)
                    AND Active = 1
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
        return 0
    
    def access_status_prod(self, RPID, status = None ):
        if status == None:
            sql = "SELECT Active FROM products WHERE RPID = %s"
            self.mycursor.execute(sql, (RPID,))
            return self.mycursor.fetchone()[0]
        else:
            sql = "UPDATE products SET Active = %s WHERE RPID = %s"
            self.mycursor.execute(sql, (status, RPID))
            self.mydb.commit()
    
    def get_all_prod(self, inv = None , trans = None, records = None):
        
        if inv:
            sql = "SELECT RPID, ProductName, CategoryID, UnitTypeID, SellingPrice, ExpirationDate, TotalStock, Description, Active FROM products "
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        elif records:
            sql = "SELECT RPID, ProductName, CategoryID, UnitTypeID, SellingPrice, ExpirationDate, TotalStock, Description, Active FROM products WHERE Active = '1'"
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        else:
            sql = "SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products WHERE Active = 1"
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        
    def get_prod_search(self, searchcate= None, searchstr=None, all= None):
        if all != None:
            sql = """
                SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products WHERE Active = 1
            """
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        elif searchcate != -1 and searchstr == None:
            sql = """
                SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products WHERE CategoryID = %s AND Active = 1
            """
            self.mycursor.execute(sql,(searchcate,))
            return self.mycursor.fetchall()
        elif searchstr != '' and searchcate != -1:
            # Search all products with category
            sql = """
                SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products 
                    WHERE (RPID LIKE %s
                        OR ProductName LIKE %s
                        OR SellingPrice LIKE %s
                        OR ExpirationDate LIKE %s
                        OR TotalStock LIKE %s)
                    AND CategoryID = %s
                    AND Active = 1
            """
            searchstr = '%' + searchstr + '%'
            self.mycursor.execute(sql,(searchstr,searchstr,searchstr,searchstr,searchstr,searchcate))
            return self.mycursor.fetchall()
        elif searchstr != '' and searchcate == -1:
            # Search all products regardless of category
            sql = """
                SELECT RPID , ProductName, SellingPrice, TotalStock, ExpirationDate FROM products 
                    WHERE (RPID LIKE %s
                    OR ProductName LIKE %s
                    OR SellingPrice LIKE %s
                    OR ExpirationDate LIKE %s
                    OR TotalStock LIKE %s )
                    AND Active = 1
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

    # Modifying/Adding Product Data
    
    # debug print found
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
        
    def reg_prod_protocol(self,Pname, Sprice, Utype , Ctype ,desc = None):
        sql =""" INSERT INTO products (RPID, ProductName, SellingPrice, Description, TotalStock,UnitTypeID, CategoryID)
                    VALUES (%s, %s, %s,%s ,%s,%s,%s)"""
        val = (self._create_rid(typeID=Ctype,prod=True,new=True),Pname, Sprice,desc, 0,Utype, Ctype )
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
    def update_prod_protocol(self,RPID, NewPlist ):
        sql ="""
        UPDATE products
        SET RPID = %s, ProductName = %s, SellingPrice = %s, Description = %s, UnitTypeID = %s, CategoryID = %s
        WHERE RPID = %s;
        """
        self.mycursor.execute(sql,NewPlist + RPID)
        self.mydb.commit()
        
    # Receipt Manipulation
    # Getting Receipt Data
    
    def get_recent_receiptID(self):
        
        sql = """
        SELECT TransactionReceiptID FROM transaction_receipts ORDER BY ID DESC LIMIT 1;
        """
        self.mycursor.execute(sql)
        return self.mycursor.fetchone()[0]
    
    def get_sales_report(self, Sdate = None, Edate = None, search = None , daily = None, monthly = None, yearly = None):
        
        if daily != None:
            sql = """
                SELECT DATE(PurchaseDate), SUM(Price)
                FROM Transaction_receipts GROUP BY DATE(PurchaseDate) ORDER BY DATE(PurchaseDate) DESC
            """
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        elif monthly != None:
            sql = """
                SELECT DATE_FORMAT(PurchaseDate, '%Y-%m') AS YearMonth, SUM(Price) AS TotalPrice
                FROM transaction_receipts GROUP BY DATE_FORMAT(PurchaseDate, '%Y-%m')
                ORDER BY YearMonth DESC;
            """
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        elif yearly != None:
            sql = """
                SELECT YEAR(PurchaseDate), SUM(Price)
                FROM Transaction_receipts GROUP BY YEAR(PurchaseDate) ORDER BY YEAR(PurchaseDate) DESC
            """
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
        elif search != None:
            
            pass
        else:
            print('No parameter selected! [Sales Report]')
            sql = """
                SELECT PurchaseDate, Price FROM Transaction_receipts
            """
            self.mycursor.execute(sql)
            return self.mycursor.fetchall()
    
    def get_all_sales(self):
        # Sales Module(side button sales)
        sql = """
            SELECT PurchaseDate, TransactionReceiptID, RUID, Price, GCashReference, PaymentTypeID FROM transaction_receipts
            ORDER BY PurchaseDate DESC
        """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def get_all_trans_receipts(self):
        
        sql = """
            SELECT TransactionReceiptID, RUID, PurchaseDate, Price, PaidPrice, PaymentTypeID, GCashReference FROM transaction_receipts ORDER BY PurchaseDate DESC
        """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def get_all_supp_receipts(self):
        
        sql = """
            SELECT SupplierReceiptID, RUID, ReceiptRef, TotalPrice, OrderDate, DeliveryDate FROM supplier_receipts
        """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def search_trans_receipts(self, searchstr, trans = True):
        if trans:
            
            sql = """

                SELECT TransactionReceiptID, RUID, PurchaseDate, Price, PaidPrice, PaymentTypeID, GCashReference FROM transaction_receipts 
                WHERE TransactionReceiptID = %s
                
            """
            
            self.mycursor.execute(sql,(searchstr,))
            return self.mycursor.fetchone()
        
        else:
            sql = """
                SELECT TransactionReceiptID, RUID, PurchaseDate, Price, PaidPrice, PaymentTypeID FROM transaction_receipts 
                WHERE TransactionReceiptID LIKE %s
                        OR RUID  LIKE %s
                        OR PurchaseDate  LIKE %s
                        OR Price LIKE %s
                        OR PaidPrice LIKE %s
                        OR PaymentTypeID LIKE %s
                        OR GCashReference LIKE %s
            """
            
            searchstr = '%' + searchstr + '%'
            val = (searchstr,searchstr,searchstr,searchstr,searchstr,searchstr,searchstr)
            self.mycursor.execute(sql,val)
            return self.mycursor.fetchall()
    
    def search_sales(self, searchstr):
        sql = """
                SELECT PurchaseDate, TransactionReceiptID, RUID, Price, GCashReference, PaymentTypeID FROM transaction_receipts
                WHERE PurchaseDate LIKE %s OR
                TransactionReceiptID LIKE %s OR 
                RUID LIKE %s OR
                Price LIKE %s OR
                PaidPrice LIKE %s OR
                GCashReference LIKE %s OR
                PaymentTypeID LIKE %s
                ORDER BY PurchaseDate DESC
                """
        searchstr = '%' + searchstr + '%'
        
        if re.search(searchstr, 'Cash', re.IGNORECASE):
            PTID = '0'
        elif re.search(searchstr, 'Gcash', re.IGNORECASE):
            PTID == '1'
        elif re.search(searchstr, 'split', re.IGNORECASE):
            PTID == '2'
        else:
            PTID = searchstr
        
        val = (searchstr,searchstr,searchstr,searchstr,searchstr,searchstr, PTID)
        self.mycursor.execute(sql,val)
        return self.mycursor.fetchall()
    
    # THIS USES SELECT *
    def search_supp_receipts(self, searchstr):
        
        sql = """
            SELECT * FROM supplier_receipts 
            WHERE SupplierReceiptID LIKE %s
                    OR RUID  LIKE %s
                    OR ReceiptRef  LIKE %s
                    OR TotalPrice LIKE %s
                    OR OrderDate LIKE %s
                    OR DeliveryDate LIKE %s
        """
        searchstr = '%' + searchstr + '%'
        val = (searchstr,searchstr,searchstr,searchstr,searchstr,searchstr,searchstr)
        
        self.mycursor.execute(sql,val)
        return self.mycursor.fetchall()

    # Adding Receipt Data
    
    def add_receipt(self,RefNo, TPrice ,ODate, DDate, Plist):
        
        sql = """INSERT INTO supplier_receipts (RUID, ReceiptRef, TotalPrice, OrderDate, DeliveryDate)
                VALUES (%s,%s,%s,%s,%s)"""
        val = (self.User.RUID, RefNo, TPrice, ODate, DDate)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
        
        self.add_supplied_products(RefNo= RefNo, DDate= DDate, Plist= Plist)
        
    def add_sold_protocol(self,Price, PPrice, SoldProductsList, Ptype, GCashRef = None):
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
        
    # Receipt Product Manipulation
    # Getting Receipt Product Data
    def get_receipt_products(self, ReceiptID, trans_rec = None):
        if trans_rec:
            sql = """
                SELECT ProductID, Price, Quantity from products_sold WHERE ReceiptID = %s
            
            """
            self.mycursor.execute(sql,(ReceiptID,))
            return self.mycursor.fetchall()
            
        else:
            sql = """
                    SELECT ProductID, Price, Quantity from products_sold WHERE ReceiptID = %s
                
            """
            self.mycursor.execute(sql,(ReceiptID,))
            return self.mycursor.fetchall()
        
    def set_dynamic_expdate(self, RPID):
        sql = """
                SELECT
                    ExpirationDate,
                    ABS(DATEDIFF(ExpirationDate, NOW())) AS date_diff,
                    SUM(CurrentQuantity) OVER() AS total_stock
                FROM
                    products_supplied
                WHERE
                    RPID = %s
                    AND CurrentQuantity > 0
                    AND ExpirationDate >= NOW()
                ORDER BY
                    ExpirationDate ASC
                LIMIT 1;

            """

        self.mycursor.execute(sql,(RPID,))
        
        prodlist = self.mycursor.fetchone()
        latestEdate = prodlist[0]
        latestStock = prodlist[2]
        sql = """
            UPDATE products SET ExpirationDate = %s, TotalStock = %s WHERE RPID = %s
        """
        self.mycursor.execute(sql, (latestEdate, latestStock, RPID))
        self.mydb.commit()

    # Adding Receipt Product Data
    
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
    
    def add_supplied_products(self,RefNo,DDate, Plist):
        sql = """INSERT INTO products_supplied (RPID, SupplierReceiptID, BoughtQuantity, CurrentQuantity, Date, CostPrice, ExpirationDate)
                VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        for prod in Plist:
            val = (prod[0], RefNo, prod[3], prod[3],DDate, prod[2],prod[4])
            self.mycursor.execute(sql,val)
            self.mydb.commit()
            self.add_inven(prod[0],prod[3])
            self.set_dynamic_expdate(RPID= prod[0])
    
    
    # sales and reports
    
    def get_inventory(self):
        sql = """
                SELECT ReceiptID, ProductID, Quantity, Price, Date FROM products_sold
                """
        self.mycursor.execute(sql)
        return self.mycursor.fetchall()
    
    def search_inventory_rec(self, SDate, EDate = None):
        if EDate == None:
            sql = "SELECT ReceiptID, ProductID, Quantity, Price, Date FROM products_sold WHERE Date = %s"
            self.mycursor.execute(sql, (SDate,))
        else:
            sql = "SELECT ReceiptID, ProductID, Quantity, Price, Date FROM products_sold WHERE Date BETWEEN %s AND %s"
            self.mycursor.execute(sql, (SDate,EDate))
        
        return self.mycursor.fetchall()
    
    def search_sales_rep(self, SDate, EDate = None, daily = None, monthly = None, yearly = None):
        
        if EDate == None:
            if daily:
                sql = """
                    SELECT PurchaseDate, Price FROM transaction_receipts WHERE DATE(PurchaseDate) = %s;
                    """
                self.mycursor.execute(sql, (SDate,))
                return self.mycursor.fetchall()
            elif monthly:
                sql = """
                    SELECT PurchaseDate, Price FROM transaction_receipts
                    WHERE YEAR(PurchaseDate) = %s AND MONTH(PurchaseDate) = %s;
                    """
                self.mycursor.execute(sql, (SDate, SDate))
                return self.mycursor.fetchall()
            elif yearly:
                sql = """
                    SELECT PurchaseDate, Price FROM transaction_receipts
                    WHERE YEAR(PurchaseDate) = %s
                    """
                self.mycursor.execute(sql, (SDate,))
                return self.mycursor.fetchall()
        else:
            
            if daily:
                sql = """
                    SELECT PurchaseDate, Price FROM transaction_receipts WHERE DATE(PurchaseDate) BETWEEN %s AND %s;
                    """
                    
                self.mycursor.execute(sql, (SDate, EDate))
                return self.mycursor.fetchall()
            
            elif monthly:
                
                sql = """
                    SELECT PurchaseDate, Price FROM transaction_receipts
                    WHERE (YEAR(PurchaseDate) = %s AND MONTH(PurchaseDate) >= %s)
                    OR (YEAR(PurchaseDate) = %s AND MONTH(PurchaseDate) <= %s)
                    OR (YEAR(PurchaseDate) > %s AND YEAR(PurchaseDate) < %s) ORDER BY PurchaseDate;
                """
                    
                start_year = SDate.year
                start_month = SDate.month
                end_year = EDate.year
                end_month = EDate.month
                    
                self.mycursor.execute(sql, (start_year, start_month, end_year, end_month, start_year, end_year))
                return self.mycursor.fetchall()
            elif yearly:
                
                sql = """
                    SELECT PurchaseDate, Price FROM transaction_receipts
                    WHERE YEAR(PurchaseDate) BETWEEN %s AND %s
                """
                
                self.mycursor.execute(sql, (SDate,))
                return self.mycursor.fetchall()
