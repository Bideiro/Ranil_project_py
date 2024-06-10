import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from login_ui import LoginUI
from DBController import dbcont

class LoginWindow(QMainWindow, LoginUI):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.setupUi(self)
        
        self.show()
        
    @pyqtSlot()
    def on_login_btn_clicked(self):
        print("hi")
        db = dbcont(self.ui.userLE.text(),self.ui.passwordLE.text())
        db.conn()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    win = LoginUI()
    win.show()
    
    sys.exit(app.exec_())