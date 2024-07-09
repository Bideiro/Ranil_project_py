import mysql.connector
import re

def extract_table_names_from_sql(file_path):
    """Extract table names from the SQL file."""
    with open(file_path, 'r') as file:
        sql_content = file.read()
    
    # Regular expression to find table names in CREATE TABLE statements
    table_names = re.findall(r'CREATE TABLE `?(\w+)`?', sql_content, re.IGNORECASE)
    
    return set(table_names)

def get_existing_tables(cursor):
    """Retrieve the list of existing tables in the database."""
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    return set(table[0] for table in tables)

def main():
    # Database connection details
    db_config = {
        'user': 'root',
        'password': 'password',
        'host': 'localhost',
        'database': 'ranil_proj'
    }

    sql_file_path = 'INIT_DB.sql'
    
    # Extract table names from the SQL file
    required_tables = extract_table_names_from_sql(sql_file_path)
    
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Retrieve existing tables from the database
    existing_tables = get_existing_tables(cursor)
    
    # Find missing tables
    missing_tables = required_tables - existing_tables
    
    if missing_tables:
        print("Missing tables:", missing_tables)
    else:
        print("All tables are present.")
    
    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
