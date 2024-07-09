import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Import MySQL Data')

        self.button = QPushButton('Open File Dialog', self)
        self.button.setGeometry(100, 80, 200, 40)
        self.button.clicked.connect(self.openFileDialog)

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
            user = 'your_username'
            password = 'your_password'
            database = 'your_database'

            # Construct the command
            command = f"mysql -h {host} -u {user} -p{password} {database} < {fileName}"

            # Execute the command
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            if result.returncode == 0:
                QMessageBox.information(self, 'Success', 'Data imported successfully.')
            else:
                QMessageBox.critical(self, 'Error', f'Error: {result.stderr}')

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
