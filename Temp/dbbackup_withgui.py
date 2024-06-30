import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel
import mysql.connector

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Database Backup/Restore')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel('Select a backup file to restore', self)
        layout.addWidget(self.label)

        self.btn = QPushButton('Open File Dialog', self)
        self.btn.clicked.connect(self.showFileDialog)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        
    def showFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "SQL Files (*.sql);;All Files (*)", options=options)
        if fileName:
            self.label.setText(f"Selected file: {fileName}")
            self.restore_database( fileName)

    def restore_database(self, backup_file):
        try:
            conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="password",
                    database="ranil_proj"
                    )
            cursor = conn.cursor()

            with open(backup_file, "r") as f:
                sql_commands = f.read().split(";\n")

            for command in sql_commands:
                if command.strip():
                    cursor.execute(command)
                    conn.commit()

            cursor.close()
            conn.close()
            self.label.setText(f"Restore completed from {backup_file}")
        except Exception as e:
            self.label.setText(f"Error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
