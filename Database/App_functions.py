import re
from datetime import datetime

from Database.DBController import dbcont

db = dbcont()

today = datetime.today().date()

def vali_email(email):
    email_pattern = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    if re.match(email_pattern, email):
        return True
    else:
        return False

def vali_phono(phone_number):
    pattern = re.compile(r'^\+639\d{9}$')
    if pattern.match(phone_number):
        return True
    else:
        return False
    
def check_user_validity(Fname ,Lname ,Uname ,Email ,LevelID ,Bdate ,SexID ,Pos ,Phono ,Add ,Hdate ,nochangepw = None ,pass1  = None ,pass2 = None):
    # Order of checking & what is checked
    # First & Last name must be 2 or more chracters
    # Username must not be empty
    # Email validity
    # Checking of LOA
    # Checking of Bdate
    # Bdate must be before Hdate
    # Checking of sex
    # Phone number
    # Checking char length of passcode
    # Checking if passcode matches
    if len(Fname) <= 2:
        return 'First name must be 2 or more characters!'
    elif len(Lname) <= 2:
        return 'Last name must be 2 or more characters!'
    elif Uname == '':
        return 'Empty Username field!'
    elif not vali_email(Email):
        return 'Invalid Email!'
    elif LevelID == -1:
        return 'Input level of access!'
    elif Bdate >= today:
        return 'Birthdate must before today!'
    elif Bdate >= Hdate:
        return 'Birthdate must before Hire Date!'
    elif SexID == -1:
        return 'Input gender!'
    elif Pos == '':
        return 'Empty position field!'
    elif not vali_phono(Phono):
        return 'Invalid Phone Number'
    elif Hdate >= today:
        return 'Hiredate must be before today!'
    elif Add == '':
        return 'Empty Address field!'
    elif nochangepw != True:
        if len(pass1) != 6 and len(pass2) != 6:
            return 'Passcode requires 6 characters!'
        elif pass2 != pass1:
            return 'Passcodes dont match!'
        else:
            print(pass1)
            print(pass2)
            return True
    else:
        return True

def check_prod_validity(Pname, Utype, Sprice, Cat):
    
    if Pname == '':
        return 'Empty Product name field!'
    elif Utype == -1:
        return 'Empty Unit type field!'
    elif Sprice == '':
        return 'Empty Selling price field!'
    elif int(Sprice) <= 0:
        return 'Price field is 0 or less than 0!'
    elif Cat == -1:
        return 'Category not set!'
    else:
        return True