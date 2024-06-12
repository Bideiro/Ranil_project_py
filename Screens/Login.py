import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Login_UI import Ui_MainWindow
from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class LoginWindow(QMainWindow, Ui_MainWindow):

    logsucc_emp = QtCore.pyqtSignal()
    logsucc_admin = QtCore.pyqtSignal()
    forgot = QtCore.pyqtSignal()
    
    
    def __init__(self):
        super(LoginWindow,self).__init__()
        self.setupUi(self)
        
    @pyqtSlot()
    # initiate login
    def on_login_btn_clicked(self):
        print("Login Attempt")
        
        self.logsucc_admin.emit()
        
        # db = dbcont(self.userLE.text(),self.passwordLE.text())
        # db.conn()
        
    @pyqtSlot()
    def on_forgotpass_btn_clicked(self):
        print("forgot")
        self.forgot.emit()
        