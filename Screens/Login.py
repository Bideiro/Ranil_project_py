import sys
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator

from .Login_ui import Ui_MainWindow
from Database.DBController import dbcont
from Database.User_Manager import UserMana
from Dialogs.DLog_Alert import DLG_Alert
from PyQt5 import QtWidgets, QtGui, QtCore
class LoginWindow(QMainWindow, Ui_MainWindow):

    logsucc_emp = QtCore.pyqtSignal()
    logsucc_admin = QtCore.pyqtSignal()
    forgot = QtCore.pyqtSignal()
    
    User = UserMana()
    
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.setupUi(self)
        self.userLE.setFocus()
        self.onlyInt = QIntValidator()
        self.passwordLE.setMaxLength(6)
        self.passwordLE.setValidator(self.onlyInt)
        
        self.SPass_RB.toggled.connect(self.change_echo)
        
        
    def change_echo(self):
        if self.SPass_RB.isChecked():
            self.passwordLE.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passwordLE.setEchoMode(QLineEdit.EchoMode.Password)
        
        
        
    @pyqtSlot()
    # initiate login
    def on_login_btn_clicked(self):
        print("Login Attempt")
        
        mydb = dbcont(self.userLE.text(), self.passwordLE.text())
        if mydb.login():
            if self.User.Level == 0:
                self.logsucc_admin.emit()
            else:
                self.logsucc_emp.emit()
        else:
            Dlg = DLG_Alert(msg='Invalid Username or Password!')
            Dlg.exec()
        
    @pyqtSlot()
    def on_forgotpass_btn_clicked(self):
        print("forgot")
        self.forgot.emit()
        