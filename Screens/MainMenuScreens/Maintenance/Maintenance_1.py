import subprocess
import os
import datetime
import mysql.connector
from PyQt5.QtWidgets import QMainWindow, QFileDialog

import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox

from .Maintenance_1_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert

from Database.DBController import dbcont

class Maintenance_Window(QMainWindow, Ui_MainWindow):
    
    db = dbcont()
    
    def __init__(self):
        super(Maintenance_Window,self).__init__()
        self.setupUi(self)
        
        self.RData_btn.clicked.connect(self.openFileDialog)
        self.BData_btn.clicked.connect(self.backup_database)
        
    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "Select MySQL File", "", "SQL Files (*.sql);;All Files (*)", options=options)
        if fileName:
            self.importData(fileName)

    def importData(self, fileName):
        try:
            # MySQL database connection parameters
            host = 'localhost'
            user = 'root'
            password = 'password'
            database = 'ranil_proj'

            # Construct the command and ensure the file path is properly quoted
            command = f'mysql -h {host} -u {user} -p{password} {database} < "{fileName}"'

            # Execute the command
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            if result.returncode == 0:
                QMessageBox.information(self, 'Success', 'Data imported successfully.')
            else:
                QMessageBox.critical(self, 'Error', f'Error: {result.stderr}')

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An unexpected error occurred: {e}')


    # def Restore_protocol(self):
        # options = QFileDialog.Options()
        # options |= QFileDialog.ReadOnly
        # fileName, _ = QFileDialog.getOpenFileName(self, "Select a SQL File", "", "SQL Files (*.sql);;All Files (*)", options=options)
        # if fileName:
        #     self.db.Restore_sql(fileName)
        # else:
        #     Dlg = DLG_Alert(msg='No SQL file Selected!')
        #     Dlg.exec()
        
        
    def backup_database(self):
        backup_path = os.path.expanduser("~/Desktop")
        # Create a backup file name with the current date
        backup_file = os.path.join(backup_path, f"Backup_File_{datetime.datetime.now().strftime('%B_%d_%Y_%H;%M')}.sql")

        # Database connection parameters
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'passwd': 'password',
            'database': 'ranil_proj'
        }

        try:
            # Connect to the database to ensure credentials are correct
            conn = mysql.connector.connect(
                host=db_config['host'],
                user=db_config['user'],
                password=db_config['passwd'],
                database=db_config['database']
            )
            if conn.is_connected():
                print('Connected to MySQL database')

            # Close the connection after verification
            conn.close()

            # Construct the mysqldump command
            dump_cmd = [
                'mysqldump',
                '--host=' + db_config['host'],
                '--user=' + db_config['user'],
                '--password=' + db_config['passwd'],
                db_config['database'],
                '--result-file=' + backup_file
            ]

            # Execute the mysqldump command
            subprocess.run(dump_cmd, check=True)
            Dlg = DLG_Alert(msg = f'Backup completed: {backup_file}')
            Dlg.exec()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        except subprocess.CalledProcessError as err:
            print(f"mysqldump error: {err}")
