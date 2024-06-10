import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from Screens.login_ui import LoginUI
from Database.DBController import dbcont

class LoginWindow(QMainWindow, LoginUI):
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.setupUi(self)
        self.show()
        
    @pyqtSlot()
    # initiate login
    def on_login_btn_clicked(self):
        print("hi")
        db = dbcont(self.ui.userLE.text(),self.ui.passwordLE.text())
        db.conn()
        
    def on_forgotpass_btn_clicked(self):
        print("forgot")
        