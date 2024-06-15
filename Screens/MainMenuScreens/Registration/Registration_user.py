import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5.QtGui import QIntValidator

from .Registration_user_ui import Ui_MainWindow
from .Dlog_tempalert import DLGsucc

from Database.DBController import dbcont
from Database.App_functions import vali_email, vali_phono

from PyQt5 import QtWidgets, QtGui, QtCore
class Registration_user_Window(QMainWindow, Ui_MainWindow):

    back_btnsgl = QtCore.pyqtSignal()
    passcode = None
    
    def __init__(self):
        super(Registration_user_Window,self).__init__()
        self.setupUi(self)
        
        self.db = dbcont("root","password")
        
        self.back_btn.clicked.connect(self.prev_window)
        self.save_btn.clicked.connect(self.init_reg_protocol)
        
        self.onlyInt = QIntValidator()
        self.PCode_LE.setMaxLength(6)
        self.PCode_LE.setValidator(self.onlyInt)
        
        self.Sex_CB.addItems(self.db.get_sex())
        
    def prev_window(self):
        self.back_btnsgl.emit()
        
    def init_reg_protocol(self):
        
        valid = False
        err = 'Unknown Error'
        
        # Checking Input validity
        
        if vali_email(self.email_LE.text()):
            valid = True
        else:
            err = 'Invalid Email'
        
        if vali_phono(self.Phono_LE.text()):
            valid = True
        else:
            err = 'Invalid Phone Number'
        
        if len(self.PCode_LE.text()) == 6 and self.PCode_LE.text().isdigit():
            valid = True
        else:
            err = 'Invalid Passcode'
            
        if valid:
            self.confirmed_reg()
        else:
            print(err)
        
    def confirmed_reg(self):
        
        db = dbcont("root", "password")
        db.reg_protocol(fname=self.FName_LE.text(), lname=self.LName_LE.text(),
                        uname = self.user_LE.text(), email = self.email_LE.text(),
                        loa = self.level_CB.currentText(), bday = self.Bday_DE.date().toPyDate(),
                        gender = self.gender_CB.currentText(),pos = self.pos_LE.text(),
                        phono = self.Phono_LE.text(),Dhired = self.DHire_DE.date().toPyDate(),
                        address= self.address_LE.text(), passcode = self.PCode_LE.text())
        dlg = DLGsucc(self)
        dlg.exec()
        self.back_btnsgl.emit()

        