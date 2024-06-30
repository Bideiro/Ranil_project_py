import mysql.connector
import os
import datetime

def backup_database(host, user, password, database, backup_dir):
    # Ensure the backup directory exists
    os.makedirs(backup_dir, exist_ok=True)
    
    # Create a backup file name with the current date
    backup_file = os.path.join(backup_dir, f"{database}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.sql")
    
    # Connect to the database
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="ranil_proj"
    )
    cursor = conn.cursor()
    
    # Get the list of tables
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    
    with open(backup_file, "w") as f:
        for table in tables:
            table_name = table[0]
            # Write the table structure
            cursor.execute(f"SHOW CREATE TABLE {table_name}")
            create_table_stmt = cursor.fetchone()[1]
            f.write(f"{create_table_stmt};\n\n")
            
            # Write the table data
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            for row in rows:
                row_data = ', '.join([f"'{str(item)}'" if item is not None else 'NULL' for item in row])
                f.write(f"INSERT INTO {table_name} VALUES ({row_data});\n")
            f.write("\n")
    
    print(f"Backup completed: {backup_file}")
    
    cursor.close()
    conn.close()

# Example usage
backup_database( "ranil_proj", "./backup_directory")
