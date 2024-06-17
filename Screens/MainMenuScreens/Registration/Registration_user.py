import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget
from PyQt5.QtCore import Qt, pyqtSlot, QFile, QTextStream
from PyQt5.QtGui import QIntValidator

from .Registration_user_ui import Ui_MainWindow
from Dialogs.DLog_Alert import DLG_Alert

from Database.DBController import dbcont
from Database.App_functions import vali_email, vali_phono

from PyQt5 import QtWidgets, QtGui, QtCore
class Registration_user_Window(QMainWindow, Ui_MainWindow):
    back_btnsgl = QtCore.pyqtSignal()
    
    def __init__(self):
        super(Registration_user_Window,self).__init__()
        self.setupUi(self)
        
        self.db = dbcont("root","password")
        
        self.back_btn.clicked.connect(self.prev_window)
        self.save_btn.clicked.connect(self.init_reg_protocol)
        
        self.onlyInt = QIntValidator()
        self.PCode_LE.setValidator(self.onlyInt)
        self.CPass_LE.setValidator(self.onlyInt)
        self.Sex_CB.addItems(self.db.get_sex())
        
    def prev_window(self):
        self.back_btnsgl.emit()
        
    def init_reg_protocol(self):
        
        valid = False
        err = 'Unknown Error'
        
        # Checking Input validity
        
        if self.Phono_LE.text() == '':
            err = 'No Phone Number!'
        elif self.Sex_CB.currentIndex() == -1:
            err = 'Sex not set!'
        elif self.Level_CB.currentIndex() == -1:
            err = 'Set Level of Access!'
        elif not vali_email(self.email_LE.text()):
            err = 'Invalid Email!'
        elif not vali_phono(self.Phono_LE.text()):
            
            err = 'Invalid Phone Number!'
        elif len(self.PCode_LE.text()) != 6:
            print(self.Phono_LE.text())
            print(self.Phono_LE.text().replace('+', '', 1))
            err = 'Invalid Passcode!'
        elif self.PCode_LE.text() != self.CPass_LE.text():
            err = 'Passcodes doesnt match!'
        else:
            valid = True
        if valid:
            self.confirmed_reg()
            
        else:
            errdlg = DLG_Alert(msg= err)
            errdlg.exec()
        
    def confirmed_reg(self):
        
        db = dbcont("root", "password")
        db.reg_user_protocol(LevelID= self.Level_CB.currentIndex(),
                        Uname= self.user_LE.text(),
                        Passcode= self.PCode_LE.text(),
                        fname= self.FName_LE.text(),
                        lname= self.LName_LE.text(),
                        sex= self.Sex_CB.currentIndex(),
                        phono= self.Phono_LE.text().replace('+', '', 1),
                        email= self.email_LE.text(),
                        pos= self.pos_LE.text(),
                        Dhired= self.DHire_DE.date().toPyDate(),
                        Bdate= self.BDate_DE.date().toPyDate(),
                        address= self.address_LE.text()
                        )
        
        succdlg = DLG_Alert()
        succdlg.exec()
        self.back_btnsgl.emit()
