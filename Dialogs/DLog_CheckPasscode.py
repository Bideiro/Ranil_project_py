import sys
from PyQt5.QtWidgets import QMainWindow,QDialog, QPushButton, QWidget, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot

from PyQt5.QtGui import QIntValidator
from Database.App_functions import check_user_validity



from Database.DBController import dbcont
from Database.User_Manager import UserMana
from Dialogs.DLog_Alert import DLG_Alert

from .DLog_CheckPasscode_ui import Ui_Dialog

class DLG_CheckPass(QDialog, Ui_Dialog):
    
    db = dbcont()
    User = UserMana()
    
    def __init__(self,parent = None, Confirm = None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.confirm = Confirm
        
        self.onlyInt = QIntValidator()
        self.PCode_LE.setValidator(self.onlyInt)
        self.VPCode_LE.setValidator(self.onlyInt)
        
        self.Confirm_btn.clicked.connect(self.confirmed)
        
    def confirmed(self):
        if self.confirm:
            if self.PCode_LE.text() == '' or self.VPCode_LE.text() == '':
                Dlg = DLG_Alert(msg='Empty Passcode field!')
                Dlg.exec()
            elif self.PCode_LE.text() != self.VPCode_LE.text():
                Dlg = DLG_Alert(msg='Passcodes dont match!')
                Dlg.exec()
            else:
                self.done(1)
        else:
            if self.PCode_LE.text() == '' or self.VPCode_LE.text() == '':
                Dlg = DLG_Alert(msg='Empty Passcode field!')
                Dlg.exec()
            elif self.PCode_LE.text() != self.VPCode_LE.text():
                Dlg = DLG_Alert(msg='Passcodes dont match!')
                Dlg.exec()
            elif self.PCode_LE.text() != self.User.Pass:
                Dlg = DLG_Alert(msg='Incorrect Passcode!')
                Dlg.exec()
            