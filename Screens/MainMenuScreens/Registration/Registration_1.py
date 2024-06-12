import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream

from .Registration_1_ui import Ui_MainWindow
from Database.DBController import dbcont
from PyQt5 import QtWidgets, QtGui, QtCore
class Registration_1_Window(QMainWindow, Ui_MainWindow):

    user_reg_btnsgl = QtCore.pyqtSignal()
    prod_reg_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Registration_1_Window,self).__init__()
        self.setupUi(self)
        
        self.user_reg_btn.clicked.connect(self.User_regist)
        self.prod_reg_btn.clicked.connect(self.Prod_regist)
        
    # initiate login
    def User_regist(self):
        print("User reg")
        
        self.user_reg_btnsgl.emit()
        
        # db = dbcont(self.userLE.text(),self.passwordLE.text())
        # db.conn()
    
    def Prod_regist(self):
        print("Prod reg")
        self.prod_reg_btnsgl.emit()
        
        