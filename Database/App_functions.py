import re

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
    
def check_user_validity(LevelID ,Uname ,pass1 ,pass2,Fname ,Lname ,SexID ,Phono ,Email ,Pos ,HDate ,BDate ,Add):
    
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
    elif SexID == -1:
        return 'Input gender!'
    elif Pos == '':
        return 'Empty Position field!'
    elif not vali_phono(Phono):
        return 'Invalid Phone Number'
    elif len(pass1) != 6 and len(pass2) != 6:
        return 'Passcode requires 6 characters!'
    elif pass2 != pass1:
        return 'Passcodes dont match!'
    else:
        return True

def check_prod_validity(Pname, Utype, Sprice, Cat):
    
    if Pname == '':
        return 'Empty Product name field!'
    elif Utype == -1:
        return 'Empty Unit type field!'
    elif Sprice == '':
        return 'Empty Selling price field!'
    elif Cat == -1:
        return 'Category not set!'
    else:
        return True