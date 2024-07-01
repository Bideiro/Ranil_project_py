import mysql.connector
import os
from datetime import datetime

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
        self.BData_btn.clicked.connect(self.exportData)

    def Restore_protocol(self):
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            fileName, _ = QFileDialog.getOpenFileName(self, "Select a SQL File", "", "SQL Files (*.sql);;All Files (*)", options=options)
            if fileName:
                self.db.Restore_sql(fileName)
            else:
                Dlg = DLG_Alert(msg='No SQL file Selected!')
                Dlg.exec()
                    
    def exportData(self):
        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user= "root",
                passwd= "password",
                database="ranil_proj")
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")

            tables = cursor.fetchall()
            options = QFileDialog.Options()
            directory = QFileDialog.getExistingDirectory(self, "Select Directory to Save SQL Backup File", options=options)
            if directory:
                # Get today's date and format it
                today = datetime.now().strftime("%Y-%m-%d")
                filename = f"backup_{today}.sql"  # Hardcoded filename with today's date
                filePath = os.path.join(directory, filename)
                with open(filePath, 'w') as f:
                    for table in tables:
                        table_name = table[0]
                        cursor.execute(f"SHOW CREATE TABLE {table_name}")
                        create_table_stmt = cursor.fetchone()[1]
                        f.write(f"{create_table_stmt};\n\n")

                        cursor.execute(f"SELECT * FROM {table_name}")
                        rows = cursor.fetchall()

                        if rows:
                            columns = [desc[0] for desc in cursor.description]
                            col_names = ", ".join(columns)
                            for row in rows:
                                values = ", ".join([f"'{str(val)}'" if val is not None else 'NULL' for val in row])
                                insert_stmt = f"INSERT INTO {table_name} ({col_names}) VALUES ({values});"
                                f.write(f"{insert_stmt}\n")
                            f.write("\n")
                
                QMessageBox.information(self, "Success", "Data exported successfully!")
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Error: {err}")
