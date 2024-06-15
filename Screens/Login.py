import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator

from .Login_ui import Ui_MainWindow
from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class LoginWindow(QMainWindow, Ui_MainWindow):

    logsucc_emp = QtCore.pyqtSignal()
    logsucc_admin = QtCore.pyqtSignal()
    forgot = QtCore.pyqtSignal()
    
    
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.setupUi(self)
        
        self.userLE.setFocus()
        self.onlyInt = QIntValidator()
        self.passwordLE.setMaxLength(6)
        self.passwordLE.setValidator(self.onlyInt)
        
    @pyqtSlot()
    # initiate login
    def on_login_btn_clicked(self):
        print("Login Attempt")
        
        mydb = dbcont(self.userLE.text(), self.passwordLE.text())
        if mydb.login():
            self.logsucc_admin.emit()
        else:
            print("Invalid credentials")
        
    @pyqtSlot()
    def on_forgotpass_btn_clicked(self):
        print("forgot")
        self.forgot.emit()
        