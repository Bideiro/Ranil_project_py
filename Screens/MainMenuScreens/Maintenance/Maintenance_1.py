import mysql.connector
import os
import datetime

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from .Maintenance_1_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert

from Database.DBController import dbcont

class Maintenance_Window(QMainWindow, Ui_MainWindow):
    
    db = dbcont()
    
    def __init__(self):
        super(Maintenance_Window,self).__init__()
        self.setupUi(self)
        
        self.RData_btn.clicked.connect(self.Restore_protocol)
        self.BData_btn.clicked.connect(self.backup_database)

    def Restore_protocol(self):
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            fileName, _ = QFileDialog.getOpenFileName(self, "Select a SQL File", "", "SQL Files (*.sql);;All Files (*)", options=options)
            if fileName:
                self.db.Restore_sql(fileName)
            else:
                Dlg = DLG_Alert(msg='No SQL file Selected!')
                Dlg.exec()
                        
    def backup_database(self):
        backup_path = os.path.expanduser("~/Desktop")
        # Create a backup file name with the current date
        backup_file = os.path.join(backup_path, f"Backup_File_{datetime.datetime.now().strftime('%Y%m%d_%H;%M')}.sql")
            
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
