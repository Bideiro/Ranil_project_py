import re

def vali_email(email):
    # Define the regex pattern for a valid email address
    email_pattern = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    
    # Use the search method to find a match
    if re.match(email_pattern, email):
        return True
    else:
        return False
    

