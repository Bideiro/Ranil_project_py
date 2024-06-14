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
    pattern = re.compile(r'^\+369[- ]?\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$')
    if pattern.match(phone_number):
        return True
    else:
        return False